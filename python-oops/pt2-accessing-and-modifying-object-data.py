class User:
    def __init__(self, username, userEmail, userNumber):
        self.username = username
        self._userEmail = userEmail # after using _ before userEmail, this means that the userEmail is now protected and can't be used outside the class 
        self.userNumber = userNumber

    def greet(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}.")

    def clean_email(self): # this is getter function 
        return self._userEmail.lower().strip()

    

#main
user1 = User("Anna Ralph","AnnaRalph@gmail.com","888-999")
user2 = User("Megan Fox","MeganFox@gmail.com","999-999")

user1.greet(user2)

user3 = User("Niko","NikoCSgo@gmail.com","000-666")
print(f"Here we are accessing the Protected Email outside the class directly ''{user3._userEmail}''")
print(f"here we are using the getter method to access the value of the protected attribute of the class. ''{user3.clean_email()}''")

