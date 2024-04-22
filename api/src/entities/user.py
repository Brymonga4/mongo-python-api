class User:
    def __init__(self, id: str, username:str, pwd: str):
        self.id = id
        self.username = username
        self.pwd = pwd

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "pwd": self.pwd  
        }