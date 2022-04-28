import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


def GPIO_Initialization(forwardPin, backwardPin):
    global forwardOutput, backwardOutput
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    pwmFreq = 1000
    dutyCycle = 0

    GPIO.setup(forwardPin, GPIO.OUT)
    GPIO.setup(backwardPin, GPIO.OUT)

    forwardOutput = GPIO.PWM(forwardPin, pwmFreq)
    backwardOutput = GPIO.PWM(backwardPin, pwmFreq)

    forwardOutput.start(dutyCycle)
    backwardOutput.start(dutyCycle)
    
def forward(forwardSpeed):
    global forwardOutput, backwardOutput
    forwardOutput.ChangeDutyCycle(forwardSpeed)
    backwardOutput.ChangeDutyCycle(0)
    
def backward(backwardSpeed):
    global forwardOutput, backwardOutput
    backwardOutput.ChangeDutyCycle(backwardSpeed)
    forwardOutput.ChangeDutyCycle(0)
    
def stop():
    global forwardOutput, backwardOutput
    backwardOutput.ChangeDutyCycle(0)
    forwardOutput.ChangeDutyCycle(0)
    
def  main():
    GPIO_Initialization(11,13)
    try: 
        for n in range(4):
            forward(10)
            time.sleep(2)
            backward(10)
            time.sleep(2)
            stop()
            time.sleep(2)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
    
if __name__ == "__main__":
    main()
    
    
    
    
