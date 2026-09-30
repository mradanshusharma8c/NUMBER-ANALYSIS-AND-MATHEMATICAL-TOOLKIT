# 🧮 Math Toolkit

> A modular, menu-driven Python console application with **14 number & math utilities** — built for the *VITyarthi – Build Your Own Project* evaluation.

| | |
|---|---|
| **Student** | Mradanshu Sharma |
| **Registration No.** | 26BAI10712 |
| **School** | School of Computer Science and Artificial Intelligence (SCAI) |
| **University** | VIT Bhopal University |
| **Course** | Introduction to Problem Solving and Programming |
| **Session** | 2026 – 2030 |

---

## 📖 Overview

Math Toolkit is a command-line program that bundles the most common number-based problems learned in an introductory programming course — prime checking, factors, GCD, Fibonacci, binary conversion and more — into one easy menu. A special **Full Analysis** option runs several of these together on a single number and prints a complete report.

The project is split into **7 clean modules** (plus a test suite), uses only the Python standard library, and validates every input so the program never crashes on bad data.

## ✨ Features

**Module 1 – Number Theory**
1. Check Prime
2. Find Factors
3. Prime Factorization
4. Find GCD (Euclidean algorithm)
5. Smallest Divisor

**Module 2 – Sequences**
6. Factorial
7. Fibonacci series

**Module 3 – Converters**
8. Reverse a number
9. Decimal → Binary
10. Character → ASCII number

**Module 4 – Math Operations**
11. Square root
12. Power
13. Random number in a range

**Module 5 – Full Analysis**
14. Even/Odd, prime, smallest divisor, factors, reverse and binary — all in one report

**Extra:** input validation with re-prompting, friendly error messages, 17 unit tests.

## 🛠️ Technologies Used

- **Python 3.8+** (standard library only – `random`, `unittest`)
- **unittest** + `unittest.mock` for testing
- **Git & GitHub** for version control

## 📁 Project Structure

```
math-toolkit/
├── main.py                  # Entry point
├── toolkit/
│   ├── __init__.py
│   ├── number_theory.py     # prime, factors, GCD, divisors
│   ├── sequences.py         # factorial, Fibonacci
│   ├── converters.py        # reverse, binary, char code
│   ├── math_ops.py          # sqrt, power, random
│   ├── analysis.py          # full analysis report
│   ├── validators.py        # safe input helpers
│   └── menu.py              # menu / user interface
├── tests/
│   └── test_toolkit.py      # 17 unit tests
├── docs/screenshots/        # program screenshots
├── README.md
├── statement.md
└── .gitignore
```

## 🚀 How to Install & Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/math-toolkit.git
cd math-toolkit

# 2. Make sure Python 3.8+ is installed
python --version

# 3. Run the program (no extra packages needed)
python main.py
```

## 🧪 How to Test

```bash
python -m unittest discover tests -v
```

Expected result: `Ran 17 tests ... OK`

## 📸 Screenshots

| Check Prime | Full Analysis |
|---|---|
| ![Prime](docs/screenshots/01_prime_check.png) | ![Analysis](docs/screenshots/02_full_analysis.png) |

| Input Validation | Unit Tests |
|---|---|
| ![Validation](docs/screenshots/03_input_validation.png) | ![Tests](docs/screenshots/04_unit_tests.png) |

## 🔮 Future Enhancements

GUI using Tkinter, history log file, more number-theory tools (LCM, perfect numbers, Armstrong numbers).

## 👤 Author

**Mradanshu Sharma (26BAI10712)** — B.Tech, SCAI, VIT Bhopal University (2026–2030)

