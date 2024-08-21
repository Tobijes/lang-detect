# Original from start of FastText project: https://fasttext.cc/docs/en/language-identification.html
from .fasttext_detector import FasttextDetector 

class Original(FasttextDetector):
    NAME="LID-176"
    MODEL_FILENAME = "lid.176.bin"

