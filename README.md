# Face Recognition Attendance System

## Introduction

This Python script implements an enhanced face recognition attendance system using the OpenCV, dlib, and face_recognition libraries. The system captures video from the camera and matches faces with pre-registered images of students. When a recognized student is detected, their attendance is marked in a CSV file.

## Dependencies

### Required Libraries:
- cmake
- opencv-python
- dlib
- face_recognition
- os
- pyttsx3
- datetime
- numpy

## Installation

Install the necessary packages using pip:

```bash
pip install cmake opencv-python dlib face-recognition pyttsx3 numpy
```

Note: The installation of dlib might require additional dependencies depending on your operating system. Refer to the [official dlib installation guide](https://github.com/davisking/dlib#compiling-dlib) for more details.

## Usage

### Folder Structure:

Place the images of students in the 'student_images' folder. Each image should contain only one face, and the filename should be the name of the student (e.g., 'john.jpg').

### CSV File:

Create an empty 'attendance.csv' file in the same directory as the script. The attendance data will be appended to this file.

### Run the Script:

Execute the script in a Python environment.

### Face Recognition:

The script captures video from the default camera (usually webcam). When a recognized student is detected, their name is displayed on the screen, and attendance is marked in the CSV file.

### Exit:

Press 'q' to exit the video window and stop the script.

## Important

- Ensure the camera is properly configured and accessible.
- Check the camera index in `cv2.VideoCapture(0)`; change it if your camera is not at index 0.


## Additional Notes

- The script uses a face recognition threshold (0.6) to determine a match. You can adjust this value based on your specific use case.
- The attendance details (name, date, and time) are stored in the 'attendance.csv' file.
- The system utilizes text-to-speech functionality (pyttsx3) to welcome the recognized student to the class.
- Ensure that the necessary permissions are granted for accessing the camera.
- Make sure to customize the script based on your specific requirements, such as camera selection, face recognition threshold, etc.

## Conclusion

This enhanced face recognition attendance system provides a robust and efficient way to automate the attendance process using the OpenCV, dlib, and face_recognition libraries in Python. Customize it to suit your needs and enjoy the convenience of automated attendance tracking.

