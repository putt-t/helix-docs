QUERY update_user(userID: ID, name: String, age: U32) =>
    updatedUsers <- N<User>(userID)::UPDATE({name: name, age: age})
    RETURN updatedUsers

QUERY get_users() =>
    users <- N<User>
    RETURN users

QUERY create_user(name: String, age: U32, email: String, now: I32) =>
    user <- AddN<User>({name: name, age: age, email: email, created_at: now, updated_at: now})
    RETURN user