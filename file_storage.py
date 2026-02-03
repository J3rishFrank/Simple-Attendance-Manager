import json
import os

# FileStorage saves the data to JSON files and loads it back, so that
# higher-level components do not need to manage file details directly.
class FileStorage:
    """Simple file-based storage for JSON data."""
    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            return json.load(file)