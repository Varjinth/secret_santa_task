# secret_santa_task


This project automates the **Secret Santa gift exchange process**. It ensures a fair and randomized assignment of gift recipients ("secret children") to employees, following business constraints and using a modular, extensible, and testable Python-based design.

---

## 📘 Overview

### 🎯 Objective

- To build a system that reads a CSV file of employee data and assigns each employee a unique secret child.
- To ensure **no employee is assigned to themselves**.
- To ensure **no employee is assigned the same person as last year** (if previous assignment data is provided).
- To ensure **one-to-one mapping** — each employee gives and receives exactly one gift.

---

## 🔧 Features

-  One-to-one, conflict-free Secret Santa assignment
-  Previous year conflict avoidance
-  Input/Output CSV support
-  Self-assignment prevention
-  Modular and OOP-friendly codebase
-  Includes unit tests

---

## 🛠 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Varjinth/secret_santa_task.git
cd secret_santa_task
bash```

Place your input CSV files in the data/ folder:
Required:
employees.csv — list of employees with name and email

Optional:
last_year_assignments.csv — prevents assigning the same person as last year


Run the program
```bash
Copy
Edit
python main.py
 After running, check output/this_year_assignments.csv for the results.


