drop trigger if exists username_change on member;

create trigger username_change
    after update
    on member
    for each row
execute procedure handle_username_change();