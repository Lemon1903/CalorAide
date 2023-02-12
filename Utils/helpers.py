"""helper functions"""

from datetime import date
from datetime import timedelta

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


def get_date_today():
    """Get the date today in custom format."""
    today = date.today()
    return today.strftime("%d-%m-%Y")

def get_date_yesterday():
    """ Get the date yesterday """
    yesterday = date.today() - timedelta(days = 1)
    return yesterday.strftime("%d-%m-%Y")
