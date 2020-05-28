# _____ _____ _____ __ __ _____ _____ 
#|     |   __|     |  |  |     |     |
#|  |  |__   |  |  |_   _|  |  |  |  |
#|_____|_____|_____| |_| |_____|_____|
#
# Use Raspberry Pi to get temperature/humidity from DHT11 sensor.
# Send to Google Spread sheet.
#
import time
import dht11
from datetime import datetime
import RPi.GPIO as GPIO

# GSP 
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#define GPIO 14 as DHT11 data pin
Temp_sensor=14
def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  # Initialise display
  # lcd_init()
  instance = dht11.DHT11(pin = Temp_sensor)

  # Google Spread Sheet Access Init. ->
  scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

  credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread-sample-278514-701e33c6159b.json', scope)
  gc = gspread.authorize(credentials)
  wks = gc.open('gspreadsample').sheet1
  #  -> Google Spread Sheet Access Init. 
 
  # Registration data line
  ln=2
  
  while True:
    #get DHT11 sensor value
    result = instance.read()
#    if result.temperature != 0:
#       #print"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%"
#        print("Last valid input:",datetime.now().strftime("%Y/%m/%d %H:%M:%S"),"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%")
#        time.sleep(60)

    # Register value in Google Spread sheet
    #print("Last valid input:",datetime.now().strftime("%Y/%m/%d %H:%M:%S"),"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%")
    wks.update_cell(ln, 1, datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print(wks.cell(ln, 1))
    wks.update_cell(ln, 2, result.temperature)
    print(wks.cell(ln, 2))
    wks.update_cell(ln, 3, result.humidity)
    print(wks.cell(ln, 3))
    time.sleep(10)

    # Maximum registration data
    if ln > 100:
      ln=2
    ln+=1


if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
#  finally:
#    lcd_byte(0x01, LCD_CMD)

