# SQI Library Management System

A simple command-line library management system written in Python. It supports two roles, **Librarian** and **User**, each with their own menu for managing and borrowing books.

## Features

### Librarian
- Add a new book (title, author, accession number)
- Remove a book by accession number
- Search for books by title, author, or accession number
- Duplicate accession numbers are rejected, and each addition is confirmed on screen

### User
- Sign up and log in with a username and password
- View all books in the library
- Search for books by title or author
- Borrow a book (blocked if it is already borrowed)
- Return a borrowed book

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries needed

## Getting Started

1. Save the code as `library.py` (or any name you like).
2. Run it from a terminal:

   ```bash
   python library.py
   ```

3. Choose a role from the main menu:

   ```
   ===== SQI LIBRARY MANAGEMENT SYSTEM =====
   Sign in as:
   1. Librarian
   2. User
   3. Quit
   ```

## Usage

### Librarian sign-in

| Field    | Value   |
|----------|---------|
| Username | `Admin` |
| Password | `1234`  |

Type `back` as the username to return to the main menu.

**Librarian menu**

```
1. Add Book
2. Remove Book
3. Search Book
4. Exit
```

### User sign-up and login

1. Select **User** from the main menu.
2. Choose **Signup** to create an account, then **Login** to sign in.
3. Once logged in, the user menu is available:

```
1. View all books
2. Search for a book
3. Borrow a book
4. Return a book
5. Exit
```

## Data Structures

| Name            | Type   | Purpose |
|-----------------|--------|---------|
| `Library_Books` | `list` | Stores each book as a dictionary |
| `Users`         | `dict` | Maps `username` to `password` |

Each book is stored like this:

```python
{
    "title": "Things Fall Apart",
    "author": "Chinua Achebe",
    "accession_number": "A001",
    "status": "Available",   # or "Borrowed"
}
```

## Known Limitations

- **No persistent storage.** All books and user accounts are held in memory and are lost when the program closes.
- **Passwords are stored in plain text**, and the librarian credentials are hardcoded. This is fine for a learning project but not for real use.
- Borrowing is not tied to a specific user, so any user can return any borrowed book.
- There is no due-date or fine tracking.

## Possible Improvements

- Save books and users to a file (JSON or CSV) or a database such as SQLite
- Hash passwords (e.g. with `hashlib` or `bcrypt`)
- Track which user borrowed which book, with due dates
- Split the code into smaller functions or classes for readability and easier testing
- Add input validation (e.g. empty titles or usernames)

## Author

Created as part of the SQI Library Management System project.