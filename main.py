import cv2
import mediapipe as mp

# Initialize MediaPipe Pose detection module
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# OpenCV to capture the video
cap = cv2.VideoCapture(0)  # Using the default camera (can use a video file here)

# Initialize variables for counting
pull_up_count = 0
is_pulling_up = False  # To track the state (is the user at the top or not)
has_reached_top = False  # To avoid counting multiple times during the ascent

def is_arms_at_top(landmarks):
    # Check if the arms are fully extended (indicating the top of a pull-up)
    left_shoulder = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    left_elbow = landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
    right_elbow = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
    
    # We assume that the top position is when the elbows are straight and shoulders are lower
    if (left_elbow.y < left_shoulder.y) and (right_elbow.y < right_shoulder.y):
        return True
    return False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    # Draw the pose landmarks
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Check if the arms are at the top position (extended elbows)
        if is_arms_at_top(results.pose_landmarks):
            if not has_reached_top:  # Only count once when the top is reached
                pull_up_count += 1
                has_reached_top = True  # Prevent counting again during ascent
        else:
            has_reached_top = False  # Allow counting again after the person descends

    # Display the count on the video feed
    cv2.putText(frame, f"Pull-ups: {pull_up_count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame with the overlay
    cv2.imshow("Pull-up Counter", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
