import sys 
import threading
import time 
from kivy.app import App
from kivy.core.window import Window  
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

class Operacion(App):
    # ----  funciones de app ----
    def salir(self):
        self.stop()
        pass

    def antiacercade(self):
        self.info.text = ''
        pass

    def acercade(self):
        self.info.text = 'Desarrollado por el equipo:\nLucas alberto, Alondra Jaimes, Jorge Luis, \nJudit Selenia, Mario de jesus y Marco Valle. \nDerechos Reservados (c) 2019.'
        pass

    def limp(self):
        self.num1.text = '0'
        self.num2.text = '0'
        self.resultaditos.text = ""
        pass

    def validar(self, para):
        self.ac = para
        self.al = str(self.num1.text)
        self.al2 = str(self.num2.text)

        if self.al is "" and self.al2 is "" or self.al != "" and self.al2 is "" or self.al is "" and self.al2 != "":
            self.resultaditos.text = "Oye joven no se aceptan campos vacios"
        else:
            self.operciones(self.ac)
        pass
    
    # ---- funciones de procesamiento de datos de entrada ----
    def operciones(self, accion):
        try:
            self.accion2 = accion
            self.n1 = float(self.num1.text)
            self.n2 = float(self.num2.text)
            # --- if ---
            if "Suma" is self.accion2:
                self.resul(str(self.n1 + self.n2), self.accion2)
            elif "Resta" is self.accion2:
                self.resul(str(self.n1 - self.n2), self.accion2)
            elif "Multiplicacion" is self.accion2:
                self.resul(str(self.n1 * self.n2), self.accion2)
            elif "Division" is self.accion2: 
                if self.n1 == 0 and self.n2 == 0 or self.n1 > 0 and self.n2 == 0:
                    self.resultaditos.text = "Oye joven no se puede dividir entre cero"
                else:
                    self.resul(str(self.n1 / self.n2), self.accion2)
            elif "Factorial" is self.accion2:
                y = int(self.n1)
                yy = int(self.n2)
                l = 1
                ll = 1
                for i in range(1, y + 1):
                    l = l * i
                
                for i in range(1, yy + 1):
                    ll = l * i
                
                self.resultaditos.text = ('El factorial de ' + str(self.n1) + ': '+ str(l) + '\nEl factorial de ' + str(self.n2) + ': '+ str(ll))
            else:
                self.resultaditos.text = "Error que paso amiguito"
            pass
        except:
            self.resultaditos.text = 'Error grave, espere futuras actualizaciones.' 
            pass 

    def resul(self, rn1, letras):
        self.tipo = letras
        self.N = rn1
        self.resultaditos.text = self.tipo + ": " + self.N
        pass

    def build(self):
        # -- Estructura de la pagina principal -- 
        Window.clearcolor = (219, 219,219 ,1) 
        self.p1 = GridLayout(rows = 50, spacing = 10, size_hint_y = 1) 
        self.p1.bind(minimum_height = self.p1.setter('height'), minimum_width = self.p1.setter('width'))
        
        # -- Menu princial --
        Color = [0, 4, 5, 1] 
        self.menu1 = MenuBar.ActionBar(pos_hint = {'top': 0}, background_color = Color) 
        self.previos = MenuBar.ActionPrevious(title = '', with_previous = False) 
        self.menu2 = MenuBar.ActionView()

        # --- Acciones de menu ---
        self.li1 = MenuBar.ActionButton(text = "Acerca de", size_hint_y = None, height = 120, on_release = lambda b1:self.acercade())
        self.li4 = MenuBar.ActionButton(text = "Ocultar", size_hint_y = None, height = 120, on_release = lambda b1:self.antiacercade())
        self.li2 = MenuBar.ActionButton(text = "Limpiar", size_hint_y = None, height = 120, on_release = lambda b1:self.limp())
        self.li3 = MenuBar.ActionButton(text = "Salir", size_hint_y = None, height = 120, on_release = lambda b1:self.salir())

        # --- Se activan para la visualizacion en la pantalla ---
            # -- Accciones de menu --
        self.menu2.add_widget(self.li2)
        self.menu2.add_widget(self.li1)
        self.menu2.add_widget(self.li4)
        self.menu2.add_widget(self.li3)
        self.menu2.add_widget(self.previos) 
        self.menu1.add_widget(self.menu2) 
        self.p1.add_widget(self.menu1) 
        
        # --- Elementos en pantalla ---
        colorl = [0,0,0,1]
        Colo = [1,0,0,1]
        self.label1 = Label(text = ' Nota: Puede realizar las siguientes operaciones: \nSuma, Multiplicacion, Resta, Division y Factorial ', size_hint_y= None, height= 180, color = colorl)
        self.p1.add_widget(self.label1)  
            # --- cuadros de textos ---
        # -- Cuadro 1 --
        self.p1.add_widget(Label(text = 'Ingrese el primer numero:', color = colorl, size_hint_y = None, height = 80))
        self.num1 = TextInput (text = '0', multiline = False, size_hint_y = None, height = 80, input_filter = "float") 
        self.p1.add_widget(self.num1)
        # -- Cuadro 2 --
        self.p1.add_widget(Label(text = 'Ingrese el segundo numero:', color = colorl, size_hint_y = None, height = 80))
        self.num2 = TextInput (text = '0', multiline = False, size_hint_y = None, height = 80, input_filter = "float") 
        self.p1.add_widget(self.num2) 
        self. resultaditos = Label(text = '', size_hint_y = None, height = 80, color = Colo)
        self.p1.add_widget(self.resultaditos) 
         # --- Bottones ---
        self.S = Button(text='Sumar', size_hint_y = None, height = 135, on_release = lambda b1:self.validar("Suma")) 
        self.p1.add_widget(self.S) 
        self.R = Button(text='Restar', size_hint_y = None, height = 135, on_release = lambda b1:self.validar("Resta")) 
        self.p1.add_widget(self.R) 
        self.M = Button(text='Multiplicar', size_hint_y = None, height = 135, on_release = lambda b1:self.validar("Multiplicacion")) 
        self.p1.add_widget(self.M) 
        self.D = Button(text='Division', size_hint_y = None, height = 135, on_release = lambda b1:self.validar("Division")) 
        self.p1.add_widget(self.D)
        self.F = Button(text='Factorial', size_hint_y = None, height = 135, on_release = lambda b1:self.validar("Factorial")) 
        self.p1.add_widget(self.F) 
        # -- info extra --
        self.info = Label(text = '', size_hint_y = None, height = 250, color = Colo)
        self.p1.add_widget(self.info) 
        self.p1.add_widget(Image(source = 'logo1.png', size_hint_y = None, height = 500))
        # -- retornamos la pantalla principal
        return self.p1

if __name__ == '__main__':
    Operacion().run()