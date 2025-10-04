CREATE TABLE users (
   id SERIAL,
   username VARCHAR(80),
   password VARCHAR(80)
);

CREATE TABLE tokens (
    id varchar(40) NOT NULL,
    user_id INT NOT NULL,
    created_at timestamp NOT NULL DEFAULT NOW(),
    expires_at timestamp NOT NULL
)


