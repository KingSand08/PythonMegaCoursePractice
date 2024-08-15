# Mobile apps MUST have main.py as main file or there will be errors
# You also could create all logic in your python file, even for desing, but it is not good
    # practice. Instead it is better to program design in a (.kv) file instead. This is
    # Written in the Kviy language
from kivy.app import App
from kivy.lang import Builder # This will be the connector of the python file to the kv file
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv') # Link the design.kv file

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen" # self = current instance of this class or
                # class where self is instance of this class. self.manager = inheriting
                # from Screen class parent to instance. current = attribute of manager 
                # function. This current attriubte will be passed screen you want to go to.

class SignUpScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

# Hierarchy of kivy apps, App -> ScreenManager(RootWidget) -> Screen (ex: login screen) 
class MainApp(App):
    def build(self): # Is overwriting the build function in App, which derives from kivy.app
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run() # run() is also a mathod of app