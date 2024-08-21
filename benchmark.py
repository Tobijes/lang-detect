import pandas as pd
from detectors import MediapipeDetector, LangdetectDetector, Original, OpenLID, NllbLID, GlotLID
from tqdm import tqdm

detectors = [
    MediapipeDetector,
    LangdetectDetector,
    Original,
    OpenLID,
    NllbLID,
    GlotLID
]

dataname = "data/data_1000"

df = pd.read_parquet(f'{dataname}.parquet', engine='pyarrow')
detector_dfs = []
print(len(df))

for detector_class in detectors:
    detector = detector_class()
    detector_results = []
    for index, row in tqdm(df.iterrows(), desc="rows"):
        url = row["url"]
        text = str(row["text"]).replace('\n', ' ')
        lang_code = row["language_code"]
        lang_name = row["language_name"]

        try:
            lang, score = detector.detect(text)
            detector_results.append({
                "lang": lang,
                "score" : score
            })

        except Exception as e:
            print(detector.NAME, index, e, lang_name, url, text)

    detector_df = pd.DataFrame(detector_results).add_prefix(f"{detector.NAME}_", axis=1)
    detector_dfs.append(detector_df)
df = pd.concat([df] + detector_dfs, axis=1)

df.to_parquet(f"{dataname}-predicted.parquet", engine="pyarrow")