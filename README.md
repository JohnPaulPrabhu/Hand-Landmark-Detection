# Hand-Landmark-Detection
This Python script utilizes MediaPipe and OpenCV libraries to detect and visualize hand landmarks in a video. It can identify up to two hands simultaneously and draws lines connecting corresponding landmarks between them.
![image](https://github.com/JohnPaulPrabhu/Hand-Landmark-Detection/assets/26264448/829dbb3e-fda4-45e3-bc11-b90e5ea24584)


## Libraries Used: 
1. MediaPipe
2. OpenCV

## Key Features:
1. Hand Detection: Detects up to two hands in each video frame using MediaPipe's pre-trained model.
2. Landmark Recognition: Identifies 21 key points (landmarks) on each detected hand.
3. Connection Visualization: Draws lines connecting corresponding landmarks between hands for better visualization.
4. Customization: Offers configuration options for:
5. Maximum number of hands to detect
6. Minimum detection confidence threshold
7. Minimum tracking confidence threshold

## Installation:
#### Install required libraries: 
- pip install mediapipe
- pip install opencv-python

## Usage:
1. Replace video_path = "obama.mp4" with the actual path to your video file.
2. Run the Python script.
3. Press 'q' to quit.
