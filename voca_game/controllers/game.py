"""Game controllers implementing the training & test flows."""
from __future__ import annotations

import random
from typing import List, Tuple
from ..models.wordbank import WordBank

__all__ = ["TrainingGame", "TestGame"]


class _BaseGame:
    def __init__(self, bank: WordBank) -> None:
        self.bank = bank
        self._word_list: List[Tuple[str, str]] = self._prepare_words()

    def _prepare_words(self) -> List[Tuple[str, str]]:
        words = self.bank.flatten()
        random.shuffle(words)
        return words


class TrainingGame(_BaseGame):
    def play(self) -> None:
        for english, translation in self._word_list:
            input(f"{english} → ")
            print(f"  {translation}\n")


class TestGame(_BaseGame):
    def play(self) -> None:
        score = 0
        for english, translation in self._word_list:
            guess = input(f"{english} → ")
            if guess.strip().lower() == translation.lower():
                score += 1
                print("✅ Correct!\n")
            else:
                print(f"❌ {translation}\n")
        print(f"Your score: {score}/{len(self._word_list)}")
