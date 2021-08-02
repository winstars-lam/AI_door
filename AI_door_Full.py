from pystubit_iot import *
from pyatcrobo2.parts import Servomotor
from pystubit.button import StuduinoBitButton
from pystubit.dsply import StuduinoBitDisplay
import time
'''
WIFI_SSID = ""
WIFI_PWD = ""
'''
url = 'https://winstarsclass09.pythonanywhere.com/send'
'''
wifi_connect(WIFI_SSID, WIFI_PWD, trytime=3)
'''
sv = Servomotor('P13')
bell = StuduinoBitButton('A')
display = StuduinoBitDisplay()
sv.set_angle(160)

while True:
    if bell.is_pressed():
        response = get_request(url)
        obj, con = response.split('_')
        con = float(con)
        print('class: ' + obj + ' confidence: ' + str(con))

        if con > 0.9 and obj != 'Others':
            display.show('o', delay=3000, wait=False, loop=False, clear=True, color=(0, 255, 0))

            sv.set_angle(20)
            time.sleep(3)
            sv.set_angle(160)
        else:
            display.show('x', delay=3000, wait=False, loop=False, clear=True, color=(255, 0, 0))
