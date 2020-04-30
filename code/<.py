
import cwiid, time
import Adafruit_PCA9685


#Once a connection has been established with the two devices the rest of the program will continue; otherwise, it will keep on trying to connect to the two devices



# Set it so that we can tell when and what buttons are pushed, and make it so that the accelerometer input can be read

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adaf-ruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150
			  # Min pulse length out of 4096
servo_max = 600
			  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
speed = 60
pwm.set_pwm_freq(speed)
pwm.set_pwm(8, 0, 150)
pwm.set_pwm(9, 000, 600)