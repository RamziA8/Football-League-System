class Player:
    def __init__(self, name, age, height, weight, position):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        self.shirt_number = None
        self.club = None

    def set_weight(self, new_weight):
        self.weight = new_weight

    def set_height(self, new_height):
        self.height = new_height

    def assign_shirt_number(self, number):
        self.shirt_number = number

    def sign_for_club(self, club):
        self.club = club
        club.players.append(self)

    def leave_club(self):
        self.club.players.remove(self)
        self.club = None

    def get_bmi(self):
        BMI = self.weight / (self.height * self.height)
        return BMI

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def print_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Height: ", self.height)
        print("Weight: ", self.weight)
        print("Position: ", self.position)
        print("Shirt Number: ", self.shirt_number)
        print("Club: ", self.club.name if self.club else "No club")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "position": self.position,
            "shirt_number": self.shirt_number,
            "club": self.club.name if self.club else "No club"
        }
    

        # Test code
#ramzi = Player("Ramzi", 19, 1.75, 72, "RW")
#ramzi.assign_shirt_number(8)
#ramzi.print_info()
#print("Is adult:", ramzi.is_adult())
#print("BMI:", ramzi.get_bmi())
#print("Dict:", ramzi.to_dict())