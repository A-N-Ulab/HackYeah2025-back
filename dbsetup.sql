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


create table trips
(
    id          serial
        constraint trips_pk
            primary key,
    user_id     integer not null
        constraint trips_users_id_fk
            references users,
    name        varchar,
    description text,
    state       varchar,
    photo_name          varchar not null,

    orientality         real    not null,
    temperature         real    not null,
    historicity         real    not null,
    sportiness          real    not null,
    forest_cover        real    not null,
    build_up_area        real    not null,
    terrain_fluctuation real    not null,
    water               real    not null
);
