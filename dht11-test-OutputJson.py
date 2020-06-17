#
#
# Use Raspberry Pi to get temperature/humidity from DHT11 sensor
#
# Version 1.0.0 ¦Â1 modified="20200617" comment="JsonOUTPUT"
#
# 

import json 
import time
import dht11
from datetime import datetime
import RPi.GPIO as GPIO

#define GPIO 14 as DHT11 data pin
Temp_sensor=14
def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  # Initialise display
#  lcd_init()
  instance = dht11.DHT11(pin = Temp_sensor)
# Json
  f = open("output.json", "w")

  while True:
    #get DHT11 sensor value
    result = instance.read()
    if result.temperature != 0:
        #print"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%"
        print("Last valid input:",datetime.now().strftime("%Y/%m/%d %H:%M:%S"),"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%") 
        
        dict_sample = {'devID':"rasp001",'time':datetime.now().strftime("%Y%m%d %H:%M:%S"),'temp':result.temperature,'humi':result.humidity,'validData':6} 
        json.dump(dict_sample, f, ensure_ascii=False, indent=4, sort_key=True, separatores=(',', ': '))
        
        time.sleep(1)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
#  finally:
#    lcd_byte(0x01, LCD_CMD)

