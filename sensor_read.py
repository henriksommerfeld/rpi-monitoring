#!/usr/bin/python3
import time
import os
import threading
import requests
from sense_hat import SenseHat
from led_message import LedStateMessage
SEND_DATA_INTERVAL_SECONDS = 10.0
DEBUG = True

def debug_reading(temp, pressure, humidity):
	t = round(temp, 1)
	p = round(pressure, 1)
	h = round(humidity, 1)
	msg = "Temperature: {0} C. Pressure: {1} mBAR. Humidity: {2}%".format(t, p, h)
	debug(msg)

def debug(message):
	if DEBUG:
		print(message)

def get_cpu_temperature():  
	full_temperature_string = os.popen('vcgencmd measure_temp').readline()  
	tempterature_string = (full_temperature_string.replace("temp=","").replace("'C\n",""))
	return (float(tempterature_string))

def get_ambient_temperature():
	cpu_temp = get_cpu_temperature()
	temperature_from_sensor = sense.get_temperature_from_pressure()
	ambient_temp = temperature_from_sensor - ((cpu_temp - temperature_from_sensor)/ 1.5)
	return ambient_temp

def send_data(temp, pressure, humidity, last_time_sent):
	try:
		if time.time() - last_time_sent > SEND_DATA_INTERVAL_SECONDS:
			d = { 'temperature': temp, 'pressure': pressure, 'humidity': humidity }
			debug("trying to send data...")
			response = requests.post("http://127.0.0.1:8080/api/current", data=d)
			debug(response)
			screen.show_ok_message()			
			last_time_sent = time.time()
	except Exception as e:
		last_time_sent = time.time()
		print(e)
		screen.show_warning_message()
	finally:
		return last_time_sent

def read_sensors():
	last_time_sent = 0.0

	while True:
		pressure = sense.get_pressure()
		humidity = sense.get_humidity()
		temperature = get_ambient_temperature()
		debug_reading(temperature, pressure, humidity)
		last_time_sent = send_data(temperature, pressure, humidity, last_time_sent)
		time.sleep(1)

def main():
	try:
		read_sensors()
	except(KeyboardInterrupt, SystemExit):
		screen.clear()
	except Exception as e:
		print(e)
		screen.show_error_message()

sense = SenseHat()  
screen = LedStateMessage(sense, 180)
screen.clear()
main()