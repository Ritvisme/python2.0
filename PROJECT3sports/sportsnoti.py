import sports 
import time 
from plyer import notification
matches=sports.get_sport(sports.CRICKET)
notification.notify(title='CRICKET SCORE',message='live',timeout='4')
time.sleep(2)