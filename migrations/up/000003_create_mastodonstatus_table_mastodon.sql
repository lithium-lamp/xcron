CREATE TABLE IF NOT EXISTS mastodonstatus (
    id serial PRIMARY KEY,
    created_at timestamp(0) with time zone NOT NULL DEFAULT NOW(),
    statusid bigint NOT NULL,
    content text NOT NULL
);