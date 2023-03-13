from manim import *

#Colorlab Intro

class PhongReflectionModel(Scene):
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

