"""
Name: InsanityNet
Last Date Edited: 18-Feb-2022

Description:
    Imperial and Metric conversion.
    Feet and Inches to Meters OR Meters to Feet and Inches

Requirements:
    fractions.Fraction function built into Python3

Known Issues:
    1. Negative Feet and Positive Inches. I can't be bothered to fix it at 11 PM.
"""

# Necessary imports for this script to function.
from fractions import Fraction as Fracs


# Imperial to Metric Conversion
def imperial(x):
    """
    This function will convert Imperial Feet (and Inches) to Metric Meters (or Centimeters if less than 1 whole Meter

    :return: Converted value from Imperial to Metric
    """

    # FEET SECTION
    # Take the feet from Array and set to variable frac_ft
    frac_ft = float(x[0])

    # Convert from Feet to Meters
    result_1 = frac_ft * 0.3048

    # Format the resulting converted float to have 4 decimal places
    result_1 = float("{:.4f}".format(result_1))

    # INCHES SECTION

    # INCH TO METERS
    # Connvert the inch (and fraction inch) to decimal inch
    frac = float(sum(Fracs(s) for s in x[1].split()))

    # Calculate Inch section of results
    result_2 = frac / 39.37

    # RESULTS
    # Calculate the results
    result = result_1 + result_2

    # Format to 4 decimal places
    result = float("{:.4f}".format(result))

    # RETURN SECTION
    # Return the converted result to be displayed
    return result


# Metric to Imperial Conversion
def metric(x):
    """
    This function will convert Metric meters to Imperial Feet (and Inches).

    :return: Converted value from Metric to Imperial
    """

    # Initial conversion
    # Meters to Feet
    meters_in_ft = float("{:.4f}".format(x * 3.280839895))

    # Inches portion of conversion
    meters_in_in = meters_in_ft % 1 * 12

    # For the weird rounding issues where it assumes .999 is 12 inches (1ft) just convert it over to prevent
    # 5 ft 12 inch issues
    if meters_in_in >= 11.992:
        meters_in_ft = meters_in_ft + 1
        meters_in_in = meters_in_in - 11.992

    # LIMIT/FORMAT OUTPUTS
    # Limit Feet to 0 decimal places
    meters_in_ft = int(meters_in_ft)
    # Limit Inches to 2 decimal places
    meters_in_in = float("{:.2f}".format(meters_in_in))

    # Return the
    return meters_in_ft, meters_in_in


