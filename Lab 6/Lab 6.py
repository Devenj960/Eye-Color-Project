import random

class Parent:
    def __init__ (self, gene1, gene2):
        self.gene1 = gene1.capitalize()
        self.gene2 = gene2.capitalize()

class Child:
    def __init__ (self, p1, p2):
        self.gene1 = random.choice([p1.gene1, p1.gene1])
        self.gene2 = random.choice([p2.gene1, p2.gene2])
        self.eye_color = self.determine_eye_color()

    def determine_eye_color(self):
        if "Brown" in [self.gene1, self.gene2]:
            return "Brown"
        return "Blue"

p1_gene1 = input("Please enter gene 1 of parent 1: ")
p1_gene2 = input("Please enter gene 2 of parent 1: ")
p2_gene1 = input("Please enter gene 1 of parent 2: ")
p2_gene2 = input("Please enter gene 2 of parent 2: ")
p1 = Parent(p1_gene1, p1_gene2)
p2 = Parent(p2_gene1, p2_gene2)
c = Child(p1, p2)
print("Parent 1 genes:", p1.gene1, p1.gene2)
print("Parent 2 genes:", p2.gene1, p2.gene2)
print("Child gene 1:", c.gene1)
print("Child gene 2:", c.gene2)
print("Child eye color:", c.eye_color)