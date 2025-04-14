The Project Translate TXT - POC 
Translate Documents(TXT) & SRT Files using LLMs and Internet Translate

This project provides a simple web interface (built with NiceGUI) that allows users to upload documents or SRT subtitle files, specify an output path, and receive translated files using either a large language model (LLM) or Google Translate.

Features:
Web-based interface for easy interaction

Supports DOC(TXT) and SRT file translation

Output saved to a user-defined path

Choose Language to Translate to (for now only to hebrew)

Translation powered by LLMs (google.generativeai)
or argostranslate Translate (free)

** My Notes
I tried to use OpenAI and Ollama. 
    - OpenAi not for free if using API
    - Ollama didn't response well to translate - may be I should use better version

About translation with API like Google Translate. 
I decided to run for free argostranslate.

Need to Improve
1. Adding more lang
2. make it faster (like MP)
3. when saving data - save only the translation. 
4. add config file
5. check if work in parallel with several pc


Requirements:
Python 3.12
key for google.generativeai