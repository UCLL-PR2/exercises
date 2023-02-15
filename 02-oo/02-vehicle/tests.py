import pytest
from student import *


@pytest.fixture
def car():
    return Car(
        make="Toyota",
        model="Corolla",
        year=2020,
        num_doors=4,
    )

@pytest.fixture
def truck():
    return Truck(
        make="Toyota",
        model="Corolla",
        year=2020,
        bed_size="large",
    )


def test_create_car():
    car = Car(
        make="Toyota",
        model="Corolla",
        year=2020,
        num_doors=4
    )

    assert car.make == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2020
    assert car.speed == 0
    assert car.num_doors == 4


def test_create_truck():
    truck = Truck(
        make="Toyota",
        model="Corolla",
        year=2020,
        bed_size="large",
    )

    assert truck.make == "Toyota"
    assert truck.model == "Corolla"
    assert truck.year == 2020
    assert truck.speed == 0
    assert truck.bed_size == "large"


def test_vehicle_accelerate(car):
    assert car.speed == 0
    car.accelerate(amount=10)
    assert car.speed == 10
    car.accelerate(amount=15)
    assert car.speed == 25


def test_vehicle_brake(car):
    assert car.speed == 0
    car.accelerate(amount=100)
    assert car.speed == 100
    car.brake(amount=20)
    assert car.speed == 80


def test_car_honk(car):
    assert car.honk() == "Beep beep!"


def test_truck_honk(truck):
    assert truck.honk() == "Honk honk!"
