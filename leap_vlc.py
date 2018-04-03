import os, sys, inspect, thread, time,string
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
#print "src dir : ",src_dir
#print os.path.realpath(__file__)
src_dir = string.replace(src_dir,'\\','/')

arch_dir = 'lib/x64' if sys.maxsize > 2**32 else 'lib/x86'

#print arch_dir
#print os.path.join(src_dir, arch_dir)
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
#print os.path.abspath(os.path.join(src_dir, arch_dir))
import Leap
import math
from selenium import webdriver
import time

status =['pause','play']
status_index=0
src_dir = os.getcwd()
#print src_dir
#print os.getcwd()
#print '{}\\phantomjs.exe'.format(src_dir)
driver = webdriver.PhantomJS('{}\\phantomjs.exe'.format(src_dir))
volume_level=10

def executeCommand(command):
    #print command
    time.sleep(0.2)
    driver.get(command)

def vlcCommand(key):
    global status,status_index,driver

    print key
    if key =='play/pause':
        command='http://localhost:8080/requests/status.xml?command=pl_{}'.format(status[status_index])
        #print command
        executeCommand(command)
        if status_index == 0:
            status_index =1
        else:
            status_index=0

    elif key == 'previous':
        command='http://localhost:8080/requests/status.xml?command=pl_{}'.format(key)
        executeCommand(command)
    elif key == 'next':
        command = 'http://localhost:8080/requests/status.xml?command=pl_{}'.format(key)
        executeCommand(command)
    elif key == 'volume up':
        command='http://localhost:8080/requests/status.xml?command=volume&val=+{}'.format(volume_level)
        executeCommand(command)
    elif key == 'volume down':
        command = 'http://localhost:8080/requests/status.xml?command=volume&val=-{}'.format(volume_level)
        executeCommand(command)

def getDistance(a,b,threshold):
    distance = abs(a-b)
    if a>b :
        if distance >threshold:
            return "previous"
    elif a<b:
        if distance >threshold:
            return "next"

    return None

def check(a,b):
    if a<0 and b<0:
        return True
    if a>0 and b>0:
        return True
    return False

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    position1=None
    position2=None
    start_frame =None
    prev_angle=None

    def on_connect(self, controller):
        print "Connected"


    def on_frame(self, controller):
        frame = controller.frame()
        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
        hand = frame.hands.rightmost
        #position = hand.palm_velocity
        #velocity = hand.palm_velocity
        direction = hand.direction


        print "no. of hands : {} hands".format(len(frame.hands)) ,

        flag = 0 #this is used to issue one command per frame
        pinch=hand.pinch_strength

        #print " pinch strenght : {} ".format(pinch)

        if pinch > 0.5 and flag == 0 :
            vlcCommand('play/pause')
            flag=1

        #print "finger {} ".format()
        #print "position : {} , velocity : {} , direction : {}".format(position,velocity,direction)
        #print getDistance(self.position1,self.position2)

        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)
                #print "start position ",swipe.start_position
                #print "current position " , swipe.position
                distance=getDistance(swipe.start_position[0],swipe.position[0] ,10)
                if flag ==0:
                    vlcCommand(distance)
                    flag=1



        #rotation_around_y_axis = hand.rotation_angle(start_frame, Vector.y_axis)

        pitch = int(direction.pitch * Leap.RAD_TO_DEG)
        if pitch <=80 :
            if self.prev_angle == None:
                self.prev_angle=int(pitch)
            else:
                angle= getDistance(int(pitch),self.prev_angle,20)
                if angle !=None and flag ==0:
                    if hand.is_left :
                        vlcCommand('volume down')
                    else:
                        vlcCommand('volume up')
                    flag=1

        os.system('cls')

        """
                for finger in hand.fingers:
            print self.finger_names[finger.type]

                distance=getDistance(swipe.start_position[1],swipe.position[1])
                if temp==0 :
                    print "inside volume"
                    if distance == 'positive':
                        distance = 'volume up'
                    else:
                        distance='volume down'
                    vlcCommand(distance)
                    temp=1

                if self.start_frame !=None:
                    rotation_around_y_axis = hand.rotation_angle(self.start_frame, Leap.Vector.y_axis)
                    print rotation_around_y_axis

                if len(frame.hands) !=0 :
                    self.start_frame=frame
        """

def main():

    listener=SampleListener()
    controller = Leap.Controller()

    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    controller.config.set("Gesture.Swipe.MinLength", 100.0)
    controller.config.set("Gesture.Swipe.MinVelocity", 750)
    controller.config.save()

    controller.add_listener(listener)


    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

