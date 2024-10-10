CREATE TABLE IF NOT EXISTS tweets (
    id serial PRIMARY KEY,
    created_at timestamp(0) with time zone NOT NULL DEFAULT NOW(),
    tweetid bigint NOT NULL,
    tweettext text NOT NULL
);