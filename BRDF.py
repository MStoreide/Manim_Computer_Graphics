from manim import *

#Colorlab Intro

class ReflectionModels(Scene):
    def construct(self):
            self.camera.background_color = GRAY_E

# Intro

            colorlab = ImageMobject(r"/Logos/CLsmall.png").move_to([3,0.5,0])
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

            phong = MathTex(r"f_{r,s}(\omega^\rightharpoonup _i ,\omega^\rightharpoonup _r) = k_s(\omega^\rightharpoonup _r.R^\rightharpoonup _{\omega i})^n = k_s(\cos \alpha)^n")
            plabel = Text("Phong Reflection Model")
            plabel.next_to(phong, UP, buff=0.5)
            self.play(Write(plabel), run_time=1)
            self.wait()
            self.play(Write(phong), run_time=1.5) 
            self.wait(2)
        

#Complete Phong

            cphong = MathTex(r"f_{r,P} = [k_a + k_d (n^\rightharpoonup . \omega^\rightharpoonup _i) + k_s (\omega^\rightharpoonup _r . R^\rightharpoonup _{\omega i})^n] \frac{L_i}{r^2}")
            cplabel = Text("Complete Phong Reflection Model")
            cplabel.next_to(phong, UP, buff=0.5)
            self.play(Write(cplabel), run_time=1)
            self.wait()
            self.play(Write(cphong, run_time=1.5))
            self.wait()

#Flat Gouraud Phong

            Flabel = Text("Flat shading: One surface normal, hence one color for each polygon")
            Glabel = Text("Gouraud shading: Color for each point is computed by interpolating the color of the vertices")
            Plabel = Text("Phong shading: Surface normal at each point is interpolated and used to compute the color of each point")
            Glabel.next_to(Flabel, DOWN, buff=0.5)
            Plabel.next_to(Glabel, DOWN, buff=0.5)

#Then visualize the same as on slide 14 of the Reflection Models

            gouraudsurface = Graph([1, 2], [(1, 2)],
                    layout={1: [-4, 0, 0], 2: [4, 0, 0]}
                    )
            self.play(Create(surface), run_time=3)
            self.wait(2)

            normalarrow = Arrow(0, 2 * UP)

            self.play(GrowArrow(normalarrow))
            self.wait(2)
            self.play(FadeOut(normalarrow))

            gouraudarrowl = Arrow(-4, 2 * UL)
            gouraudarrowr = Arrow(4, 2 * UR)

            #phongarrows = 

#Blinn-Phong

            blinnphong = MathTex(r"f_{r,BP}(\omega _i,\omega _r) = k_s(n.h)^n")
            label = Text("Blinn-Phong Reflection Model")
            label.next_to(blinnphong, UP, buff=0.5)

# Ward

            ward = MathTex(r"f_r,_W(\omega _i, \omega _r) = \frac{\rho _d}{\pi} + \frac{\rho _d}{\sqrt{\cos(\theta _i) \cos (\theta _r)})} . \frac{e^{\tan^2 (\frac{\theta _h}{\alpha^2})}}{4 \pi \alpha^2}")
            label = Text("Ward Reflection Model")
            label.next_to(ward, UP, buff=0.5)

# Cook-Torrance

            cooktorrance = MathTex(r"f_{r,s}(\omega _i, \omega _r) = \frac{F(\theta _r)D(h)G(\omega _i, \omega _r)}{\pi \cos (\theta _r) \cos(\theta _i)}")
            ctlabel = Text("Cook-Torrance Reflection Model")
            ctlabel.next_to(cooktorrance, UP, buff=0.5)

# Cook-Torrance Elements

            ct1 = Tex(r"D(h) = \frac{1}{4m^2 \cos^4 \theta _h} exp(- \frac{\tan \theta _h}{m})^2")
            ct2 = Tex(r"G(\omega _i, \omega _r) = min(1, \frac{2(n.h)(n.\omega _r)}{\omega _r.h}, \frac{2(n.h)(n.\omega _i)}{\omega _r.h})")
            ct2.next_to(ct1, DOWN, buff=0.5)
            ct3 = Tex(r"F(\theta _r) = \frac{(g-c)^2}{2(g+c)^2}(1+\frac{(c(g+c)-1)^2}{(c(g-c)+1)^2})") #c = \omega _r.h #g = \eta^2 + c^2 -1
            ct3.next_to(ct2, DOWN, buff=0.5)

