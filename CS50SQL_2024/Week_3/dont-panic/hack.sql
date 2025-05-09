-- Change admin password
UPDATE "users" SET "password" = '982c0381c279d139fd221fce974916e7'
WHERE "username" = 'admin';

-- Add false data as admin password as changed as emily33's password
INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
VALUES ('update', 'admin', 'admin',
    (SELECT "password" FROM "users" WHERE "username" = 'admin'),
    (SELECT "password" FROM "users" WHERE "username" = 'emily33')
);

-- Delete actual log
DELETE FROM "user_logs" WHERE "old_username" = 'admin' AND "new_password" = '982c0381c279d139fd221fce974916e7';


-- current admin e10adc3949ba59abbe56e057f20f883e
-- current emily33 44bf025d27eea66336e5c1133c3827f7