# Main function
def main():
    # Initialize variables
    system_value = bool()  # 0 for Metric start, 1 for Imperial start.
    initial = str()  # The initial value to convert FROM.
    sysloop = True  # Internal loop 1 initial starting value [Unit of measure validation loop]

    # User input and Validation
    while sysloop is True:
        try:
            # Get the system [Metric or Imperial] that the initial value will be in
            system = str(input(f"What system of measure are you converting from?\n"
                               f"[M]etric or [I]mperial?\n"
                               f">>> "))

            # If metric start, set system_value to 0
            if system.lower() == "m" or system.lower() == "metric":
                system_value = bool(0)
                break

            # If imperial start, set system_value to 1
            elif system.lower() == "i" or system.lower() == "imperial":
                system_value = bool(1)
                break

            # If not either of them, invalid, indicate, repeat input request.
            else:
                print(f"Invalid input, please select M for Metric or I for Imperial.")
                continue
        except ValueError:
            continue

    # ---------- IMPERIAL SECTION ----------

    # Send initial value to imperial function to convert to metric
    if system_value == 1:

        # Loop data validation, initial imperial input
        while True:

            initial = []

            # Initial validation and conversion from str fraction to decimal notation
            # using the fractions.Fraction imported function
            try:
                # Initial input of value to convert from
                x = str(input(f"\n"
                              f"How many Feet would you like to convert?\n"
                              f">>> "))
                
                y = str(input(f"\n"
                              f"How many inches would you like to convert?\n"
                              f">>> "))

                # Add to array
                initial.append(x)
                initial.append(y)

                # Break the loop
                break

            # IF Value error THEN print message and CONTINUE
            except ValueError:

                # Print error
                print("There was an error in your input. Please ensure it is in the proper notation.")

                # Clear array to retry
                initial.clear()

                # Continue loop (Retry)
                continue

        # Call imperial function and store the returned value in result variable.
        result = imperial(initial)

        # IF result is a whole number THEN print in Meters ELSE print in Centimeters

        # PLURAL VS SINGULAR CHECKS AND PRINTING
        # IF GREATER THAN 1
        if abs(float(result)) > 1:
            print(f"\n"
                  f"Your converted value is: {result} Meters")

        # OR IF EQUALS 1
        elif abs(float(result)) == 1:
            print(f"\n"
                  f"You converted value is: {result} Meter")

        # OR IF LESS THAN 1, CONVERT TO CENTIMETERS
        else:
            # Convert Decimal meters below 1 meter to centimeters
            result = result * 100

            # IF GREATER THAN 1
            if abs(result) > 1:
                print(f"\n"
                      f"Your converted value is: {result} Centimeters")

            # OR IF EQUALS 1
            if abs(result) == 1:
                print(f"\n"
                      f"Your converted value is: {result} Centimeter")

            # OR IF LESS THAN 1
            elif abs(result) < 1:
                print(f"\n"
                      f"Your converted value is: {result} Centimeters")

    # ---------- METRIC SECTION ----------

    # Send initial value to metric function to convert to imperial
    elif system_value == 0:

        # User input validation
        while True:
            try:
                initial = float(input(f"How many Meters would you like to convert?\n"
                                      f"In decimal notation please. [I.e, 1.75]\n"
                                      f">>> "))
            except ValueError:
                print("There was an error in your input. Please ensure it is in the proper notation.")
                continue
            break

        # Call metric function and store the returned value in result variable.
        result = metric(initial)

        # This section was recommended to be added by my Australian friend Kolock. F KOLOCK!
        # PLURAL VS SINGULAR CHECKS

        # IF FEET EQUALS 1
        if abs(result[0]) == 1:

            # AND IF INCHES LESS THAN 0.01
            if abs(result[1]) < 0.01:
                print(f"Your converted value is:\n"
                      f"{result[0]} Foot")

            # OR IF INCHES EQUALS 1
            elif abs(result[1]) == 1:
                print(f"Your converted value is:\n"
                      f"{result[0]} Foot {result[1]} Inch")

            # OR IF INCHES GREATER THAN 1
            elif abs(result[1]) > 1:
                print(f"Your converted value is:\n"
                      f"{result[0]} Foot {result[1]} Inches")

        # OR IF FEET EQUALS 0
        elif abs(result[0]) == 0:

            # AND IF INCHES EQUALS 1
            if abs(result[1]) == 1:
                print(f"Your converted value is:\n"
                      f"{result[1]} Inch")

            # OR IF INCHES NOT EQUALS 1
            else:
                print(f"Your converted value is:\n"
                      f"{result[1]} Inches")

        # OTHERWISE, IF FEET BETWEEN (0 AND 1) AND FEET GREATER THAN 1
        else:

            # AND IF INCHES EQUALS 1
            if abs(result[1]) == 1:
                print(f"Your converted value is:\n"
                      f"{result[0]} Feet and {result[1]} Inch")

            # OR IF INCHES LESS THAN 1 AND GREATER THAN 0
            elif 0 < abs(result[1]) < 1.01:
                print(f"Your converted value is:\n"
                      f"{result[0]} Feet {result[1]} Inches")

            # OR IF INCHES APPROXIMATELY EQUALS 0
            elif abs(result[1]) < 0.01:
                print(f"Your converted value is:\n"
                      f"{result[0]} Feet")

    # Print end of program information
    print(f"\n"
          f"Thank you for converting!")

    # Quit the program with error code 0 [Success]
    quit(0)


# If not called as library, run the specified function automatically.
if __name__ == "__main__":

    # MEME CONTROL! 'Cause it's 11 PM and I have no impulse control.
    coconut = 1

    # If coconut != NULL run the program
    if coconut != '':
        main()

    # Otherwise, find the coconut so the program can run!
    else:
        print(f"Coconut is NULL. Find the Coconut.")

# My friend Kolock can go <explitive> himself for recommending complexity be added to this program.
# If negative feet and positive inches are input, wrong answer. I do not care enough to fix it at this time
# This is essentially python 101 so this is already overcomplicated based on your teachings. -_-
# My friend Kolock also specified I needed to add this: Coconut.jpg
# The above Something about good luck. Oh well, it's 11 PM, and I am tired of programming for the day.
# My Australian friend is a bad influence on me when I do not have impulse control this late at night.
