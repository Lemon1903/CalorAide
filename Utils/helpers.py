"""helper functions"""

from datetime import date


def get_bmi_classification(height: float, weight: float):
    """Function to get the bmi classification
    Args:
        height (float): the height in meters.
        weight (weight): the weight in kilograms.
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
    bmi = weight / (height / 100) ** 2
    for bmi_classification, bmi_value in bmi_classifications.items():
        if bmi <= bmi_value:
            return bmi_classification
    return "Morbidly Obese"

def get_user_bmr(gender, weight, height, age):
    if gender == "Male":
        return (10*weight)+(6.25*height)-(5*age)+5
    return (10*weight)+(6.25*height)-(5*age)-161

def calculate_calorie_goal(base_bmr, activity, mode, goal):
    """Function to calculate the calorie goal intake based on user's preferences.
    Args:
        base_bmr: the initial bmr based on Mifflin St Jeor computation
        activity: the user's activity based on their lifestyle in String form
        mode: the user's mode of choice in String choice
        goal: the user's activities' intensity
    Returns:
        float: the value of the calorie goal itself.
    """

    bmr = 0
    activity_multipliers = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very Active": 1.9
    }
    goals_list = {
        "sedentary": 0,
        "mild": 275.577828,
        "standard": 551.155655,
        "extreme": 1102.311311,
    }

    for user_activity, scale_factor in activity_multipliers.items():
        if activity == user_activity:
            bmr = base_bmr*scale_factor

    for intensity, value in goals_list.items():
        if goal == intensity:
            if mode == "lose":
                return bmr - value
            if mode == "gain":
                return bmr + value
            return bmr

def get_date_today():
    """Get the date today in custom format."""
    today = date.today()
    return today.strftime("%d-%m-%Y")
