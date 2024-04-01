# 📝 CLI To-Do List Manager (Python)

A simple command-line to-do list application written in Python. This project allows you to add, view, complete, and remove tasks directly from your terminal, with tasks saved persistently to a JSON file.

## 📦 Features

- ✅ Add new tasks with descriptions  
- 📋 List all tasks with status  
- ✔️ Mark tasks as complete  
- ❌ Remove tasks by ID  
- 💾 Persistent storage using `todo.json`

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/TOBEDO47/todo-cli.git
cd todo-cli

Usage
Use the Python script with the following commands:

Add a Task:
python todo.py add "Your task description here"

List All Tasks:
python todo.py list

Remove a Task:
python todo.py remove <task_id>

Complete a Task:
python todo.py complete <task_id>

Example:
python todo.py add "Study for CSE exam"
python todo.py list
python todo.py complete 1
python todo.py list
python todo.py remove 1
