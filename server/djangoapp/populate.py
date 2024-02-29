from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology",
            "founded_year": 1980, "headquarters": "Tokio",
            "website": "https://www.nissan-global.com/EN/COMPANY/PROFILE/"},
        {"name": "Mercedes", "description": "Great cars. German technology",
            "founded_year": 1980, "headquarters": "Stuttgart",
            "website": "https://group.mercedes-benz.com/contact/"},
        {"name": "Audi", "description": "Great cars. German technology",
            "founded_year": 1980, "headquarters": "Ingolstadh", "website": ""},
        {"name": "Kia", "description": "Great cars. Korean technology",
            "founded_year": 1980, "headquarters": "Seoul", "website": ""},
        {"name": "Toyota", "description": "Great cars. Japanese technology",
            "founded_year": 1980, "headquarters": "Toyota", "website": ""},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'], description=data['description'], founded_year=data['founded_year'], headquarters=data['headquarters'], website=data['website']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "color": "Red",
            "doors": "Five", "extras": "SOUND", "price": 10000,
            "dealer_id": 1},
        {"name": "Qashqai", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "color": "Red",
            "doors": "Five", "extras": "NAV", "price": 11000,
            "dealer_id": 1},
        {"name": "XTRAIL", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "color": "Green",
            "doors": "Three", "extras": "NONE", "price": 12000,
            "dealer_id": 1},
        {"name": "A-Class", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "color": "Red",
            "doors": "Five", "extras": "SOUND", "price": 13000,
            "dealer_id": 1},
        {"name": "C-Class", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "color": "Red",
            "doors": "Three", "extras": "AIR", "price": 14000,
            "dealer_id": 1},
        {"name": "E-Class", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "color": "Yellow",
            "doors": "Five", "extras": "NAV", "price": 15000,
            "dealer_id": 1},
        {"name": "A4", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "color": "Red",
            "doors": "Five", "extras": "SOUND", "price": 15400,
            "dealer_id": 1},
        {"name": "A5", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "color": "Red",
            "doors": "Three", "extras": "AIR", "price": 16000,
            "dealer_id": 1},
        {"name": "A6", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "color": "Yellow",
            "doors": "Five", "extras": "SOUND", "price": 17000,
            "dealer_id": 1},
        {"name": "Sorrento", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "color": "Yellow",
            "doors": "Five", "extras": "SOUND", "price": 20000,
            "dealer_id": 1},
        {"name": "Carnival", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "color": "Red",
            "doors": "Five", "extras": "SOUND", "price": 10200,
            "dealer_id": 1},
        {"name": "Cerato", "model_type": "Sedan", "year": 2023,
            "car_make": car_make_instances[3], "color": "Red",
            "doors": "Three", "extras": "SOUND", "price": 10001,
            "dealer_id": 1},
        {"name": "Corolla", "model_type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "color": "Red",
            "doors": "Five", "extras": "SOUND", "price": 10030,
            "dealer_id": 1},
        {"name": "Camry", "model_type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "color": "Red",
            "doors": "Five", "extras": "SOUND", "price": 10400,
            "dealer_id": 1},
        {"name": "Kluger", "model_type": "SUV", "year": 2023,
            "car_make": car_make_instances[4], "color": "Red",
            "doors": "Five", "extras": "NAV", "price": 10300,
            "dealer_id": 1},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], car_make=data['car_make'],
            model_type=data['model_type'], year=data['year'],
            color=data['color'], doors=data['doors'],
            price=data['price'], dealer_id=data['dealer_id'],
            extras=data['extras'])
