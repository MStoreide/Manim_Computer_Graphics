from manim import *

# Video about formats of 3D objects

#NURBS, Parametric, Polygons, etc

class Objects(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E

# Intro

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
        title = Text("3D Objects")
        title.scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(Unwrite(title, reverse=False))
        self.wait()


# Parametric Objects

#NURBS Objects

        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.add(l1, d1, l2, d2)
        self.play(Create(bezier))
        self.wait(2)

#Polygons

        surface = Graph([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)],
                  layout={1: [-4, 0, 0], 2: [-3, 0, 0], 3: [-2, 0, 0], 4: [-1, 0, 0], 5: [0, 0, 0], 6: [1, 0, 0], 7: [2, 0, 0], 8: [3, 0, 0], 9: [4, 0, 0]}
                  )
        self.play(Create(surface), run_time=3)
        self.wait(2)
        self.play(surface.animate.change_layout("circular"))
        self.wait(2)
        self.play(surface.animate.change_layout("spiral"))
        self.wait(2)
        self.play(surface.animate.change_layout("planar"))
        self.wait(2)