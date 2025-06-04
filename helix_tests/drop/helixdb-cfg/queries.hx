QUERY drop_following(userID: ID) =>
    DROP N<User>(userID)::Out<Follows>
    RETURN NONE

// general queries

QUERY get_users() =>
    users <- N<User>
    RETURN users

QUERY create_user(name: String, age: U32, email: String, now: I32) =>
    user <- AddN<User>({name: name, age: age, email: email, created_at: now, updated_at: now})
    RETURN user

QUERY create_follow(follower_id: ID, followed_id: ID, now: I32) =>
    follower <- N<User>(follower_id)
    followed <- N<User>(followed_id)
    AddE<Follows>({since: now})::From(follower)::To(followed)
    RETURN "success"

QUERY get_followed_users(user_id: ID) =>
    followed <- N<User>(user_id)::Out<Follows>
    RETURN followed