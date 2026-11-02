
# Crop Recommendation System
# Without using external libraries

print("===================================")
print("     CROP RECOMMENDATION SYSTEM")
print("===================================")

try:
    # Get input from the user
    N = float(input("Enter Nitrogen: "))
    P = float(input("Enter Phosphorus: "))
    K = float(input("Enter Potassium: "))
    T = float(input("Enter Temperature: "))
    H = float(input("Enter Humidity: "))
    ph = float(input("Enter soil pH: "))
    R = float(input("Enter Rainfall: "))

    # Crop recommendation logic
    if N >= 80 and P >= 40 and K >= 40 and R >= 150:
        crop = "Rice"

    elif N >= 50 and P >= 45 and T >= 24 and R >= 90:
        crop = "Wheat"

    elif N <= 35 and P <= 35 and K <= 35 and R <= 90:
        crop = "Groundnut"

    elif T >= 25 and H >= 55 and ph >= 6.0:
        crop = "Millet"

    elif N >= 35 and K >= 35 and R >= 100:
        crop = "Maize"

    else:
        crop = "Millet"

    # Display the result
    print("\n-----------------------------------")
    print("Recommended Crop:", crop)
    print("-----------------------------------")

except ValueError:
    print("Invalid input! Please enter numeric values.")