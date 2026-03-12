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

Універсальний модуль для роботи з JSON‑файлами у Python.  
Надає зручні функції для:

- пошуку кореня проєкту (`find_project_root`)
- збереження JSON у будь‑яку директорію (`save_json`)
- завантаження JSON з будь‑якої директорії (`load_json`)

Модуль побудований на `pathlib` та підтримує автоматичне створення директорій.

## 🚀 Можливості

✔️ Автоматичний пошук кореня проєкту  
✔️ Гнучке збереження JSON у будь‑який шлях  
✔️ Завантаження JSON з будь‑якого шляху  
✔️ Автоматичне створення директорій  
✔️ Обробка помилок через декоратори  
✔️ Підтримка UTF‑8 та форматування JSON  
✔️ Безпечне додавання нових елементів у список JSON  


## 📂 Структура проєкту (приклад)
```
project_root/
├── 📄 main.py
├── 📄 save_load.py
└── 📁 data/
    └── 📁 files_json/
        └── 📄 example.json
```
## 📦 Встановлення

Просто додайте файл `save_load.py` у свій проєкт і імпортуйте функції:

```python
from save_load import save_json, load_json, append_to_json_file
```

## 🧠 Використання
🔹 Збереження JSON у довільний шлях
```python
save_json(
    data={"name": "Serhii", "age": 30},
    file_name="user.json",
    relative_path="data/files_json"
)
```
🔹 Завантаження JSON
```python
data = load_json(
    file_name="user.json",
    relative_path="data/files_json"
)
print(data)
```

## 🧩 Документація функцій

✔️`find_project_root(marker_file="main.py")`

Піднімається вгору по директоріях, поки не знайде файл‑маркер.
Повертає шлях до кореня проєкту.

✔️`save_json(data, file_name, relative_path=None)`

Зберігає JSON у вказаний шлях відносно кореня проєкту.
* автоматично створює директорії
* зберігає у UTF‑8
* форматування indent=4

✔️`load_json(file_name, relative_path=None)`

Завантажує JSON з вказаного шляху.
* повертає Python‑об’єкт
* піднімає помилки, якщо файл не знайдено або JSON пошкоджений

## 🛠 Вимоги

* Python 3.8+
* Модулі:
    * json
    * pathlib

## 👤 Автор
Serhii Olkhovskyi  
GitHub: https://github.com/Olkhovskyi-Serhii
