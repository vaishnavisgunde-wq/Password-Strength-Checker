## 🔐 Password Strength Validator (Python)

A beginner-friendly Python script that validates password strength based on common security standards.
It securely prompts the user for a password (with masked input) and checks for length, digits, uppercase/lowercase letters, and special characters.
If the password is weak, it clearly explains which requirements were not met.

---

### 🧰 Features

* Secure password input using `pwinput` (input hidden while typing)
* Checks for:

  * Minimum length of 8 characters
  * At least one uppercase and one lowercase letter
  * At least one digit (0–9)
  * At least one special character (`!@#$%^&*()_+={}[]...`)
* Detailed feedback for weak passwords
* Stores valid passwords temporarily in a list (for demonstration purposes)

---

### 💻 Example Output

```
PS C:\Users\Anonymous\Desktop\Coding> python new.py
Enter password to validate: ********

Password is too weak!
--- Requirements ---
- Must contain at least one digit (0-9).
- Must contain at least one special character (e.g., !@#$).
```

---

### 🧩 How to Run

1. Install Python (3.8 or higher recommended).
2. Install `pwinput` using:

   ```bash
   pip install pwinput
   ```
3. Run the script:

   ```bash
   python new.py
   ```

---

### ⚙️ Technologies Used

* **Python** (core language)
* **pwinput** – for secure, masked input
* **re** – regular expressions for pattern checking
* **time** – for simple delay effects

---

### 🚀 Future Improvements

* Add password hashing (using `hashlib`) for secure storage
* Implement a graphical or web-based interface
* Save strong passwords to an encrypted file

---

