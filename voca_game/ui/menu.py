"""Text-based Main Menu UI."""
from __future__ import annotations

from typing import Callable, Dict
from ..models.wordbank import WordBank
from ..controllers.game import TrainingGame, TestGame
from .editor import EditorUI

__all__ = ["MainMenu"]


class MainMenu:
    def __init__(self) -> None:
        self.bank = WordBank()
        self._actions: Dict[str, Callable[[], None]] = {
            "train": self._train,
            "test": self._test,
            "edit": self._edit,
        }

    def run(self, initial_mode: str | None = None) -> None:
        if initial_mode:
            self._dispatch(initial_mode)
            return
        while True:
            print("\n=== Vocabulary Game ===")
            print("1. Training mode")
            print("2. Test mode")
            print("3. Edit word bank")
            print("4. Exit")
            choice = input("> ")
            lookup = {"1": "train", "2": "test", "3": "edit", "4": "exit"}
            self._dispatch(lookup.get(choice, ""))

    def _dispatch(self, mode: str) -> None:
        if mode == "exit":
            raise SystemExit
        action = self._actions.get(mode)
        if action:
            action()
        else:
            print("Invalid selection. Try again.")

    def _train(self) -> None:
        TrainingGame(self.bank).play()

    def _test(self) -> None:
        TestGame(self.bank).play()

    def _edit(self) -> None:
        EditorUI(self.bank).run()
