import os
from src.dataPaths import *
from src.mainProcess import mainProcess
from src.readSaveData import *
from nicegui import ui
from models.paramModel import *


def languageSelected(e):
    ParamModel.selectedLang = e.value
    print(f'Language selected: {ParamModel.selectedLang}')

def headerPage():
    ui.page_title('ZH Software')

    with ui.header(elevated=True).style('background-color: #000000').classes('items-center justify-between'):
        with ui.row().classes('items-center w-full justify-between p-8'):
            ui.image(IMAGE_LOGO_PATH).classes('w-72 h-auto')
            ui.image(IMAGE_TITLE_PATH).classes('w-72 h-auto')
            dark = ui.dark_mode()
            dark.enable()
            ui.switch('Dark mode').bind_value(dark)

def handleUpload(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ['.srt', '.txt']:
        ui.notify(f"❌ Only .srt or .txt files are allowed (got {ext})", color='red')
        return
    ParamModel.txtToTranslate= file.content.read()
    ParamModel.fileName = os.path.splitext(file.name)[0]
    ParamModel.extension = os.path.splitext(file.name)[-1]
    ui.notify(f"Uploaded file")
    print(f"Uploaded file extension {ParamModel.fileName},{ParamModel.extension}")


def mainCenterSection():
    with ui.column().classes('items-center justify-center h-auto p-8'):
        with ui.column().classes('w-full max-w-xl flex flex-col items-center space-y-4'):
            ui.label('🌍 This site is for translating documents (.txt) and subtitle (.srt) files easily using AI or online services.')\
                .classes('text-lg text-gray-600 text-center')

    with ui.column().classes('items-center justify-center pt-4 p-8'):
        ParamModel.method = ui.toggle(['🤖 AI', '🌐 Internet'], value='🌐 Internet')

    with ui.column().classes('items-center justify-center pt-4'):
        with ui.row().classes('items-center w-full justify-between p-8'):
            ui.upload(on_upload=handleUpload, label='📂 Browse a file to translate',
                      auto_upload=True)
            ui.label('    ').classes('h-8')
            # ParamModel.outputPath = ui.input('📁 Enter output path to save:') # todo: output path
            ui.label('    ').classes('h-8')
            ui.label('Choose Language to Translate to:')
            ui.select(
                options=['English', 'French', 'Hebrew'],
                on_change=languageSelected, value='Hebrew'
            ).classes('w-40')


    with (ui.column().classes('items-center justify-center pt-4 p-8')):
        def translate():
            if ParamModel.txtToTranslate != "" and ParamModel.selectedLang != "":
                ui.notify('🚀 Translation started...')
                mainProcess()
            else:
                ui.notify('Please upload a file and and select lang.', color='red')

        ui.button('🚀 Start Translate', on_click=translate).classes('mt-2')

    pass


def footerPage():
    with ui.footer().style('background-color: #000000'):
        data_txt = readDataTxt(ABOUT_FILE)
        ui.label(data_txt
        ).classes('text-sm text-white-400 mt-12 border-t pt-4 text-center w-full')

    pass


def uiMain():
    headerPage()
    mainCenterSection()
    footerPage()
    ui.run(title='Translate doc/srt', port=8081)