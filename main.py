from machine import Pin, ADC, PWM
from math import log
from time import sleep
adc28 = ADC(28)
adc27 = ADC(27)
pin21 = PWM(Pin(21))
pin20 = PWM(Pin(20))
pin20.freq(1000) 
pin21.freq(10000) 
pin0 = Pin(0, Pin.IN)
B = 3.9E3;
T0 = 298;   
R = 10E3;
conversion_factor = 3.3/ 65535

while True:
  value = adc28.read_u16() * conversion_factor
  Re = (((value)*10000)/(3.3 - value))
  temp = ((T0 * B)/(T0*log(Re/R)+ B)) - 273.15
  value2 = (adc27.read_u16() * 80)/65535
  if temp > value2:
    pin21.duty_u16(int((temp * 80)/65535))
    p
    pin20.duty_u16(0)
  else:
    pin20.duty_u16(int((value2 * 80)/65535000)) 
    pin21.duty_u16(0)