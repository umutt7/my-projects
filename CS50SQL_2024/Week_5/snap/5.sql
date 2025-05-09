SELECT "id" FROM "users"
WHERE "id" IN (
    SELECT "friend_id" FROM "friends"
    JOIN "users" ON "users"."id" = "friends"."friend_id"
    WHERE "user_id" = (SELECT "id" FROM "users" WHERE "username" = 'lovelytrust487')
    INTERSECT
    SELECT "friend_id" FROM "friends"
    JOIN "users" ON "users"."id" = "friends"."friend_id"
    WHERE "user_id" = (SELECT "id" FROM "users" WHERE "username" = 'exceptionalinspiration482')
);
