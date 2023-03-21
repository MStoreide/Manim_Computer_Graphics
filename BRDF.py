from manim import *
import numpy as np

# Split all of these BRDF into separate videos?

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
        colorlabcorner = ImageMobject("/home/markus/Manim_Computer_Graphics/Manim_Computer_Graphics/Logos/CLsmall.png/").to_corner(DOWN + RIGHT)
        colorlabcorner.scale(0.5)
        NTNU = ImageMobject(f"/home/markus/Manim_Computer_Graphics/Manim_Computer_Graphics/NTNU.png").move_to([0, 2, 0])
        NTNU.scale(0.3)
        NTNUcorner = ImageMobject(f"/home/markus/Manim_Computer_Graphics/Manim_Computer_Graphics/NTNU.png").to_corner(DOWN + LEFT)
        NTNUcorner.scale(0.2)

        self.wait()

        self.play(FadeIn(colorlab, shift=RIGHT*2), FadeIn(NTNU, shift=RIGHT*2), Write(colorlabtext, shift=LEFT*2), Write(cg, run_time=0.7))
        self.wait(1)

        self.play(Transform(colorlab, colorlabcorner), Transform(NTNU, NTNUcorner), Unwrite(colorlabtext, shift=RIGHT), Unwrite(cg, run_time=0.7))

        self.wait()

# Title
            
        title = Text("Reflection Models")
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

        Flabel = Text("Flat shading: One surface normal, hence one color for each polygon", font_size=25, t2c={'[:13]':BLUE_E}).move_to([0, -2.6, 0])
        Glabel = Text("Gouraud shading: Color for each point \n is computed by interpolating the color of the vertices", font_size=25, t2c={'[:16]':GREEN_E}).move_to([0, -2.8, 0])
        Plabel = Text("Phong shading: Surface normal at each \n point is interpolated and used to compute \n the color of each point", font_size=25, t2c={'[:14]':RED_E}).move_to([0, -3, 0])

        gouraudsurface = Graph([1, 2], [(1, 2)],
                layout={1: [-4, -2, 0], 2: [4, -2, 0]}
                )
        self.play(Create(gouraudsurface), run_time=3)
        self.wait(2)

        normalarrow = Arrow(np.array([0, -2, 0]), np.array([0, 2, 0]))

        self.play(GrowArrow(normalarrow), Write(Flabel))
        self.wait(2)
        self.play(FadeOut(normalarrow))

        gouraudarrowl = Arrow(np.array([-4, -2, 0]), np.array([-6, 2, 0]))
        gouraudarrowr = Arrow(np.array([4, -2, 0]), np.array([6, 2, 0]))

        self.play(GrowArrow(gouraudarrowr), GrowArrow(gouraudarrowl))
        self.wait(2)

        interpolation = CurvedArrow(np.array([-2, 0, 0]), np.array([2, 0, 0]), radius = -5)
        self.play(FadeIn(interpolation), Transform(Flabel, Glabel))

        self.wait(4)

        phongarrows = [
                Arrow(np.array([-3, -2, 0]), np.array([-4.5, 2.7, 0]), stroke_width=2),
                Arrow(np.array([-2, -2, 0]), np.array([-3, 3.3, 0]), stroke_width=2),
                Arrow(np.array([-1, -2, 0]), np.array([-1.5, 3.6, 0]), stroke_width=2),
                Arrow(np.array([0, -2, 0]), np.array([0, 3.8, 0]), stroke_width=2),
                Arrow(np.array([1, -2, 0]), np.array([1.5, 3.6, 0]), stroke_width=2),
                Arrow(np.array([2, -2, 0]), np.array([3, 3.3, 0]), stroke_width=2),
                Arrow(np.array([3, -2, 0]), np.array([4.5, 2.7, 0]), stroke_width=2)
        ]
        self.play(FadeOut(interpolation), Transform(Flabel, Plabel))
        self.play(GrowArrow(phongarrows[0]),
                GrowArrow(phongarrows[1]),
                GrowArrow(phongarrows[2]),
                GrowArrow(phongarrows[3]),
                GrowArrow(phongarrows[4]),
                GrowArrow(phongarrows[5]),
                GrowArrow(phongarrows[6]), 
        )
        self.wait(2)

        self.play(FadeOut(gouraudarrowl, gouraudarrowr, gouraudsurface, Flabel, phongarrows[0], phongarrows[1], phongarrows[2], phongarrows[3], phongarrows[4], phongarrows[5], phongarrows[6]))
        self.wait()

# List all shadings next to each other here. 

        Flabel2 = Text("Flat shading: One surface normal, hence one color for each polygon", font_size=20, t2c={'[:13]':BLUE_E}).move_to([-1.5, 3, 0])
        Glabel2 = Text("Gouraud shading: Color for each point \n is computed by interpolating the color of the vertices", font_size=20, t2c={'[:16]':GREEN_E}).next_to(Flabel2, DOWN, buff=1)
        Plabel2 = Text("Phong shading: Surface normal at each \n point is interpolated and used to compute \n the color of each point", font_size=20, t2c={'[:14]':RED_E}).next_to(Glabel2, DOWN, buff=1)

        labels = VGroup(Flabel2, Glabel2, Plabel2)

        self.play(Write(labels))
        
       # self.play(Transform(Flabel, Plabel2), Write(Flabel2), Write(Glabel2))
        self.wait()

# Fix text positioning, add small examples for each approach
# Find renders/images as examples as well.