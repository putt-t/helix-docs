import helix
from helix import Client, Query, Payload
from typing import Tuple, List, Any

db = Client(local=True)

class get_users(helix.Query):
    def __init__(self):
        super().__init__()
    def query(self) -> List[Any]:
        return [{}]
    def response(self, response):
        return response
    
class create_user(Query):
    def __init__(self, name:str, age:int, email:str, now:int):
        super().__init__()
        self.name = name
        self.age = age
        self.email = email
        self.now = now
    
    def query(self) -> List[Payload]:
        return [{"name": self.name, "age": self.age, "email": self.email, "now": self.now}]
            
    def response(self, response):
        return response


class create_follow(Query):
    def __init__(self, follower_id: str, followed_id: str, now: int):
        super().__init__()
        self.follower_id = follower_id
        self.followed_id = followed_id
        self.now = now
    
    def query(self):
        return [{"follower_id": self.follower_id, "followed_id": self.followed_id, "now": self.now}]
            
    
    def response(self, response):
        return response


class get_shortest_path(helix.Query):
    def __init__(self, from_id: str, to_id: str):
        super().__init__()
        self.from_id = from_id
        self.to_id = to_id
    
    def query(self) -> List[Any]:
        return [{"from_id": self.from_id, "to_id": self.to_id}]
    
    def response(self, response):
        return response

class get_followed_users(Query):
    def __init__(self, user_id: str):
        super().__init__()
        self.user_id = user_id
    
    def query(self) -> List[Payload]:
        return [{"user_id": self.user_id}]
    
    def response(self, response):
        return response
    
# add some users in
print("Creating users...")
user1 = db.query(create_user("John", 30, "john@example.com", 1722222222))

print("Created user1:", user1)

user2 = db.query(create_user("Jane", 25, "jane@example.com", 1722222222))
print("Created user2:", user2)

user3 = db.query(create_user("Bob", 35, "bob@example.com", 1722222222))
print("Created user3:", user3)

user4 = db.query(create_user("James", 21, "james@example.com", 1722222222))
print("Created user4:", user4)

# get users info
# users_result = db.query(get_users())
# print("Get users result:", users_result)



# Create a follow relationship between John and Bob using actual IDs

# print("Creating follow relationship...")
follow_result = db.query(create_follow(user1['id'], user2['id'], 1892222222))
print("Follow result:", follow_result)


# Path I tried
# John -> Bob -> James
# John -> James

# # Bob to James
# follow_result = db.query(create_follow("1f04086c-bb0c-64d8-92e4-01020304050", "1f04086c-bb1b-6320-92e5-010203040506", 1892222222))
# # print("Follow result:", follow_result)

# # John to James
# follow_result = db.query(create_follow("1f04086c-baec-6e62-92e2-010203040506", "1f04086c-bb1b-6320-92e5-010203040506", 1892222222))
# # print("Follow result:", follow_result)

# # incase you want to see followed result
# followed_users_result = db.query(get_followed_users("1f04086c-baec-6e62-92e2-010203040506"))
# print("Followed users result:", followed_users_result)


# # Test shortest path between the same users (John -> Bob)
# # print("Testing shortest path...")
# path_result = db.query(get_shortest_path("1f04086c-baec-6e62-92e2-010203040506", "1f04086c-bb1b-6320-92e5-010203040506"))
# print("Shortest path result:", path_result)

# # the above should give John to James but it gave me a weird error 