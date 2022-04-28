import camera
import infrared as ir
import Pwm_Functions as pwm
import RPi.GPIO as GPIO
import cv2 as cv

def main():
    pwm.GPIO_Initialization(11,13,15,19)
    infrared = ir.Infrared(21)
    cam = camera.Camera(0)
    
    #Press q to quit
    print("Press q to quit camera")
    while True:
        cam.capture()
        isThere = infrared.check()
        middlePoint = cam.middlePoint
        center = cam.HorizontalCenter
        if isThere:
            pwm.stop()
        else:
            #moving the servo or motors
            if middlePoint < center - 50:
#                 initialPosition += 1
                #Replace this with your code
                print("Turn Left!")
                pwm.turnLeft()
            elif middlePoint > center + 50:
#                 initialPosition -= 1
                #Replace this with your code
                print("Turn Right")
                pwm.turnRight()
            else:
                #Replace this with your code
                print("Move forward!")
                pwm.forward(100)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    #Clean up before exiting
    cam.close()
    GPIO.cleanup()    

if __name__ == "__main__":
    main()