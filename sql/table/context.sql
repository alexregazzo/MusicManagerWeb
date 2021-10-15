CREATE TABLE IF NOT EXISTS "smartify"."context" (
    con_id SERIAL NOT NULL PRIMARY KEY,
    con_type TEXT NOT NULL,
    con_uri TEXT NOT NULL UNIQUE
);