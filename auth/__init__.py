
from extern import query
from werkzeug.security import generate_password_hash, check_password_hash

class loginClass():

    def __init__(self,username,password):
        self.username=username
        self.password=generate_password_hash(password)
        print(self.password)
        self.verify()

    def verify(self):
        sql="SELECT * FROM users WHERE username=%s"
        getData=query(sql,"select",[self.username.lower()])
        print(getData)
        for i in getData:
            if check_password_hash(i[2], self.password):
                return True
            else:
                return False
print(loginClass("bogdan","password").verify())