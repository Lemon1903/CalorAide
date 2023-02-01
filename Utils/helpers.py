"""helper functions"""


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
