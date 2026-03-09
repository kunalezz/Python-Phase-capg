class User:
    def __init__(self, email):
        self._email = email # protected

    @property # getter property
    def email(self):
        return self._email
    
    @email.setter # setter property
    def email(self, newEmail):
        if '@' and '.com' in newEmail:
            self._email = newEmail
        else :
            print("error")

#main
user1 = User('csgo@gmail.com')
print(user1.email)
user1.email = 'kez@gmail.com'
print(user1.email)
