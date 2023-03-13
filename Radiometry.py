from manim import *

#Colorlab Intro

class Radiometry(Scene):
    def construct(self):

        #Colorlab Intro

        radiance = MathTex(r"L(x,\omega) \equiv \frac{dI(x \omega)}{dA} = \frac{d^2 \Phi (x, \omega)}{d \omega dA}")
        self.play(Write(radiance, run_time=2))
        self.wait()

        self.play(FadeOut(radiance))

        self.wait()

        irradiance = MathTex(r"E(x) = lim _{\Delta A \to 0} \frac{\Delta \Phi}{\Delta A} = \frac{d \Phi}{dA}")
        formula2 = MathTex(r"E(x, \omega) = L(x, \omega) \cos \theta d\omega") 
        formula2.next_to(irradiance, DOWN, buff=0.5) #It does not like this for some reason.
        self.play(Write(irradiance, formula2, run_time=2))
        self.wait()


 #       inversesquarelaw = MathTex(r"E \propto \frac{1}{r^2}")

 #       lambert = MathTex(r"E(x) +propto \Phi \frac{\cos \theta}{r^2}")

  #      radiantexitance = MathTex(r"M(x) \equiv \frac{d \Phi _O}{dA}")

   #     radiantintensity = MathTex(r"I(\omega) = lim _{\Delta \omega \to 0} \frac{\Delta \Phi}{\Delta \omega} = \frac {d \Phi}{d \omega}")

    #    entiresphereformula = MathTex(r"I = \frac{\Phi}{4 \pi}")

     #   luminance = MathTex(r"Y = \int _{\lambda} L(\lambda) V(\lambda) d(\lambda)")