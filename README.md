# playtello

You can control Tello with PC and receive H.264 video stream. In auto-tracking mode, PC pilots Tello automatically to keep the distance from your face and Tello and to keep your face center on the screen.

**Please pay close attention to your Tello to avoid uncontrollable trouble. Play at your own risk!**

my environments
- macOS 10.12.6
- Python 3.6.5
- OpenCV 3.4.1


## Usage
```
sudo python drone.py
```

Key | Operation
--- | ---
Space | takeoff / land
Enter | exit
w | up (low speed)
Shift + w | up (high speed)
s | down (low speed)
Shift + s | down (high speed)
a | ccw (low speed) 
Shift + a | ccw (high speed)
d | cw (low speed)
Shift + d | cw (high speed)
i or up | forward (low speed)
Shift + i | forward (high speed)
k or down | back (low speed)
Shift + k | back (hightspeed)
j or left | left (low speed)
Shift + j | left (high speed)
l or right | right (low speed)
Shift + l | (high speed)
9 | face detect on/off
0 | face tracking on/off
