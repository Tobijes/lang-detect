# Generic Fasttext model
from .detector import Detector
import fasttext

class FasttextDetector(Detector):
    NAME="EmptyFasttext"

    def __init__(self) -> None:
        super().__init__()
        self.detector = fasttext.load_model(self.MODEL_PATH)
        labels = self.detector.get_labels()
        self.supported = set(map(lambda x: x.replace("__label__", ""), labels))

    def detect(self, text):
        label, score = self.detector.predict(text)
        # print(label, score)
        detected_lang = label[0].replace("__label__", "")
        detected_score = score[0]
        return detected_lang, detected_score