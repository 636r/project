# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

from seconds import Seconds

age = 7
name = " "
p1,p2,p3 = 0,0,0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False
    
    
class page1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        instr = Label(text=txt_instruction, halign='left', valign='middle')
        lb1 = Label(text = "Ім'я:")
        self.in_name=TextInput(multiline = False)
        
        
        lb2= Label(text = "Вік:")
        self.in_age=TextInput(multiline = False)
        
        self.btn = Button(text = "Почати", size_hint = (0.8,0.5),pos_hint = {'center_x': 0.5})
        
        self.btn.on_press = self.next
        
        line1 = BoxLayout(size_hint = (0.9,None))
        line2 = BoxLayout(size_hint = (0.9,None))
        
        line1.add_widget(lb1)
        line1.add_widget(self.in_name)
        
        line2.add_widget(lb2)
        line2.add_widget(self.in_age)
        
        main_l1 = BoxLayout(orientation ="vertical",padding=8,spacing= 8, )
        main_l1.add_widget(instr)
        main_l1.add_widget(line1)
        main_l1.add_widget(line2)
        main_l1.add_widget(self.btn)
        
        self.add_widget(main_l1)

    def next(self):
        
        global name, age
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)

        else:
            self.manager.current = "page2"
                
class Page2Scr(Screen):
    def __init__(self, **kwargs ):
        super().__init__(**kwargs )
        
        self.next_screen = False

        instr = Label(text = txt_test1)
        self.lb_sec = Seconds(5)
        self.lb_sec.bind(done=self.timer_finished)

        lb_result = Label(text = "Результат:",halign='right')
        self.in_result = TextInput(text = "0", multiline= False, padding = 0)
        line = BoxLayout( size_hint=(0.8, 0.2), )
        line.add_widget(lb_result)
        line.add_widget(self.in_result)
        self.in_result.set_disabled(True)

        self.btn = Button(text="Почати", size_hint = (0.3,0.5), pos_hint = {"center_x" : 0.5} )
        self.btn.on_press = self.next
        main_l2 = BoxLayout(orientation = "vertical", spacing = 13)
        main_l2.add_widget(instr)
        main_l2.add_widget(self.lb_sec)
        main_l2.add_widget(line)
        main_l2.add_widget(self.btn)
        
        
        self.add_widget(main_l2)
        
    def timer_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'


    def next(self):
        if not self.next_screen:
           self.btn.set_disabled(True)
           self.lb_sec.start()
        else:
           global p1
           p1 = check_int(self.in_result.text)
           if p1 == False or p1 <= 0:
               p1 = 0
               self.in_result.text = str(p1)
           else:
               self.manager.current = 'page3'
               
               
class Page3Scr(Screen):
    def __init__(self, **kwargs ):
        super().__init__(**kwargs )
        self.lb_sec = Seconds(4)
        self.lb_sec.bind(done=self.timer_finished)
        self.next_screen = False

        lb_sit = Label(text =txt_sits)
        self.btn = Button(text = "Почати" , size_hint = (0.5,0.3), pos_hint = {"center_x": 0.5 })
        self.btn.on_press = self.next
        
        main_line = BoxLayout(orientation="vertical")
        main_line.add_widget(lb_sit)
        main_line.add_widget(self.lb_sec)

        main_line.add_widget(self.btn)

        self.add_widget(main_line)
    def timer_finished(self, *args):
        self.next_screen = True
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'

 
    def next(self):
        if not self.next_screen:
            self.btn.disabled = True
            self.lb_sec.start()
        else:
            self.manager.current = 'page4'
        
class Page4Scr(Screen):
    def __init__(self, **kwargs ):
        super().__init__(**kwargs )
        
        self.next_screen = False
        self.stage = 0
        instr = Label(text = txt_test3)
        self.lb_sec = Seconds(4)
        self.lb_sec.bind(done=self.timer_finished)
        self.lbl1 = Label(text='Рахуйте пульс')
        lb_result = Label(text = "Результат:",halign='right')
        self.in_result = TextInput(text = "0", multiline= False, padding = 0)
        line = BoxLayout( size_hint=(0.8, 0.3), )
        line.add_widget(lb_result)
        line.add_widget(self.in_result)
        
        lb_result2 = Label(text = "Результат:",halign='right')
        self.in_result2 = TextInput(text = "0", multiline= False, padding = 0)
        line2 = BoxLayout( size_hint=(0.8, 0.3), )
        line2.add_widget(lb_result2)
        line2.add_widget(self.in_result2)
        self.in_result.set_disabled(True)
        self.in_result2.set_disabled(True)

        self.btn = Button(text="Почати", size_hint = (0.3,0.5), pos_hint = {"center_x" : 0.5} )
        self.btn.on_press = self.next
        main_l2 = BoxLayout(orientation = "vertical", spacing = 10)
        main_l2.add_widget(instr)
        main_l2.add_widget(self.lbl1)
        main_l2.add_widget(self.lb_sec)
        main_l2.add_widget(line)
        main_l2.add_widget(line2)

        main_l2.add_widget(self.btn)
        
        
        self.add_widget(main_l2)
        
    def timer_finished(self, *args):
        if self.lb_sec.done == True:
            if self.stage == 0:
                # закінчили перший підрахунок, відпочиваємо
                self.stage = 1
                self.lbl1.text = 'Відпочивайте'
                self.lb_sec.restart(30)
                self.in_result.set_disabled(False)
            elif self.stage == 1:
                # закінчили відпочинок, вважаємо
                self.stage = 2
                self.lbl1.text= 'Рахуйте пульс'
                self.lb_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершити'
                self.next_screen = True



    def next(self):
        if not self.next_screen:
           self.btn.set_disabled(True)
           self.lb_sec.start()
        else:
           global p2, p3
           p2 = check_int(self.in_result.text)
           p3 = check_int(self.in_result2.text)
           if p2 == False:
               p2 = 0
               self.in_result1.text = str(p2)
           elif p3 == False:
               p3 = 0
               self.in_result2.text = str(p3)
           else:
               # переходимо
               self.manager.current = 'result'
               
class Result(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       self.instr = Label(text = '')
       self.outer.add_widget(self.instr)
 
       self.add_widget(self.outer)
       self.on_enter = self.before
  
   def before(self):
       global name
       self.instr.text = name + '\n' + test(p1, p2, p3, age)
       
class HeartCheck(App):
   def build(self):
        sm = ScreenManager()
        sm.add_widget(page1(name='page1'))
        sm.add_widget(Page2Scr(name='page2'))
        sm.add_widget(Page3Scr(name='page3'))
        sm.add_widget(Page4Scr(name='page4'))
        sm.add_widget(Result(name='result'))
        return sm
       
app = HeartCheck()
app.run()
