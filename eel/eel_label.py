import eel
from PyMCP2221A import BME280
#import time
device = BME280.BME280()


eel.init('web')     # Webファイルを格納しているフォルダを設定する

@eel.expose     # この関数をJavascriptに公開する
def read_BME280():
    device.readData()
    print ("temperature : %-6.2f ℃" % (device.temperature) )
    print ("hum : %6.2f ％" % (device.var_h) )
    print ("pressure : %7.2f hPa" % (device.pressure/100))


    temp = str('%-6.2f' % device.temperature) + " °C"
    hum  = str('%6.2f' % device.var_h) +  "%"
    preessure = str('%7.2f' % (device.pressure/100)) + " hpa"
    
    eel.output_temperature(temp , hum ,preessure)   # Javascript側の関数を呼ぶ


eel.start('eel_test.html', size=(300, 200))    # 開始
