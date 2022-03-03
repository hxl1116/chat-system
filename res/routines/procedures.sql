-- noinspection SqlWithoutWhereForFile

-- Drop procedures if they already exist
drop procedure if exists drop_all_tables;
drop procedure if exists delete_test_data;
drop procedure if exists reload_test_data;
drop procedure if exists insert_test_data;

drop procedure if exists insert_test_community_data;
drop procedure if exists insert_test_channel_data;
drop procedure if exists insert_test_direct_message_data;
drop procedure if exists insert_test_member_data;
drop procedure if exists insert_test_membership_data;
drop procedure if exists insert_test_message_data;
drop procedure if exists insert_test_message_status_data;
drop procedure if exists insert_test_suspension_data;

-- Drop all tables
create procedure drop_all_tables()
    language plpgsql as
$$
begin
    drop table if exists "channel";
    drop table if exists "community";
    drop table if exists "membership";
    drop table if exists "direct_message";
    drop table if exists "member";
    drop table if exists "message";
    drop table if exists "message_status";
    drop table if exists "suspension";
end;
$$;

-- Delete all data
create procedure delete_test_data()
    language plpgsql as
$$
begin
    delete from "channel";
    delete from "community";
    delete from "direct_message";
    delete from "membership";
    delete from "member";
    delete from "message";
    delete from "message_status";
    delete from "suspension";
end
$$;

-- Reload all data
create procedure reload_test_data()
    language plpgsql as
$$
begin
    call delete_test_data();
    call insert_test_data();
end
$$;

-- Insert dummy data
create procedure insert_test_data()
    language plpgsql as
$$
begin
    call insert_test_community_data();
    call insert_test_channel_data();
    call insert_test_member_data();
    call insert_test_membership_data();
    call insert_test_message_data();
    call insert_test_message_status_data();
    call insert_test_direct_message_data();
    call insert_test_suspension_data();
end;
$$;

-- Insert dummy community data
create procedure insert_test_community_data()
    language plpgsql as
$$
begin
    insert into community (community_id, community_name) values (uuid_generate_v4(), 'Arrakis');
    insert into community (community_id, community_name) values (uuid_generate_v4(), 'Comedy');
end
$$;

-- Insert dummy channel data
create procedure insert_test_channel_data()
    language plpgsql as
$$
declare
    arrakis_id uuid;
    comedy_id  uuid;
begin
    select community_id into arrakis_id from community where community_name = 'Arrakis';
    select community_id into comedy_id from community where community_name = 'Comedy';

    insert into channel (channel_id, community_id, channel_name)
    values (uuid_generate_v4(), arrakis_id, 'worms');

    insert into channel (channel_id, community_id, channel_name)
    values (uuid_generate_v4(), arrakis_id, 'random');

    insert into channel (channel_id, community_id, channel_name)
    values (uuid_generate_v4(), comedy_id, 'argument-clinic');

    insert into channel (channel_id, community_id, channel_name)
    values (uuid_generate_v4(), comedy_id, 'dialogs');
end
$$;

-- Insert dummy direct message data
create procedure insert_test_direct_message_data()
    language plpgsql as
$$
declare
    paul_id uuid;
    moe_id  uuid;
begin
    select member_id into paul_id from member where last_name = 'Atreides';
    select member_id into moe_id from member where first_name = 'Moses';

    -- Paul
    insert into direct_message (sender_id, receiver_id, content, unread)
    values (paul_id, moe_id, 'Fear is the mind killer Moe.', false);

    -- Moe
    insert into direct_message (sender_id, receiver_id, content, unread)
    values (moe_id, paul_id, 'Yeah I don''t know what that means.', false);

    -- Paul
    insert into direct_message (sender_id, receiver_id, content)
    values (paul_id, moe_id, 'It means I''m the duke now.');
end
$$;

-- Insert dummy member data
create procedure insert_test_member_data()
    language plpgsql as
