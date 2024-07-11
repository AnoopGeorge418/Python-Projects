class UnitConvertor:
    def __init__(self):
        self.menu()
        
    def menu(self):
        print('Welcome to the Unit convertor!')
        while True:
            print("\nChoose a conversion type:")
            print("1. Temperature (Celsius to Fahrenheit)")
            print("2. Distance (Kilometers to Miles)")
            print("3. Weight (Kilograms to Pounds)")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")
            if choice == '1':
                self.convert_temperature()
            elif choice == '2':
                self.convert_distance()
            elif choice == '3':
                self.convert_weight()
            elif choice == '4':
                print('Goodbye')
                break
            else:
                print('Invalid choice. Please try again.')
                self.menu()
                
    def convert_temperature(self):
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        
    def convert_distance(self):
        kilometers = float(input("Enter distance in kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} km is equal to {miles} miles")
        
    def convert_weight(self):
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kg is equal to {pounds} lbs")
        
if __name__ == '__main__':
    UnitConvertor()