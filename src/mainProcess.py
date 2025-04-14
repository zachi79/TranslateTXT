from models.paramModel import ParamModel
from src import translate
from src.readSaveData import saveDataTxt
from nicegui import ui

def mainProcess():
    try:
        if "AI" in ParamModel.method.value:
            #ui.notify('The Method translation is not support right now, please try later', color='red')
            ParamModel.translated = translate.callAIToTranlate(ParamModel.selectedLang, ParamModel.txtToTranslate)
        else:
            #ui.notify('The Method translation is not support right now, please try later', color='red')
            ParamModel.translated = translate.callInternetToTranlate(ParamModel.selectedLang, ParamModel.txtToTranslate)

        fileName = ParamModel.fileName+"_"+ParamModel.selectedLang+ParamModel.extension
        saveDataTxt(fileName, ParamModel.translated)
    except:
        ui.notify('The Method translation Failed, please try later', color='red')
    pass
