from manim import *
import math


class Struct(Scene):

    def construct(self):
        # # Introduction
        # title_l1 = TextMobject("Binary Max Heap")
        # title_l2 = TextMobject("Insert")
        # title_l1.scale(1.8)
        # title_l2.scale(1.3)
        # title_l1.shift([0, 0.5, 0])
        # title_l2.shift([0, -0.35, 0])
        # line = Line([-3.8, 0, 0], [3.8, 0, 0])
        # line.set_stroke(WHITE, 1.1, 1)
        # creators = TextMobject("Made by Matin Tavakoli \& Hossein Zaredar")
        # creators.scale(0.4)
        # creators.move_to([5, -3.7, 0])
        # self.add(title_l1)
        # self.add(title_l2)
        # self.add(line)
        # self.wait(2)
        # self.play(Write(creators), run_time=0.7)
        # self.wait(2)
        # self.play(FadeOut(title_l1), FadeOut(title_l2), FadeOut(line))
        # self.wait(1.5)

        # # title
        # title = TextMobject("Euclidean Algorithm:")
        # title.to_edge(LEFT, buff=0.8)
        # title.shift([-0.5, 2.5, 0])
        # title.scale(0.9)

        line1 = Line(4 * UP + 2.5 * LEFT, 4 * DOWN + 2.5 * LEFT)
        line2 = Line(4 * UP + 2.5 * RIGHT, 4 * DOWN + 2.5 * RIGHT)
        self.play(Write(line1), Write(line2))

        exp1 = TextMobject(r"$a[2].name$")
        exp2 = TextMobject(r"$(*(a+2)).name$")
        exp3 = TextMobject(r"$(a+2)\rightarrow name$")

        exp1.scale(0.7)
        exp2.scale(0.7)
        exp3.scale(0.7)

        exp1.move_to([-5, 2, 0])
        exp2.move_to([0, 2, 0])
        exp3.move_to([5, 2, 0])

        self.play(Write(exp1), Write(exp2), Write(exp3))

        ############################################################################
        # expression 1
        create_table(self, -6.25, -2, 5, 1, border_mode=True)

        indices = VGroup()
        for i in range(3):
            index = TextMobject(str(i))
            index.scale(0.7)
            index.move_to([-6 + 0.5 * i, -2.25, 0])
            index.set_color(PURPLE)
            self.play(Write(index))
        ############################################################################

        ############################################################################
        # expression 2
        create_table(self, -1.25, -2, 5, 1, border_mode=True)

        pointer = Arrow([-1, -3.5, 0], [-1, -2.5, 0])
        pointer.set_color(RED)
        self.play(Write(pointer))  # TODO: why didn't GrowArrow work?
        for i in range(1, 3):
            new_pointer = Arrow([-1 + 0.5 * i, -3.5, 0], [-1 + 0.5 * i, -2.5, 0])
            new_pointer.set_color(RED)
            self.play(Transform(pointer, new_pointer))
            self.wait(0.5)
        ############################################################################

        ############################################################################
        # expression 3
        create_table(self, 3.75, -2, 5, 1, border_mode=True)

        rect = Polygon([4.75,-2.5, 0], [5.25,-2.5, 0], [5.25,-2, 0], [4.75,-2, 0])
        rect.set_color(YELLOW)
        self.play(Write(rect), rate_func=smooth, run_time=1)
        ############################################################################


def create_table(self, x_start, y_start, vertical_num, horizontal_num, vspace=0.5, hspace=0.5, border_mode=False):
    x_end = x_start + vertical_num * vspace
    y_end = y_start - horizontal_num * hspace

    if border_mode:
        vertical_num += 1
        horizontal_num += 1
        offset = 0
    else:
        vertical_num -= 1
        horizontal_num -= 1
        offset = 1

    horizontal_lines = VGroup()
    for i in range(horizontal_num):
        line = Line([x_start - hspace * offset, y_start - vspace * (i + offset), 0],
                    [x_end - hspace * offset, y_start - vspace * (i + offset), 0])
        horizontal_lines.add(line)
    self.play(*[Write(line) for line in horizontal_lines], rate_func=linear, run_time=1)

    self.wait(0.3)

    vertical_lines = VGroup()
    for i in range(vertical_num):
        line = Line([x_start + hspace * i, y_end, 0], [x_start + hspace * i, y_start, 0])
        vertical_lines.add(line)
    self.play(*[Write(line) for line in vertical_lines], rate_func=linear, run_time=1)
