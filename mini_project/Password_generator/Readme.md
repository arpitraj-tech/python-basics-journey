# 🔐 Password Generator

A lightweight **Password Generator** built with Python.
Generate secure, randomized passwords in three strength levels — Easy, Medium, or Hard — instantly from your terminal.

---

## 📸 Preview

```
Please tell the level of password u wanna generate easy medium hard: hard

Your Generated password is : k3J!mZ9#nA$2
```

---

## 🚀 Features

- 🟢 **Easy** — Lowercase + Uppercase letters (8 characters)
- 🟡 **Medium** — Lowercase + Uppercase + Numbers (8 characters)
- 🔴 **Hard** — Lowercase + Uppercase + Numbers + Symbols (12 characters)
- 🔀 **Randomized every time** — Uses `random.sample()` + `random.shuffle()` for true randomness
- ✅ **Input validation** — Loops until a valid level is entered
- ⚡ **Zero dependencies** — Only Python built-ins needed

---

## 📁 Project Structure

```
password-generator/
│
├── function.py      # Core logic — password_generator(level) function
├── main.py          # Entry point — takes input & calls the generator
└── README.md        # You're reading it!
```

---

## ⚙️ Requirements

- Python **3.x** only
- No external libraries — uses only the built-in `random` module

---

## 🛠️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

**2. Run the app**
```bash
python main.py
```

---

## 📖 Password Levels Explained

| Level | Lowercase | Uppercase | Numbers | Symbols | Total Length |
|-------|-----------|-----------|---------|---------|-------------|
| `easy` | ✅ 6 chars | ✅ 2 chars | ❌ | ❌ | **8 characters** |
| `medium` | ✅ 3 chars | ✅ 2 chars | ✅ 3 chars | ❌ | **8 characters** |
| `hard` | ✅ 3 chars | ✅ 3 chars | ✅ 3 chars | ✅ 3 chars | **12 characters** |

**Symbols used in Hard mode:** `! @ # $ % &`

---

## 🧪 Sample Output

```
# Easy
Your Generated password is : mKrzpJqt

# Medium
Your Generated password is : p7Kn3mA9

# Hard
Your Generated password is : r!3Km#9nZ$pA
```

> Every run produces a **different password** — even for the same level.

---



---

## 🧠 Modules Used

| Module | Type | Purpose |
|--------|------|---------|
| `random` | Built-in | `random.sample()` to pick unique chars, `random.shuffle()` to randomize order |

---



