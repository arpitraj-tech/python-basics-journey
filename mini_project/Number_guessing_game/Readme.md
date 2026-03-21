# 🎯 Number Guessing Game

A fun little **Number Guessing Game** built with Python!
The computer picks a secret number — you try to guess it. Too high? Too low? Keep going until you nail it! 🎉

> *Made purely for fun — a great little game to kill time and challenge yourself!*

---

## 🎮 How to Play

```
please enter the length of digits you want to guess: 3

please enter your no.: 500
ops! your no. is smaller please retry

please enter your no.: 750
ops! your number is greater please retry

please enter your no.: 623
hurray!! your guess was correct in '3' turns 🎉
```

---

## ✨ What Makes it Fun

- 🎲 **You choose the difficulty** — pick how many digits the secret number has
- 🔼🔽 **Hot & Cold hints** — instantly told if your guess is too high or too low
- 📊 **Turn counter** — tracks how many attempts it took you to win
- 🔁 **Replay anytime** — just run it again for a brand new number!
- 🧠 **Tests your logic** — the longer the number, the harder the challenge!

---

## 📁 Project Structure

```
number-guessing-game/
│
├── functions.py     # Generates the secret random number
├── main.py          # Game loop — takes guesses & gives hints
└── README.md        # You're reading it!
```

---

## ⚙️ Requirements

- Python **3.x** only
- No libraries to install — uses only the built-in `random` module!

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game
```

**2. Start the game!**
```bash
python main.py
```

---

## 🎯 Difficulty Guide

| Digits | Example Number | Difficulty |
|--------|---------------|------------|
| `1` | 7 | 😴 Too Easy |
| `2` | 43 | 🙂 Warm Up |
| `3` | 628 | 😤 Getting Real |
| `4` | 3174 | 🔥 Hard |
| `5` | 89423 | 💀 Madness |

> **Pro tip:** Try to guess in the fewest turns possible — the real challenge is beating your own record! 🏆

---

## 🔬 How It Works

```python
# functions.py — generates the secret number

# 1. Picks random unique digits using random.sample()
# 2. Makes sure the number doesn't start with 0
# 3. Returns the number as a string (converted to int in main.py)

# main.py — runs the game loop
# 1. You enter how many digits you want
# 2. Secret number is generated silently
# 3. You keep guessing — getting "too small" or "too big" hints
# 4. Game ends when you guess correctly & shows your attempt count
```

---

## 🧠 Module Used

| Module | Purpose |
|--------|---------|
| `random` | `random.sample()` to pick unique digits for the secret number |

---

## 🔮 Ideas to Make it Even More Fun

- [ ] **Best score tracker** — save your personal best (fewest turns)
- [ ] **Time challenge** — race against a timer
- [ ] **Multiplayer mode** — two players take turns guessing
- [ ] **Hint limit** — limit the number of guesses (game over if exceeded)
- [ ] **Leaderboard** — save top scores to a file

---



## 📄 License

This project is open source and available under the [MIT License](LICENSE).
