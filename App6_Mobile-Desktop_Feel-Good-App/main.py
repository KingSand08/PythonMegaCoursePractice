# Mobile apps MUST have main.py as main file or there will be errors
# You also could create all logic in your python file, even for desing, but it is not good
    # practice. Instead it is better to program design in a (.kv) file instead. This is
    # Written in the Kviy language
from datetime import datetime 
import glob
import json
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App
from kivy.lang import Builder # This will be the connector of the python file to the kv file
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv') # Link the design.kv file

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction= 'left'
        self.manager.current = "sign_up_screen" # self = current instance of this class or
                # class where self is instance of this class. self.manager = inheriting
                # from Screen class parent to instance. current = attribute of manager 
                # function. This current attriubte will be passed screen you want to go to.
    def login(self, uname, pword):
        if(uname != "" or pword != ""):
            with open("users.json", 'r') as file:
                users = json.load(file)
            if uname in users and users[uname]['password'] == pword:
                self.manager.transition.direction= 'left'
                self.manager.current = "login_screen_success"
            else:
                self.ids.login_wrong.text = "Wrong username or password!"
        else:
            self.ids.login_wrong.text = "Cannot leave input blank!"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        if(uname != "" or pword != ""):
            with open("users.json", 'r') as file:
                users = json.load(file)
            users[uname] = {'username' : uname, 'password' : pword,
                            'created' : datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
            print(users)
            with open("users.json", 'w') as file:
                json.dump(users, file)
            self.manager.current = "sign_up_screen_success"
        else:
            self.ids.signup_wrong.text = "Cannot leave input blank!"
            
    def go_to_login(self):
        self.manager.transition.direction= 'right'
        self.manager.current = "login_screen"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"
        
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        
        if(feel in available_feelings):
            with open(f"quotes/{feel}.txt", 'r') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes) # gets list and returns random output
        else : 
            self.ids.quote.text = "Try another feeling to get output. (happy, sad, and unloved)"

# ording matters when extending as certain functions may be overwritten in the child class unkowingly
class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

# Hierarchy of kivy apps, App -> ScreenManager(RootWidget) -> Screen (ex: login screen) 
class MainApp(App):
    def build(self): # Is overwriting the build function in App, which derives from kivy.app
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run() # run() is also a mathod of app