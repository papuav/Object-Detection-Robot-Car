import cv2 as cv
import numpy as np

class Camera:
    def __init__(self, usb):
        self.cap = cv.VideoCapture(usb)
        self.width = self.cap.get(3)
        self.height = self.cap.get(4)
        self.HorizontalCenter = self.width/2
        self.VerticalCenter = self.height/2
        
        
    def capture(self):
        # read each frame
        _, frame = self.cap.read()
        #Convert color mode BGR to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        
        #define range of blue color
        lower_blue = np.array([71, 112, 112])
        upper_blue = np.array([128, 255, 255])
        
        #threshold the HSV image to get only blue colors
        blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
        
        #Find the contours of the object
        contours, hie = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        
        #sorted the contours from the biggest
        contours = sorted(contours, key=lambda x:cv.contourArea(x), reverse = True)
        
        #for each contours frame, find the middle point of that object and draw  the rectangle around it
        for c in contours:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
            middlePoint = int((x + x + w)/2)
            break
        
        #Uncomment this line if you want to use center line too 
        #cv.line(frame, (int(self.HorizontalCenter), 0), (int(self.HorizontalCenter), 480), (0, 255, 0), 2)
        
        #show the normal frame
        cv.imshow('Frame', frame)
        
    def close(self):
        self.cap.release()
        cv.destroyAllWindows()

def main():
    cam = Camera(0)
    #Press q to quit
    print("Press q to quit camera")
    while True:
        cam.capture()
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cam.close()


if __name__ == "__main__":
    main()