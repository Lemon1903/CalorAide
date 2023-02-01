import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class NoteApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.note_input = TextInput(text="Enter your note here...", multiline=True)
        layout.add_widget(self.note_input)

        self.note_output = Label(text="", font_size=20)
        layout.add_widget(self.note_output)

        self.note_input.bind(text=self.update_note_output)

        bold_button = Button(text="Bold", on_press=self.make_bold)
        layout.add_widget(bold_button)

        size_button = Button(text="Change Font Size", on_press=self.change_font_size)
        layout.add_widget(size_button)

        return layout

    def update_note_output(self, instance, value):
        self.note_output.text = value

    def make_bold(self, instance):
        self.note_output.bold = True

    def change_font_size(self, instance):
        self.note_output.font_size += 2


if __name__ == "__main__":
    NoteApp().run()
