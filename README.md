# Intelligent Surveillance and Species Detection System

A smart surveillance system designed to detect wild animals near farmland and alert users in real-time. This project uses *ESP32-CAM, **Raspberry Pi, and computer vision techniques such as **MobileNet, **Haar Cascade, and **CNN* to protect crops from damage caused by wildlife.

---

## Objectives

- Detect animal presence in restricted or farm areas
- Recognize known vs unknown species or people
- Send alerts to farmers through the Blink App
- Provide real-time video monitoring via ESP32-CAM

---

## Tools & Technologies Used

- ESP32-CAM (real-time camera)
- Raspberry Pi (processing unit)
- MobileNet, Haar Cascade, CNN, LBPH (for face/object recognition)
- Blink App (mobile alert system)
- Python (for detection logic and notifications)
- OpenCV (image processing)

---

## Features

- Real-time camera view using ESP32-CAM  
- Known person/animal detection using face recognition (LBPH)  
- Alerts through Blink App when unknown movement is detected  
- Uses lightweight ML models for efficient image detection  
- Can be used for crop protection and general rural surveillance

---

## How It Works

1. ESP32-CAM streams live video to Raspberry Pi
2. Raspberry Pi runs detection logic (using MobileNet or Haar Cascade)
3. If an unknown animal/person is detected:
   - Face/image is captured
   - Alert is sent to the user via Blink App
4. Known persons (e.g., farmer or worker) are ignored

---

## Project Images

You can upload images of your hardware setup, detection screenshots, and circuit diagrams here.

---

## Future Improvements

- Add GSM/SMS alert system  
- Night vision integration  
- Expand to multiple camera modules  
- Integrate a voice-based notification feature

---

## Credits

Developed as a final-year academic project by  
*Akshaya T S* — B.Tech Electronics and Communication Engineering  
Vidya Academy of Science and Technology, Kerala
