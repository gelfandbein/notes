import os
import time
import json

class NoteApp:
    def __init__(self, filename=None):
        self.filename = filename if filename is not None else "notes.json"

    def init(self):
        if not os.path.exists(self.filename):
            with open(self.filename) as f:
                json.dump({"notes": []}, f, indent=2, sort_keys=True)

    def run (self):
        while True:
            print("I'm running")
            time.sleep(1)

    def shutdown(self):
        print("\nShutdown")


if __name__ == "__main__":
    app = NoteApp()
    try:
        app.run()
    except KeyboardInterrupt:
        app.shutdown()
