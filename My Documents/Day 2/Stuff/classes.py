class Person:
    parts = ["head", "eyes", 'mouth', 'body']

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []
        
    def addskill(self,skill):
        self.skills.append(skill)
ob1 = Person("")
print(p1.parts)