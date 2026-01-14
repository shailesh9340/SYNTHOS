from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
import time

from memory.memory_core import MemoryCore


class SynthosUI(BoxLayout):
    status_text = StringProperty("Waiting...")
    glow = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.memory = MemoryCore()
        Clock.schedule_interval(self.animate_glow, 0.6)

    def animate_glow(self, dt):
        self.glow = not self.glow
        if self.glow:
            self.ids.voice_circle.opacity = 1
        else:
            self.ids.voice_circle.opacity = 0.6

    def start_voice(self):
        self.status_text = "Listening..."
        self.memory.add("Voice Assistant Activated")

    def fake_auth(self):
        self.status_text = "✔ Access Granted"
        self.memory.add("Mobile Auth Success")

    def view_memory(self):
        data = self.memory.get_all()
        if not data:
            self.status_text = "Memory empty"
        else:
            self.status_text = data[-1]["data"]


class SynthosApp(App):
    def build(self):
        return SynthosUI()


if __name__ == "__main__":
    SynthosApp().run()
