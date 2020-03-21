
import os
import time
import json


class NotesApp:
    def __init__(self, filename=None):
        self.filename = filename if filename is not None else "notes.json"

    def init(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({"notes": []}, f, indent=2, sort_keys=True)

    def run(self):
        while True:
            print("I'm running")
            time.sleep(1)
    
    def shutdown(self):
        print("Shutdown")


if __name__ == "__main__":
    app = NotesApp()
    try:
        app.init()
        app.run()
    except KeyboardInterrupt:
        app.shutdown()
