import time
import threading

class DataBus:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()

    def set(self, key, value):
        with self._lock:
            self._data[key] = {"value": value, "ts": time.time()}

    def get(self, key, default=None):
        with self._lock:
            item = self._data.get(key)
            return default if item is None else item["value"]

    def snapshot(self):
        with self._lock:
            return {k: v["value"] for k, v in self._data.items()}
