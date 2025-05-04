# 📝 Custom Dictionary (Thread-Safe) with CLI

This project is a thread-safe, in-memory dictionary that allows you to:

- Add words
- Search for words
- Auto-complete words by prefix
- Remove words
- Save the dictionary to a file
- Load the dictionary from a file
- Unit testing (via `unittest`)
- Interact with a simple Command-Line Interface (CLI)

Built entirely in Python — no external libraries required.

---

## 🚀 Features

### ✅ Add a Word
```python
dictionary.add_word("cat")
add cat
```

### 🔍 Search a Word
```python
dictionary.search_word("cat") # Returns True/False
search cat  # Returns True/False
```

### 🤖 Auto-complete
```python
dictionary.auto_complete("ca")  # e.g., ['cat', 'car', 'carbon']
autocomplete ca # e.g., ['cat', 'car', 'carbon']
```

### ❌ Remove a Word
```python
dictionary.remove_word("cat")  # Returns True if removed
remove cat  # Returns True if removed
```

### 💾 Save to File
```python
dictionary.save_to_file("my_dict.txt")
save my_dict.txt
```

### 📂 Load from File
```python
dictionary.load_from_file("my_dict.txt")
load my_dict.txt
```

### 🚪 Exit the Program
```python
exit
```

---

## 📂 Project Structure

```bash
Custom-Dictionary/
├── custom_dictionary.py        # Core dictionary logic (thread-safe)
├── test_custom_dictionary.py   # Unit tests
├── dictionary_cli.py           # Command-Line Interface (CLI) app
├── README.md                   # (this file)