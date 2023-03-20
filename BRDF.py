from manim import *
import numpy as np

#Colorlab Intro

class ReflectionModels(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E

# Intro

        colorlab = ImageMobject("/home/markus/Manim_Computer_Graphics/Manim_Computer_Graphics/Logos/CLsmall.png/").move_to([3,0.5,0])
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

# Title
            
        title = Text("3D Objects")
        title.scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(Unwrite(title, reverse=False))
        self.wait()


# Phong

        phong = MathTex(r"f_{r,s}(\omega^\leftharpoonup _i ,\omega^\leftharpoonup _r) = k_s(\omega^\leftharpoonup _r.R^\leftharpoonup _{\omega i})^n = k_s(\cos \alpha)^n")
        plabel = Text("Phong Reflection Model")
        plabel.next_to(phong, UP, buff=0.5)
        self.play(Write(plabel), run_time=1)
        self.wait()
        self.play(Write(phong), run_time=1.5) 
        self.wait(2)

        self.play(FadeOut(phong, plabel))
        

# Complete Phong

        cphong = MathTex(r"f_{r,P} = [k_a + k_d (n^\leftharpoonup . \omega^\leftharpoonup _i) + k_s (\omega^\leftharpoonup _r . R^\leftharpoonup _{\omega i})^n] \frac{L_i}{r^2}")
        cplabel = Text("Complete Phong Reflection Model")
        cplabel.next_to(phong, UP, buff=0.5)
        self.play(Write(cplabel), run_time=1)
        self.wait()
        self.play(Write(cphong, run_time=1.5))
        self.wait()
        self.play(FadeOut(cphong, cplabel))
        self.wait()

# Flat Gouraud Phong

        Flabel = Text("Flat shading: One surface normal, hence one color for each polygon")
        Glabel = Text("Gouraud shading: Color for each point is computed by interpolating the color of the vertices")
        Plabel = Text("Phong shading: Surface normal at each point is interpolated and used to compute the color of each point")
        Glabel.next_to(Flabel, DOWN, buff=0.5)
        Plabel.next_to(Glabel, DOWN, buff=0.5)

#Then visualize the same as on slide 14 of the Reflection Models

        gouraudsurface = Graph([1, 2], [(1, 2)],
                layout={1: [-4, -2, 0], 2: [4, -2, 0]}
                )
        self.play(Create(gouraudsurface), run_time=3)
        self.wait(2)

        normalarrow = Arrow(np.array([0, -2, 0]), np.array([0, 2, 0]))

        self.play(GrowArrow(normalarrow))
        self.wait(2)
        self.play(FadeOut(normalarrow))

        gouraudarrowl = Arrow(np.array([-4, -2, 0]), np.array([-6, 2, 0]))
        gouraudarrowr = Arrow(np.array([4, -2, 0]), np.array([6, 2, 0]))

        self.play(GrowArrow(gouraudarrowr), GrowArrow(gouraudarrowl))
        self.wait(2)

        interpolation = CurvedArrow(np.array([-2, 0, 0]), np.array([2, 0, 0]), radius = -5)
        self.play(FadeIn(interpolation))
        self.wait()

        phongarrows = [
                Arrow(np.array([-3, -2, 0]), np.array([-4.5, 2.7, 0])),
                Arrow(np.array([-2, -2, 0]), np.array([-3, 3.3, 0])),
                Arrow(np.array([-1, -2, 0]), np.array([-1.5, 3.6, 0])),
                Arrow(np.array([0, -2, 0]), np.array([0, 3.8, 0])),
                Arrow(np.array([1, -2, 0]), np.array([1.5, 3.6, 0])),
                Arrow(np.array([2, -2, 0]), np.array([3, 3.3, 0])),
                Arrow(np.array([3, -2, 0]), np.array([4.5, 2.7, 0]))
        ]

        self.play(GrowArrow(phongarrows[0]),
                GrowArrow(phongarrows[1]),
                GrowArrow(phongarrows[2]),
                GrowArrow(phongarrows[3]),
                GrowArrow(phongarrows[4]),
                GrowArrow(phongarrows[5]),
                GrowArrow(phongarrows[6]), 
        )
        self.wait(2)

        self.play(FadeOut(gouraudarrowl, gouraudarrowr))
        self.wait()


