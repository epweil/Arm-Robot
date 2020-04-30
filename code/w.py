
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


# Set frequency to 60hz, good for servos.
speed = 300
pwm.set_pwm_freq(speed)
pwm.set_pwm(0, 0, 300)
pwm.set_pwm(1, 150, 0)
pwm.set_pwm(2, 0, 300)
pwm.set_pwm(3, 150, 0)
		
