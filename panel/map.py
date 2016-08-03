from django.shortcuts import render
from django.shortcuts import redirect


from matrix.python.rgbmatrix import graphics
from matrix.python.rgbmatrix import RGBMatrix


import time


def Run():
    matrix = RGBMatrix(32, 1, 1)
    matrix.pwmBits = 11
    matrix.brightness = 100
    offscreenCanvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("../../fonts/7x13.bdf")
    textColor = graphics.Color(255, 255, 0)
    pos = offscreenCanvas.width
    myText = "Hello World!"

    while True:
        offscreenCanvas.Clear()
        len = graphics.DrawText(offscreenCanvas, font, pos, 10, textColor, myText)
        pos -= 1
        if (pos + len < 0):
            pos = offscreenCanvas.width

        time.sleep(0.05)
        offscreenCanvas = matrix.SwapOnVSync(offscreenCanvas)




def show_page(request) :
    if not request.user.is_authenticated():
        return redirect('/login')
    Run()
    return render(request, 'map.html')





