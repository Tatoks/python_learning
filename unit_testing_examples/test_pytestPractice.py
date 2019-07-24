from Concepts_with_examples.modules_and_packages.carsPackage import Audi
import pytest


@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    print("Executed Test_file1")


@pytest.mark.set2
def test_new_car():
    car = Audi.AudiSubDealers()
    print(car.dealers())
    assert 1 == 1, "should be equal"

# pytest -m set2 -v filepath
