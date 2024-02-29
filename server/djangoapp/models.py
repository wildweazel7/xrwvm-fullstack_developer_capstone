# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = \ 
    models.TextField(help_text="Any useful information about maker")
    founded_year = models.IntegerField \
    (help_text="Year the company was founded")
    headquarters = models.CharField(max_length=255, \
    help_text="Location of the company's headquarters")
    website = models.URLField(max_length=200, blank=True, \ 
    help_text="Company's official website")


    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    mColorChoice = [
        ('RED',"Red"), 
        ('Blue', "Blue"), 
        ('Black', "Black"), 
        ('White', "White"), 
        ('Green', "Green"), 
        ('Yellow', "Yellow")
    ]
    mDoorChoice = [
        ("Three","Three"), 
        ("Five","Five")
    ]
    mExtraChoice = [
        ("NONE","No Extra"),
        ("SOUND","Sound system"), 
        ("AIR","Air-cooling-system"), 
        ("NAV", "Navigation system")
    ]
    mTypeCoice = [
        ('SEDAN', 'Sedan'), 
        ('SUV', 'SUV'), 
        ('WAGON', 'Wagon')
    ]
       
    name = models.CharField(max_length=255, unique=True, help_text="Name of model")
    model_type = models.CharField(max_length=50, choices=mTypeCoice, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2015)
        ])
    car_make = models.ForeignKey\
    (CarMake, on_delete=models.CASCADE, related_name='car_models')
    color = models.CharField\
    (max_length=255, choices=mColorChoice, help_text="Offered colors of the model")
    doors = models.CharField\
    (max_length=255, choices=mDoorChoice, help_text="Number of doors possible", default="Five")
    extras = models.CharField\
    (max_length=255, choices=mExtraChoice, help_text="List of extras",blank=True, default='NONE')
    price = models.DecimalField\
    (max_digits=10, decimal_places=2, help_text="Price in USD",blank=True, default=10000)
    dealer_id = models.IntegerField(blank=True,null=True,default=1)

    def __str__(self):
        # Returns the name of the car make when it's printed
        return f"{self.car_make.name} {self.name} - \
        {self.extras} - {self.color} - {self.doors} - {self.price}"
