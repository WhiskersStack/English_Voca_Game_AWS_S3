# 📘 English Vocabulary Game

A command-line tool to **practice, train, and manage English vocabulary** with support for multiple units, test modes, and a JSON-based word bank.

---

## 🧩 Features

- 🧠 Vocabulary Training with spaced repetition logic (each word shown 7 times).
- 🎯 Test Mode with real-time scoring and feedback.
- ✍️ Edit Mode: Add, update, or delete words.
- 📂 Words are organized into units (`unit_1`, `unit_2`, etc.).
- 💾 Data stored in `vocabulary.json`.

---

## 📁 Project Structure

```
.
├── add_new_word.py       # Add new words to JSON
├── create_game.py        # Launch training game
├── delete.py             # Delete words from JSON
├── edit_controller.py    # Command-line word manager
├── loading_feature.py    # Loading animation
├── main.py               # Main menu (entry point)
├── play_test.py          # Test mode
├── play_training.py      # Training mode
├── print_options.py      # Prints menu options
├── print_words.py        # Prints vocabulary
├── update.py             # Update word meanings
├── vocabulary.json       # Word database
└── .gitignore            # Ignore __pycache__/
```

---

## 🚀 Getting Started

1. **Install Python** (if not installed)
2. Run the main script:

```bash
python main.py
```

---

## 🎮 Menu Options

- `1`: Start Training Game  
- `2`: Edit Vocabulary (Add / Update / Delete)  
- `3`: Show Menu Options  
- `4`: Show All Words  
- `5`: Exit

---

## ✏️ Word Format (vocabulary.json)

```json
{
  "unit_1": [
    {
      "word": "apple",
      "meaning": "תפוח"
    }
  ]
}
```