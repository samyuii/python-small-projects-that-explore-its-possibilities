# translation APIs = Google Translate API
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    text_to_translate = input("Enter the text to translate: ")
    target_language = input("Enter the target language: ")
    translated_text = translate_text(text_to_translate, target_language)
    print("Translated Text:", translated_text)
