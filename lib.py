from distutils.command.upload import upload
from moviepy.editor import *
from gtts import gTTS
from youtube_dl import YoutubeDL
from upload_video import *


def writeText(text, fontSize=28, size=None):
    return TextClip(txt=text, color='black', stroke_width=.2, font="Segoe-UI-Emoji", fontsize=fontSize, size=size)


def getVideo(url):
    with YoutubeDL(
        {
            'format': '18',
            'outtmpl': './assets/musica.%(ext)s',
        }
    ) as ydl:
        ydl.download([url])


def speak(frase, name, speed=None):
    tts = gTTS(
        (frase),
        lang='pt',
        tld='com.br',
        slow=speed
    )

    tts.save('./assets/tts' + name + '.mp3')



def uploadYt(file,title,description,categorieId,keywords):
    #24 = 
    args = f"Namespace(file='{file}', title='{title}', description='{description}', category='{categorieId}', keywords='{keywords}', privacyStatus='private')"
    
    upload(file,title,description,categorieId,keywords)

    
