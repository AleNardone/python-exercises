from translate import Translator

translator = Translator(from_lang="english", to_lang="german")
translation = translator.translate("Hello, how are you?")
print(translation)
