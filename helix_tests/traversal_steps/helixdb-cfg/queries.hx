
// generic queries

QUERY create_user(name: String, age: U32, email: String, now: I32) =>
    user <- AddN<User>({name: name, age: age, email: email, created_at: now, updated_at: now})
    RETURN user

QUERY create_follow(follower_id: ID, followed_id: ID, now: I32) =>
    follower <- N<User>(follower_id)
    followed <- N<User>(followed_id)
    AddE<Follows>({since: now})::From(follower)::To(followed)
    RETURN "success"

QUERY create_post(user_id: ID, content: String, now: I32) =>
    user <- N<User>(user_id)
    post <- AddN<Post>({content: content, created_at: now, updated_at: now})
    AddE<Created>({created_at: now})::From(user)::To(post)
    RETURN post

QUERY get_users() =>
    users <- N<User>
    RETURN users


QUERY get_posts() =>
    posts <- N<Post>
    RETURN posts

// traversals from nodes

QUERY get_user_following(userID: ID) =>
    following <- N<User>(userID)::Out<Follows>
    RETURN following

QUERY get_user_followers(userID: ID) =>
    followers <- N<User>(userID)::In<Follows>
    RETURN followers

QUERY get_following_details(userID: ID) =>
    following <- N<User>(userID)::OutE<Follows>
    RETURN following

QUERY get_followers_details(userID: ID) =>
    followers <- N<User>(userID)::InE<Follows>
    RETURN followers

// traversal from edges

QUERY get_follower_from_relationship(relationshipID: ID) =>
    follower <- E<Follows>(relationshipID)::FromN
    RETURN follower

QUERY get_following_from_relationship(relationshipID: ID) =>
    followed_user <- E<Follows>(relationshipID)::ToN
    RETURN followed_user