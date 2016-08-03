from django.shortcuts import render
from django.shortcuts import redirect


from matrix.python.samples.samplebase import SampleBase
from matrix.python.samples.rgbmatrix import graphics

import time

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def Run(self):
        offscreenCanvas = self.matrix.CreateFrameCanvas()
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
            offscreenCanvas = self.matrix.SwapOnVSync(offscreenCanvas)




def show_page(request) :
    if not request.user.is_authenticated():
        return redirect('/login')
    parser = RunText()
    if (not parser.process()):
        parser.print_help()
    return render(request, 'map.html')





