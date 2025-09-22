class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Example usage and MRO exploration
if __name__ == "__main__":
    ff = FlyingFish()
    ff.fly()
    ff.swim()
    ff.habitat()
    print("MRO:", [cls.__name__ for cls in FlyingFish.mro()])