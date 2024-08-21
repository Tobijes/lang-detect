# Facebook's NLLB Project: https://github.com/facebookresearch/fairseq/tree/nllb#lid-model
from .fasttext_detector import FasttextDetector 

class NllbLID(FasttextDetector):
    NAME="NLLB-LID-218"
    MODEL_FILENAME = "nllb_lid.218e.bin"
    LANGS_FILENAME = "nllb_lid.218e.txt"
