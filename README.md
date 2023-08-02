Real-Time Ball Detection with Color and Password Authentication

This Python code presents a project that combines secure ball detection using computer vision techniques with a simple password authentication system. The project allows the user to enter a username and password via a Pygame-based graphical user interface (GUI). Upon successful authentication, the system uses OpenCV and a webcam to detect and track colored balls in real-time.

Features:

Username and Password Authentication: The program prompts the user to enter a username and password. The entered password is masked with asterisks for added security.

Password Security Check: The code performs a basic password security check by verifying if the entered password contains at least one digit and one uppercase letter. However, the implementation lacks the functionality to notify the user in case of a weak password.

Password Hashing: The entered password is hashed using MD5 with an appended salt value, adding a minimal layer of security to protect the stored passwords.

Ball Detection: The program uses computer vision techniques with OpenCV to detect colored balls (red, green, blue, yellow, and orange) in the video stream from the webcam. It applies color filtering and morphological operations to identify the balls' positions and draws bounding circles with labels around them.

Requirements:

Python: The code is written in Python, so you need to have Python installed on your system.

Pygame: Install the Pygame library for the graphical user interface.

OpenCV: The code relies on OpenCV for image processing and ball detection. Make sure you have OpenCV installed.

Numpy: This code utilizes Numpy for numerical computations, so ensure Numpy is installed.

Webcam: The code requires access to a webcam to capture video frames for ball detection.

Project Scope:
The project serves as a demonstration of combining simple password authentication with real-time object detection. However, as it stands, the password security check and hashing implementation are basic and not suitable for production-level security. If you intend to use this as a secure login system, it's essential to enhance the password security measures significantly. Additionally, the ball detection part can be extended to include other objects or be integrated with a larger system or game that utilizes object tracking.

Please note that this code snippet may require additional dependencies or modifications based on your Python environment and system configuration. Always ensure to use strong and robust password security measures in a real-world application.
