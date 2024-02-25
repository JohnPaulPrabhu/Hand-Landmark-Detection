import mediapipe as mp
import cv2

# Create a MediaPipe Hands object
hands = mp.solutions.hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Specify the video file path
video_path = "obama.mp4"

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


    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_id, hand_landmarks in enumerate(results.multi_hand_landmarks):
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    # Display the image
    cv2.imshow('Hand Landmarks', image)

    # Quit if 'q' key is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
