# The Center for Information and Language Processing University of Munich (LMU) https://huggingface.co/cis-lmu/glotlid
from .fasttext_detector import FasttextDetector 

class GlotLID(FasttextDetector):
    NAME="GlotLID-v3"
    MODEL_FILENAME = "glotlid_v3.bin"
