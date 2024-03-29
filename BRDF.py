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
        colorlabcorner = ImageMobject("/home/markus/Manim_Computer_Graphics/Manim_Computer_Graphics/Logos/CLsmall.png/").to_corner(DOWN + RIGHT)
        colorlabcorner.scale(0.5)
        NTNU = ImageMobject(f"/home/markus/Manim_Computer_Graphics/Manim_Computer_Graphics/NTNU.png").move_to([0, 2, 0])
        NTNU.scale(0.3)
        NTNUcorner = ImageMobject(f"/home/markus/Manim_Computer_Graphics/Manim_Computer_Graphics/NTNU.png").move_to([-5, -3, 0])
        NTNUcorner.scale(0.2)

        self.wait()

        self.play(FadeIn(colorlab, shift=RIGHT*2), FadeIn(NTNU, shift=RIGHT*2), Write(colorlabtext, shift=LEFT*2), Write(cg, run_time=0.7))
        self.wait(2)

        self.play(Transform(colorlab, colorlabcorner), Transform(NTNU, NTNUcorner), Unwrite(colorlabtext, shift=RIGHT), Unwrite(cg, run_time=0.7))

        self.wait()

# Title
            
        title = Text("Reflection Models")
        title.scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(Unwrite(title, reverse=False))
        self.play(FadeOut(colorlab, NTNU))
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
        #self.play(Write(cplabel), run_time=1)
        #self.wait()
        #self.play(Write(cphong, run_time=1.5))
        #self.wait()
        #self.play(FadeOut(cphong, cplabel))
        #self.wait()

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

        self.play(GrowArrow(gouraudarrowr), GrowArrow(gouraudarrowl), Transform(Flabel, Glabel))
        self.wait(2)

        interpolation = CurvedArrow(np.array([-2, 0, 0]), np.array([2, 0, 0]), radius = -5)
        self.play(FadeIn(interpolation))

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

        Flabel2 = Text("Flat shading: One polygon color", font_size=20, t2c={'[:13]':BLUE_E}).move_to([-4, 3, 0])
        Glabel2 = Text("Gouraud shading: Color interpolated from vertex color", font_size=20, t2c={'[:16]':GREEN_E}).next_to(Flabel2, DOWN, buff=2, aligned_edge=LEFT) 
        Plabel2 = Text("Phong shading: Surface normal is interpolated \n over the polygon", font_size=20, t2c={'[:14]':RED_E}).next_to(Glabel2, DOWN, buff=2, aligned_edge=LEFT)

        labels = VGroup(Flabel2, Glabel2, Plabel2)

# Small versions of reflections

       # gouraudsurface.scale(0.5), normalarrow.scale(0.5)
        smallflat = VGroup(gouraudsurface, normalarrow).move_to([4, 3, 0])
        smallflat.scale(0.3)

        gouraudsurface1 = Graph([1, 2], [(1, 2)],
                layout={1: [-4, -2, 0], 2: [4, -2, 0]}
        )
        smallgouraud = VGroup(gouraudsurface1, gouraudarrowl, gouraudarrowr, interpolation).move_to([4, 1, 0])
        smallgouraud.scale(0.3)

        gouraudsurface2 = Graph([1, 2], [(1, 2)],
                layout={1: [-4, -2, 0], 2: [4, -2, 0]}
        )
        gouraudarrowl2 = Arrow(np.array([-4, -2, 0]), np.array([-6, 2, 0]))
        gouraudarrowr2 = Arrow(np.array([4, -2, 0]), np.array([6, 2, 0]))

        smallphong = VGroup(gouraudsurface2, 
                        gouraudarrowl2, 
                        gouraudarrowr2, 
                        phongarrows[0], 
                        phongarrows[1], 
                        phongarrows[2], 
                        phongarrows[3], 
                        phongarrows[4], 
                        phongarrows[5], 
                        phongarrows[6]).move_to([4, -1, 0])
        smallphong.scale(0.3)

        self.play(Write(labels), Create(smallflat), Create(smallgouraud), Create(smallphong))
        
        self.wait(2)

        self.play(FadeOut(smallflat, smallgouraud, smallphong, labels))

# Fix text positioning, add small examples for each approach
# Find renders/images as examples as well.


# Outro and contact

        outrocolor = Text("Colourlab", font_size=30, weight=BOLD).move_to([0, 3, 0])
        outrocg = Text("IDIG4002 - Computer Graphics", font_size=20).next_to(outrocolor, DOWN)
        contact = Text("Contact:", font_size=30, weight=BOLD)
        contact2 = Text("Markus Storeide", font_size=20).next_to(contact, DOWN)
        contact3 = Text("markus.s.b.storeide@ntnu.no", font_size=20).next_to(contact2, DOWN)
        self.play(Write(outrocolor), Write(outrocg), Write(contact), Write(contact2), Write(contact3), FadeIn(NTNU, colorlab))
        self.wait(6)
        self.play(FadeOut(contact, contact2, contact3, outrocg, outrocolor, NTNU, colorlab))

