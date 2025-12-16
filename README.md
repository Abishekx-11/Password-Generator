# Password Generator

## Description
A command-line password generator that creates secure random passwords based on user preferences. Includes input validation, character type selection, and password strength analysis.

## Features
- ✅ Custom password length (minimum 4 characters)
- ✅ Choose character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- ✅ Password strength analyzer (Weak/Medium/Strong/Very Strong)
- ✅ Input validation with error handling
- ✅ Must select at least one character type

## How to Run
```bash
python password_generator.py
```
## How to use
- Download or copy code
- Save file with name [ To_do_list.py]
- Run python To_do_list.py in your Terminal
- After that, You will be shown options that you may want to perform like add_task, delete_task, show_task and mark task that yo completed
- Generate as many Password as you want

## Example Usage
```
How long the password should be? (min 4): 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters (!@#$%^&*)? (y/n): n

Password is: aB7dKp2QmXvL
Your Password strength: Strong
```

## Password Strength Criteria
- **Weak ⚠️:** Less than 8 characters OR only 1 character type
- **Medium:** 8-11 characters with 2 types
- **Strong:** 12-15 characters with 3 types
- **Very Strong ✅:** 16+ characters with all 4 types

## What I Learned
- Using `random.choice()` for random character selection
- String manipulation with `string` module (`ascii_uppercase`, `ascii_lowercase`, `digits`)
- Input validation with try-except blocks
- List comprehension: `[random.choice(container) for _ in range(n)]`
- Converting lists to strings with `"".join()`
- Using `sys.exit()` to terminate program
- Tracking multiple boolean conditions for strength analysis
- Writing clean, commented code for readability

## Technical Details
- **Language:** Python 3
- **Libraries:** `random`, `string`, `sys`
- **Input validation:** Ensures numeric input and minimum length
- **Character pool:** Dynamically built based on user selection
