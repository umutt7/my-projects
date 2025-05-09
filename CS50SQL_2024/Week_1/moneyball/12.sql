SELECT "first_name", "last_name" FROM "players"
WHERE "id" IN (
    SELECT * FROM (
        SELECT "performances"."player_id" FROM "performances"
        JOIN "salaries" ON "salaries"."player_id" = "performances"."player_id"
        AND "salaries"."year" = "performances"."year"
        WHERE "salaries"."year" = 2001 AND "salaries"."salary" > 0 AND "performances"."H" > 0
        GROUP BY "performances"."player_id"
        ORDER BY "salary" / "H" ASC
        LIMIT 10
    )
    INTERSECT
    SELECT * FROM (
        SELECT "performances"."player_id" FROM "performances"
        JOIN "salaries" ON "salaries"."player_id" = "performances"."player_id"
        AND "salaries"."year" = "performances"."year"
        WHERE "salaries"."year" = 2001 AND "salaries"."salary" > 0 AND "performances"."RBI" > 0
        GROUP BY "performances"."player_id"
        ORDER BY "salary" / "RBI" ASC
        LIMIT 10
    )
);
