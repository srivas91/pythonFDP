from translate import Translator
translator= Translator(to_lang="hi")
translation = translator.translate("This is a pen.")
print(translation)