-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

-- Inserting a few books that I have in my library
-- First we will add the authors
INSERT INTO "Authors" ("AuthorName", "Nationality")
VALUES ("Niccolò Machiavelli", "Italian"),
("Fyodor Dostoyevski", "Russian"),
("Mustafa Kemal Atatürk", "Turkish"),
("Milton Crane", "American");

-- Then, we will add the informations of books and status that if I have read or not
INSERT INTO "Books" ("Title", "YearPublished", "PageCount", "Language", "Status", "AuthorID")
VALUES
("Il Principe", 1513, 144, "English", "Not Read Yet",
(SELECT "AuthorID" FROM "Authors" WHERE "AuthorName" = 'Niccolò Machiavelli')
),
("Crime and Punishment", 1866, 671, "English", "Finished Reading",
(SELECT "AuthorID" FROM "Authors" WHERE "AuthorName" = 'Fyodor Dostoyevski')
),
("50 Great Short Stories", 1952, 571, "English", "Not Read Yet",
(SELECT "AuthorID" FROM "Authors" WHERE "AuthorName" = 'Milton Crane')
),
("Nutuk", 1927, 543, "Turkish", "Finished Reading",
(SELECT "AuthorID" FROM "Authors" WHERE "AuthorName" = 'Mustafa Kemal Atatürk')
);

