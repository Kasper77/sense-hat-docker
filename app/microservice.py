#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  tp = sense.get_temperature_from_pressure()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  tp = round(tp, 1)
  p = round(p, 1)
  h = round(h, 1)

  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "T (from Humidity,Celsius): " + str(t) + " - T (from Pressure, Celsius): " + str(tp) + " - Pres (Millibars): " + str(p) + " - Hum (percentage): " + str(h)

  print message

  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.03)

