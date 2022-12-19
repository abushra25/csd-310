##WhataBook program created by Ahmed Bushra
##Data/Database Security 

##Imports##
import mysql.connector 
from mysql.connector import errorcode
import sys

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
##===========================================================================================================================
##Menu Display for users - creating menu function
def show_menu():
    print ("Main Menu")
    print ("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit")

    ##Try block to include except in case user chooses incorrect option
    try:
        user_choice = int(input ('Please enter 1, 2, 3, or 4 to proceed with the selected menu option: '))
        return user_choice
    except ValueError:
        print ("Entered value is invalid. Program will now end - thank you.")
        sys.exit(0)

##===========================================================================================================================
##Creating function to view books with INNER JOIN
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    
    ##Obtain query results
    books = _cursor.fetchall()
    print ("BOOK LISTINGS")

    for book in books:
        print(" Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book [1], book[2], book[3]))

##===========================================================================================================================
##Creating function to view locations
def show_locations(_cursor):

    ##Executing query to pull store location
    _cursor.execute ("SELECT store_id, locale FROM store")

    ##Obtaining query results
    locations = _cursor.fetchall()
    print ("\nSTORE LOCATIONS")

    for location in locations:
        print ("Location: {}\n".format(location[1]))

##===========================================================================================================================
##Creating function to validate users
def validate_user():
    try:
        users_id = int(input (" Enter customer ID: "))

        ##Nullifying bad user_id entries that are not in the database
        if users_id < 0 or users_id > 3:
            print ("Invalid customer ID. Please make another selection.")

            return users_id

    except ValueError:
        print ("Entered value is invalid. Please make another selection.")

##===========================================================================================================================
##Creating function to display account menu
def show_account_menu():
    try:
        print ("Customer Account Menu")
        print (" 1. Wishlist\n 2. Add Book\n 3. Main Menu")
        account_option = int(input (" Enter the appropriate menu option to proceed with selection: "))
        return account_option

    except ValueError:
        print ("Entered value is invalid. Please make another selection.")

##===========================================================================================================================
## Creating function to display wishlist 
def show_wishlist(_cursor,_user_id):

    ##INNER JOIN user & book on wishlist
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id= user.user_id " +
                    "INNER JOIN book on wishlist.book_id = book.book_id " +
                    "WHERE user.user_id = {}".format(_user_id))

    ##Obtaining query results
    wishlist = _cursor.fetchall()

    ##Wishlist display
    print ("WISHLIST ITEMS")

    for book in wishlist:
        print (" Book Name:{}\n Author{}\n".format(book[4], book[5]))

##===========================================================================================================================
##Creating function to show books to add
def show_books_to_add(_cursor,_user_id):
    ##Query variable for NOT IN
    query = ("SELECT book_id, book_name, author, details"
             "FROM book"
             "Where book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)
    _cursor.execute(query)

    books_to_add = _cursor.fetchall()
    
    ##Available books header
    print (" AVAILABLE BOOKS")
    for book in books_to_add:
        print ("Book ID {}\n Book Name{}\n".format(book[0], book[1]))

##===========================================================================================================================
##Creating function to add books to wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):

    ##Passing user_id and book_id into executable query
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES {},{}".format(_user_id, _book_id))

##===========================================================================================================================

try:
    ##Connecting to database
    db = mysql.connector.connect(**config)

    ##Cursor to queries 
    cursor = db.cursor()

    ##Welcome message
    print ("Welcome to the main menu of the WhatABook app.")

    ##User selection variable to call proper above function
    selection = show_menu()

    ##While statement if user does not choose to terminate program
    while selection !=4:

    ##If user selects 1, show_books function is called to query books and display results
        if selection ==1:
            show_books(cursor)
    
    ##If user selects 2, show_locations function is called to display available WhatABook locations with address
        if selection ==2:
            show_locations(cursor)
    
    ##If user selects option 3, validate_user function is called to validate the user_id entry + show account menu options
        if selection ==3:
            users_id = validate_user()
            account_options = show_account_menu()
            ##While statement if account option is not 3 - which is to revert back to main menu
            while account_options !=3:
                if account_options ==1:
                    show_wishlist(cursor, users_id)
                
                if account_options ==2:
                    show_books_to_add(cursor, users_id)
                    book_id = int(input ("Enter the corresponding ID of the book you would like to add to the wishlist"))
                    add_book_to_wishlist(cursor, users_id, book_id)

                    ##Commitment of changes to DB
                    db.commit()
                    ##Validation of commitment to user
                    print (" Book id:{} was added to the wishlist.".format(book_id))

                if account_options <0 or account_options >4:
                    print (" Invalid selection.")

        user_selection = show_menu()
    print ("Program has ended.")

finally:
    """end of try"""