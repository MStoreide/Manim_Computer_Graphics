from manim import *     

class Software(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E

#Intro

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

        title = Text("3D Processing Sofware")
        title.scale(1.5)
        self.play(Write(title))

        self.wait(2)

        self.play(Unwrite(title))

# Softwares

        blender = ImageMobject("Blender.png").move_to([3,2,0])
        blender.scale(2)
        maya = ImageMobject("Autodesk Maya.png").move_to([3,0,0])
        maya.scale(2)
        cinema4d = ImageMobject("Cinema 4D.png").move_to([3,-2,0])
        cinema4d.scale(0.5)

        self.play(FadeIn(blender, shift=RIGHT*2))
        self.wait(0.3)
        self.play(FadeIn(maya), shift=RIGHT*2)
        self.wait(0.3)
        self.play(FadeIn(cinema4d), shift=RIGHT*2)
        self.wait()

        self.play(FadeOut(blender, maya, cinema4d))

# APIs and Programming

# Transformation examples

        origin = Matrix([['x'],['y'],['z']]).move_to([-1,0,0])
        transform = Matrix([['\\Delta', 'x'],['\\Delta', 'y'],['\\Delta', 'z']]).set_column_colors(RED).move_to([1,0,0])

        self.add(origin)
        self.add(transform)     
        self.wait(2)

# Have a video of the object moving in 3D space, and the corresponding matrix. 

# Video of manipulating this in 3D software, just with the wizard. 
        