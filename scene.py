#Phong Model

from manim import * 

class PhongBRDFModel(Scene):
    def construct(self):
        formula = MathTex(r"fr,s(wi, wr)")
        self.play(Write(formula), run_time=3)
        self.wait
        