# 🧵 Chapter 2 — Python Strings

## 📌 What I Learned

Python String methods for Data Engineering 
— cleaning, transforming, and parsing 
real-world messy data.

## 🛠️ Methods Covered

| Category | Methods |
|----------|---------|
| Transform | replace(), split(), f-string, join() |
| Cleaning | strip(), lstrip(), rstrip(), lower(), upper() |
| Search | find(), startswith(), endswith(), in |
| Validation | isdigit(), isalpha(), isnumeric() |
| Slicing | text[0], text[1:3], text[-1] |
| Filter | filter(str.isdigit, text) |

## 🚀 Challenges Solved

### Challenge 1 — Messy String Cleaner
**Input:** `"968-maria, (D@t@ Engineer);; 27y"`  
**Output:** `name: maria | role: data engineer | age: 27`  
Solved 2 ways — Slicing + Split()

### Challenge 2 — Employee Data Parser  
**Input:** `"EMP101#Zaid_Khan*| ( Python-Developer ) |; Salary-85k++"`  
**Output:** `zaid khan | python developer | 85`

### Challenge 3 — Phone Number Cleaner
**Input:** `"+49 (176) 123-4567"`  
**Output:** `004917612345678`

## 📸 Output Screenshots

### Challenge 1 — Messy String
![Challenge 1 Output](./Screenshot%202026-03-30%20114756.png)

### Challenge 2 — Employee Parser
![Challenge 2 Output](./Screenshot%202026-03-30%20114809.png)

### Challenge 3 — Phone Number
![Challenge 3 Output](./Screenshot%202026-03-30%20114852.png)

## 💡 Key Learning
String cleaning is used in every 
real-world ETL pipeline — this is 
not just Python theory!