$$
declare
    abbott_id   uuid = uuid_generate_v4();
    costello_id uuid = uuid_generate_v4();
    curly_id    uuid = uuid_generate_v4();
    moe_id      uuid = uuid_generate_v4();
    larry_id    uuid = uuid_generate_v4();
    paul_id     uuid = uuid_generate_v4();
    chani_id    uuid = uuid_generate_v4();

begin
    insert into member (member_id, last_name, first_name, username, email)
    values (abbott_id, 'Abbott', 'Bud', 'buddy_boy', 'bud@state.nj.us');

    insert into member (member_id, last_name, first_name, username, email)
    values (costello_id, 'Costello', 'Lou', 'lousy', 'lou@state.nj.us');

    insert into member (member_id, last_name, first_name, username, email)
    values (curly_id, 'Horwitz', 'Jerome', 'curly', 'curly@state.ny.us');

    insert into member (member_id, last_name, first_name, username, email)
    values (moe_id, 'Horwitz', 'Moses', 'moe', 'moe@state.ny.us');

    insert into member (member_id, last_name, first_name, username, email)
    values (larry_id, 'Feinberg', 'Louis', 'larry', 'larry@state.pa.us');

    insert into member (member_id, last_name, first_name, username, email)
    values (paul_id, 'Atreides', 'Paul', 'spicelover', 'house@atreides.dune');

    insert into member (member_id, last_name, first_name, username, email)
    values (chani_id, 'Kynes', 'Chani', 'sihaya', 'fremen@arrakis.dune');
end
$$;

-- Insert dummy membership data
create procedure insert_test_membership_data()
    language plpgsql as
$$
declare
    comedy_id   uuid;
    arrakis_id  uuid;
    abbott_id   uuid;
    costello_id uuid;
    curly_id    uuid;
    moe_id      uuid;
    larry_id    uuid;
    paul_id     uuid;
    chani_id    uuid;
begin
    select community_id into comedy_id from community where community_name = 'Comedy';
    select community_id into arrakis_id from community where community_name = 'Arrakis';

    select member_id into abbott_id from member where last_name = 'Abbott';
    select member_id into costello_id from member where last_name = 'Costello';
    select member_id into curly_id from member where first_name = 'Jerome';
    select member_id into moe_id from member where first_name = 'Moses';
    select member_id into larry_id from member where last_name = 'Feinberg';
    select member_id into paul_id from member where last_name = 'Atreides';
    select member_id into chani_id from member where last_name = 'Kynes';

    insert into membership values (comedy_id, abbott_id);
    insert into membership values (comedy_id, costello_id);
    insert into membership values (comedy_id, curly_id);
    insert into membership values (comedy_id, moe_id);
    insert into membership values (comedy_id, larry_id);
    insert into membership values (comedy_id, paul_id);
    insert into membership values (comedy_id, chani_id);

    insert into membership values (arrakis_id, paul_id);
    insert into membership values (arrakis_id, chani_id);
end
$$;

-- Insert dummy message data
-- TODO: Add messages to 'dialog' channel
create procedure insert_test_message_data()
    language plpgsql as
$$
declare
    dialogs_channel_id uuid;
    worms_channel_id   uuid;
    abbott_id          uuid;
    costello_id        uuid;
    moe_id             uuid;
    larry_id           uuid;
    paul_id            uuid;
    chani_id           uuid;
