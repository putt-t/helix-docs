import helix
from helix import Client, Query, Payload
from typing import Tuple, List, Any

db = Client(local=True)

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


class user_statistics(helix.Query):
    def __init__(self):
        super().__init__()
    
    def query(self) -> List[Payload]:
        return [{}]
    
    def response(self, response):
        return response.get('user_count')

class get_users(Query):
    def __init__(self):
        super().__init__()
    
    def query(self) -> List[Payload]:
        return [{}]
    
    def response(self, response):
        return response

class get_range(Query):
    def __init__(self, start: int, end: int):
        super().__init__()
        self.start = start
        self.end = end
    
    def query(self) -> List[Payload]:
        return [{"start": self.start, "end": self.end}]
    
    def response(self, response):
        return response
    
# add some users in
# print("Creating users...")
# user1 = db.query(create_user("John", 30, "john@example.com", 1722222222))

# print("Created user1:", user1)

# user2 = db.query(create_user("Jane", 25, "jane@example.com", 1722222222))
# print("Created user2:", user2)

# user3 = db.query(create_user("Bob", 35, "bob@example.com", 1722222222))
# print("Created user3:", user3)

# user4 = db.query(create_user("James", 21, "james@example.com", 1722222222))
# print("Created user4:", user4)


# users = db.query(get_users())
# print("Users:", users)

# user_count = db.query(user_statistics())
# print("User count:", user_count)

range = db.query(get_range(1, 3))
print("Range:", range)


    
