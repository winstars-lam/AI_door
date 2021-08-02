from pyatcrobo2.parts import Servomotor
import time

sv = Servomotor('P13')
sv.set_angle(160)


sv.set_angle(20)
time.sleep(3)
sv.set_angle(160)

