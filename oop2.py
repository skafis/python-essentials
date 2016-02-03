 #!/usr/bin/python3

class AnimalActions:
    def quack (self): return self.strings[feathers'quack']
    def feathers(self): return self.strings['feathers']
    def bark (self): return self.strings ['bark']
    def fur (self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict (
        quack = "Quaaaak",
        feathers = "The duck has gray white feathers",
        bark = "the duck can not bark",
        fur = "the duck has no fur"
    )
class Person(AnimalActions):
    strings = dict(
       quack = "the person imitates a duck",
        feathers= "the person takes feathers from the ground and shows it."
        bark = "the person says woof",
        fur = "the person puts on a fur coat"
    )

class Dog (AnimalActions):
    strings = dict(
        quack = "the dog cannot quack",
        feathers = "the dog has no feathers",
        bark = "Arf!",
        fur= "the dog has white fur with blackspots"
    )

def in_the_doghouse():
    print(dog.bark())
    print (dog.fur())

def in_the_forest():
    print(duck.bark())
    print (duck.fur())

def main ():
    donald = Duck()
    john   = Person()
    fido = Dog()

    print("-In the forest:")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("-In the doghouse:")
    for o in (donald, john, fido):
        in_the_doghouse(o)


if __name__=="__main__":main()
