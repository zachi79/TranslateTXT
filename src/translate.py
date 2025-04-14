# import requests
# import ollama
import argostranslate.package
import argostranslate.translate
from argostranslate.translate import get_installed_languages
import google.generativeai as genai


def split_into_chunks(text, num_chunks=50):
    chunk_size = len(text) // num_chunks
    chunks = [text[i * chunk_size: (i + 1) * chunk_size] for i in range(num_chunks - 1)]
    chunks.append(text[(num_chunks - 1) * chunk_size:])  # last chunk includes any remainder
    return chunks


def callAIToTranlate(selectedLang: str, txtToTranlate: str) -> str:
    #todo: add LLM
    # ollama - is not working well for translate
    response = ""
    text_to_send = txtToTranlate.decode('utf-8')
    chunks = split_into_chunks(text_to_send)
    API_KEY = "Not-REAL-KEY-AIzaSyDpIUFYVu-DEnzymeItn4DeqnWnFHUuGkxI"
    genai.configure(api_key=API_KEY)

    model_flash = genai.GenerativeModel('gemini-2.0-flash')
    response_flash = model_flash.generate_content(f"Translate {chunks[0]} to Heb.")
    print(response_flash.text)

    return response

def callInternetToTranlate(selectedLang: str, txtToTranlate: str) -> str:
    # LibreTranslate / argostranslate
    text_to_send = txtToTranlate.decode('utf-8')
    # Update the package index (fetches list of available language packages)
    # argostranslate.package.update_package_index()
    # # Get list of available packages
    # available_packages = argostranslate.package.get_available_packages()
    # # Find the English to Hebrew package
    # package_to_install = next(
    #     (p for p in available_packages if p.from_code == "en" and p.to_code == "he"),
    #     None
    # )
    #
    # # Install the package if it's found
    # if package_to_install:
    #     downloaded_path = package_to_install.download()
    #     argostranslate.package.install_from_path(downloaded_path)
    #     print("English to Hebrew package installed!")
    # else:
    #     print("English to Hebrew package not found.")

    installed_languages = get_installed_languages()
    from_lang = next(lang for lang in installed_languages if lang.code == "en")
    to_lang = next(lang for lang in installed_languages if lang.code == "he")
    translation = from_lang.get_translation(to_lang)
    chunks = split_into_chunks(text_to_send)
    translatedText = translation.translate(chunks[0]) # TODO: bring back [translation.translate(row) for row in chunks]

    #''.join(map(str, translatedText))
    print(translatedText)
