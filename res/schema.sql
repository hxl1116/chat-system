-- Extension for generating uuid
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Set the timezone for the database
SET TIMEZONE = 'America/New_york';

CALL drop_all_tables();

CREATE TABLE IF NOT EXISTS community
(
    community_id   uuid primary key default uuid_generate_v4(),
    community_name varchar(255)
);

CREATE TABLE IF NOT EXISTS channel
(
    channel_id   uuid primary key default uuid_generate_v4(),
    community_id uuid         not null,
    channel_name varchar(225) not null
);

CREATE TABLE IF NOT EXISTS membership
(
    community_id uuid not null,
    member_id    uuid not null,
    join_date    date default current_date
);

CREATE TABLE direct_message
(
    message_id  uuid primary key default uuid_generate_v4(),
    sender_id   uuid         not null,
    receiver_id uuid         not null,
    content     varchar(225) not null,
    unread      bool             default true,
    timestamp   timestamptz      default now()
);

CREATE TABLE IF NOT EXISTS member
(
    member_id             uuid primary key default uuid_generate_v4(),
    username              varchar(255) not null,
    password              varchar(225) not null,
    last_name             varchar(255) not null,
    first_name            varchar(255) not null,
    email                 varchar(255) not null,
    username_changed_date date
);

CREATE TABLE IF NOT EXISTS message
(
    message_id uuid primary key default uuid_generate_v4(),
    channel_id uuid         not null,
    sender_id  uuid         not null,
    content    varchar(225) not null,
    timestamp  timestamptz      default now()
);

CREATE TABLE message_status
(
    message_id  uuid not null,
    receiver_id uuid not null,
    read_status bool default false
);

CREATE TABLE suspension
(
    suspension_id  uuid primary key default uuid_generate_v4(),
    community_id   uuid not null,
    member_id      uuid not null,
    duration       int  not null,
    date_suspended date not null
);
