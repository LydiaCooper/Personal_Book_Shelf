import json

#Load the bookshelf dictionary from the JSON file
with open('bookshelf.json', 'r') as json_file:
    books_dict = json.load(json_file)

#opening query
def display_menu():
    print("\nWelcome to your bookshelf! What would you like to do today?\n")
    print("1. Search bookshelf")
    print("2. Edit bookshelf")
    print("3. Add new book")
    print("4. Remove book")
    print("5. Exit")

def search_by_genre():
    genre = input("Enter the genre to search for: ")
    matching_books = [title for title, book in books_dict.items() if book.get('genre', '').lower() == genre.lower()]
    return matching_books

def search_by_read_status():
    read_status = input("Enter the read status to search for: ")
    matching_books = [title for title, book in books_dict.items() if book.get('read_status', '').lower() == read_status.lower()]
    return matching_books

def search_by_publish_year():
    publish_year = int(input("Enter the publish year to search for: "))
    matching_books = [title for title, book in books_dict.items() if book.get('publication_year', 0) == publish_year]
    return matching_books

def search_bookshelf():
    print("Search options:")
    print("1. Genre")
    print("2. Read Status")
    print("3. Publish Year (by decade)")
    print("4. Cancel")

    search_criteria = []

    while True:
        search_choice = input("\nEnter your search choice (1-4, or 'done' to finish): ")

        if search_choice == '1':
            genre = input("\nEnter the genre to search for: ")
            search_criteria.append(('genre', genre))
        elif search_choice == '2':
            read_status = input("\nEnter the read status to search for: ")
            search_criteria.append(('read_status', read_status))
        elif search_choice == '3':
            while True:
                decade_input = input("\nEnter the decade to search for (e.g., '1980'): ")

                try:
                    # Attempt to convert the input to an integer
                    decade = int(decade_input)
                except ValueError:
                    print("\nInvalid input. Please enter a valid decade (e.g., '1980').")
                    continue

                if 1000 <= decade <= 9999 and decade % 10 == 0:
                    search_criteria.append(('publish_year', decade))
                    break
                else:
                    print("\nInvalid decade. Please enter a valid decade (e.g., '1980').")
        elif search_choice.lower() == 'done':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4, or 'done' to finish.")

    #Filter out empty criteria before passing to filter_books
    search_criteria = [criteria for criteria in search_criteria if criteria[1]]

    matching_books = filter_books(search_criteria)

    if matching_books:
        print("Matching books:")
        for title in matching_books:
            print(f"{title} by {books_dict[title]['author']}")
    else:
        print("No matching books found.")

def filter_books(criteria):
    matching_books = []

    for title, book in books_dict.items():
        matches_all_criteria = True

        for key, value in criteria:
            if key == 'publish_year':
                #Extract the decade from the publishing year
                book_decade = (book.get('publication_year', 0) // 10) * 10
                search_decade = (int(value) // 10) * 10

                if book_decade != search_decade:
                    matches_all_criteria = False
                    break
            elif str(book.get(key, '')).lower() != str(value).lower():
                matches_all_criteria = False
                break

        if matches_all_criteria:
            matching_books.append(title)

    return matching_books

def edit_bookshelf():
    book_title = input("Enter the title of the book to edit: ")

    if book_title in books_dict:
        print("Edit options:")
        print("1. Author")
        print("2. Goodreads Rating")
        print("3. Read Status")
        print("4. Personal Rating")
        print("5. Publication Year")
        print("6. Genre")
        print("7. Cancel")

         #Editing existing books in file
        edit_choice = input("Enter your edit choice (1-7): ")

        if edit_choice == '1':
            books_dict[book_title]['author'] = input("Enter the new author: ")
        elif edit_choice == '2':
            books_dict[book_title]['goodreads_rating'] = float(input("Enter the new Goodreads rating: "))
        elif edit_choice == '3':
            books_dict[book_title]['read_status'] = input("Enter the new read status: ")
        elif edit_choice == '4':
            books_dict[book_title]['personal_rating'] = float(input("Enter the new personal rating: "))
        elif edit_choice == '5':
            books_dict[book_title]['publication_year'] = int(input("Enter the new publication year: "))
        elif edit_choice == '6':
            books_dict[book_title]['genre'] = input("Enter the new genre: ")
        elif edit_choice == '7':
            print("Edit canceled.")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
    else:
        print(f"Book with title '{book_title}' not found.")

#Adding a new book
def add_new_book():
    new_book_title = input("Enter the title of the new book: ")

    if new_book_title not in books_dict:
        books_dict[new_book_title] = {
            'author': input("Enter the author: "),
            'goodreads_rating': float(input("Enter the Goodreads rating: ")),
            'read_status': input("Enter the read status: "),
            'personal_rating': float(input("Enter the personal rating: ")),
            'publication_year': int(input("Enter the publication year: ")),
            'genre': input("Enter the genre: ")
        }
        print(f"New book '{new_book_title}' added.")
    else:
        print(f"Book with title '{new_book_title}' already exists.")

#Removing a book
def remove_book():
    book_title_to_remove = input("Enter the title of the book to remove: ")
    
    #Request removal confirmation incase accidentally selected
    if book_title_to_remove in books_dict:
        confirm = input(f"Are you sure you want to remove '{book_title_to_remove}'? (yes/no): ").lower()
        if confirm == 'yes':
            del books_dict[book_title_to_remove]
            print(f"Book '{book_title_to_remove}' removed.")
        else:
            print("Removal cancelled.")
    else:
        print(f"Book with title '{book_title_to_remove}' not found.")

def save_to_json():
    #Save the updated books_dict to the JSON file
    with open('bookshelf.json', 'w') as json_file:
        json.dump(books_dict, json_file)

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            search_bookshelf()
        elif choice == '2':
            edit_bookshelf()
        elif choice == '3':
            add_new_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            save_to_json()
            print("Goodbye! Happy reading.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
