QUERY get_by_index(index_field: String) =>
    node <- N<User>({email:index_field})
    RETURN node

// users

QUERY create_user(name: String, age: U32, email: String, now: I32) =>
    user <- AddN<User>({name: name, age: age, email: email, created_at: now, updated_at: now})
    RETURN user

QUERY get_users() =>
    users <- N<User>
    RETURN users