use whatabook;

CREATE TABLE User (
    user_id int NOT NULL AUTO_INCREMENT,
    first_name varchar(75) NOT NULL,
    Last_name varchar(75) NOT NULL,
    PRIMARY KEY (user_id)
); 
CREATE TABLE Book (
    book_id int NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500) NOT NULL,
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY (book_id)
); 
CREATE TABLE Store (
    store_id int NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    -- this will be a string field that will include the street address, city, state, and zip
    PRIMARY KEY (store_id)
); 
CREATE TABLE Wishlist (
    wishlist_id int NOT NULL AUTO_INCREMENT,
    user_id int NOT NULL,
    book_id int NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id) REFERENCES User(user_id)
); 
