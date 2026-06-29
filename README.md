# 🖱️ Head-Controlled Mouse

Control your mouse cursor using head movements through your webcam using Python and OpenCV.

This project detects your face in real-time and moves the mouse pointer depending on your head position.

---

## 🎥 Demo

![Project Demo](demo.gif)

---

## 🚀 Features

- Real-time face detection using OpenCV
- Mouse cursor control using head movement
- Eye detection inside the detected face (ROI)
- Boundary protection to avoid screen overflow
- PyAutoGUI fail-safe support

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- PyAutoGUI
- Haar Cascade Classifiers

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/head-controlled-mouse.git
cd head-controlled-mouse
```

### 2. Install dependencies

```bash
pip install opencv-python numpy pyautogui
```

---

## ▶️ Run the Project

Run the main script:

```bash
python mouse.py
```

Press **Q** to exit the application.

---

## 🧠 How It Works

1. The webcam captures video frames.
2. Frames are converted to grayscale for faster processing.
3. A Haar Cascade classifier detects faces.
4. The center of the detected face is calculated.
5. Face movement relative to a boundary box moves the mouse cursor.
6. Eye detection runs only inside the face region (ROI).

---

## 📁 Project Structure

```
project/
│
├── model/
│   ├── haarcascade_frontalface_default.xml
│   └── haarcascade_eye.xml
│
├── mouse.py
├── demo.gif
└── README.md
```

---

## ⚠️ Notes

- Make sure your webcam is connected.
- Good lighting improves detection accuracy.
- PyAutoGUI fail-safe is enabled by default.
- Move the mouse to a screen corner to trigger the fail-safe and stop the script.

---

## 🔧 Possible Improvements

- Smooth mouse movement using filtering
- Blink detection for mouse clicks
- Face landmarks using MediaPipe
- Adjustable sensitivity settings

---

## ⭐ If you like this project

Consider giving it a star on GitHub!
