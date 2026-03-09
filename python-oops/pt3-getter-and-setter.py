import datetime as datetime

class User:
    def __init__(self, email):
        self._email = email # protected

    def getEmail(self): # Getter method
        print(f"The email was accessed recently.")
        print(self._email)
    
    def setEmail(self, newEmail):
        if '@' and '.com' in newEmail:
            self._email = newEmail
        else:
            print('error')


#main
user1 = User('Danny@gmail.com')
user1.getEmail()
user1.setEmail('csgo@gmail.com')
user1.getEmail()