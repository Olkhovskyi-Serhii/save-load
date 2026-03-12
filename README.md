<p align="center">
  <img src="https://img.shields.io/badge/Save%20%26%20Load-Utilities-blue?style=for-the-badge&logo=python&logoColor=white" alt="Save & Load Utilities Banner">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" alt="Project Status">
</p>

🌐 Available languages: [English](README.md) | [Українська](README_UA.md)


# Save & Load Utilities

A lightweight utility module for safe and convenient JSON file operations in Python.  
It provides functions for:

- detecting the project root (`find_project_root`)
- saving JSON to any custom path (`save_json`)
- loading JSON from any custom path (`load_json`)

The module uses `pathlib` and automatically creates required directories.



## 🚀 Features

✔️ Automatic project root detection  
✔️ Flexible JSON saving to any directory  
✔️ JSON loading from any directory  
✔️ Automatic directory creation  
✔️ UTF‑8 support and pretty formatting  
✔️ Error handling via decorators  



## 📂 Example Project Structure

```
project_root/
├── 📄 main.py
├── 📄 save_load.py
└── 📁 data/
    └── 📁 files_json/
        └── 📄 example.json
```
## 📦 Installation

Simply include `save_load.py` in your project and import the functions:

```python
from save_load import save_json, load_json
```

## 🧠 Usage
🔹 Save JSON to a custom path
```
save_json(
    data={"name": "Serhii", "age": 30},
    file_name="user.json",
    relative_path="data/files_json"
)
```
🔹 Load JSON
```
data = load_json(
    file_name="user.json",
    relative_path="data/files_json"
)
print(data)
```
🔹 Save to project root

```
save_json({"debug": True}, "config.json")
```
🔹 Load from project root
```
config = load_json("config.json")
```
## 🧩 Function Documentation
✔️`find_project_root(marker_file="main.py")`

Traverses upward until the marker file is found.
Returns the absolute path to the project root.

✔️`save_json(data, file_name, relative_path=None)`

Saves JSON to a custom path relative to the project root.

* automatically creates directories
* saves in UTF‑8
* formats JSON with indent=4

✔️`load_json(file_name, relative_path=None)`

Loads JSON from a custom path.

* returns a Python object
* raises errors if the file is missing or corrupted

## 🛠 Requirements

* Python 3.8+
* Modules:
    * json
    * pathlib


## 👤 Author
Serhii Olkhovskyi  
GitHub: https://github.com/Olkhovskyi-Serhii
