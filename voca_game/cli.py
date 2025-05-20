"""Command-line entry-point (invoked via `voca-game` script or `python -m voca_game`)."""
from __future__ import annotations

import argparse
from .ui.menu import MainMenu


def main() -> None:  # pragma: no cover
    parser = argparse.ArgumentParser(
        prog="voca-game",
        description="Vocabulary Game — train, test, and manage your word bank.",
    )
    parser.add_argument(
        "--mode",
        choices=["train", "test", "edit"],
        help="Skip the menu and launch a mode directly.",
    )
    args = parser.parse_args()

    menu = MainMenu()
    menu.run(initial_mode=args.mode)


if __name__ == "__main__":  # pragma: no cover
    main()
