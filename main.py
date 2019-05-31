import sys
import threading
import time
from kyvy.app import app
from kyvy.core.windows import Window
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.widget import Widget
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image 
from kivy.factory import Factory as MenuBar
from kivy.base import runTouchApp 
from kivy.graphics import Color, Ellipse, Line, Rectangle 

class Oper(App):
    """
        |----- Opciones de menu -----
            |---> Sumar
            |---> Restar
            |---> Multiplicar
            |---> Dividir
            |---> Factorial
            |---> Limpiar
            |---> Salir
    """
    # ----  funciones de app ----

    def salir(self):
        self.stop()
        pass

    def infor(self):
        self.inf.text = '''Desarrollado por el Equipo: \nLucas Alberto, Alondra Jaimes, Judith Selenia, Jorge Luis (RALJ).
            \n todos los derechos reservados (c) 2019.'''
        pass
    
    def limp(self):
        self.num1.text = '0'
        self.num2.text = '0'
        pass
    
    # ---- funciones de procesamiento de datos de entrada ----

    def suma(self):
        try:
            self.da1 = float(self.num1.text)
            self.da2 = float(self.num2.text)

            self.inf.text = ("La Suma es: " + str(self.da1 + self.da2) + "")
        except:
            self.inf.text = "Rayoosss!! Un error con la suma ni modo :v, Espere futuras actualizaciones."