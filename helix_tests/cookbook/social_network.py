import helix
from helix.client import Query
from helix.types import Payload
from typing import List

db = helix.Client(local=True)

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

print("Creating users")
print(db.query(create_user("John", 30, "john@example.com", 1722222222)))
print(db.query(create_user("Jane", 25, "jane@example.com", 1722222222)))

class get_users(Query):
    def __init__(self):
        super().__init__()
    
    def query(self) -> List[Payload]:
        return [{}]
    
    def response(self, response):
        return response
    
print("Getting users")
print(db.query(get_users()))

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

print("Creating follow")
follower_id = input("Enter follower id: ")
followed_id = input("Enter followed id: ")
print(db.query(create_follow(follower_id, followed_id, 1892222222)))

class create_post(Query):
    def __init__(self, user_id: str, content: str, now: int):
        super().__init__()
        self.user_id = user_id
        self.content = content
        self.now = now
    
    def query(self):
        return [{"user_id": self.user_id, "content": self.content, "now": self.now}]
            
    
    def response(self, response):
        return response

print("Creating post")
user_id = input("Enter user id: ")
content = "Sample Post Content Hello World"
print(db.query(create_post(user_id, content, 1983333333)))
    
class get_posts(Query):
    def __init__(self):
        super().__init__()
    
    def query(self) -> List[Payload]:
        return [{}]
    
    def response(self, response):
        return response
    
print("Getting posts")
print(db.query(get_posts()))

class get_posts_by_user(Query):
    def __init__(self, user_id: str):
        super().__init__()
        self.user_id = user_id
    
    def query(self) -> List[Payload]:
        return [{"user_id": self.user_id}]
    
    def response(self, response):
        return response
    
print("Getting posts by user")
user_id = input("Enter user id: ")
print(db.query(get_posts_by_user(user_id)))

class get_followed_users(Query):
    def __init__(self, user_id: str):
        super().__init__()
        self.user_id = user_id
    
    def query(self) -> List[Payload]:
        return [{"user_id": self.user_id}]
    
    def response(self, response):
        return response
    
print("Getting followed users")
user_id = input("Enter user id: ")
print(db.query(get_followed_users(user_id)))

class get_followed_users_posts(Query):
    def __init__(self, user_id: str):
        super().__init__()
        self.user_id = user_id
    
    def query(self) -> List[Payload]:
        return [{"user_id": self.user_id}]
    
    def response(self, response):
        return response

print("Getting followed users posts")
user_id = input("Enter user id: ")
print(db.query(get_followed_users_posts(user_id)))
