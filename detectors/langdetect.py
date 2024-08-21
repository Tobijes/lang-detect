# Python port of Nakatani Shuyo's language-detection library (version from 03/03/2014) to Python.
from .detector import Detector
import langdetect

class LangdetectDetector(Detector):
    NAME="Langdetect"

    def __init__(self) -> None:
        super().__init__(langs_file="langdetect.txt")

    def detect(self, text):
        try:
            top_languages = langdetect.detect_langs(text)
        except langdetect.lang_detect_exception.LangDetectException:
            return None, 0
        
        if not len(top_languages):
            return None, 0
        
        if top_languages[0].prob == 0:
            return None, 0
        
        detected_lang = top_languages[0].lang
        detected_score = top_languages[0].prob

        return detected_lang, detected_score
    
