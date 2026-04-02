# 🔢 Chapter 3 — Python Numbers

## 📌 What I Learned
Python number types and math operations
for Data Engineering.

## 🛠️ Topics Covered

| Topic | Details |
|-------|---------|
| int & float | Whole numbers vs decimals |
| Math Operators | +, -, *, /, //, **, % |
| Modulus % | Find remainder — even/odd check |
| Rounding | round(), ceil(), floor() |
| Random | randint(), random() |
| Validation | isnumeric(), isdigit() |

## 🚀 Challenge Solved

**Generate random number + check even/odd**

Input: Random integer between 1 and 100
Output: Number + whether it is even or odd
```python
import random
num = random.randint(1, 100)
print(f"Number: {num}")
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
```

## 📸 Output Screenshots
[![Challenge Output](./Screenshot%202026-04-02%20152141.png)]

## 💡 Key Learning
Modulus operator `%` is used in 
data pipelines for batch processing —
e.g. process every 100th record.
