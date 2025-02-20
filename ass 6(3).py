class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()
        self.conversion_factors = {
            'inches': 1,
            'feet': 1 / 12,
            'yards': 1 / 36,
            'miles': 1 / 63360,
            'kilometers': 1 / 39370.1,
            'meters': 1 / 39.3701,
            'centimeters': 1 / 2.54,
            'millimeters': 1 / 25.4
        }
    
    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if self.unit not in self.conversion_factors or target_unit not in self.conversion_factors:
            return "Invalid unit"
        base_length = self.length / self.conversion_factors[self.unit]
        return base_length * self.conversion_factors.get(target_unit, 1)
    
    def inches(self):
        return self.convert_to('inches')
    
    def feet(self):
        return self.convert_to('feet')
    
    def yards(self):
        return self.convert_to('yards')
    
    def miles(self):
        return self.convert_to('miles')
    
    def kilometers(self):
        return self.convert_to('kilometers')
    
    def meters(self):
        return self.convert_to('meters')
    
    def centimeters(self):
        return self.convert_to('centimeters')
    
    def millimeters(self):
        return self.convert_to('millimeters')

length = float(input("Enter the length: "))
unit = input("Enter the unit: ")

converter = Converter(length, unit)
print(f"{length} {unit} in feet: {converter.feet()}")
print(f"{length} {unit} in yards: {converter.yards()}")
print(f"{length} {unit} in miles: {converter.miles()}")
print(f"{length} {unit} in kilometers: {converter.kilometers()}")
print(f"{length} {unit} in meters: {converter.meters()}")
print(f"{length} {unit} in centimeters: {converter.centimeters()}")
print(f"{length} {unit} in millimeters: {converter.millimeters()}")
