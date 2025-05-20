"""Interactive CLI editor for the word bank."""
from __future__ import annotations

from ..models.wordbank import WordBank

__all__ = ["EditorUI"]


class EditorUI:
    def __init__(self, bank: WordBank) -> None:
        self.bank = bank

    def run(self) -> None:
        while True:
            print("\n=== Edit Word Bank ===")
            print("1. Add word")
            print("2. Update word")
            print("3. Delete word")
            print("4. List all words")
            print("5. Back to main menu")
            choice = input("> ")
            if choice == "1":
                self._add()
            elif choice == "2":
                self._update()
            elif choice == "3":
                self._delete()
            elif choice == "4":
                self._list_all()
            elif choice == "5":
                break
            else:
                print("Invalid selection.")

    def _add(self) -> None:
        unit, eng, trans = self._prompt()
        self.bank.add_word(unit, eng, trans)

    def _update(self) -> None:
        unit, eng, trans = self._prompt("New translation")
        self.bank.update_word(unit, eng, trans)

    def _delete(self) -> None:
        unit = input("Unit: ")
        eng = input("English: ")
        self.bank.delete_word(unit, eng)

    def _list_all(self) -> None:
        for unit, words in self.bank.all_words().items():
            print(f"\n[{unit}]")
            for eng, trans in words.items():
                print(f"  {eng:<20} → {trans}")

    @staticmethod
    def _prompt(translation_label: str = "Translation"):
        unit = input("Unit: ")
        eng = input("English: ")
        trans = input(f"{translation_label}: ")
        return unit, eng, trans
