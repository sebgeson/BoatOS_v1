from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import Any, Dict


@dataclass
class DataValue:
    value: Any
    source: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    status: str = "OK"


class DataBus:
    def __init__(self):
        self._data: Dict[str, DataValue] = {}
        self._lock = Lock()

    def publish(self, key: str, value: Any, source: str, status: str = "OK") -> None:
        with self._lock:
            self._data[key] = DataValue(value=value, source=source, status=status)

    def get(self, key: str, default: Any = None) -> Any:
        with self._lock:
            item = self._data.get(key)
            return item.value if item else default

    def snapshot(self) -> Dict[str, DataValue]:
        with self._lock:
            return dict(self._data)
