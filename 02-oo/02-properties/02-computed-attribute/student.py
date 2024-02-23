# Write your code here

class BMICalculator:
    def __init__(self,weight_in_kg,height_in_m):
        self.weight = weight_in_kg
        self.height = height_in_m

    @property
    def bmi(self):
        return self.weight / self.height ** 2

    @property
    def category(self):
        Bmi = self.bmi
        if Bmi < 18.5:
            return "underweight"
        elif 18.5 < Bmi < 25:
            return "normal"
        else:
            return  "overweight"

