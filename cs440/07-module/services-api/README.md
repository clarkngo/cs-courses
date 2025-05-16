# 🧪 Git Practice Lab with Flask Mini App

This lab uses a simple Flask-based to-do app to walk you through essential Git workflows.

---

## 📋 Project Overview

**Features:**
- Add a task: POST `/add`
- List tasks: GET `/list`
- Delete a task: DELETE `/delete/<task_id>`

---

## 🧩 Git Exercises Breakdown

| Task   | Git Concepts                | Learning Outcome                      |
|--------|-----------------------------|----------------------------------------|
| Part 1 | Clone, Commit, Branch       | Basic Git workflow                     |
| Part 2 | Merge Conflict              | Conflict resolution                    |
| Part 3 | History Tools               | Debugging with `log`, `diff`, `blame`  |
| Part 4 | Mistake Recovery            | Reset, Revert, Stash                   |
| Part 5 | Collaborative Pull Requests | Merge PRs, resolve online              |

---

## ✅ Instructions

### 🔹 Part 1: Run, Commit, Branch

- Go to project folder `cd git-flask-lab`
- Run app `flask --app app.todo run`
- Open a new terminal
- Go to project folder `cd git-flask-lab`
- Run tests `python -m unittest discover tests`
- Create a new branch `feature/due-date`
- Modify `add_task()` to accept an optional `"due_date"` field
- Commit the changes with a clear message

---

### 🔹 Part 2: Merge Conflict (Solo Simulated)

- Create branch `bugfix/approach-a`: Fix `delete_task()` using an `if` check
- Create branch `bugfix/approach-b`: Fix `delete_task()` using `try/except`
- Merge both into main to trigger a conflict
- Resolve the conflict manually

---

### 🔹 Part 3: Git History Tools

Run the following and write observations in `answers/part3.md`:
- `git log --oneline`
- `git diff HEAD~1`
- `git blame app/todo.py`

---

### 🔹 Part 4: Mistake Recovery

- Make and commit a bad change (e.g. remove all tasks from `/list`)
- Use:
  - `git reset` (soft)
  - `git revert` (clean history)
  - `git stash` (temporary save)

---

### 🔹 Part 5: Pull Request Simulation

- Push a new branch with a new feature or test
- Open a Pull Request on GitHub
- Leave a comment, merge using "Squash and Merge"
- Document what happened in `answers/part5.md`

---

## 🧪 Run and Test

Install Flask:
```bash
cd git-flask-lab
pip install -r requirements
