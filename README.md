# Computer Vision Projects

A collection of **computer vision applications** built using **Python**, **OpenCV**, and **MediaPipe**.  
These projects explore real-time image processing, hand tracking, and gesture-based interaction systems.

---

## Hand Tracking
This project implements **real-time hand landmark detection** using **MediaPipe** and **OpenCV**.  
It identifies **21 unique landmarks** on each detected hand and overlays visual connections on the live camera feed.

### Features
- Real-time hand detection and tracking  
- Visual rendering of hand landmarks and connections  
- FPS (frames per second) counter for performance monitoring  
- Compatible with any standard webcam  

---

## Hand Tracking Module
A modular implementation that defines a reusable **`handDetector` class** for detecting and tracking hands.  
This class provides landmark coordinates for use in downstream computer vision tasks, such as gesture recognition and hand-controlled interfaces.

### Key Highlights
- Reusable **object-oriented structure**  
- Supports detection of up to two hands simultaneously  
- Provides pixel coordinates for all 21 hand landmarks  
- Easily extendable for gesture or motion-based control systems  

---

## Technologies Used
- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://developers.google.com/mediapipe)
