# Google Project for fast LID: https://ai.google.dev/edge/mediapipe/solutions/text/language_detector
from .detector import Detector
from mediapipe.tasks import python
from mediapipe.tasks.python import text

class MediapipeDetector(Detector):
    NAME="Mediapipe"
    MODEL_FILENAME = "language_detector.tflite"

    def __init__(self) -> None:
        super().__init__(langs_file="mediapipe.txt")
        self.detector = python.text.LanguageDetector.create_from_model_path(self.MODEL_PATH)

    # def __del__(self):
    #     self.detector.close()


    def detect(self, text):
        detections = self.detector.detect(text).detections
        # print(detections)
        if not len(detections):
            return None, 0
        
        if detections[0].language_code == "unknown":
            return None, 0

        return detections[0].language_code, detections[0].probability

    