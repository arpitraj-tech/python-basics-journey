# 📝To-Do List Manager

A simple yet functional **command-line To-Do List application** built with Python.
Manage your tasks right from the terminal — add, update, delete, and view tasks with persistent JSON storage.

---

## 📸 Preview

```
               welcome to to do list               
1. add task
2. update task
3. delete task
4. show tasks
5. Exit

Please type the option (1,2,3,4,5) to proceed:
```

---

## 🚀 Features

- ✅ **Add tasks** — with Done / Not Done status
- ✏️ **Update tasks** — change task status anytime
- 🗑️ **Delete tasks** — remove tasks by serial number
- 📋 **View all tasks** — display full task list with status
- 💾 **Persistent storage** — all data saved in `data.json`
- 🖥️ **Auto screen clear** — clean UI after each action

---

## 📁 Project Structure

```
todo-list/
│
├── main.py          # Entry point — menu loop & navigation
├── functions.py     # Core logic — add, update, delete, show
├── data.json        # Task storage (auto-created/updated)
└── README.md        # You're reading it!
```

---

## ⚙️ Requirements

- Python **3.x** (no external libraries needed)
- Uses only built-in modules: `json`, `os`, `time`

---

## 🛠️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/todo-list.git
cd todo-list
```

**2. Run the app**
```bash
python main.py
```

> Make sure `data.json`, `functions.py`, and `main.py` are all in the **same folder**.

---

## 📖 How to Use

| Option | Action | Description |
|--------|--------|-------------|
| `1` | Add Task | Enter task name, then set status as `done` or `not done` |
| `2` | Update Task | Enter serial no. → change task status |
| `3` | Delete Task | Enter serial no. of task to remove |
| `4` | Show Tasks | Displays all tasks with their current status |
| `5` | Exit | Closes the application |

### Example Session

```
Please type the option (1,2,3,4,5) to proceed: 1

please enter the task u wanna add: Buy groceries
tell whether task is done or not done: not done
task Buy groceries updated successfully

---

Please type the option (1,2,3,4,5) to proceed: 4

1 - task-> Buy groceries : status-> status = Not done
2 - task-> Submit assignment : status-> status = Done
```

---

## 🗄️ Data Storage Format

Tasks are stored in `data.json` in the following format:

```json
{
    "task_history": [
        [{"Buy groceries": "status = Not done"}],
        [{"Submit assignment": "status = Done"}]
    ]
}
```

---

## 🧠 Modules Used

| Module | Purpose |
|--------|---------|
| `json` | Read & write task data to `data.json` |
| `os` | Detect OS to clear terminal (`cls` / `clear`) |
| `time` | Pause screen after actions for better UX |

---


