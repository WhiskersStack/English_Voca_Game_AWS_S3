"""WordBank model — simple JSON persistence layer."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

__all__ = ["WordBank"]


class WordBank:
    DATA_FILE = Path(__file__).resolve().parent.parent / "vocabulary.json"

    def __init__(self, path: Path | None = None) -> None:
        self.path: Path = path or self.DATA_FILE
        self._data: Dict[str, Dict[str, str]] = self._load()

    def _load(self) -> Dict[str, Dict[str, str]]:
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as fp:
                return json.load(fp)
        return {}

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as fp:
            json.dump(self._data, fp, indent=2, ensure_ascii=False)

    # CRUD API
    def add_word(self, unit: str, english: str, translation: str) -> None:
        self._data.setdefault(unit, {})[english] = translation
        self.save()

    def update_word(self, unit: str, english: str, translation: str) -> None:
        self.add_word(unit, english, translation)

    def delete_word(self, unit: str, english: str) -> None:
        if unit in self._data and english in self._data[unit]:
            del self._data[unit][english]
            if not self._data[unit]:
                del self._data[unit]
            self.save()

    # Queries
    def all_units(self) -> List[str]:
        return list(self._data.keys())

    def all_words(self) -> Dict[str, Dict[str, str]]:
        return self._data

    def flatten(self) -> List[tuple[str, str]]:
        return [item for unit in self._data.values() for item in unit.items()]
