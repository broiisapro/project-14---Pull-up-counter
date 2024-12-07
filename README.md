This project counts the number of pull-ups performed using computer vision techniques with the help of **OpenCV** and **MediaPipe**. It tracks a person's arm movement in real-time and increments the count each time they complete a pull-up.

## Features:
- Detects pull-ups using a back-facing camera (no need for the head to be visible).
- Uses **MediaPipe Pose** for pose detection, specifically focusing on **elbow** and **shoulder** positions.
- Real-time counting with display of the current count on the video feed.
- Easy to use and lightweight.

## Requirements:
- Python 3.x
- OpenCV
- MediaPipe

### Use the Application
- The program will use the default camera to track your movements.
- Make sure you are positioned in front of the camera with your back facing it.
- The pull-up count will be displayed in real-time on the video feed.
- The program will count your pull-ups by detecting when your elbows fully extend during each pull-up.
- Press **'q'** to quit the program.

## How It Works

The program uses **MediaPipe Pose** to detect human body landmarks. Specifically:
- The **left and right shoulders** and **elbows** are used to determine the position of the arms during a pull-up.
- The program counts a pull-up every time the elbows reach their maximum extension (when the arms are fully straight).

### Key Components:
- **MediaPipe Pose Detection**: A pre-trained model that detects human pose keypoints in the video feed.
- **OpenCV**: Used for real-time video capture and display.
- **Pull-up Logic**: The program increments the pull-up count each time both elbows are fully extended, indicating the top of the pull-up motion.

### Detecting Pull-ups:
1. The program detects when both elbows are fully extended above the shoulders (top position of the pull-up).
2. The pull-up count increases when this position is reached.
3. The program ensures the count increments once per pull-up by toggling the state after the top position is reached.

## Troubleshooting

- **Incorrect Counting**: If the program counts incorrectly, ensure that your arms are visible and the camera is properly aligned. The detection depends on the clear visibility of the elbows and shoulders.
- **Performance Issues**: If you experience performance issues, try adjusting the `min_detection_confidence` and `min_tracking_confidence` parameters in the `pose` initialization. Lowering these values may help with faster processing but may decrease accuracy.

readme made with AI assistance
