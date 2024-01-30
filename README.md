<h1>Face Recognition Attendance System</h1>


<h2>Introduction </h2>

This Python script implements an enhanced face recognition attendance system using the OpenCV, dlib, and face_recognition libraries. The system captures video from the camera and matches faces with pre-registered images of students. When a recognized student is detected, their attendance is marked in a CSV file.


<h2>Dependencies </h2>

<h4>Ensure you have the required libraries and tools installed before running the script:</h4>
<ul>
<li>cmake</li>
<li>opencv-python</li>
<li>dlib</li>
<li>face_recognition</li>
<li>os</li>
<li>pyttsx3</li>
<li>datetime</li>
<li>numpy</li>
</ul>

<h3>Install the necessary packages using pip install.</h3>

<h3>Note: The installation of dlib might require additional dependencies depending on your operating system. Refer to the official dlib installation guide for more details.</h3>


<h2>Usage </h2>

<b>1- Folder Structure:</b> Place the images of students in the 'student_images' folder. Each image should contain only one face, and the filename should be the name of the student (e.g., 'john.jpg').

<b>2- CSV File:</b> Create an empty 'attendance.csv' file in the same directory as the script. The attendance data will be appended to this file.

<b>3- Run the Script:</b> Execute the script in a Python environment.

<b>4- Face Recognition:</b> The script captures video from the default camera (usually webcam). When a recognized student is detected, their name is displayed on the screen, and attendance is marked in the CSV file.

<b>5- Exit:</b> Press 'q' to exit the video window and stop the script.


<h2>Additional Notes </h2>
<ul>
<li>The script uses a face recognition threshold (0.6) to determine a match. You can adjust this value based on your specific use case.</li>

<li>The attendance details (name, date, and time) are stored in the 'attendance.csv' file.</li>

<li>The system utilizes text-to-speech functionality (pyttsx3) to welcome the recognized student to the class.</li>

<li>Ensure that the necessary permissions are granted for accessing the camera.</li>

<li>Make sure to customize the script based on your specific requirements, such as camera selection, face recognition threshold, etc.</li>
</ul>

<h2>Conclusion </h2>

This face recognition attendance system provides a robust and efficient way to automate the attendance process using the OpenCV, dlib, and face_recognition libraries in Python. Customize it to suit your needs and enjoy the convenience of automated attendance tracking.
