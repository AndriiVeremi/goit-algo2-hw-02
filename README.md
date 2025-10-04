# Homework: Fundamentals of Analysis and Algorithmic Strategies

This project contains the implementation of two algorithmic tasks.

---

### 1. Task 1: Min/Max Search

An implementation of a recursive search for the minimum and maximum elements in an array using the "Divide and Conquer" principle.

*   **Time Complexity:** `O(n)`
*   **Space Complexity:** `O(log n)` (due to the recursion stack)

---

### 2. Task 2: 3D Printer Queue Optimizer

A greedy algorithm for optimizing a 3D print queue. Jobs are sorted by priority, after which print batches are formed, taking into account the printer's constraints on volume and number of models. The execution time of a batch is determined by the longest job in it.

*   **Time Complexity:** `O(n log n)` (due to sorting)
*   **Space Complexity:** `O(n)`

---

### 🚀 How to Run

Run the main script and select the desired task from the interactive menu.

```bash
python3 main.py
```

---

### 📂 File Structure

```
goit-algo2-hw-02/
├─ main.py
├─ README.md
├─ .gitignore
├─ task_1/
│  └─ task.py
└─ task_2/
   └─ task2.py
```