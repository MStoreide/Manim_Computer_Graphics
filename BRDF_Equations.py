from manim import *

#Colorlab Intro

class ReflectionModels(Scene):
    def construct(self):
        formula = MathTex(r"f_{r,s}(\omega^\rightharpoonup _i ,\omega^\rightharpoonup _r) = k_s(\omega^\rightharpoonup _r.R^\rightharpoonup _{\omega i})^n = k_s(\cos \alpha)^n")
        label = Text("Phong Reflection Model")
        label.next_to(formula, UP, buff=0.5)
        self.play(Write(label), run_time=1)
        self.wait()
        self.play(Write(formula), run_time=1.5) 
        self.wait(2)
        

#Complete Phong

        formula2 = MathTex(r"f_{r,P} = [k_a + k_d (n^\rightharpoonup . \omega^\rightharpoonup _i) + k_s (\omega^\rightharpoonup _r . R^\rightharpoonup _{\omega i})^n] \frac{L_i}{r^2}")
        label2 = Text("Complete Phong Reflection Model")
        label2.next_to(formula2, UP, buff=0.5)
        self.play(Write(label2), run_time=1)
        self.wait()
        self.play(Write(formula2), run_time=1.5) 
        self.wait()

#Flat Gouraud Phong

        Flabel = Text("Flat shading: One surface normal, hence one color for each polygon")
        Glabel = Text("Gouraud shading: Color for each point is computed by interpolating the color of the vertices")
        Plabel = Text("Phong shading: Surface normal at each point is interpolated and used to compute the color of each point")
        Glabel.next_to(Flabel, DOWN, buff=0.5)
        Plabel.next_to(Glabel, DOWN, buff=0.5)

#Then visualize the same as on slide 14 of the Reflection Models

#Blinn-Phong

        formula = MathTex(r"f_{r,BP}(\omega _i,\omega _r) = k_s(n.h)^n")
        label = Text("Blinn-Phong Reflection Model")
        label.next_to(formula, UP, buff=0.5)

# Ward

        formula = MathTex(r"f_r,_W(\omega _i, \omega _r) = \frac{\rho _d}{\pi} + \frac{\rho _d}{\sqrt{\cos(\theta _i) \cos (\theta _r)})} . \frac{e^{\tan^2 (\frac{\theta _h}{\alpha^2})}}{4 \pi \alpha^2}")
        label = Text("Ward Reflection Model")
        label.next_to(formula, UP, buff=0.5)

# Cook-Torrance

        formula = MathTex(r"f_{r,s}(\omega _i, \omega _r) = \frac{F(\theta _r)D(h)G(\omega _i, \omega _r)}{\pi \cos (\theta _r) \cos(\theta _i)}")
        label = Text("Cook-Torrance Reflection Model")
        label.next_to(formula, UP, buff=0.5)

# Cook-Torrance Elements

        formula1 = Tex(r"D(h) = \frac{1}{4m^2 \cos^4 \theta _h} exp(- \frac{\tan \theta _h}{m})^2")
        formula2 = Tex(r"G(\omega _i, \omega _r) = min(1, \frac{2(n.h)(n.\omega _r)}{\omega _r.h}, \frac{2(n.h)(n.\omega _i)}{\omega _r.h})")
        formula2.next_to(formula1, DOWN, buff=0.5)
        formula3 = Tex(r"F(\theta _r) = \frac{(g-c)^2}{2(g+c)^2}(1+\frac{(c(g+c)-1)^2}{(c(g-c)+1)^2})") #c = \omega _r.h #g = \eta^2 + c^2 -1
        formula3.next_to(formula2, DOWN, buff=0.5)

