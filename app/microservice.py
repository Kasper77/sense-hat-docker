#!/usr/bin/env python

import time
from datetime import datetime
from sense_hat import SenseHat
sense = SenseHat()

sensor_file = open("sensors_data.txt", "w")

while True:

  # Take readings from all three sensors
  th = sense.get_temperature()
  tp = sense.get_temperature_from_pressure()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  th = round(th, 1)
  tp = round(tp, 1)
  p = round(p, 1)
  h = round(h, 1)

  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = str(datetime.now()) + ": "
  message += "TH (Celsius): " + str(th) + " - TP (Celsius): " + str(tp) + " - Pres (Millibars): " + str(p) + " - Hum (percentage): " + str(h)

  print message

  sensor_file.write(message + '\n')

  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.03)

