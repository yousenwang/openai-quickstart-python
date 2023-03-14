from googletrans import Translator

translator = Translator()


res = translator.translate(
    "I love you.",
    dest='zh-tw'
    )

print(res)

# Translated(src=en, dest=zh-tw, text=我愛你。, pronunciation=Wǒ ài nǐ., extra_data="{'confiden...")
