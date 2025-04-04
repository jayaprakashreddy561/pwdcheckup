# PwdCheckup - Password Strength Checker

PwdCheckup is a powerful password strength checker designed for Kali Linux. It evaluates the strength of a password and estimates how long it would take to crack it using brute force attacks.

---

## Features

- Check the strength of a single password.
- Process multiple passwords from a file.
- Estimate the time required to crack a password.
- Save results to an output file.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/PwdCheckup.git
cd PwdCheckup
pip install -r requirements.txt
```

---

## Usage

Run the tool using the following command:

```bash
python3 pwdcheckup.py -h
```

### Command-Line Options:

| Option             | Description                         |
| ------------------ | ----------------------------------- |
| `-s <password>`    | Check a single password.            |
| `-f <file>`        | Check passwords from a text file.   |
| `-o <output_file>` | Save the results to an output file. |

---

## Example Usage

### Single Password Check:

```bash
python3 pwdcheckup.py -s "P@ssw0rd!"
```

**Output:**

```
Password Strength: Strong
Estimated time to crack: 15 years, 2 months, 5 days
```

---

### File Input:

```bash
python3 pwdcheckup.py -f passwords.txt -o results.txt
```

This will check all passwords listed in `passwords.txt` and save the results in `results.txt`.

---

## Contributing

Feel free to fork the repository, improve the tool, and submit a pull request!

---

## Contact

For any issues or suggestions, reach out via GitHub.

