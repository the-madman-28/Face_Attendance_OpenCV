# Face Recognition Attendance System

## Project Overview
This project implements a Face Recognition Attendance System using Python, OpenCV, and the face_recognition library. The system captures video from a webcam, recognizes faces of registered students, and marks their attendance in a CSV file. It also provides audio feedback using text-to-speech functionality.

## Technologies Used
- **Python**: The primary programming language used for the implementation.
- **OpenCV**: A computer vision library used for image processing and video capture.
- **face_recognition**: A library built on top of dlib for face detection and recognition.
- **pyttsx3**: A text-to-speech conversion library for providing audio feedback.
- **NumPy**: A library for numerical operations, used for handling arrays and mathematical functions.
- **datetime**: A module for handling date and time operations.
- **CSV**: Used for storing attendance records.

## Features
- Real-time face detection and recognition using a webcam.
- Attendance marking in a CSV file with timestamps.
- Audio feedback for recognized students.
- User-friendly interface with visual feedback on recognized faces.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required libraries:
   ```bash
   pip install opencv-python face_recognition pyttsx3 numpy
   ```

3. Create a directory named `student_images` and add images of students with their names as filenames.

4. Run the application:
   ```bash
   python attendance_system.py
   ```

## Usage
- Ensure the webcam is connected and functioning.
- Run the script, and the webcam feed will open.
- The system will recognize faces and mark attendance automatically.
- Press 'q' to exit the application.
