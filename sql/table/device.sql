CREATE TABLE IF NOT EXISTS "smartify"."device"
(
    dev_id SERIAL NOT NULL PRIMARY KEY,
    use_id INTEGER NOT NULL,
    dev_token TEXT NOT NULL,
    dev_active BOOLEAN NOT NULL DEFAULT FALSE,
    dev_created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT current_timestamp,
    FOREIGN KEY (use_id) REFERENCES "smartify"."user"(use_id)
);