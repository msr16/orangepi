import subprocess

class GPIO:
    IN = 'in'
    OUT = 'out'
    
    HIGH = 1
    LOW = 0
    
    def __init__(self):
        pass
        
    @classmethod
    def setup(cls, num_gpio, mode):
        subprocess.check_output(f'echo {num_gpio} | sudo tee /sys/class/gpio/export', shell=True)
        subprocess.check_output(f'echo {mode} | sudo tee /sys/class/gpio/gpio{num_gpio}/direction', shell=True)
    
    @classmethod
    def output(cls, num_gpio, level):
        subprocess.check_output(f'echo {level} | sudo tee /sys/class/gpio/gpio{num_gpio}/value', shell=True)
    
    @classmethod
    def input(cls, num_gpio):
        result = subprocess.check_output(f'cat /sys/class/gpio/gpio{num_gpio}/value', shell=True)
        return int(result.decode('ASCII').strip())
    
    @classmethod
    def cleangpio(cls, num_gpio):
        subprocess.check_output(f'echo {num_gpio} | sudo tee /sys/class/gpio/unexport', shell=True)