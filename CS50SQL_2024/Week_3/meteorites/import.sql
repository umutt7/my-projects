-- Create a temp table
CREATE TABLE "meteorites_temp" (
    "name" TEXT,
    "id" INTEGER,
    "nametype" TEXT,
    "class" TEXT,
    "mass" NUMERIC,
    "discovery" TEXT,
    "year" INTEGER,
    "lat" NUMERIC,
    "long" NUMERIC,
    PRIMARY KEY("id")
);

-- Create the original table
CREATE TABLE "meteorites" (
    "id" INTEGER,
    "name" TEXT,
    "class" TEXT,
    "mass" NUMERIC,
    "discovery" TEXT,
    "year" INTEGER,
    "lat" NUMERIC,
    "long" NUMERIC,
    PRIMARY KEY("id")
);

-- Import csv to temp table
.import --csv --skip 1 meteorites.csv meteorites_temp

-- Update of NULLs
UPDATE "meteorites_temp"
SET "mass" = NULL
WHERE "mass" = '';

UPDATE "meteorites_temp"
SET "year" = NULL
WHERE "year" = '';

UPDATE "meteorites_temp"
SET "lat" = NULL
WHERE "lat" = '';

UPDATE "meteorites_temp"
SET "long" = NULL
WHERE "long" = '';

-- Round values
UPDATE "meteorites_temp"
SET "mass" = ROUND("mass", 2), "lat" = ROUND("lat", 2), "long" = ROUND("long", 2);

-- Remove Relicts
DELETE FROM "meteorites_temp"
WHERE "nametype" = 'Relict';

-- Remove nametype column
ALTER TABLE "meteorites_temp"
DROP COLUMN "nametype";

-- Import temp to original
INSERT INTO meteorites (name, class, mass, discovery, year, lat, long)
SELECT name, class, mass, discovery, year, lat, long FROM meteorites_temp
ORDER BY year ASC, name;
