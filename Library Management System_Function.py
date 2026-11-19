# Project: Library Management System:

Library_Books = []
Users = {}   # username: password


def library_system():
    while True:
        # ---------------- SQI LIBRARY PORTAL ----------------
        print("\n===== SQI LIBRARY MANAGEMENT SYSTEM =====")
        print("Sign in as:")
        print("1. Librarian\n2. User\n3. Quit")
        role = input("Select your role: ")

        # ---------------- LIBRARIAN ----------------
        if role == "1":
            # Sign in
            while True:
                print("\nLibrarian sign in (type 'back' as username to return)")
                username = input("Username: ")
                if username.lower() == "back":
                    break
                password = input("Password: ")
                if username == "Admin" and password == "1234":
                    print("Welcome, kindly proceed with your choice.")

                    # Librarian menu
                    while True:
                        print("\n--- Librarian Menu ---")
                        print("1. Add Book\n2. Remove Book\n3. Search Book\n4. Exit")
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            title = input("Enter Title: ")
                            author = input("Enter Author's Name: ")
                            accession_number = input("Enter accession number: ")

                            for book in Library_Books:
                                if book["accession_number"] == accession_number:
                                    print("A book with this accession number already exists.")
                                    break
                            else:
                                Library_Books.append({
                                    "title": title,
                                    "author": author,
                                    "accession_number": accession_number,
                                    "status": "Available",
                                })
                                # Confirm the book was added before proceeding
                                if Library_Books[-1]["accession_number"] == accession_number:
                                    print(f'Confirmed: "{title}" by {author} ({accession_number}) has been added.')
                                else:
                                    print("Something went wrong. The book was NOT added.")

                        elif choice == "2":
                            accession_number = input("Enter the accession number of the book to remove: ")
                            for book in Library_Books:
                                if book["accession_number"] == accession_number:
                                    Library_Books.remove(book)
                                    print("Book removed successfully.")
                                    break
                            else:
                                print("Book not found.")

                        elif choice == "3":
                            keyword = input("Enter title, author or accession number to search: ").lower()
                            matches = 0
                            for book in Library_Books:
                                if (keyword in book["title"].lower()
                                        or keyword in book["author"].lower()
                                        or keyword == book["accession_number"].lower()):
                                    print(f'{book["accession_number"]} | {book["title"]} by {book["author"]} | {book["status"]}')
                                    matches = matches + 1
                            if matches == 0:
                                print("No matching book found.")

                        elif choice == "4":
                            print("Librarian signed out.")
                            break

                        else:
                            print("Invalid choice. Please try again.")
                    break   
                else:
                    print("Invalid username or password. Please try again.")

        # ---------------- USER ----------------
        elif role == "2":
            # Signup / Login
            while True:
                print("\nWelcome to SQI Library User Portal")
                print("1. Signup\n2. Login\n3. Back")
                choice = input("Enter your choice: ")

                if choice == "1":
                    username = input("Choose a username: ")
                    if username in Users:
                        print("Username already taken.")
                    else:
                        Users[username] = input("Choose a password: ")
                        print("Signup successful. You can now log in.")

                elif choice == "2":
                    username = input("Username: ")
                    password = input("Password: ")
                    if username in Users and Users[username] == password:
                        print(f"Welcome, {username}!")

                        # User menu
                        while True:
                            print("\n--- User Menu ---")
                            print("1. View all books\n2. Search for a book\n3. Borrow a book")
                            print("4. Return a book\n5. Exit")
                            choice = input("Enter your choice: ")

                            if choice == "1":
                                if len(Library_Books) == 0:
                                    print("No books in the library yet.")
                                else:
                                    for book in Library_Books:
                                        print(f'{book["accession_number"]} | {book["title"]} by {book["author"]} | {book["status"]}')

                            elif choice == "2":
                                keyword = input("Enter title or author to search: ").lower()
                                matches = 0
                                for book in Library_Books:
                                    if keyword in book["title"].lower() or keyword in book["author"].lower():
                                        print(f'{book["accession_number"]} | {book["title"]} by {book["author"]} | {book["status"]}')
                                        matches = matches + 1
                                if matches == 0:
                                    print("No matching book found.")

                            elif choice == "3":
                                accession_number = input("Enter the accession number of the book to borrow: ")
                                for book in Library_Books:
                                    if book["accession_number"] == accession_number:
                                        if book["status"] == "Borrowed":
                                            print("Sorry, this book is already borrowed.")
                                        else:
                                            book["status"] = "Borrowed"
                                            print("You have borrowed the book successfully.")
                                        break
                                else:
                                    print("Book not found.")

                            elif choice == "4":
                                accession_number = input("Enter the accession number of the book to return: ")
                                for book in Library_Books:
                                    if book["accession_number"] == accession_number:
                                        if book["status"] == "Borrowed":
                                            book["status"] = "Available"
                                            print("Book returned successfully.")
                                        else:
                                            print("This book was not borrowed.")
                                        break
                                else:
                                    print("Book not found.")

                            elif choice == "5":
                                print("Thank you for visiting. Goodbye!")
                                break

                            else:
                                print("Invalid choice. Please try again.")
                        break   # leave signup/login loop, back to role menu
                    else:
                        print("Invalid username or password.")

                elif choice == "3":
                    break

                else:
                    print("Invalid choice. Please try again.")

        # ---------------- QUIT ----------------
        elif role == "3":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Please try again.")


library_system()