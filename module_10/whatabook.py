import mysql.connector
from mysql.connector import errorcode

#
#   GRANT ALL ON whatabook.* TO 'whatabook_user'@'localhost';
#
'''

To display a user’s Wishlist you will need to use two INNER JOINs to combine the user
and book tables. 
○ Store, Book, Wishlist, User


● Create a method to display the account menu
● Use variables to capture the user’s entry for user_id
● User variables to capture the user’s entry for book_id
● If you get stuck, the courses GitHub repository has the final solution to compare your 
code against. But, again, only use this as a last resort. To truly learn these topics, you 
will need to make an effort and try to complete the project on your own.
'''
'''
Main Menu
1 - View Books
2 - View Store Locations
3  My Account
   Prompt the user to enter a user_id
1, 2, or 3
Note: before a user can access their account, they must enter a valid user_id.
Wishlist Menu
Wishlist
Add Book
Display the available books
The output will show the book_id, book_name, author, and details
Prompt the user to select a book to add to their wishlist
To add a book to the user's Wishlist, the insert statement will need the book_id and user_id

This option takes users back to the main menu
4 - Exit Program
Exits the program
'''
def show_menu():
    print("Main Menu\n")
    print("1 - View Books")
    print("2 - View Store Locations")
    print("3 - My Account")
    print("4 - Quit\n")
    ans = int(input("Enter 1, 2, 3, or 4 "))
    return ans

def show_books(_cursor, choice=1, _user_id=0):
    wishlistBooks = ""
    if _user_id > 0:
        query = "select book_id from Wishlist where user_id = " + str(_user_id)
        _cursor.execute(query)
        bookRecords = _cursor.fetchall()
        for book in bookRecords:
            if len(wishlistBooks) > 0:
                wishlistBooks += ", "
            wishlistBooks += str(book[0])
    query = "select book_id,book_name, author, details from Book"
    if len(wishlistBooks) > 0:
        query += " where book_id not in (" + wishlistBooks + ")"
    _cursor.execute(query)
    bookRecords = _cursor.fetchall()
    validBookIds = []
    for book in bookRecords:
        validBookIds.append(book[0])

    while True:
        for book in bookRecords:
            print("BookID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))
        if choice <= 0:
            choice = int(input("Enter bookID: "))
            if choice not in validBookIds:
                print("Invalid book Id, please try again!")
        else:
            break

    return choice

def show_locations(_cursor):
    locationRecords = _cursor.fetchall()
    for location in locationRecords:
        print("StoreID: {}\nLocale: {}\n".format(location[0], location[1]))

def validate_user(cursor):
    users = cursor.fetchall()
    validUserIds = []
    user_id = 0

    for user in users:
        validUserIds.append(user[0])
    while user_id not in validUserIds:
        print("Users")
        print("UserId  -  Name\n")
        for user in users:
            print("{} - {} {}".format(user[0], user[1], user[2]))
        print("\n")
        user_id = int(input("Please enter a user_id: "))
        if user_id not in validUserIds:
            print("Invalid User id, please try again!")

    return user_id

def show_account_menu ():
    pass

def show_wishlist (_cursor, _user_id):
    user_info = "SELECT first_name, Last_name " + \
                    "FROM User " + \
                    "WHERE user_id = " + str(_user_id)

    _cursor.execute(user_info)
    userRecord = _cursor.fetchall()
    print("\nWish List for  {} {}\n".format(userRecord[0][0], userRecord[0][1]))
    user_wishlist = "SELECT Book.book_id, book_name, details, author " + \
                    "FROM Wishlist " + \
                    "INNER JOIN Book " + \
                    "ON Wishlist.book_id = Book.book_id " + \
                    "INNER JOIN User " + \
                    "ON Wishlist.user_id = User.user_id " + \
                    "WHERE Wishlist.user_id = " + str(_user_id) + ";"
                    
    _cursor.execute(user_wishlist)
    wishlistRecords = _cursor.fetchall()
    for wishlist in wishlistRecords:
        print("BookID: {}\nBook Name: {}\nDetails: {}\nAuthor: {}\n".format(wishlist[0], wishlist[1], wishlist[2], wishlist[3]))


def show_books_to_add (_cursor, _user_id):
    book_id = show_books(_cursor, -1, _user_id)

    return book_id

def add_book_to_wishlist (_cursor, _user_id, _book_id):
    try:
        query = "insert into Wishlist (user_id, book_id) values (" + str(_user_id) + ", " + str(_book_id) + ")"
        _cursor.execute(query)
    except Exception as e: 
        print(e)

def show_wishlist_menu (_cursor, _user_id):
    choice = 1
    while choice != 3:
        print("Wishlist Menu\n")
        print("1 - Wishlist")
        print("2 - Add Book")
        print("3 - Main Menu")
        choice = int(input("\nPlease enter 1, 2, or 3: "))
        if choice == 1:
            show_wishlist(_cursor, _user_id)        
        elif choice == 2:
            book_id = show_books_to_add (_cursor, _user_id)
            add_book_to_wishlist(_cursor, _user_id, book_id)

def display_account_menu(cursor):
    query = "select * from User"
    cursor.execute(query)
    user_id = validate_user(cursor)
    #book_id
    show_wishlist_menu(cursor, user_id)    

ans = 1
config = {
           "user": "whatabook_user",
          "password": "MySQL8IsGreat!",
          "host": "127.0.0.1", 
          "database": "whatabook",
          "raise_on_warnings": True
}
db = None
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    while ans != 4:
        ans = show_menu()
        if ans == 1:
            show_books(cursor)
        elif ans == 2:
            query = "select * from Store"
            cursor.execute(query)
            show_locations(cursor)
        elif ans == 3:
            display_account_menu(cursor)

except Exception as e:
    print(e)
