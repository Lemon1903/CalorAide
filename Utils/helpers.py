"""helper functions"""

from datetime import date, timedelta
from decimal import Decimal


def get_bmi_value(height_cm: float, weight_kg: float):
    """BMI formula that estimates a person's fat based on their height and weight.
    This function will return user's BMI value.
    """
    height_m = height_cm / 100
    return weight_kg/ (height_m**2)


def get_bmi_classification(value: float):
    """Function to get the bmi classification

    Args:
        value (float): the bmi value to be classified.

    Returns:
        str: the bmi classification base on the bmi computed.
    """
    bmi_classifications = {
        "Severely Underweight": 16,
        "Underweight": 18.5,
        "Normal": 24.9,
        "Overweight": 29.9,
        "Obese": 34.9,
        "Severely Obese": 39.9,
    }
    for bmi_classification, bmi_value in bmi_classifications.items():
        if value <= bmi_value:
            return bmi_classification
    return "Morbidly Obese"


def get_date_today():
    """Get the date today in custom format."""
    today = date.today()
    return today.strftime("%d-%m-%Y")


def get_date_yesterday():
    """Get the date yesterday."""
    yesterday = date.today() - timedelta(days=1)
    return yesterday.strftime("%d-%m-%Y")


def get_user_bmr(gender, weight, height, age):
    """This formula is based on Mifflin-St. Jeor Equation.
    This returns the value of the Basal Metabolic Rate of a person.
    That is the amount of calories they naturally burn with bodily functions.
    """
    value = 5 if gender == "Male" else -161
    return (10 * weight) + (6.25 * height) - (5 * age) + value


def calculate_calorie_goal(base_bmr, activity, mode, goal):
    """Function to calculate the calorie goal intake based on user's preferences.

    Args:
        base_bmr (float): the initial bmr based on Mifflin St Jeor computation
        activity (str): the user's activity based on their lifestyle in String form
        mode (str): the user's mode of choice in String choice
        goal (str): the user's activities' intensity

    Returns:
        float: the value of the calorie goal itself.
    """
    activity_multipliers = {
        "Sedentary": Decimal("1.2"),
        "Light": Decimal("1.375"),
        "Moderate": Decimal("1.55"),
        "Active": Decimal("1.725"),
        "Very Active": Decimal("1.9")
    }
    goals_list = {
        "Sedentary": 0,
        "Mild": Decimal("275.577828"),
        "Standard": Decimal("551.155655"),
        "Extreme": Decimal("1102.311311"),
    }

    calorie_goal = Decimal(str(base_bmr)) * activity_multipliers[activity]
    if mode == "Lose":
        return round(calorie_goal - goals_list[goal], 1)
    if mode == "Gain":
        return round(calorie_goal + goals_list[goal], 1)
    return round(calorie_goal, 1)
