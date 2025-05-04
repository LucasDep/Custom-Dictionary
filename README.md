# 📝 Custom Dictionary (Thread-Safe) with CLI

This project is a thread-safe, in-memory dictionary that allows you to:

- Add words
- Search for words
- Auto-complete words by prefix
- Remove words
- Save the dictionary to a file
- Load the dictionary from a file
- Unit testing (via `unittest`)
- Stress Unit testing (via `unittest`)
- Interact with a simple Command-Line Interface (CLI)

Built entirely in Python — no external libraries required.

---

## ▶️ How to Run the Program

```bash
python custom_dictionary.py
```

## 🧪 How to Run Unit Tests
This project uses Python’s built-in unittest. No installation needed.

### 📦 Run Unit Tests (Simple)

```bash
python test_custom_dictionary.py
```

### ⚡ Run Unit Tests (Stress)

```bash
python test_custom_dictionary_stress.py
```

### ▶️ Run with Discovery (If you have multiple test files)

```bash
python -m unittest discover
```

---

## 🚀 Console input examples for each Feature

### ✅ Add a Word
```bash
add cat
```

### 🔍 Search a Word
```bash
search cat  # Returns True/False
```

### 🤖 Auto-complete
```bash
autocomplete ca # e.g., ['cat', 'car', 'carbon']
```

### ❌ Remove a Word
```bash
remove cat  # Returns True if removed
```

### 💾 Save to File
```bash
save my_dict.txt
```

### 📂 Load from File
```bash
load my_dict.txt
```

### 🚪 Exit the Program
```bash
exit
```

---

## 📂 Project Structure

```bash
Custom-Dictionary/
├── custom_dictionary.py                # Core dictionary logic (thread-safe)
├── test_custom_dictionary.py           # Unit tests
├── test_custom_dictionary_stress.py    # Stress Unit tests
├── dictionary_cli.py                   # Command-Line Interface (CLI) app
├── README.md                           # (this file)