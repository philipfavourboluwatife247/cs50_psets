""" 
Author - Philip Favour Boluwatife
Date - 3rd December, 2025
Pset Name - Fuel Gauge
Pset Detail - implement a program that prompts the user for a fraction, 
formatted as X/Y, wherein each of X and Y is a positive integer, and then 
outputs, as a percentage rounded to the nearest integer, how much fuel is in 
the tank. If, though, 1% or less remains, output E instead to indicate that 
the tank is essentially empty. And if 99% or more remains, output F instead 
to indicate that the tank is essentially full. If, though, X or Y is not an 
integer, X is greater than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like 
ValueError or ZeroDivisionError.
"""

def main():
    print(calculate_fuelgauge())

def calculate_fuelgauge():
    while True:
        fraction = input("Fraction: ")
        try:
            numerator, denominator = map(int, fraction.strip().split("/"))
            if numerator < 0 or denominator <= 0:
                print("Invalid input. Numerator and Denominator should be positive integers.")
            elif numerator > denominator:
                print("Invalid input. Numerator should be less than or equal to Denominator.")
            else:
                fuel_gauge = int(round(numerator / denominator * 100))
                if fuel_gauge <= 1:
                    return "E"
                elif fuel_gauge >= 99:
                    return "F"
                else:
                    return f"{fuel_gauge}%"
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction (e.g. 1/2).")

if __name__ == "__main__":
    main()
