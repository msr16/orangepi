from OPi import GPIO
from time import sleep

class ShiftIn:
    def __init__(self, ld_pin, data_pin, clk_pin):
        GPIO.setup(ld_pin, GPIO.OUT)
        GPIO.setup(clk_pin, GPIO.OUT)
        GPIO.setup(data_pin, GPIO.IN)
    
        GPIO.output(ld_pin, GPIO.HIGH)
        GPIO.output(clk_pin, GPIO.LOW)
        
        self.ld_pin = ld_pin
        self.data_pin = data_pin
        self.clk_pin = clk_pin
        
        chip_count = 4
        self.data_width = chip_count * 8
        self.delay_time = 0.002
        
    def read(self):
        GPIO.output(self.ld_pin, GPIO.LOW)
        sleep(self.delay_time)
        GPIO.output(self.ld_pin, GPIO.HIGH)
        sleep(self.delay_time)
        
        result = 0
        for i in range(self.data_width):
            result = result << 1 | GPIO.input(self.data_pin)
            
            GPIO.output(self.clk_pin, GPIO.HIGH)
            sleep(self.delay_time)
            GPIO.output(self.clk_pin, GPIO.LOW)

        return result
    
    def __del__(self):
        GPIO.cleangpio(self.ld_pin)
        GPIO.cleangpio(self.clk_pin)
        GPIO.cleangpio(self.data_pin)