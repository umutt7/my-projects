SELECT "username" FROM "users"
JOIN "messages" ON "messages"."to_user_id" = "users"."id"
GROUP BY "username"
ORDER BY COUNT("pictures") DESC
LIMIT 1;
