# Design Document

By Umut ARI

Video overview: <URL HERE>

## Scope

I have tried to implement the books in my personal library to a database. By using my project, I can
- Keep my collection of books with detailed information
- Track the reading status of each book I have
- View the books based on the reading status

## Functional Requirements

In the database, there is a table for authors that stores their names and nationality. The books table includes detailed information such as title, publication year, page counts, language and reading status. There are also three views, one is for the combined information about books, the other two views sorts the books based by the reading status.

I could also imply a few things, like book genres and tags, quotes, reviews and ratings. I'm planning to add these features with a user interface that let users see and edit the informations easily.

## Representation

### Entities

#### Authors

- **AuthorID**: Unique identifier for each author.
- **AuthorName**: Name of the author.
- **Nationality**: Nationality of the author.

##### Data Types

- **AuthorID (INTEGER, PRIMARY KEY)**: Using INTEGER ensures uniqueness and allows for automatic incrementing in SQLite.
- **AuthorName (TEXT)**: TEXT is suitable for storing names.
- **Nationality (TEXT)**: TEXT is suitable for storing nationality information.

##### Constraints

- **PRIMARY KEY (AuthorID)**: Guarantees unique identification of each author.

#### Books

- **BookID**: Unique identifier for each book.
- **Title**: Title of the book.
- **AuthorID**: Foreign key referring to the Authors entity.
- **YearPublished**: Year the book was published.
- **PageCount**: Total number of pages in the book.
- **Language**: Language in which the book is written.
- **Status**: Reading status of the book (e.g., "Finished Reading", "Not Read Yet").

##### Data Types

- **BookID (INTEGER, PRIMARY KEY)**: Unique identifier for each book, using INTEGER allows automatic incrementing.
- **Title (TEXT)**: TEXT type is suitable for storing book titles.
- **AuthorID (INTEGER, FOREIGN KEY)**: Links a book to its author.
- **YearPublished (INTEGER)**: INTEGER is suitable for storing year information.
- **PageCount (INTEGER)**: Number of pages as an integer.
- **Language (TEXT)**: TEXT is suitable for storing language information.
- **Status (TEXT)**: TEXT is suitable for storing predefined status values.

##### Constraints

- **PRIMARY KEY (BookID)**: Ensures unique identification of each book.
- **FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)**: Enforces referential integrity by linking books to an existing author.


#### Views

- **BooksView**: Combines book and author information.
- **FinishedBooksView**: Displays books marked as "Finished Reading".
- **NotReadBooksView**: Displays books marked as "Not Read Yet".

### Relationships

![ER Diagram](ERDiagram.jpg)

In my project, I have two tables called Books and Authors. Every book is written by an author, and an author can write many books. In that case, the relationship between my tables should be one to many.

## Optimizations

The schema I have created includes several optimizations that improve query performance and simplify data retrieval.

### Indexes

- **Primary Key Indexes**: Primary keys automatically create unique indexes. This ensures fast retrieval of rows by their primary key values. (Books.BookID and Authors.AuthorID)
- **Foreign Key Indexes**: Although foreign keys don't automatically create indexes, explicitly indexing them optimizes queries that join tables based on these foreign key columns. (Books.AuthorID)

### Views

- **BooksView**: Simplifies data retrieval by combining Books and Authors tables, and provides a comprehensive view of all books with their authors and key information.
- **FinishedBooksView**: Filters books that are marked as "Finished Reading." and allows the user to quickly see which books have been completed.
- **NotReadBooksView**: Filters books that are marked as "Not Read Yet." and enables the user to identify unread books easily.

### Foreign Key Constraints

- **Books**.AuthorID: Ensures referential integrity between Books and Authors, and maintains data consistency by ensuring that each book references a valid author.

## Limitations

While the current design of the Reading List Tracker database is simple and effective for basic tracking, it does have a number of limitations:

### Limited Status Representation

The Status attribute in the Books table is a TEXT field, this can lead to inconsistencies and misspellings when inserting or updating. To solve this, I can create a separate Statuses table to standardise the values, or use MySQL instead of SQLite3 and add the Status with ENUM type.

### Genre Classification and Author Information

To have more and complex information about the books I own, I can classify the books by genre. By doing this, I can categorise the books by query and gather information easily without having to go and check the book in my library. This can be achieved by creating another table for the genres.

The same goes for the authors of the books I own. A more detailed author table can include detailed information such as biography, date of birth, notable works and genres.

### Review and Rating System

Since I have read most of the books I own, it would be nice to keep track of my ratings and reviews for each book. Another table called Reviews can store this information with the book ID, review date etc.

### No Support for Multiple Users

This database is for personal use. In our house, the books are stored in different bookshelves in one room. Even though every member of my family can read every book, this database contains some personal information like status, the book I finished might still be on my mother's reading list. Or, after implementing ratings and reviews, the corresponding table can only store my thoughts about the books. A simple user table linked to the books and reviews tables can solve this problem.
