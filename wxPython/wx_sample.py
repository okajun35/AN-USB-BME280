#-*- coding: utf-8 -*-

import wx

from PyMCP2221A import BME280
device = BME280.BME280()

class Example(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title,size = (400,300)) 
             
      self.InitUI() 
      self.Centre() 
      self.Show()      
      
      self.timer = wx.Timer(self)
      self.Bind(wx.EVT_TIMER, self.OnTimer)
      self.timer.Start(500)
      
   def InitUI(self): 
	
      device.readData()
      print ("temp : %-6.2f ℃" % (device.temperature) )
      print ("hum : %6.2f ％" % (device.var_h) )
      print ("pressure : %7.2f hPa" % (device.pressure/100))


      r_temp = str('%-6.2f' % device.temperature) + " °C"
      r_hum  = str('%6.2f' % device.var_h) +  "%"
      r_preessure = str('%7.2f' % (device.pressure/100)) + " hpa"

      self.panel = wx.Panel(self) 
      
      
      gs = wx.GridSizer(rows=3, cols=2, gap=(0, 0)) 
	  
      label1 = "temp"
      label2 = "hum"
      label3 = "pressure"

      self.temp = wx.TextCtrl(self.panel, wx.ID_ANY)
      self.temp.SetValue(r_temp)

      self.hum = wx.TextCtrl(self.panel, wx.ID_ANY)
      self.hum.SetValue(r_hum)

      self.pressure = wx.TextCtrl(self.panel, wx.ID_ANY)
      self.pressure.SetValue(r_preessure)


      gs.Add(wx.StaticText(self.panel, wx.ID_ANY, label = label1, style=wx.ALIGN_CENTER))
      gs.Add(self.temp) 
      gs.Add(wx.StaticText(self.panel, wx.ID_ANY, label = label2, style=wx.ALIGN_CENTER))
      gs.Add(self.hum) 
      gs.Add(wx.StaticText(self.panel, wx.ID_ANY, label = label3, style=wx.ALIGN_CENTER)) 
      gs.Add(self.pressure)  
      
      self.panel.SetSizer(gs)

   def OnTimer(self, event):
      

      device.readData()
      print ("temp : %-6.2f ℃" % (device.temperature) )
      print ("hum : %6.2f ％" % (device.var_h) )
      print ("pressure : %7.2f hPa" % (device.pressure/100))
      r_temp = str('%-6.2f' % device.temperature) + " °C"
      r_hum  = str('%6.2f' % device.var_h) +  "%"
      r_preessure = str('%7.2f' % (device.pressure/100)) + " hpa"

      # 値を更新
      self.temp.SetValue(r_temp)
      self.hum.SetValue(r_hum)
      self.pressure.SetValue(r_preessure)


if __name__ == '__main__':
      app = wx.App() 
      Example(None, title = '温度計デモ') 
      app.MainLoop()