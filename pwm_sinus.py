import RPi.GPIO as GPIO
import time
import math

# Ställ in GPIO
GPIO.setmode(GPIO.BCM)  # Använd BCM pin-nummer
GPIO.setup(18, GPIO.OUT)  # Använd GPIO 18 för PWM

# Skapa PWM-objekt
pwm = GPIO.PWM(18, 1000)  # Frekvens = 1000 Hz
pwm.start(0)  # Starta med 0% duty cycle

try:
    while True:
        # Generera sinusvåg som duty cycle (mellan 0 och 100%)
        for i in range(0, 360, 5):
            duty_cycle = (math.sin(math.radians(i)) + 1) * 50  # Sinusvåg från 0% till 100%
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)  # Vänta lite för att generera korrekt frekvens

except KeyboardInterrupt:
    pass  # Avbryt när du trycker på Ctrl+C

# Stäng av PWM och rensa GPIO
pwm.stop()
GPIO.cleanup()
