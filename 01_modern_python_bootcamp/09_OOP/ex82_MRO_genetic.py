# class Mother:
#     def __init__(self, eye_color, hair_color, hair_type):
#         self.eye_color = eye_color
#         self.hair_color = hair_color
#         self.hair_type = hair_type

# class Father:
#     def __init__(self, eye_color, hair_color, hair_type):
#         self.eye_color = eye_color
#         self.hair_color = hair_color
#         self.hair_type = hair_type

# class Child(Mother, Father):
#     pass


class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"

class Child(Mother, Father):
    pass