# BCA-1

My programming work while pursuing an Online BCA at Manipal University Jaipur, built alongside a self-directed 3-year roadmap toward becoming an AI/ML engineer. Started August 2026.

The repo is split into two folders:
- **`projects/`** — real builds: fundamentals, file handling, and OOP
- **`leetcode/`** — DSA practice problems, solved and pushed as they're completed

Each project follows the same reflection format: **what it does, why I built it, what I'd do differently.**

---

## 🚀 Projects

### Tic-Tac-Toe
**What it does:** A command-line two-player game. Maps a 3x3 grid to a single flat list (index 0-8), prints the board after every move, and checks all 8 win combinations (3 rows, 3 columns, 2 diagonals) after each turn.

**Why I built it:** To practice mapping 2D coordinates onto a 1D data structure, and to work with nested win-condition logic.

**What I'd do differently:** I originally had the draw-check run *before* the win-check, which meant a winning final move on the last empty square got misreported as a draw — Python hit the draw condition and broke out of the loop before ever calling `check_win()`. Fixed it by reordering the checks so a win is always tested first. Next time, I'd refactor the board into a `Board` class from the start instead of a plain list, and add a replay loop like my other games have.

---

### Dynamic Quiz App
**What it does:** A command-line trivia game that reads questions, four options, and the correct answer from an external `questions.csv` file using `csv.DictReader`, then tracks and reports a final score.

**Why I built it:** To practice reading structured external data instead of hardcoding everything into the script.

**What I'd do differently:** Shuffle the question order and the answer options on each run so the quiz isn't identical every time. Also add input validation so a typo doesn't silently count as a wrong answer.

---

### Contact Book
**What it does:** Stores contacts (name, phone, email) as dictionaries in a list, with add, view, and delete options. Persists data to a text file (`contact.txt`) so contacts survive between runs.

**Why I built it:** To practice file persistence and using a `for...else` loop for the delete-by-name search.

**What I'd do differently:** Switch from manually parsing comma-separated lines to using Python's `json` module for storage — it would be far more robust than string-splitting, especially once names or emails contain commas. I'd also add an "edit contact" option.

---

### Number Guessing Game
**What it does:** The computer picks a random number between 1 and 100; the player has 7 attempts to guess it, with "too high / too low" hints after each try.

**Why I built it:** To practice `while` loops, attempt counting, and handling invalid (non-numeric) input without crashing.

**What I'd do differently:** Track and display the player's best (fewest-attempts) score across rounds, and let the player choose a difficulty level that changes the number range and attempt limit.

---

### Rock, Paper, Scissors
**What it does:** Plays rounds of rock-paper-scissors against the computer using Python's `random` module, tracking wins, losses, and ties across the session.

**Why I built it:** To practice conditional logic across three possible player choices and three possible outcomes.

**What I'd do differently:** Replace the long `if/elif` chain with a lookup dictionary (e.g., mapping each choice to what it beats) — it would cut the logic down significantly and make it easier to extend to variants like rock-paper-scissors-lizard-spock.

---

### Unit Converter
**What it does:** Converts between km/miles, kg/lbs, and meters/feet based on a menu choice, using fixed conversion constants.

**Why I built it:** To practice building a simple menu-driven program with multiple independent operations.

**What I'd do differently:** Store the conversions in a dictionary keyed by choice, and split each conversion into its own small function, instead of one long `if/elif` block.

---

### Calculator
**What it does:** Performs addition, subtraction, multiplication, and division on two user-entered numbers in a loop, with error handling for invalid (non-numeric) input and division by zero.

**Why I built it:** My first real project — to practice `try/except` for input validation and basic control flow.

**What I'd do differently:** Add a visible prompt for the operator (right now it's a bare `input()` with no text), support for more operations (like exponents), and split the arithmetic into separate functions.

---

### Binary Search
**What it does:** Searches a sorted list for a target number by repeatedly checking the middle element and cutting the remaining search range in half, instead of scanning item by item.

**Why I built it:** To implement a classic algorithm from scratch and understand why it runs in O(log n) instead of O(n) — a search that stays fast even as the list grows enormously (roughly 10 comparisons for 1,000 items, ~20 for a million, ~30 for a billion).

**What I'd do differently:** My first version compared `mid` (a list position) directly to the target value, instead of comparing `list[mid]` (the value stored at that position) — so it never actually found anything that wasn't sitting at the exact position the math landed on. Fixed by indexing into the list with `list[mid]` on every comparison. Next time, I'd write it as a reusable function that takes any sorted list and target, instead of a fixed script.

---

