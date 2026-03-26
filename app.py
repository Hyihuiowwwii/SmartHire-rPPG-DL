import cv2
from src.face_detection import FaceDetector

video_path = "sample_data/test_video.mp4"

cap = cv2.VideoCapture(video_path)
detector = FaceDetector()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    bbox = detector.detect_face(frame)

    if bbox is not None:
        frame = detector.draw_face_box(frame, bbox)

    cv2.imshow("Face Detection Test", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
