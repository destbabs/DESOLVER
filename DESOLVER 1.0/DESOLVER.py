import kivymd
import math
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout, MDAdaptiveWidget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRoundFlatButton,MDRectangleFlatButton
from kivymd.uix.list import MDList
from kivy.properties import ObjectProperty
from kivymd.uix.toolbar import MDTopAppBar, MDBottomAppBar
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivy.uix.screenmanager import ScreenManager, Screen  

Window.size = (300, 500)




class SimultaneousEqn(Screen):
    def reset(self):
        self.ent1.text = ""
        self.ent2.text = ""
        self.ent3.text = ""
        self.ent4.text = ""
        self.ent5.text = ""
        self.ent6.text = ""

    def eqn2(self):
        a = int(self.ent1.text)
        b = int(self.ent2.text)
        c = int(self.ent3.text)
        d = int(self.ent4.text)
        e = int(self.ent5.text)
        f = int(self.ent6.text)

        A = int(a * e) - int(b * d)
        Ax = int(c * e) - int(b * f)
        AY = int(a * f) - int(c * d)
        X = Ax / A
        Y = AY / A
        self.value1.text = str(f"x= {X.__round__(2)}")
        self.value2.text = str(f"y = {Y.__round__(2)}")
        self.eq1.text = f"{a}x +{b}y = {c}"
        self.eq2.text = f"{d}x +{e}y = {f}"

        print('''THE ANSWER FOR x AND y IS ''')
        print(f"x = {X}")
        print(f"y = {Y}")


class QuadraticEqn(Screen):
    def reset(self):
        self.entry1.text = ""
        self.entry2.text = ""
        self.entry3.text = ""

    def eqn1(self):
        if self.entry1.text == "":
            self.root1.text = 'Error'
            self.root2.text = 'Error'
            self.reset()
        elif self.entry2.text == "":
            self.root1.text = 'Error'
            self.root2.text = 'Error'
            self.reset()
        elif self.entry1.text == "":
            self.root1.text = 'Error'
            self.root2.text = 'Error'
            self.reset()
        else:
            a = int(self.entry1.text)
            b = int(self.entry2.text)
            c = int(self.entry3.text)
            self.reset()
            first = int((b ** 2) - 4 * a * c)
            if '-' in str(first):
                print(first)
                self.root1.text = 'Error'
                self.root2.text = 'Error'
                self.reset()

            else:
                sqroot = math.sqrt(first)

                second = int(sqroot)

                x1 = (-b + second) / 2 * a
                x2 = (-b - second) / 2 * a
                self.root1.text = str(x1.__round__(2))
                self.root2.text = str(x2.__round__(2))
                self.eqn.text = f"{a}x²+{b}x+{c}=0"
                print(f"THE ROOTS ARE {x1} AND {x2}")



class WindowManager(ScreenManager):
    pass


class Main(Screen):
    pass
def load_kv():
    Builder.load_file('DESOLVER.kv')

class DESOLVERApp(MDApp):
    def build(self):
        return load_kv()


    def go_home(self):
        self.root.current = 'main'
        self.root.transition.direction = 'right'


if __name__ == "__main__":
    DESOLVERApp().run()
