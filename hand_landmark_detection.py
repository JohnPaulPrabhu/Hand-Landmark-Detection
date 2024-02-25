import mediapipe as mp
import cv2

# Create a MediaPipe Hands object
hands = mp.solutions.hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Specify the video file path
video_path = "path/to/your/video.mp4"

# Initialize video capture
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file:", video_path)
    exit()

while True:
    success, image = cap.read()

    if not success:
        print("Ignoring empty camera frame.")
        # If video ends, break the loop
        break

    # Convert the image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image
    results = hands.process(image)

    # Draw connections if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Connect the hand landmarks
            thickness = 2
            color = (0, 0, 255)

            # Iterate through consecutive points and draw lines
            for i in range(len(hand_landmarks.landmark) - 1):
                start_point = (int(hand_landmarks.landmark[i].x * image.shape[1]),
                               int(hand_landmarks.landmark[i].y * image.shape[0]))
                end_point = (int(hand_landmarks.landmark[i + 1].x * image.shape[1]),
                             int(hand_landmarks.landmark[i + 1].y * image.shape[0]))
                cv2.line(image, start_point, end_point, color, thickness)

    # Display the image
    cv2.imshow('Hand Landmarks', image)

    # Quit if 'q' key is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
