import json
import os
import time

MEMORY_FILE = "memory.json"


class MemoryCore:
    def __init__(self):
        self.memory = []
        self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r") as f:
                    self.memory = json.load(f)
            except:
                self.memory = []
        else:
            self.memory = []

    def save_memory(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=4)

    def add(self, text):
        self.memory.append({
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "data": text
        })
        self.save_memory()

    def get_all(self):
        return self.memory
