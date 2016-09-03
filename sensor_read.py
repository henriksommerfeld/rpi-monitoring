#!/usr/bin/python3
import time
import os
from sense_hat import SenseHat
from led_message import LedStateMessage
SEND_DATA_INTERVAL_SECONDS = 10

def debug(temp, pressure, humidity):
	t = round(temp, 1)
	p = round(pressure, 1)
	h = round(humidity, 1)
	msg = "Temperature: {0} C. Pressure: {1} mBAR. Humidity: {2}%".format(t, p, h)
	print(msg)

def get_cpu_temperature():  
	full_temperature_string = os.popen('vcgencmd measure_temp').readline()  
	tempterature_string = (full_temperature_string.replace("temp=","").replace("'C\n",""))
	return (float(tempterature_string))

def get_ambient_temperature():
	cpu_temp = get_cpu_temperature()
	temperature_from_sensor = sense.get_temperature_from_pressure()
	ambient_temp = temperature_from_sensor - ((cpu_temp - temperature_from_sensor)/ 1.5)
	return ambient_temp

def send_data(temp, pressure, humidity):
	try:
		time.sleep(SEND_DATA_INTERVAL_SECONDS)
		# todo: send data 
		screen.show_ok_message()
	except Exception,e:
		print str(e)
		screen.show_warning_message()	

def read_sensors():
	while True:
		pressure = sense.get_pressure()
		humidity = sense.get_humidity()
		temperature = get_ambient_temperature()
		debug(temperature, pressure, humidity)
		send_data(temperature, pressure, humidity)		
		time.sleep(1)

def main():
	try:
		read_sensors()
	except(KeyboardInterrupt, SystemExit):
		screen.clear()
	except Exception,e:
		print str(e)
		screen.show_error_message()

sense = SenseHat()  
screen = LedStateMessage(sense, 180)
screen.clear()
main()