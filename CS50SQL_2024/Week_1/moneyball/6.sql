SELECT "name", SUM("H") FROM "teams"
JOIN "performances" ON "performances"."team_id" = "teams"."id"
WHERE "performances"."year" = 2001
GROUP BY "name"
ORDER BY SUM("H") DESC
LIMIT 5;
