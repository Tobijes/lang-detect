class Detector:
    NAME="DEFAULT"
    BASE_PATH = '/home/tobijes/dev/lang-detect/'
    MODEL_FILENAME = ""
    MODEL_PATH = ""
    supported: set

    def __init__(self, langs_file=None):
        if langs_file:
            with open(self.BASE_PATH + "supported_langs/" + langs_file) as f:
                langs = f.read().splitlines()
                self.supported = set(map(lambda x : self.normalize(x), langs))
        
        self.MODEL_PATH = self.BASE_PATH + "models/" + self.MODEL_FILENAME

    def predict(self, text):
        raise NotImplementedError()

    def normalize(self, lang):
        return lang
    
    def is_supported(self, lang):
        return lang in self.supported