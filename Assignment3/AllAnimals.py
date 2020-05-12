from Animals import Animals  # abstraction


class Cat(Animals):
    __colour = "black"  # private access specifier
    print("Cats are " + __colour + " in colour(colour variable accessed only within the class")

    def qualities(self):
        print("Cats have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Cats have a tail")
        else:
            print("Cats don't have a tail")


class Dog(Animals):
    __colour = "brown"
    print("Dogs are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Dogs have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Dogs have a tail")
        else:
            print("Dogs don't have a tail")


class Human(Animals):
    __colour = "skin"
    print("Humans are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Humans have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Humans have a tail")
        else:
            print("Humans don't have a tail")


class Mouse(Animals):
    __colour = "grey"
    print("Mouses are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Mouses have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Mouses have a tail")
        else:
            print("Mouses don't have a tail")


class Horse(Animals):
    __colour = "brown"
    print("Horses are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Horses have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Horses have a tail")
        else:
            print("Horses don't have a tail")


class Lion(Animals):
    __colour = "yellow"
    print("Horses are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Lions have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Lions have a tail")
        else:
            print("Lions don't have a tail")


class Elephant(Animals):
    __colour = "grey"
    print("Elephants are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Elephants have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Elephants have a tail")
        else:
            print("Elephants don't have a tail")


class Rabbit(Animals):
    __colour = "white"
    print("Rabbits are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Rabbits have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Rabbits have a tail")
        else:
            print("Rabbits don't have a tail")


class Penguin(Animals):
    __colour = "white"
    print("Penguins are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Penguins have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Penguins have a tail")
        else:
            print("Penguins don't have a tail")


class Bear(Animals):
    __colour = "brown"
    print("Bears are " + __colour + " in colour(colour variable accessed only within the class)")

    def qualities(self):
        print("Bears have " + str(self.legs) + " legs(legs variable accessed outside the class)")
        if self.tail:
            print("Bears have a tail")
        else:
            print("Bears don't have a tail")
