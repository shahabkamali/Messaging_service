import argparse, time, sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix
from rgbmatrix import graphics

class SampleBase(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(SampleBase, self).__init__(*args, **kwargs)

        self.add_argument("-t", "--text", action="store",help="text", default="Hello World", type=str)

        self.args = {}

    def usleep(self, value):
        time.sleep(value / 1000000.0)

    def Run(self):
        offscreenCanvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreenCanvas.width

        myText = self.args["text"]

        while True:
            offscreenCanvas.Clear()
            len = graphics.DrawText(offscreenCanvas, font, pos, 10, textColor, myText)
            pos -= 1
            if (pos + len < 0):
                pos = offscreenCanvas.width

            time.sleep(0.05)
            offscreenCanvas = self.matrix.SwapOnVSync(offscreenCanvas)

    def process(self):
        self.args = vars(self.parse_args())


        self.matrix = RGBMatrix(32, 6, 1)
        self.matrix.pwmBits = 11
        self.matrix.brightness = 100


        try:
            # Start loop
            print("Press CTRL-C to stop sample")
            self.Run()
        except KeyboardInterrupt:
            print "Exiting\n"
            sys.exit(0)

        return True