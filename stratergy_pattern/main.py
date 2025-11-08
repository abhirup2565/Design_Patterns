from duck import MallardDuck,ModelDuck
from fly import FlyRocketPowered

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()

    print("\n--- Changing behavior at runtime ---")
    model = ModelDuck()
    model.display()
    model.perform_fly()
    # Change behavior dynamically
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()