CREATE TABLE IF NOT EXISTS "smartify"."token" (
	tok_id SERIAL NOT NULL PRIMARY KEY,
	use_id INTEGER NOT NULL UNIQUE,
	tok_token VARCHAR NOT NULL,
	tok_token_type VARCHAR NOT NULL,
	tok_token_scope VARCHAR NOT NULL,
	tok_token_expires_in INTEGER NOT NULL,
	tok_token_refresh VARCHAR NOT NULL,
	tok_token_expires_at INTEGER NOT NULL,
	tok_last_updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT current_timestamp,
	FOREIGN KEY(use_id) REFERENCES "smartify"."user" (use_id)
)