from moviepy.editor import *

screensize = (360, 640)


def writeText(text):
    return TextClip(txt=text, color='yellow', stroke_color='black', stroke_width=.2, font="Noto-Color-Emoji", fontsize=24)


cvc = CompositeVideoClip(
    [
        writeText("Duvido você adivinhar a").set_position(
            ("center", 100)),
        writeText("música só com os emojis").set_position(
            ("center", 140)),
        writeText("😀 😃 ").set_position("center", 250)
    ],
    size=screensize
).set_duration(10).on_color(color=(255, 255, 255))

print(TextClip.list("font"))

cvc.write_videofile("teste.mp4", fps=5)
