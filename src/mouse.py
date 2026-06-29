import cv2
import os
import numpy as np
import pyautogui as robot
# ---------- Configuration ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
CASCADE_PATH = os.path.join(BASE_DIR, "..", "model", "haarcascade_frontalface_default.xml")
CASCADE_PATH2 = os.path.join(ROOT_DIR,"model", "haarcascade_eye.xml")
CAMERA_INDEX = 1

# print("BASE_DIR:", BASE_DIR)
# print("CASCADE_PATH2:", CASCADE_PATH2)
# print(__file__)


def load_face_detector(cascade_path: str):
    """Load Haar Cascade model for face detection."""
    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
    if face_cascade.empty():
        raise IOError(f"Failed to load cascade file: {cascade_path}")
    return face_cascade


def load_eye_detector(cascade_path2: str):
    """Load Haar Cascade model for face detection."""
    eye_cascade = cv2.CascadeClassifier(CASCADE_PATH2)
    if eye_cascade.empty():
        raise IOError(f"Failed to load cascade file: {cascade_path2}")
    return eye_cascade


def start_camera(index: int):
    """Initialize webcam capture."""
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise RuntimeError("Could not open camera.")
    return cap


def main():
    """Run real-time face and eyes detection."""
    face_detector = load_face_detector(CASCADE_PATH)
    eye_detector = load_eye_detector(CASCADE_PATH2)
    cap = start_camera(CAMERA_INDEX)
    
    screen_w, screen_h = robot.size()
    while True:
        ret,fr = cap.read()
        if not ret or fr is None:
            continue 
        gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=9,
            minSize=(60, 60)
        )
        eyes = []
        for (x, y, w, h) in faces:
            cv2.rectangle(fr, (x, y), (x + w, y + h), (0, 255, 0), 2)

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = fr[y:y+h, x:x+w]
            a=robot.position()
            b=(a.x)
            c=(a.y)
            print('x:',x , 'y:' , y)
            color=(255,255,255)

            b = max(10, min(screen_w - 10, b))
            c = max(10, min(screen_h - 10, c))
            if x<150:
                color=(255,0,0)
                b=b-(3*abs(x-200))
                robot.moveTo(b,c,0.3)

            elif x+w>400:
                color=(255,0,0)
                b=b+(3*abs(x+w-450))
                robot.moveTo(b,c,0)
            elif y<70:
                color=(255,0,0)
                c=c-(3*abs(y-30))
                robot.moveTo(b,c,0)
            elif y+h>250:
                color=(255,0,0)
                c=c+(3*abs(y+h-250))
                robot.moveTo(b,c,0)
       

            
            cv2.rectangle(fr, (150, 70), (400,250), color, 2)
            eyes=eye_detector.detectMultiScale (
            roi_gray,
            scaleFactor=1.05,
            minNeighbors=8,
            minSize=(20, 20),
            maxSize=(50,50)
            )
        

        for (xe, ye, we, he) in eyes:
            cv2.rectangle(roi_color, (xe, ye), (xe + we, ye + he), (0, 0, 255), 2)
        cv2.imshow("Face detection (press q to quit)", fr)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()



 