begin
    select channel_id into dialogs_channel_id from channel where channel_name = 'dialogs';
    select channel_id into worms_channel_id from channel where channel_name = 'worms';
    select member_id into abbott_id from member where last_name = 'Abbott';
    select member_id into costello_id from member where last_name = 'Costello';
    select member_id into larry_id from member where last_name = 'Feinberg';
    select member_id into moe_id from member where first_name = 'Moses';
    select member_id into paul_id from member where last_name = 'Atreides';
    select member_id into chani_id from member where last_name = 'Kynes';

    -- Abbott
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('969974b9-7de1-41a3-abe7-887585a4a2be', '7ca2c1c9-a174-4b7f-942c-f82f7e942a87',
            abbott_id, 'You throw the ball to first base.', '1922-06-22 19:10:25-05');

    -- Costello
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('ed2cac47-62c2-4d17-af6d-a85d14b3597f', '7ca2c1c9-a174-4b7f-942c-f82f7e942a87',
            costello_id, 'Then who gets it?', '1922-06-22 19:10:50-05');

    -- Abbott
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('fb21c41b-6f42-4229-8aa2-35ef122ca558', '7ca2c1c9-a174-4b7f-942c-f82f7e942a87',
            abbott_id, 'Naturally.', '1923-06-22 19:11:13-05');

    -- Costello
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('253efe17-3894-4b6c-bdd1-f0b04c422a6d', '7ca2c1c9-a174-4b7f-942c-f82f7e942a87',
            costello_id, 'Naturally.', '1934-06-22 19:11:25-05');

    -- Abbott
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('cb819bb4-12bf-4369-940f-6eacae1b1ac2', '7ca2c1c9-a174-4b7f-942c-f82f7e942a87',
            abbott_id, 'Now you''ve got it.', '1936-06-22 19:11:45-05');

    -- Costello
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('16ab7ba9-17df-4b06-9305-bfc81c0895a1', '7ca2c1c9-a174-4b7f-942c-f82f7e942a87',
            costello_id, 'I throw the ball to Naturally.', '1940-06-22 19:12:01-05');

    -- Abbott
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('ce854c6e-cc3e-4065-944e-4f977c45afc6', '7ca2c1c9-a174-4b7f-942c-f82f7e942a87',
            abbott_id, 'You don''t! You throw it to Who!', '1945-06-22 19:12:06-05');

    -- Moe
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('8d08b058-18fb-4b3f-bcbd-0f703a71448d', '916d2d30-0e3e-4b8e-8244-3f96f7f7c619',
            moe_id, 'Ah well.', '1947-06-22 19:12:06-05');

    -- Moe
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('7af059b6-1749-450a-ad8f-6f62c275583f', '916d2d30-0e3e-4b8e-8244-3f96f7f7c619',
            moe_id, 'Oh, before we answer that, I wanna prove we''re not gentlemen.',
            '1955-06-22 19:14:07-05');

    -- Larry
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('b54dd3f0-b222-42b4-abe8-7197f280f371', '916d2d30-0e3e-4b8e-8244-3f96f7f7c619',
            larry_id, 'Ow!', '1955-06-22 19:14:10-05');

    -- Moe
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('3c99f294-3fce-4638-9092-913fa58dd31a', '916d2d30-0e3e-4b8e-8244-3f96f7f7c619',
            moe_id, 'Fooled you, didn''t we?', '1955-06-22 19:15:06-05');

    -- Larry
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('0128340d-02dc-48c2-adfa-eb3382cf50ba', '916d2d30-0e3e-4b8e-8244-3f96f7f7c619',
            larry_id, 'We came to answer your ad.', '1967-06-22 19:20:45-05');

    -- Larry
    insert into message (message_id, channel_id, sender_id, content, timestamp)
    values ('e2df6c64-60c2-456c-a278-8da912e15c84', '916d2d30-0e3e-4b8e-8244-3f96f7f7c619',
            larry_id, 'Fine detectives we turned out to be. This is humiliatin''.',
            '1970-06-22 19:22:03-05');

    -- Paul
    insert into message (channel_id, sender_id, content, timestamp)
    values (worms_channel_id, paul_id, 'Fear is the mind killer @spicelover.', now()::timestamp - '2 weeks'::interval);

    -- Chani
    insert into message (channel_id, sender_id, content, timestamp)
    values (worms_channel_id, chani_id, 'please reply', now()::timestamp - '1 week'::interval);

    -- Paul
    insert into message (channel_id, sender_id, content, timestamp)
    values (worms_channel_id, paul_id, 'i replied already!', now()::timestamp - '1 week'::interval);
end
$$;

