CREATE TABLE IF NOT EXISTS "smartify"."history"
(
    his_id SERIAL NOT NULL PRIMARY KEY,
    use_id INTEGER NOT NULL,
    tra_id TEXT NOT NULL,
    his_played_at TIMESTAMP WITH TIME ZONE NOT NULL,
    con_id INTEGER NULL,
    FOREIGN KEY (use_id) REFERENCES "smartify"."user"(use_id),
    FOREIGN KEY (con_id) REFERENCES "smartify"."context"(con_id),
    UNIQUE(use_id, his_played_at)
);