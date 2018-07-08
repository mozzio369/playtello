import tello
import cv2
import time
import datetime
import math as m

LOCAL_IP = '192.168.10.2'
LOCAL_PORT_VIDEO = '8080'

# Center Cordinates
CX = 480
CY = 360

# Reference Distance
L0 = 100
S0 = 25600

# Base Distance
LB = 120

if __name__ == '__main__':

    drone = tello.Tello()
    addr = 'udp://' + LOCAL_IP + ':' + str(LOCAL_PORT_VIDEO) + '?overrun_nonfatal=1&fifo_size=50000000'
    cap = cv2.VideoCapture(addr)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            if drone.mode_detect:
                if drone.is_detect:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    drone.is_detect = False
                try:
                    for (x,y,w,h) in faces:
                        if w != 0:
                            d = round(L0 * m.sqrt(S0 / (w * h)))
                            dx = x + w/2 - CX
                            dy = y + h/2 - CY
                        else:
                            d = LB
                        cv2.putText(frame, ' D:' + str(d) + 'cm X:' + str(dx) + 'px Y:' + str(dy) + 'px', (360, 710), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                        if drone.mode_tracking:
                            if (d - LB) > 15:
                                drone.pitch = drone.STICK_HOVER + drone.STICK_L
                            elif (d - LB) < -15:
                                drone.pitch = drone.STICK_HOVER - drone.STICK_L
                            else:
                                drone.pitch = drone.STICK_HOVER
                            if dx > 80:
                                drone.roll = drone.STICK_HOVER + drone.STICK_L
                            elif dx < -80:
                                drone.roll = drone.STICK_HOVER - drone.STICK_L
                            else:
                                drone.roll = drone.STICK_HOVER
                            if dy > 50:
                                drone.thr = drone.STICK_HOVER - drone.STICK_L
                            elif dy < -50:
                                drone.thr = drone.STICK_HOVER + drone.STICK_L
                            else:
                                drone.thr = drone.STICK_HOVER
                except NameError:
                    break 
            cv2.putText(frame, 'Detecting:' + str(drone.mode_detect) + ' Tracking:' + str(drone.mode_tracking), (5, 710), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow("frame", frame)
            k = cv2.waitKey(1)
            if drone.stop_drone:
                print('stop: ' + str(drone.stop_drone))
                time.sleep(1)
                break
    cap.release()
    cv2.destroyAllWindows()
