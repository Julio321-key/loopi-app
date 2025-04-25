from kivy.core.window import Window
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle

# Konfigurasi awal window
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'resizable', '0')
Window.fullscreen = 'auto'
Window.borderless = True

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.default_color = (0.83, 0.16, 0.49, 1)  # Pink pekat
        self.pressed_color = (0.65, 0.12, 0.4, 1)   # Warna lebih gelap saat ditekan

        with self.canvas.before:
            self.color_instruction = Color(*self.default_color)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[20]
            )

        self.bind(pos=self.update_rect, size=self.update_rect)
        self.bind(on_press=self.on_press_effect)
        self.bind(on_release=self.on_release_effect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_press_effect(self, *args):
        self.color_instruction.rgba = self.pressed_color

    def on_release_effect(self, *args):
        self.color_instruction.rgba = self.default_color

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # FloatLayout agar elemen bisa diposisikan bebas
        root_layout = FloatLayout()

        # Background full window
        with root_layout.canvas.before:
            Color(0.984, 0.906, 0.937, 1)  # Sweetly Pink
            self.rect = Rectangle(size=Window.size, pos=root_layout.pos)
        Window.bind(size=lambda *args: setattr(self.rect, 'size', Window.size))

        # BoxLayout utama (untuk taskbar dll) di dalam FloatLayout
        box_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 1), pos_hint={"x": 0, "y": 0})

        # Spacer
        box_layout.add_widget(Widget())

        # Taskbar bawah
        taskbar = Widget(size_hint_y=None, height=80)
        with taskbar.canvas:
            Color(0.83, 0.16, 0.49, 1)  # Pink terang tapi pekat gelap
            taskbar.rect = Rectangle(size=taskbar.size, pos=taskbar.pos)
        taskbar.bind(size=lambda inst, val: setattr(taskbar.rect, 'size', val))
        taskbar.bind(pos=lambda inst, val: setattr(taskbar.rect, 'pos', val))

        box_layout.add_widget(taskbar)
        root_layout.add_widget(box_layout)

        # Label judul 
        title_label = Label(
            text="SELAMAT DATANG DI MESIN PEMILAH SAMPAH LOOPI",
            font_size=50,
            color=(0, 0, 0, 1),
            font_name="Font/CalSans-Regular.ttf",
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5, 'top': 0.95}
        )
        root_layout.add_widget(title_label)
        
        # Logo Loopi
        logo = Image(
            source="Image/LoopiLogo.png",
            size_hint=(None, None),
            size=(110,110),
            pos_hint={'x': 0.02, 'top': 0.98}
        )
        root_layout.add_widget(logo)
        
        #Logo WA
        logo1 = Image(
            source="Image/WAIcon.png",
            size_hint=(None, None),
            size=(60, 60),
            pos_hint={'x': 0.6, 'y': 0.01}
        )
        root_layout.add_widget(logo1)
        
        # logo playstore
        logo2 = Image(
            source="Image/playstore.png",
            size_hint=(None, None),
            size=(380, 380),
            pos_hint={'x': 0.06, 'y': 0.09}
        )
        root_layout.add_widget(logo2)
        
        # logo appstore
        logo3 = Image(
            source="Image/Appstore.png",
            size_hint=(None, None),
            size=(370, 370),
            pos_hint={'x': 0.26, 'y': 0.093}
        )
        root_layout.add_widget(logo3)
        
        # teks WA
        label_WA = Label(
            text="WA CUSTOMER SERVICE   +62 812 3456 7890",
            font_size=30,
            color=(0, 0, 0, 1),
            font_name="Font/Nunito-SemiBold.ttf",
            size_hint=(None, None),
            pos_hint={'x': 0.785, 'y': -0.01}
        )
        root_layout.add_widget(label_WA)
        
        # teks 1
        label_teks = Label(
            text="Syarat dan Ketentuan Penukaran Botol",
            font_size=45,
            color=(0, 0, 0, 1),
            font_name="Font/CalSans-Regular.ttf",
            size_hint=(None, None),
            pos_hint={'x': 0.24, 'y': 0.68}
        )
        root_layout.add_widget(label_teks)
        
        #teks 2
        label_teks1 = Label(
            text="1. Pastikan Anda sudah download & install aplikasi Loopi",
            font_size=35,
            color=(0, 0, 0, 1),
            font_name="Font/Nunito-SemiBold.ttf",
            text_size=(1000, None),
            size_hint=(None, None),
            pos_hint={'x': 0.302, 'y': 0.6}
        )
        root_layout.add_widget(label_teks1)
        
        label_teks2 = Label(
            text="2. Kami menerima 4 jenis sampah botol (plastik, kaca, kaleng, dan susu kotak (kertas))",
            font_size=35,
            color=(0, 0, 0, 1),
            font_name="Font/Nunito-SemiBold.ttf",
            text_size=(1000, None),
            size_hint=(None, None),
            pos_hint={'x': 0.302, 'y': 0.52}
        )
        root_layout.add_widget(label_teks2)
        
        label_teks3 = Label(
            text="3. Pastikan botol dalam keadaan kering (tidak ada air)",
            font_size=35,
            color=(0, 0, 0, 1),
            font_name="Font/Nunito-SemiBold.ttf",
            size_hint=(None, None),
            text_size=(1000, None),
            pos_hint={'x': 0.302, 'y': 0.44}
        )
        root_layout.add_widget(label_teks3)
        
        label_teks4 = Label(
            text="4. Setiap jenis botol memiliki nilai point yang berbeda",
            font_size=35,
            color=(0, 0, 0, 1),
            font_name="Font/Nunito-SemiBold.ttf",
            size_hint=(None, None),
            text_size=(1000, None),
            pos_hint={'x': 0.302, 'y': 0.38}
        )
        root_layout.add_widget(label_teks4)
        
        self.add_widget(root_layout)
        
        #Tombol MULAI
        self.start_button = RoundedButton(
            text='MULAI',
            font_name='Font/Nunito-SemiBold.ttf',
            font_size='24sp',
            size_hint=(0.35, 0.09),
            pos_hint={'right': 0.97, 'y': 0.12},
            color=(1, 1, 1, 1),
        )
        self.add_widget(self.start_button)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
