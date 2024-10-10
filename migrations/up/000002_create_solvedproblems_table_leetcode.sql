CREATE TABLE IF NOT EXISTS solvedproblems (
    id text PRIMARY KEY,
    created_at timestamp(0) with time zone NOT NULL DEFAULT NOW(),
    difficulty text NOT NULL,
    completed_time_unix BIGINT NOT NULL,
    lang text NOT NULL,
    title text NOT NULL,
    runtime text NOT NULL,
    memory text NOT NULL
);