"""Vocabulary Game — Python package."""

__all__ = ["__version__", "main"]
__version__ = "0.1.0"

from .cli import main  # re-export for `python -m voca_game`
