SELECT "year", "salary" FROM "salaries"
JOIN "players" ON "players"."id" = "salaries"."player_id"
WHERE "players"."first_name" = 'Cal'
ORDER BY "year" DESC;
