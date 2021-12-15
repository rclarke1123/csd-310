create database whatabook;
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
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED BY 'MySQL8IsGreat!';
GRANT ALL ON whatabook.* TO 'whatabook_user'@'localhost';

-- this will be a string field that will include the street address, city, state, and zip
insert into Store (locale) values ('134 West Market St. New York, NY 00853');

insert into Book (book_name, details, author) values ('The Loud House', 'PaperCuts, 2011, Children', 'L. Cooke');
insert into Book (book_name, details, author) values ('All Dogs go to Heaven', 'Smithville, 2003, Young Adult','S. Smith' );
insert into Book (book_name, details, author) values ('Feet Feet Feet ', 'Club Books, 1996, Children', 'Dr. Suess');
insert into Book (book_name, details, author) values ('To Kill A MOckingbird', 'McGrawHill, 1960, Young Adults', 'Harper Lee');
insert into Book (book_name, details, author) values ('One Flew Over the Cuckoos Nest ', 'McGrawHill, 1949, Adult', 'E. Lester');
insert into Book (book_name, details, author) values ('Pride and Prejudice', 'Hancock Press, 1889, Adult', 'J. Austin');
insert into Book (book_name, details, author) values ('Unbreakable', 'Hancock Press, 1996, Adult', 'B. Lewis');
insert into Book (book_name, details, author) values ('Pinkalicious', 'PaperCuts, 2002, Children', 'S. Wakes');
insert into Book (book_name, details, author) values ('Fancy Nancy', 'Club Books, 2004, Children', 'F. Bains');

insert into User (first_name, Last_name) values ('Rebecca', 'Clarke');
insert into User (first_name, Last_name) values ('Liz', 'Johnson');
insert into User (first_name, Last_name) values ('Ed', 'Miller');

insert into Wishlist (user_id, book_id) values (1, 9);
insert into Wishlist (user_id, book_id) values (2, 8);
insert into Wishlist (user_id, book_id) values (3, 7);
