-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

--  Table for Books
CREATE TABLE "Books" (
    "BookID" INTEGER,
    "Title" TEXT,
    "AuthorID" INTEGER,
    "YearPublished" INTEGER,
    "PageCount" INTEGER,
    "Language" TEXT,
    "Status" TEXT,
    PRIMARY KEY("BookID"),
    FOREIGN KEY("AuthorID") REFERENCES "Authors"("AuthorID")
);

-- Table for Authors
CREATE TABLE "Authors" (
    "AuthorID" INTEGER,
    "AuthorName" TEXT,
    "Nationality" TEXT,
    PRIMARY KEY("AuthorID")
);

-- View for the books with key information
CREATE VIEW "BooksView" AS
SELECT "Title", "AuthorName", "YearPublished", "PageCount", "Status", "Language"
FROM "Books", "Authors"
WHERE "Books"."AuthorID" = "Authors"."AuthorID";

-- View for the books that I finished reading
CREATE VIEW "FinishedBooksView" AS
SELECT "Title", "AuthorName", "YearPublished", "PageCount", "Language"
FROM "Books", "Authors"
WHERE "Books"."AuthorID" = "Authors"."AuthorID" AND "Books"."Status" = 'Finished Reading';

-- View for the books that I didn't read yet
CREATE VIEW "NotReadBooksView" AS
SELECT "Title", "AuthorName", "YearPublished", "PageCount", "Language"
FROM "Books", "Authors"
WHERE "Books"."AuthorID" = "Authors"."AuthorID" AND "Books"."Status" = 'Not Read Yet';

