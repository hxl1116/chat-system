-- Check if a member is suspended from a community (username and community name)
create or replace function is_suspended(username text, comm_name text) returns bool
    language plpgsql as
$$
declare
    resume_date date;

begin
    select (date_suspended + '1 day'::interval * duration)::date
    into resume_date
    from community,
         membership,
         member,
         suspension
    where community.community_id = suspension.community_id
      and member.member_id = suspension.member_id
      and member.username = is_suspended.username
      and community_name = comm_name;

    return resume_date >= now();
end
$$;

-- Check if a member is suspended from a community (member id and community id)
create or replace function is_suspended(mem_id uuid, comm_id uuid) returns bool
    language plpgsql as
$$
declare
    resume_date date;

begin
    select (date_suspended + '1 day'::interval * duration)::date
    into resume_date
    from suspension
    where suspension.community_id = comm_id
      and suspension.member_id = mem_id;

    return resume_date >= now();
end
$$;

-- Check if a member can change their username
create or replace function can_change_username(member_id uuid) returns bool
    language plpgsql as
$$
declare
    can_change_date date;
begin
    select (username_changed_date + interval '6' month)::date
    into can_change_date
    from member
    where member.member_id = can_change_username.member_id;

    return can_change_date <= now() or can_change_date is null;
end
$$;

-- Get a member's `member_id` by their last name
create or replace function get_member_id_by_last(last_name text) returns uuid
    language plpgsql as
$$
declare
    id uuid;
begin
    select member_id into id from member where member.last_name = get_member_id_by_last.last_name;

    return id;
end
$$;

-- Get a list of suspended members who have sent a message within a given date range
-- FIXME: Returns no member ids
create or replace function get_suspended_msg_senders(start_date date, end_date date) returns uuid[]
    language plpgsql as
$$
declare
    record  record;
    members uuid[];
begin
    for record in select member_id, community_id
                  from membership,
                       message
                  where sender_id = member_id
                    and timestamp between start_date and end_date
        loop
            if is_suspended(member_id := record.member_id, community_id := record.community_id) then
                members = members || record.member_id;
            end if;
        end loop;

    return members;
end
$$;
