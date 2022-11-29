#!/usr/bin/env python3

# Height in M
height = -1.75
# Weight in KG
weight = 80

bmi_category = ""


# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.


def get_bmi_category():
    # You need to change the following part of the function
    # to determine the BMI and return the correct category.

    bmi = weight / (height**2)
    bmi = round(bmi, 2)

    if height < 0 or weight < 0:
        return "N/A"

    if 0 <= bmi <= 18.5:
        bmi_category = "Underweight"
    elif 18.5 < bmi <= 25:
        bmi_category = "Normal weight"
    elif 25 < bmi <= 30:
        bmi_category = "Pre-obesity"
    elif 30 < bmi <= 35:
        bmi_category = "Obesity class I"
    elif 35 < bmi <= 40:
        bmi_category = "Obesity class II"
    elif 40 < bmi:
        bmi_category = "Obesity class III"

    # Return the BMI values and the correct category after you have calculated the BMI.
    return f"BMI: {bmi}, Category: {bmi_category}"

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())
