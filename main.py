from moviepy.editor import *
from gtts import gTTS

screensize = (360, 640)

def writeText(text,fontSize = 32,size=None):
    
    a = TextClip(txt=text, color='black', stroke_width=.2, font="Segoe-UI-Emoji", fontsize=fontSize, size=size)
    return a


emojis = "🪒 🧼 🗻 🐸"

tts = gTTS(("Duvido você adivinhar a música só com os emojis"),lang='pt', tld='com.br',slow=1)
tts.save('./assets/1.mp3')
tts2 = gTTS((emojis),lang='pt', tld='com.br',)
tts2.save('./assets/2.mp3')


music = concatenate_audioclips([AudioFileClip("./assets/"+"1.mp3"),AudioFileClip("./assets/"+"2.mp3"), AudioFileClip("./assets/"+"silence.mp3") ,AudioFileClip("./assets/"+"sapo.mp3").subclip(60,75),])

firstClip = CompositeVideoClip(
    [
        writeText("Duvido você adivinhar a").set_position(
            ("center", 100)),
        writeText("música só com os emojis").set_position(
            ("center", 140)),
        writeText(emojis,fontSize=50,size=[321, 65]).set_position("center", 350)
    ],
    size=screensize
).set_duration(music.duration).on_color(color=(255, 255, 255)).set_audio(music)

counter = [firstClip]
for x in range(5,0,-1):
    counter.append(CompositeVideoClip([writeText(str(x),fontSize=50).set_position("center",500)],size=screensize).set_duration(1).on_color(color=(255, 255, 255)))
    
finalClip = concatenate_videoclips(counter)
finalClip.write_videofile("teste.mp4", fps=30)
