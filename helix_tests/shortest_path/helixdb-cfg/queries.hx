
QUERY hnswinsert(vector: [F64]) =>
    AddV<Embedding>(vector)
    RETURN "Success"

QUERY hnswsearch(query: [F64], k: I32) =>
    res <- SearchV<Embedding>(query, k)
    RETURN res

QUERY create_user(name: String, age: U32, email: String, now: I32) =>
    user <- AddN<User>({name: name, age: age, email: email, created_at: now, updated_at: now})
    RETURN user


QUERY get_users() =>
    users <- N<User>
    RETURN users

QUERY get_shortest_path(from_id: ID, to_id: ID) => 
    path_to <- N<User>(from_id)::ShortestPath::To(to_id)
    path_from <- N<User>(from_id)::ShortestPath::From(to_id)
    RETURN path_to, path_from


QUERY create_follow(follower_id: ID, followed_id: ID, now: I32) =>
    follower <- N<User>(follower_id)
    followed <- N<User>(followed_id)
    AddE<Follows>({since: now})::From(follower)::To(followed)
    RETURN "success"

QUERY get_followed_users(user_id: ID) =>
    followed <- N<User>(user_id)::Out<Follows>
    RETURN followed
