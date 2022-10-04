
class User:
    def __init__(self,first_name, last_name, email, age):        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

my_user = User("Joshua", "Roy", "joshua.roy69@gmail.com", "27")
user1 = User("Hannah", "Roy", "hannah.roy@gmail.com", "27")
user2 = User("Bob", "Saget", "bobsaget@gmail.com", "56")
my_user.display_info()
user1.display_info()
user2.display_info()
my_user.enroll()
user1.enroll()
user2.enroll()
my_user.display_info()
user1.display_info()
user2.display_info()
user1.spend_points(50)
user2.spend_points(80)
my_user.spend_points(35)
my_user.display_info()
user1.display_info()
user2.display_info()