-- Insert dummy message status data
create procedure insert_test_message_status_data()
    language plpgsql as
$$
declare
    abbott_id   uuid;
    costello_id uuid;
begin
    select member_id into abbott_id from member where last_name = 'Abbott';
    select member_id into costello_id from member where last_name = 'Costello';

    -- Abbott & Costello messages
    insert into message_status (receiver_id, message_id, read_status)
    values (costello_id, '969974b9-7de1-41a3-abe7-887585a4a2be', true);

    insert into message_status (receiver_id, message_id, read_status)
    values (abbott_id, 'ed2cac47-62c2-4d17-af6d-a85d14b3597f', true);

    insert into message_status (receiver_id, message_id, read_status)
    values (costello_id, 'fb21c41b-6f42-4229-8aa2-35ef122ca558', false);

    insert into message_status (receiver_id, message_id, read_status)
    values (abbott_id, '253efe17-3894-4b6c-bdd1-f0b04c422a6d', true);

    insert into message_status (receiver_id, message_id, read_status)
    values (costello_id, 'cb819bb4-12bf-4369-940f-6eacae1b1ac2', false);

    insert into message_status (receiver_id, message_id, read_status)
    values (abbott_id, '16ab7ba9-17df-4b06-9305-bfc81c0895a1', false);

    insert into message_status (receiver_id, message_id, read_status)
    values (costello_id, 'ce854c6e-cc3e-4065-944e-4f977c45afc6', false);

    -- Moe & Larry messages
    -- TODO: Convert uuid's to dynamic values
    insert into message_status(receiver_id, message_id, read_status)
    values ('c6d256cc-c6bf-4a65-a74e-26eba5bdba9e',
            '8d08b058-18fb-4b3f-bcbd-0f703a71448d', false);

    insert into message_status(receiver_id, message_id, read_status)
    values ('c6d256cc-c6bf-4a65-a74e-26eba5bdba9e',
            '7af059b6-1749-450a-ad8f-6f62c275583f', true);

    insert into message_status(receiver_id, message_id, read_status)
    values ('982dd2ff-35e3-46f3-bdbc-acfacf28e225',
            'b54dd3f0-b222-42b4-abe8-7197f280f371', false);

    insert into message_status(receiver_id, message_id, read_status)
    values ('c6d256cc-c6bf-4a65-a74e-26eba5bdba9e',
            '3c99f294-3fce-4638-9092-913fa58dd31a', true);

    insert into message_status(receiver_id, message_id, read_status)
    values ('982dd2ff-35e3-46f3-bdbc-acfacf28e225',
            '0128340d-02dc-48c2-adfa-eb3382cf50ba', true);

    insert into message_status(receiver_id, message_id, read_status)
    values ('982dd2ff-35e3-46f3-bdbc-acfacf28e225',
            'e2df6c64-60c2-456c-a278-8da912e15c84', true);
end
$$;

-- Insert dummy suspension data
create procedure insert_test_suspension_data()
    language plpgsql as
$$
declare
    cooperstown_id uuid;
    arrakis_id     uuid;
    larry_id       uuid;
    curly_id       uuid;
    paul_id        uuid;
begin
    select community_id into cooperstown_id from community where community_name = 'Comedy';
    select community_id into arrakis_id from community where community_name = 'Arrakis';
    select member_id into larry_id from member where last_name = 'Feinberg';
    select member_id into curly_id from member where first_name = 'Jerome';
    select member_id into paul_id from member where last_name = 'Atreides';

    -- Larry suspension
    insert into suspension (community_id, member_id, duration, date_suspended)
    values (cooperstown_id, larry_id, 32609, '1970-09-26');

    -- Curly suspension
    insert into suspension (community_id, member_id, duration, date_suspended)
    values (cooperstown_id, curly_id, 3651, '1990-01-01');

    insert into suspension (community_id, member_id, duration, date_suspended)
    values (arrakis_id, paul_id, 60, now()::timestamp - '1 week'::interval);
end
$$;
