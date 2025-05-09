SELECT "first_name", "last_name" FROM "players"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
WHERE "salary" = (
    SELECT MAX("salary") FROM "salaries"
);
