import os
from gtts import gTTS

text = ""
language = "en"

output = gTTS(text=text, lang=language, slow=False)
output.save("speech.mp3")
