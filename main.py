from moviepy.editor import *
from gtts import gTTS
from youtube_dl import YoutubeDL


def writeText(text, size):
    return TextClip(txt=text, color='black', stroke_width=.2, font="Segoe-UI-Emoji", fontsize=size)

# Save audio in ./assets/musica.mp3


def getAudio(url):
    audio_downloader = YoutubeDL(
        {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }],
            "outtmpl": "./assets/musica.mp3"
        }
    )
    audio_downloader.extract_info(url)


url = "https://www.youtube.com/watch?v=g6J77jc3Bzg"
getAudio(url)

screensize = (360, 640)
fontSize = 32

frase = "Duvido você adivinhar a música só com os emojis"
emojis = "🪒 🧼 🗻 🐸"

tts = gTTS((frase + emojis), lang='pt', tld='com.br')
tts.save('./assets/1.mp3')

music = concatenate_audioclips([AudioFileClip("./assets/"+"1.mp3"), AudioFileClip(
    "./assets/"+"silence.mp3"), AudioFileClip("./assets/"+"musica.mp3").subclip(62, 72)])

cvc = CompositeVideoClip(
    [
        writeText("Duvido você adivinhar a", fontSize).set_position(
            ("center", 100)),
        writeText("música só com os emojis", fontSize).set_position(
            ("center", 140)),
        writeText(emojis, fontSize).set_position("center", 350)
    ],
    size=screensize
).set_duration(15).on_color(color=(255, 255, 255)).set_audio(music)

cvc.write_videofile("teste.mp4", fps=5)
