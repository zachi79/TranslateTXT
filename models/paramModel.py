from dataclasses import dataclass


@dataclass
class ParamModel:
    method: str = "Internet"
    fileToTranslate: str = ""
    outputPath: str = ""
    selectedLang: str = "Hebrew"
    txtToTranslate: str = ""
    fileName: str = ""
    extension: str = ""




