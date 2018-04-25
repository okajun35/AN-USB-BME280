#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.listview import ListItemButton
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.clock import Clock

from PyMCP2221A import BME280
#import time
device = BME280.BME280()
# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#resource_add_path('/storage/emulated/0/kivy/calc/fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する



class bme280App(App):
    temp  = StringProperty()
    hum  = StringProperty()
    preessure  = StringProperty()

    def __init__(self, **kwargs):
        super(bme280App, self).__init__(**kwargs)
        device.readData()
        print ("temp : %-6.2f ℃" % (device.temperature) )
        print ("hum : %6.2f ％" % (device.var_h) )
        print ("pressure : %7.2f hPa" % (device.pressure/100))


        self.title = 'temp'

        self.temp = str('%-6.2f' % device.temperature) + " °C"
        self.hum  = str('%6.2f' % device.temperature) +  "%"
        self.preessure = str('%7.2f' % (device.temperature/100)) + " hpa"

        Clock.schedule_interval(self.calc_temp, 1.0)
    pass

    def calc_temp(self, dt):
        ''' 温度を再計算 '''
        device.readData()
        print ("temp : %-6.2f ℃" % (device.temperature) )
        print ("hum : %6.2f ％" % (device.var_h) )
        print ("pressure : %7.2f hPa" % (device.pressure/100))


        self.temp = str('%-6.2f' % device.temperature) + " °C"
        self.hum  = str('%6.2f' % device.var_h) +  "%"
        self.preessure = str('%7.2f' % (device.pressure/100)) + " hpa"

if __name__ == '__main__':
	bme280App().run()