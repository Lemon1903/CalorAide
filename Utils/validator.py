"""Validator module for checking textfield value."""

import re


class Validator:
    """Validator class that checks text in textfield according to the validator type."""

    @staticmethod
    def check_text(textfield, text):
        """Called when text is entered into a text field.

        Args:
            textfield (MDTextField): the textfield to be checked.
            text (str): the text inputted to the textfield.
        """
        textfield.error = False
        textfield.bind(error=Validator._on_error)

        if Validator._get_has_error(textfield.validator_type, text):
            textfield.error = True

    @staticmethod
    def _on_error(textfield, has_error):
        # set helper text to the set error message of the textfield
        if has_error:
            if textfield.error_message and textfield.text:
                textfield.helper_text = textfield.error_message
            else:
                textfield.helper_text = "This field is required"

    @staticmethod
    def _get_has_error(validator_type: str, text: str):
        if validator_type:
            return not {
                "name": Validator._is_valid_name,
                "numeric": Validator._is_valid_numeric,
            }[validator_type](text)
        return not text

    @staticmethod
    def _is_valid_name(text: str):
        return re.match(r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$", text)

    @staticmethod
    def _is_valid_numeric(text: str):
        try:
            float(text)
            return True
        except ValueError:
            return False
