from manim import *
import numpy as np

#Colorlab Intro

class Radiometry(Scene):
    def construct(self):

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

# Title
        title = Text("Radiometry")
        title.scale(1.5)
        self.play(Write(title))

        self.wait(2)

# Add a fancy light animation here.

# Mirror Arrows

        arrows = [Arrow(2 * UL, 1 * DR), Arrow(1 * DR, 2 * UR)]
        #VGroup(*arrows).set_x(-1).arrange(buff=0)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1]))
        self.wait()

        self.play(Unwrite(title, reverse=False))

# Short Introduction

#Arrow anim, inversesquare anim, 

# Begin Info

        radiance = MathTex(r"L(x,\omega) \equiv \frac{dI(x \omega)}{dA} = \frac{d^2 \Phi (x, \omega)}{d \omega dA}")
        self.play(Write(radiance, run_time=2))
        self.wait()

        # Same anim as before, but only first arrow. 

        self.play(Unwrite(radiance), reverse=False)

        self.wait()

        irradiance = MathTex(r"E(x) = lim _{\Delta A \to 0} \frac{\Delta \Phi}{\Delta A} = \frac{d \Phi}{dA}")
        formula2 = MathTex(r"E(x, \omega) = L(x, \omega) \cos \theta d\omega") 
        self.play(Write(irradiance, run_time=2))
        self.wait()

        self.play(Unwrite(irradiance), reverse=False)

# Grid

        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-6.0, 6.0, 1))

        #self.add(grid)
        #self.play(
        #    Create(grid, run_time=3, lag_ratio=0.1),
        #)
        #self.wait()

        #Same anim, continuatuin, but with second arrow.


 #       inversesquarelaw = MathTex(r"E \propto \frac{1}{r^2}")

 #       lambert = MathTex(r"E(x) +propto \Phi \frac{\cos \theta}{r^2}")

  #      radiantexitance = MathTex(r"M(x) \equiv \frac{d \Phi _O}{dA}")

   #     radiantintensity = MathTex(r"I(\omega) = lim _{\Delta \omega \to 0} \frac{\Delta \Phi}{\Delta \omega} = \frac {d \Phi}{d \omega}")

    #    entiresphereformula = MathTex(r"I = \frac{\Phi}{4 \pi}")

     #   luminance = MathTex(r"Y = \int _{\lambda} L(\lambda) V(\lambda) d(\lambda)")

# Graph

        #ax=Axes(x_range=[-5,5,0.5], y_range=[-3,3,0.5], 
        #        x_axis_config={"numbers_to_include": np.arange(-5,5,1)}, 
        #        y_axis_config={"numbers_to_include": [1]})
        #ax_labels=ax.get_axis_labels()
        #ax_group=VGroup(ax, ax_labels)
       # 
       # self.play(Create(ax_group), run_time=6)
       # self.wait()




     