"""Validator module for checking textfield value."""

from kivymd.uix.textfield import MDTextField


class Validator:
    """Validator class that checks text in textfield according to the validator type."""

    @staticmethod
    def check_text(instance_text_field: MDTextField, text: str):
        """Called when text is entered into a text field.

        Args:
            instance_text_field (MDTextField): the textfield to be checked.
            text (str): the text inputted to the textfield.
        """
        instance_text_field.error = False
        if not text:
            instance_text_field.error = True
            instance_text_field.helper_text = "This field is required"
        else:
            if (
                instance_text_field.validator_type == "numeric"
                and not Validator._is_valid_numeric(text)
            ):
                instance_text_field.error = True
                instance_text_field.helper_text = (
                    f"Enter a valid value for {instance_text_field.hint_text.lower()}"
                )

    @staticmethod
    def _is_valid_numeric(text: str):
        try:
            float(text)
            return True
        except ValueError:
            return False
