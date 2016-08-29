from django.shortcuts import render
from django.shortcuts import redirect

import sys
sys.path.append('/home/pi/mainserver/matrix/python/samples')


# from samplebase import SampleBase


import time

# class RunText(SampleBase):
#     def __init__(self, *args, **kwargs):
#         super(RunText, self).__init__(*args, **kwargs)
#
#
#
#
# """
# from .core import RGBMatrix, FrameCanvas
# import graphics
# import time
#
#
# def RunText():
#     matrix = RGBMatrix(32, 6, 1)
#     matrix.pwmBits = 11
#     matrix.brightness = 100
#
#     offscreenCanvas = matrix.CreateFrameCanvas()
#
#
#     font = graphics.Font()
#
#     font.LoadFont("../matrix/fonts/7x13.bdf")
#
#     textColor = graphics.Color(255, 255, 0)
#
#     pos = offscreenCanvas.width
#     myText = "Hello World!"
#
#
#     while True:
#         offscreenCanvas.Clear()
#         len = graphics.DrawText(offscreenCanvas, font, pos, 10, textColor, myText)
#         pos -= 1
#         if (pos + len < 0):
#             pos = offscreenCanvas.width
#         time.sleep(0.05)
#         offscreenCanvas = matrix.SwapOnVSync(offscreenCanvas)
#
# import threading
# import thread
# def worker():
#     print "in worker"
#     parser = SimpleSquare()
#     if (not parser.process()):
#         parser.print_help()
#
#
# def SimpleSquare():
#     matrix = RGBMatrix(32, 6, 1)
#     matrix.pwmBits = 11
#     matrix.brightness = 100
#
#     offsetCanvas = matrix.CreateFrameCanvas()
#     while True:
#         for x in range(0, matrix.width):
#             offsetCanvas.SetPixel(x, x, 255, 255, 255)
#             offsetCanvas.SetPixel(offsetCanvas.height - 1 - x, x, 255, 0, 255)
#
#         for x in range(0, offsetCanvas.width):
#             offsetCanvas.SetPixel(x, 0, 255, 0, 0)
#             offsetCanvas.SetPixel(x, offsetCanvas.height - 1, 255, 255, 0)
#
#         for y in range(0, offsetCanvas.height):
#             offsetCanvas.SetPixel(0, y, 0, 0, 255)
#             offsetCanvas.SetPixel(offsetCanvas.width - 1, y, 0, 255, 0)
#         offsetCanvas = matrix.SwapOnVSync(offsetCanvas)
#
#
# def RunGraphics():
#
#     matrix = RGBMatrix(32, 6, 1)
#     matrix.pwmBits = 11
#     matrix.brightness = 100
#     canvas = matrix;
#     font = graphics.Font()
#     font.LoadFont("4x6.bdf")
#
#     red = graphics.Color(255, 0, 0)
#     graphics.DrawLine(canvas, 5, 5, 22, 13, red)
#
#     green = graphics.Color(0, 255, 0)
#     graphics.DrawCircle(canvas, 15, 15, 10, green)
#
#     blue = graphics.Color(0, 0, 255)
#     graphics.DrawText(canvas, font, 2, 10, blue, "Text")
#
#     time.sleep(10)  # show display for 10 seconds before exit
#
#     """
import threading
from django.http import HttpResponse
def show_page(request) :
    #parser = RunText()
    #if (not parser.process()):
    #    parser.print_help()
    if not request.user.is_authenticated():
        return redirect('/login')
    #threading.Thread(target=worker).start()
    #RunText()
    if request.method == "GET":
        return render(request, 'map.html')
    else:
        import os,logging
        text = request.POST['text']
        def run_bash():
            os.system("sudo ps aux | grep 'text-example'  | awk '{print $2}' | xargs kill -9")
            time.sleep(1)
            os.system("(while :; do echo '%s' ; sleep 0.2 ; done) | sudo /home/pi/LED-Sign-Controller/text-example -f /home/pi/LED-Sign-Controller/fonts/8x13B.bdf -y8 -c2 -C0,0,255 -c12 -r16h -b10 " % text)
        t = threading.Thread(target=run_bash)
        t.start()
        #time.sleep(10)
        #os.system("sudo ps aux | grep 'text-example'  | awk '{print $2}' | xargs kill -9" )
        return HttpResponse("done")





