# import Audi module from cars package aliased as car

import Day5.carsPackage.Audi as car

car1 = car.AudiCar()
print(car1.out_models())

dealer1 = car.AudiSubDealers()
print(dealer1.out_dealers())