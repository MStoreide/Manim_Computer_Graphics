from manim import *

class Software(Scene):
    def construct(self):

#Intro

        colorlab = ImageMobject("CLsmall.png").move_to([3,0.5,0])
        colorlab.scale(2)
        colorlabtext = Text("Colourlab").move_to([-1,0,0])
        colorlabtext.scale(2)
        cg = Text("IDIG4002 - Computer Graphics").move_to([0,-1,0])
        cg.scale(0.5)

        #ntnu = ImageMobject(NTNULOGO)

        self.wait()

        self.play(FadeIn(colorlab, shift=RIGHT*2), Write(colorlabtext, shift=LEFT*2), Write(cg, run_time=0.7))
        self.wait(1)

        self.play(FadeOut(colorlab, shift=LEFT), Unwrite(colorlabtext, shift=RIGHT), Unwrite(cg, run_time=0.7))

        self.wait()