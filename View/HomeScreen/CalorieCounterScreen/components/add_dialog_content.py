"""This module holds the `AddDialogContent` class for the add intake dialog."""

from kivymd.uix.boxlayout import MDBoxLayout


class AddDialogContent(MDBoxLayout):
    """The content for the add intake dialog."""

    def clear_textfields(self):
        """Clear the textfields text and error."""
        for textfield in self.children:
            textfield.text = ""
            textfield.error = False
            textfield.required = False

    def make_textfields_required(self):
        """Mark all textfields as required."""
        for textfield in self.children:
            textfield.required = True
            textfield.error = not textfield.text

    def get_input(self):
        """Get all the intake input of the user."""
        return [textfield.text for textfield in self.children]

    def has_empty_field(self):
        """Check if there is no text inputted."""
        return any(not text for text in self.get_input())

    def has_no_error(self):
        """Check there are no errors in the textfields."""
        return all(not textfield.error for textfield in self.children)
