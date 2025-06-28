# 🎉 Automated Birthday Mail Sender 📬

Send personalized birthday emails automatically using Python!  
This project reads birthday data from a CSV file, picks a random letter template, customizes it, and sends it via email — all with zero manual effort.

---

## 📌 Features

- 📅 Checks if today matches anyone’s birthday
- ✉️ Sends personalized email messages using SMTP
- 🎨 Chooses a random birthday message from template files
- 🔐 Handles credentials securely (environment variables recommended)
- 🧹 Clean, modular, and easy-to-read code

---

## 🛠️ Technologies Used

- Python
- Pandas
- `datetime` module
- `smtplib` for sending emails
- CSV for data storage
- Randomized content from text files

---

## 📂 Folder Structure

birthday-mail-sender/
├── birthdays.csv
├── main.py
├── letter_templates/
│ ├── letter_1.txt
│ ├── letter_2.txt
│ └── letter_3.txt
└── README.md
