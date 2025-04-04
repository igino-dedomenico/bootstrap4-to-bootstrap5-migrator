# 🔄 Bootstrap 4 to Bootstrap 5 Migration Script

A fully customizable Python script that **automatically updates HTML and Angular TypeScript files** from [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) to [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/).  
This tool is designed to **simplify your migration process**, saving time and reducing errors when upgrading legacy Bootstrap 4 projects.

---

## 🚀 Features

- ✅ Automatic migration of Bootstrap 4 class names to Bootstrap 5.
- ✅ Supports `.html` and `.ts` files (Angular friendly).
- ✅ Easy to configure source and output folders.
- ✅ Regex-based replacement system for easy customization.
- ✅ Lightweight, no dependencies needed beyond Python standard library.

---

## 🧩 How It Works

This script performs **pattern-based replacements** on Bootstrap 4 syntax to convert it to Bootstrap 5 equivalents. It also updates Angular-specific decorators like `@ViewChild` and `@ViewChildren`.

---

## 🔧 Setup Instructions

### 1. Requirements

- Python 3.6+
- A folder with your **Bootstrap 4** files

### 2. Installation

Clone or download this repository, then place your Bootstrap 4 files in the `./bootstrap4-html` folder:

```bash
git clone https://github.com/igino-dedomenico/bootstrap4-to-bootstrap5-migrator.git
cd bootstrap4-to-bootstrap5-migrator
```

Place your files in `bootstrap4-html/`.

---

## ⚙️ Configuration

Edit the Python script to customize:

```python
SOURCE_FOLDER = "./bootstrap4-html"  # Input folder
OUTPUT_FOLDER = "./bootstrap5-html"  # Output folder
```

You can also edit the `REPLACEMENTS` list to add or remove Bootstrap class transformations:

```python
REPLACEMENTS = [
    (r'form-group', 'mb-3'),
    (r'float-left', 'float-start'),
    ...
]
```

---

## ▶️ How to Run

Once configured, run the script:

```bash
python migrate_bootstrap.py
```

The updated files will be saved to the `bootstrap5-html/` folder.

---

## 📝 Example Replacements

| Bootstrap 4          | Bootstrap 5          |
|----------------------|----------------------|
| `form-group`         | `mb-3`               |
| `float-left`         | `float-start`        |
| `ml-3`               | `ms-3`               |
| `badge-pill`         | `badge rounded-pill` |
| `@ViewChild(...)`    | `@ViewChild(..., { static: false })` |

---

## 🔄 Customization Tips

- **Add new patterns**: You can insert your own regex replacements to handle custom class names.
- **Process other file types**: Add more extensions in the file filter (e.g. `.jsx`, `.tsx`).
- **Update Angular logic**: Extend TypeScript replacements for Angular or other frameworks.

---

## 📈 SEO Keywords

**bootstrap 4 to bootstrap 5 migration**, **convert bootstrap classes**, **html migration tool**, **angular viewchild update**, **automatic bootstrap upgrade**, **bootstrap upgrade script**, **python bootstrap migrator**

---

## 🛠 Contributing

Feel free to open issues or submit pull requests to extend the supported class replacements or features.

---

## 📄 License

MIT License - Use, modify, and distribute freely.
