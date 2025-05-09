CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL CHECK("type" IN ('Elementary School', 'Middle School', 'Middle School',
                                        'Lower School', 'Upper School', 'College', 'University')),
    "location" TEXT NOT NULL,
    "founded" INTEGER,
    PRIMARY KEY("id")
);

CREATE TABLE "companies" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "connections" (
    "user_id" INTEGER,
    "connection_user_id" INTEGER,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("connection_user_id") REFERENCES "users"("id")
);

CREATE TABLE "school_affiliation" (
    "user_id" INTEGER,
    "school_id" INTEGER,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC NOT NULL,
    "degree" TEXT NOT NULL CHECK("degree" IN ('BA', 'MA', 'PhD')),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")
);

CREATE TABLE "company_affiliation" (
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC NOT NULL,
    "title" TEXT NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "companies"("id")
);
