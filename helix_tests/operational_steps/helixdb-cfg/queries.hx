
QUERY create_user(name: String, age: U32, email: String, now: I32) =>
    user <- AddN<User>({name: name, age: age, email: email, created_at: now, updated_at: now})
    RETURN user


QUERY user_statistics() =>
    user_count <- N<User>::COUNT
    RETURN user_count

QUERY get_range(start: U32, end: U32) =>
    range <- N<User>::RANGE(start, end)
    RETURN range
    
QUERY get_users() =>
    users <- N<User>
    RETURN users

