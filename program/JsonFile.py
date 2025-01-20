import json
import os

class JsonFile:
    def __init__(self, file):
        self.path = file
        # Проверяем, существует ли файл, чтобы избежать ошибок
        if not os.path.exists(self.path):
            # Если файл не существует, создаем пустой файл
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)
        with open(self.path, encoding='utf-8') as f:
            self.data = json.load(f)

    def writeValue(self, key, value):
        try:
            self.data[key] = value
            self.writeAll()
        except Exception as e:
            print(f"Error writing value: {e}")

    def readValue(self, key):
        try:
            return self.data.get(key, None)
        except Exception as e:
            print(f"Error reading value: {e}")
            return None

    def readAll(self):
        return self.data

    def writeAll(self):
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error writing all data: {e}")

    def clear(self):
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error clearing file: {e}")

    def writeValueInDict(self, key_0, key_1, value):
        try:
            if key_0 not in self.data:
                self.data[key_0] = {}
            self.data[key_0][key_1] = value
            self.writeAll()
        except Exception as e:
            print(f"Error writing in dict: {e}")

    def removeValue(self, key):
        try:
            if key in self.data:
                del self.data[key]
                self.writeAll()
            else:
                print(f"Key {key} not found.")
        except Exception as e:
            print(f"Error removing value: {e}")
