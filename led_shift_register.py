import OPi.GPIO as GPIO
from time import sleep

class ShiftOut:
    def __init__(self, data_pin, rclk_pin, sclk_pin, chips_count=4):
        GPIO.setup(rclk_pin, GPIO.OUT)
        GPIO.setup(sclk_pin, GPIO.OUT)
        GPIO.setup(data_pin, GPIO.OUT)
        
        self.data_pin = data_pin
        self.rclk_pin = rclk_pin
        self.sclk_pin = sclk_pin
        
        GPIO.output(self.rclk_pin, 0)
        GPIO.output(self.sclk_pin, 0)
        
        self.data_width = chips_count * 8
        self.delay_time = 0.001
        
    def write(self, leds):
        data = [1 for i in range(self.data_width)]
        for num in leds:
            data[num] = 0
            
        for bit in data:
            GPIO.output(self.data_pin, bit)
            sleep(self.delay_time)
            
            GPIO.output(self.sclk_pin, 1)
            sleep(self.delay_time)
            GPIO.output(self.sclk_pin, 0)
            
        sleep(self.delay_time)
        GPIO.output(self.rclk_pin, 1)
        sleep(self.delay_time)
        GPIO.output(self.rclk_pin, 0)
