# import Audi module from cars package aliased as car

import Concepts_with_examples.modules_and_packages.carsPackage.Audi as Car

car1 = Car.AudiCar()
print(car1.out_models())

dealer1 = Car.AudiSubDealers()
print(dealer1.out_dealers())