### Bank Account Simulation (OOP)
**What it does:** An `Account` class that models a bank account — stores an account number, name, and balance, supports depositing and withdrawing money (with overdraft protection that blocks a withdrawal larger than the current balance), and keeps a running transaction history as a list of `(type, amount)` tuples. A `SavingAccount` subclass extends `Account` using inheritance and `super().__init__()`, adding an `interest_rate` and an `add_interest()` method that grows the balance independently of the base class's logic.

**Why I built it:** My first real Object-Oriented Programming project — to practice `class`, `__init__`, and `self`, and to move from function-based scripts to bundling data and behavior together. `SavingAccount` was added afterward to practice inheritance — reusing `Account`'s deposit/withdraw/history behavior without rewriting any of it.

**What I'd do differently:** After building the first working version, I tested myself by closing the file and rewriting `deposit` and `withdraw` from memory, with no autocomplete. Two real bugs showed up: the overdraft check had silently dropped to just `amount > 0` (no longer checking against the balance), and a typo mismatch between `acc_transaction` and `acc_transactions` would have crashed the program the first time a transaction was logged. Fixing both by hand, without help, is what's actually in this repo now. Next time, I'd add a `transfer` method between two accounts, and store transactions as small dictionaries instead of tuples so each entry could carry a timestamp too.

---

### To-Do List Manager (OOP)
**What it does:** A command-line application using a custom class to manage state. It features an infinite application loop that routes user inputs to add, view, and delete tasks directly from a list.

**Why I built it:** To reinforce Object-Oriented Programming (OOP) concepts by writing state and behavior logic entirely from scratch without autocomplete, and to transition from a GUI version control tool to executing raw Git commands via the terminal.

**What I'd do differently:** During development, I accidentally treated a list of strings like a list of dictionaries inside my delete method. I fixed it by dropping the complex loop and using Python's built-in `in` operator and `.remove()` method. Next time, I would add `.strip().lower()` to the search logic so that user input becomes case-insensitive.

---

## 🧩 LeetCode Practice (`leetcode/`)

| # | Problem | Approach | Result |
|---|---------|----------|--------|
| 001 | Two Sum | Brute force, nested loops | Accepted |
| 002 | Palindrome Number | First: string slicing. Optimized: modulo/floor division, no string conversion | Accepted |
| 003 | Contains Duplicate | Hash set with early exit | Accepted, O(n) time/space |
| 004 | Valid Anagram | Hash map frequency counting | Accepted |
| 005 | Group Anagrams (Medium) | Sorted-word as dictionary key, grouping into lists | Accepted, beats 95% runtime |

Each problem was attempted from scratch before any help — including a full rebuild of the nested-loop logic for Two Sum after initially blanking on how to translate the idea into code.

---

## 🧠 Core Skills Demonstrated

*   **File Handling (I/O):** Reading and writing external data using Python's `csv` module and plain text files.
*   **Data Structures:** Lists, nested dictionaries, tuples, sets, and 1D-to-2D grid mapping.
*   **Control Flow:** Game loops built with `for` loops, `while` loops, `if/elif/else`, and a `for...else` search pattern.
*   **Input Validation:** `try/except` blocks to catch invalid input across every project rather than letting the program crash.
*   **Debugging:** Found and fixed real logic bugs in Tic-Tac-Toe (draw-check running before win-check) and Binary Search (comparing a position to a value instead of the value stored at that position), in both cases by tracing execution step by step and constructing a specific test case to confirm the fix.
*   **Algorithms:** Implemented binary search from scratch and can explain why it runs in O(log n). Solved 5 LeetCode problems independently, including one Medium (Group Anagrams) with a top-5% runtime.
*   **Object-Oriented Programming:** Built a bank account simulation using `class`, `__init__`, and `self` — with overdraft protection and transaction history — then extended it with inheritance (`SavingAccount(Account)` using `super()`).
*   **Self-Testing:** Verified the OOP project actually stuck by rewriting it from memory with no autocomplete, and caught two real bugs (a dropped overdraft check, a naming typo) doing so.
*   **Version Control:** Managing staging, commits, and pushing entirely via the terminal (`git add`, `git commit`, `git push`) rather than a GUI tool.
*   **Terminal Navigation:** Comfortable with `pwd`, `ls`, `cd`, `mkdir`, and `rm -r` for everyday file navigation.
*   **Virtual Environments:** Created and activated a `venv`, installed a package inside it, and verified isolation by comparing `pip list` inside vs. outside the environment.
*   **Problem Journal:** A running log (`leetcode/JOURNAL.md`) of what was tried and what clicked for each LeetCode problem — including the ones where I leaned on outside help more than others.

## 🔜 Coming Next

*   **Discrete Math:** Started with Neso Academy's Discrete Mathematics series — covered discrete vs. continuous, and built AND/OR truth tables by hand. Propositional logic and set theory are next.
*   **Linear Algebra Intuition:** Vectors, scalar multiplication, and dot products (Month 5-6 math thread).
