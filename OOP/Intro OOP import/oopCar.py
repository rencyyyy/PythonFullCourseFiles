class Car:
    def __init__(self,Model,Year,Color,For_sale):
        self.Model = Model
        self.Year = Year
        self.Color = Color
        self.For_sale = For_sale

    def drive(self):
        print(f"The {self.Model} is moving")

    def stop(self):
        print(f"The {self.Model} is not moving")