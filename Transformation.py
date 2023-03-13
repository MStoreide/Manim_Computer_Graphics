from manim import *

class Transformation(Scene):
    def constructi(self):

#Translation

        origin = Matrix([[x],[y],[z]])
        transform = Matrix([[\Delta x],[\Delta y],[\Delta z]])
        self.play(Write(origin), run_time=2)
        self.wait()

        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-6.0, 6.0, 1))

        self.add(grid)
        self.play(
            Create(grid, run_time=3, lag_ratio=0.1),
        )

        #Scaling

origin = Matrix([[x],[y],[z]])
scalematrix = Matrix([[s_x, 0, 0],[0, s_y, 0], [0, 0, s_z]])

#Should make a video here that shows how we move objects to the origin, scale, and then move it back. With grids.

#Rotation

#Rotation around the origin

m2 = Matrix([[\cos \theta, -\sin \theta, 0], [\sin \theta, \cos \theta, 0], [0, 0, 1]],
    left_bracket="(",
    right_bracket=")")