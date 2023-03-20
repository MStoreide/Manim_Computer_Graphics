from manim import *

class Transformation(Scene):
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
        title = Text("Transformations")
        title.scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(Unwrite(title, reverse=False))
        self.wait()

#Translation

        origin = Matrix([['x'],['y'],['z']])
        transform = Matrix([['\\Delta', 'x'], ['\\Delta', 'y'], ['\\Delta', 'z']])
        self.play(Write(origin))
        self.wait()
        self.play(Unwrite(origin))
        self.wait()

        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-6.0, 6.0, 1))

     #   self.add(grid)
     #   self.play(
     #       Create(grid, run_time=3, lag_ratio=0.1),
     #   )

        #Scaling

        origin = Matrix([['x'],['y'],['z']])
        scalematrix = Matrix([['sx', 0, 0],[0, 'sy', 0], [0, 0, 'sz']])

#Should make a video here that shows how we move objects to the origin, scale, and then move it back. With grids.

#Rotation

#Rotation around the origin

        rotation = Matrix([['\\cos' '\\theta', '-\\sin' '\\theta', 0], ['\\sin' '\\theta', '\\cos' '\\theta', 0], [0, 0, 1]],
        left_bracket="(",
        right_bracket=")")



# Coordinate system

        axes = Axes()
        self.play(Create(axes), run_time=2)
        self.wait(2)