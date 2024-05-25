from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

colors = {
    "#ff0000": "красный",
    "#ff8800": "оранжевый",
    "#ffff00": "желтый",
    "#00ff00": "зеленый",
    "#00ffff": "голубой",
    "#0000ff": "синий",
    "#ff00ff": "фиолетовый"
}

class RainbowApp(App):
    
    def build(self):
        layout = BoxLayout(orientation='vertical')
        text_input = TextInput()
        label = Label()
        layout.add_widget(text_input)
        layout.add_widget(label)
        for color_code, color_name in colors.items():
            button = Button(text=color_name)
            button.background_color = color_code
            button.bind(on_press=lambda instance, color_code=color_code, color_name=color_name: self.on_button_press(color_code, color_name, text_input, label))
            layout.add_widget(button)
        
        
        
        return layout

    def on_button_press(self, color_code, color_name, text_input, label):
        text_input.text = color_code
        label.text = color_name

if __name__ == '__main__':
    RainbowApp().run()
