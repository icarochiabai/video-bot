from lib import *


url = 'https://www.youtube.com/watch?v=g6J77jc3Bzg'
info = getVideo(url)

videoStart = 60
videoDuration = 5

screensize = (360, 640)

frase = "Duvido você adivinhar a música só com os emojis"
emojis = "🪒 🧼 🗻 🐸"

speak(frase, 'Frase', 1)
speak(emojis, 'Emojis')

totalAudio = concatenate_audioclips(
    [AudioFileClip("./assets/ttsFrase.mp3"),
     AudioFileClip("./assets/ttsEmojis.mp3"),
     AudioFileClip("./assets/silence.mp3"),
     ]
)


startCounter = 8

firstClip = CompositeVideoClip(
    [
        writeText("Duvido você adivinhar a").set_position(
            ("center", 100)).set_start(0.5),
        writeText("música só com os emojis").set_start(2).set_position(
            ("center", 140)),
        writeText(emojis, fontSize=50, size=[
                  321, 65]).set_start(5).set_position("center", 350),
        writeText("5").set_start(
            startCounter).set_end(startCounter + 1).set_position(("center", 500)),
        writeText("4").set_start(
            startCounter + 1).set_end(startCounter + 2).set_position(("center", 500)),
        writeText("3").set_start(
            startCounter + 2).set_end(startCounter + 3).set_position(("center", 500)),
        writeText("2").set_start(
            startCounter + 3).set_end(startCounter + 4).set_position(("center", 500)),
        writeText("1").set_start(
            startCounter + 4).set_end(startCounter + 5).set_position(("center", 500))
    ],
    size=screensize
).set_duration(totalAudio.duration).on_color(color=(255, 255, 255)).set_audio(totalAudio).set_fps(24)

musicClip = VideoFileClip(
    "./assets/musica.mp4").subclip(videoStart, videoStart + videoDuration).resize(screensize)

finalClip = concatenate_videoclips(
    [
        firstClip,
        musicClip.set_position("center")
    ]
)

finalClip.write_videofile("teste.mp4", fps=24)
