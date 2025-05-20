"""Simple console spinner (context manager)."""
from __future__ import annotations

import itertools
import sys
import threading
import time
from types import TracebackType
from typing import Optional, Type

__all__ = ["Spinner"]


class Spinner:
    def __init__(self, message: str = "Loading") -> None:
        self.message = message
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def __enter__(self) -> "Spinner":
        self._running = True
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> bool:
        self._running = False
        if self._thread:
            self._thread.join()
        print("\r", end="", flush=True)
        return False

    def _spin(self) -> None:
        for frame in itertools.cycle("|/-\\"):
            if not self._running:
                break
            print(f"\r{self.message}… {frame}", end="", flush=True)
            time.sleep(0.1)
