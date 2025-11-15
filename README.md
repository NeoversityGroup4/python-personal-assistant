# 🤖 Personal Assistant CLI

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Smart personal assistant for managing contacts and notes**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Directory Structure](#-directory-structure) • [Commands](#-commands)

</div>

---

## 📋 Description

Personal Assistant CLI is a console application built with Python for efficient personal information management. The application allows you to store contacts with complete information (phone, email, address, birthday), create notes with tags, and perform global search across all data.

### ✨ Features

- 📇 **Contact Management**
    - Add contacts with data validation
    - Store phones, emails, addresses, and birthdays
    - Search contacts
    - Unique identifiers for each contact

- 📝 **Notes System**
    - Create notes
    - Tag support for categorization
    - Search by content and tags

- 🎂 **Birthday Reminders**
    - Tracking of upcoming birthdays
    - Customizable notification period (up to 365 days)
    - Sorting by date

- 🔍 **Global Search**
    - Unified search across contacts and notes
    - Quick access to any information
    - Relevant results with context

- 💾 **Reliable Storage**
    - Automatic saving to JSON
    - Storage in user's home directory

---

### 📁 Directory Structure

```
python-personal-assistant/
│
├── src/                          # Application source code
│   ├── __init__.py
│   ├── main.py                   # Application entry point
│   ├── app.py                    # Composition root (DI)
│   │
│   ├── commands/                 # CLI commands (Presentation Layer)
│   │   ├── __init__.py
│   │   ├── contacts_cmd.py       # Contact commands
│   │   ├── notes_cmd.py          # Note commands
│   │   ├── birthdays_cmd.py      # Birthday commands
│   │   └── search_cmd.py         # Global search commands
│   │
│   ├── services/                 # Business logic (Service Layer)
│   │   ├── __init__.py
│   │   ├── contacts_service.py   # Contact management
│   │   ├── notes_service.py      # Note management
│   │   ├── birthday_service.py   # Birthday logic
│   │   └── search_service.py     # Global search
│   │
│   ├── core/                     # Application core (Domain Layer)
│   │   ├── __init__.py
│   │   ├── models/               # Domain models
│   │   │   ├── __init__.py
│   │   │   ├── contacts.py       # Contact, Name, Phone, Email, etc.
│   │   │   └── notes.py          # Note, Text, Tag
│   │   ├── utils/                # Helper utilities
│   │   │   ├── __init__.py
│   │   │   └── dates.py          # Date operations
│   │   ├── validators.py         # Data validation
│   │   └── errors.py             # Custom exceptions
│   │
│   ├── storage/                  # Persistence layer
│   │   ├── __init__.py
│   │   └── file_store.py         # JSON storage
│   │
│   └── config/                   # Configuration
│       ├── __init__.py
│       └── constants.py          # Application constants
│
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

---

## 🚀 Installation

### Requirements

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd python-personal-assistant
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # Activation on Windows
   venv\Scripts\activate
   
   # Activation on Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt  # if file exists
   ```

4. **Run the application:**
   ```bash
   python -m src.main
   ```

---

## 💻 Usage

### Starting the Application

```bash
python -m src.main
```

After starting, you'll see the command prompt:
```
Personal Assistant CLI. Type 'help' to see available commands. Type 'exit' to quit.
> 
```

### 📖 Commands

#### Contact Management

| Command | Description | Example |
|---------|-------------|---------|
| `add-contact <name> [phone] [email] [address] [birthday]` | Add a new contact | `add-contact John 1234567890 john@email.com "123 Street" 15.03.1990` |
| `list-contacts` | Show all contacts | `list-contacts` |
| `search-contacts <query>` | Search contacts | `search-contacts John` |

**Examples:**
```bash
> add-contact Alice 0501234567 alice@example.com "Kyiv, Ukraine" 12.05.1995
Contact added successfully!

> add-contact Bob 0679876543 bob@example.com
Contact added successfully!

> list-contacts
Contact ID: 123e4567-e89b-12d3-a456-426614174000
Name: Alice
Phone: +380501234567
Email: alice@example.com
Address: Kyiv, Ukraine
Birthday: 12.05.1995
---
Contact ID: 123e4567-e89b-12d3-a456-426614174001
Name: Bob
Phone: +380679876543
Email: bob@example.com

> search-contacts alice
Found 1 contact(s):
Contact ID: 123e4567-e89b-12d3-a456-426614174000
Name: Alice
...
```

#### Note Management

| Command | Description | Example |
|---------|-------------|---------|
| `add-note <text> [#tag1 #tag2 ...]` | Add a note with tags | `add-note Buy groceries #shopping #urgent` |
| `list-notes` | Show all notes | `list-notes` |
| `search-notes <query>` | Search notes by text | `search-notes groceries` |
| `search-notes-tag <tag>` | Search by tag | `search-notes-tag urgent` |

**Examples:**
```bash
> add-note Meeting with team tomorrow at 10 AM #work #meeting
Note added successfully!

> add-note Buy milk and bread #shopping
Note added successfully!

> list-notes
Note[123e4567-e89b-12d3-a456-426614174002]: Meeting with team tomorrow at 10 AM | Tags: work, meeting
Note[123e4567-e89b-12d3-a456-426614174003]: Buy milk and bread | Tags: shopping

> search-notes-tag work
Found 1 note(s) with tag 'work':
Note[123e4567-e89b-12d3-a456-426614174002]: Meeting with team tomorrow at 10 AM | Tags: work, meeting
```

#### Birthdays

| Command | Description | Example |
|---------|-------------|---------|
| `birthdays <days>` | Show birthdays in the next N days | `birthdays 7` |

**Examples:**
```bash
> birthdays 30
Upcoming birthdays in the next 30 days:
Alice - 12.05.1995 (in 5 days)
Bob - 20.05.1988 (in 13 days)
```

#### Global Search

| Command | Description | Example |
|---------|-------------|---------|
| `search <query>` | Search across all contacts and notes | `search meeting` |

**Examples:**
```bash
> search alice
=== Global Search Results for 'alice' ===

Contacts (1):
Contact ID: 123e4567-e89b-12d3-a456-426614174000
Name: Alice
Phone: +380501234567
Email: alice@example.com

Notes (0):
No matching notes found.
```

#### System Commands

| Command | Description |
|---------|-------------|
| `help` | Show available commands |
| `exit` or `quit` | Exit the application |

---

## 🔧 Technical Details

### Data Validation

The application includes strict validation:

- **Phones**: Automatic normalization and format checking
- **Email**: Validation using regular expressions
- **Dates**: Support for `DD.MM.YYYY` and `YYYY-MM-DD` formats
- **Names**: Cannot be empty
- **Tags**: Automatic extraction from text (start with `#`)

### Data Storage

- Data is saved in a JSON file: `~/.personal_assistant_data.json`
- Automatic saving after each operation
- UUID support for unique record identification
- Safe object serialization/deserialization

### Error Handling

The application uses custom exceptions:

- `ContactNotFoundError` - contact not found
- `DuplicateContactError` - duplicate contact
- `InvalidPhoneError` - invalid phone format
- `InvalidEmailError` - invalid email format
- `InvalidDateError` - invalid date format

---

## 🧪 Usage Examples

### Scenario 1: Adding a Contact with Full Information

```bash
> add-contact "John Doe" 0501234567 john.doe@example.com "123 Main St, Kyiv" 15.03.1990
Contact added successfully!

> search-contacts john
Found 1 contact(s):
Contact ID: abc123...
Name: John Doe
Phone: +380501234567
Email: john.doe@example.com
Address: 123 Main St, Kyiv
Birthday: 15.03.1990
```

### Scenario 2: Organizing Notes with Tags

```bash
> add-note Prepare presentation for Monday meeting #work #urgent #presentation
Note added successfully!

> add-note Call dentist to schedule appointment #personal #health
Note added successfully!

> search-notes-tag urgent
Found 1 note(s) with tag 'urgent':
Note[xyz789...]: Prepare presentation for Monday meeting | Tags: work, urgent, presentation
```

### Scenario 3: Tracking Birthdays

```bash
> add-contact Alice 0501111111 alice@example.com "" 20.12.1995
Contact added successfully!

> add-contact Bob 0502222222 bob@example.com "" 25.12.1990
Contact added successfully!

> birthdays 10
Upcoming birthdays in the next 10 days:
Alice - 20.12.1995 (in 3 days)
Bob - 25.12.1990 (in 8 days)
```

---

## 🤝 Contributing

We welcome contributions to the project! Here's how you can help:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

---

## 📝 License

This project is distributed under the MIT License. See the `LICENSE` file for details.

---

## 👥 Development Team

The project was created by a team of developers as part of learning Python.

---

## 📞 Contact and Support

If you have questions or suggestions:

- Create an **Issue** in the repository
- Submit a **Pull Request** with improvements
- Contact the development team

---

<div align="center">

**Made with ❤️ in Python**

⭐ Star the project if you like it!

</div>
