from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class BMIApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=30, spacing=15)

        self.weight = TextInput(hint_text="Weight in kg", input_filter="float",
                                multiline=False, font_size=30)
        self.height = TextInput(hint_text="Height in cm", input_filter="float",
                                multiline=False, font_size=30)
        btn = Button(text="Calculate", font_size=30)
        btn.bind(on_press=self.calculate)
        self.result = Label(text="", font_size=30, halign="center")

        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(btn)
        layout.add_widget(self.result)
        return layout

    def calculate(self, instance):
        try:
            weight = float(self.weight.text)
            height = float(self.height.text)
            bmi = weight / (height / 100) ** 2
        except (ValueError, ZeroDivisionError):
            self.result.text = "Please enter valid numbers"
            return

        if bmi < 18.5:
            category = "Under Weight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Over Weight"
        else:
            category = "Obese"

        self.result.text = f"Your BMI is: {bmi:.1f}\n{category}"


BMIApp().run()
