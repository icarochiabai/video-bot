from moviepy.editor import *
from gtts import gTTS



screensize = (360, 640)
fontSize = 32

def writeText(text,size):
    return TextClip(txt=text, color='black', stroke_width=.2, font="Segoe-UI-Emoji", fontsize=size)

make_frame = lambda t: 0 


tts = gTTS("Duvido você adivinhar a música só com os emojis",lang='pt', tld='com.br',)
tts.save('./assets/1.mp3')


music = concatenate_audioclips([AudioFileClip("./assets/"+"1.mp3"),AudioFileClip("./assets/"+"sapo.mp3").subclip(62,72)])

cvc = CompositeVideoClip(
    [
        writeText("Duvido você adivinhar a",fontSize).set_position(
            ("center", 100)),
        writeText("música só com os emojis",fontSize).set_position(
            ("center", 140)),
        writeText("🪒 🧼 🗻 🐸",fontSize).set_position("center", 350)
    ],
    size=screensize
).set_duration(15).on_color(color=(255, 255, 255)).set_audio(music)

# print(TextClip.list("font"))

cvc.write_videofile("teste.mp4", fps=5)
