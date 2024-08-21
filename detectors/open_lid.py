# Wikimedia project: https://huggingface.co/laurievb/OpenLID
from .fasttext_detector import FasttextDetector 

class OpenLID(FasttextDetector):
    NAME="OpenLID-201"
    MODEL_FILENAME = "openlid.201.bin"
