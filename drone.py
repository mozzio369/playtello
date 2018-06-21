import tello
import cv2
import time

LOCAL_IP = '192.168.10.2'
LOCAL_PORT_VIDEO = '8080'

if __name__ == '__main__':

    drone = tello.Tello()
    addr = 'udp://' + LOCAL_IP + ':' + str(LOCAL_PORT_VIDEO)
    cap = cv2.VideoCapture(addr)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow("Flame", frame)
            k = cv2.waitKey(1)
            if drone.stop_drone:
                print(drone.stop_drone)
                time.sleep(1)
                break
    cap.release()
    cv2.destroyAllWindows()
