CREATE TABLE IF NOT EXISTS "smartify"."user"
(
    use_id SERIAL NOT NULL PRIMARY KEY,
    use_username TEXT NOT NULL UNIQUE,
    use_password_salt TEXT NOT NULL,
    use_password TEXT NOT NULL,
    use_created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT current_timestamp
);