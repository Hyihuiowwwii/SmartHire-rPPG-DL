import cv2


class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def detect_face(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        if len(faces) > 0:
            x, y, w, h = faces[0]
            return (x, y, w, h)

        return None

    def draw_face_box(self, frame, bbox):
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame

    def get_roi(self, frame, bbox):
        x, y, w, h = bbox

        roi_x1 = x + int(0.3 * w)
        roi_y1 = y + int(0.15 * h)
        roi_x2 = x + int(0.7 * w)
        roi_y2 = y + int(0.35 * h)

        roi = frame[roi_y1:roi_y2, roi_x1:roi_x2]

        return roi, (roi_x1, roi_y1, roi_x2 - roi_x1, roi_y2 - roi_y1)

    def draw_roi_box(self, frame, roi_bbox):
        x, y, w, h = roi_bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame
