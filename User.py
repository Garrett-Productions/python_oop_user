class User:
    def __init__(self, first_name, last_name, email, age):
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
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True 
            self.gold_card_points = 200
            return True


    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Sorry you're broke.")



Garrett = User("Garrett", "Turner", "GarrettTurnerProductions@gmail.com", 28)

Garrett.display_info()
Garrett.enroll()
Garrett.spend_points(50)

#We created 2 more instances of the user class below

Baker = User("Justin", "Baker", "JustinBaker268@gmail.com", 29)
Big_jerm = User("Jeremy", "Brinson", "BigJerm@aol.com", 28)

Baker.display_info()
Big_jerm.display_info()

#We are enrolling the 2nd User Below 

Baker.enroll()
Baker.display_info()

#Our 2nd User is spending 80 points Below

Baker.spend_points(80)
Baker.display_info()

#Does our user have enough points to spend?

Baker.spend_points(200)
