from manim import *
import math

class scene(Scene):
    def construct(self):
        Euclidean.construct(self)
        RemoveAllObjectsInScreen.construct(self)
        #Pseudocode.construct(self)
        Euclidean_example.construct(self)

class Euclidean(Scene):
    def construct(self):

        ### part 0: Title
        title_l1 = TextMobject("Introduction to pseudocode")
        title_l2 = TextMobject("Euclidean Algorithm")
        title_l1.scale(1.8)
        title_l2.scale(1.3)
        title_l1.shift([0, 0.5, 0])
        title_l2.shift([0, -0.35, 0])
        line = Line([-3.8, 0, 0], [3.8, 0, 0])
        line.set_stroke(WHITE, 1.1, 1)
        creators = TextMobject("Made by Matin Tavakoli \& Bahar Kaviani")
        creators.scale(0.4)
        creators.move_to([5, -3.7, 0])
        self.add(title_l1)
        self.add(title_l2)
        self.add(line)
        self.wait(2)
        self.play(Write(creators), run_time=0.7)
        self.wait(2)
        self.play(FadeOut(title_l1), FadeOut(title_l2), FadeOut(line))
        self.wait(1.5)

        ### part 1: Introduction
        title = TextMobject("GCD (Greatest Common Divisor):")
        title.to_edge(LEFT, buff=1.3)
        title.shift([0, 3, 0])
        title.scale(1.2)
        self.play(Write(title))
        self.wait(0.5)

        def_1 = TextMobject("How do we find the GCD of two numbers?")
        def_2 = TextMobject("We follow these three steps:")
        def_3 = TextMobject("Step 1: Find the larger number")
        def_4 = TextMobject("Step 2: Subtract the smaller number from the bigger one, and assign the result")
        def_5 = TextMobject("Step 3: Check if the numbers are equal. If they're not, go back to step 1")

        # part 1: fix texts features
        def_1.set_color(BLUE)
        def_2.set_color(BLUE)
        def_3.set_color(GREEN)
        def_4.set_color(GREEN)
        def_5.set_color(GREEN)

        def_1.scale(0.85)
        def_2.scale(0.85)
        def_3.scale(0.7)
        def_4.scale(0.7)
        def_5.scale(0.7)

        def_1.to_edge(LEFT, 0.7)
        def_2.to_edge(LEFT, 0.7)
        def_3.to_edge(LEFT, 1.05)
        def_4.to_edge(LEFT, 1.05)
        def_5.to_edge(LEFT, 1.05)

        def_1.shift([0, 1.7, 0])
        def_2.shift([0, 1.25, 0])
        def_3.shift([0, 0.6, 0])
        def_4.shift([0, 0, 0])
        def_5.shift([0, -0.6, 0])

        # part 1: write texts on screen
        self.play(Write(def_1))
        self.wait(0.7)
        self.play(Write(def_2))
        self.wait(0.9)
        self.play(Write(def_3))
        self.wait(0.9)
        self.play(Write(def_4), run_time=3)
        self.wait(1.5)
        self.play(Write(def_5), run_time=3)
        self.wait(1.5)

        old_steps = VGroup(def_3, def_4, def_5)
        new_steps = VGroup(def_3.copy(), def_4.copy(), def_5.copy())
        new_steps.shift([-0.35, 1.5, 0])

        self.play(FadeOut(def_1), FadeOut(def_2), run_time=1.5)
        self.play(*[Transform(old_steps[i], new_steps[i]) for i in range(len(old_steps))], run_time=1)

        self.wait(1)

        ### part 2: start of example
        def_7 = TextMobject("Let's see this on an example")
        def_7.set_color(BLUE)
        def_7.scale(0.85)
        def_7.to_edge(LEFT, 0.7)
        def_7.shift([0, -0.3, 0])
        self.play(Write(def_7))
        self.wait(1.5)

        # part 2: define and show a, b
        a, b = 54, 24

        a_object = TextMobject("a = {}".format(a))
        a_object.to_edge(LEFT, 0.7)
        a_object.scale(0.7)
        a_object.shift([0, -1.5, 0])
        self.play(Write(a_object))

        b_object = TextMobject("b = {}".format(b))
        b_object.to_edge(LEFT, 0.7)
        b_object.scale(0.7)
        b_object.shift([0, -2.5, 0])
        self.play(Write(b_object))

        self.wait(0.3)

        objects = VGroup(a_object, b_object)
        brace = Brace(objects, LEFT, buff=0.1)

        self.play(
            GrowFromCenter(brace),
            run_time=2
        )
        self.wait(1)

        # part 2: result array
        x_start = 0
        y_start = 0
        vspace = 0.5
        hspace = 0.5
        vertical_num = 10
        horizontal_num = 2
        Euclidean.create_table(self, x_start, y_start, vertical_num, horizontal_num)

        a_var_object = TextMobject("a")
        a_var_object.move_to([x_start - hspace / 2, y_start + vspace / 2 - vspace, 0])
        a_var_object.scale(0.65)
        self.play(Write(a_var_object))
        a_var_object = TextMobject(str(a))
        a_var_object.move_to([x_start - hspace / 2 + hspace, y_start + vspace / 2 - vspace, 0])
        a_var_object.scale(0.65)
        self.play(Write(a_var_object))
        self.wait(0.4)

        b_var_object = TextMobject("b")
        b_var_object.move_to([x_start - hspace / 2, y_start - vspace / 2 - vspace, 0])
        b_var_object.scale(0.65)
        self.play(Write(b_var_object))
        b_var_object = TextMobject(str(b))
        b_var_object.move_to([x_start - hspace / 2 + hspace, y_start - vspace / 2 - vspace, 0])
        b_var_object.scale(0.65)
        self.play(Write(b_var_object))
        self.wait(0.4)

        # part 2: trace the algorithm with arrow
        step_line_arrow = Arrow([-6.9, 2.1, 0], [-6.6, 2.1, 0])
        step_line_arrow.set_color(ORANGE)
        step_line_arrow.set_stroke(width=5)
        self.play(ShowCreation(step_line_arrow))
        self.wait(1)

        ### part 3: algorithm execution
        while a != b:
            if a > b:
                larger_object = a_object

                a = a - b  # new value
                new_a_object = TextMobject("a = {}".format(a))
                new_a_object.scale(0.7)
                new_a_object.move_to(a_object.get_center() + (2.25 * RIGHT))

                new_b_object = TextMobject("b = {}".format(b))
                new_b_object.scale(0.7)
                new_b_object.move_to(b_object.get_center() + (2.25 * RIGHT))

            else:
                larger_object = b_object

                b = b - a  # new value
                new_b_object = TextMobject("b = {}".format(b))
                new_b_object.scale(0.7)
                new_b_object.move_to(b_object.get_center() + (2.25 * RIGHT))

                new_a_object = TextMobject("a = {}".format(a))
                new_a_object.scale(0.7)
                new_a_object.move_to(a_object.get_center() + (2.25 * RIGHT))

            new_objects = VGroup(new_a_object, new_b_object)

            surrounding = SurroundingRectangle(larger_object, buff=0.04, color=YELLOW)
            self.play(Write(surrounding))

            self.wait(0.7)

            new_step_line_arrow = step_line_arrow.copy()
            new_step_line_arrow.shift([0, -0.6, 0])
            self.play(ReplacementTransform(step_line_arrow, new_step_line_arrow))
            step_line_arrow = new_step_line_arrow

            self.wait(0.7)

            rightarrow = TextMobject("""$$\\Rightarrow$$""")
            rightarrow.move_to(new_objects.get_center() + (1.25 * LEFT))
            self.play(Write(rightarrow))

            self.wait(0.5)

            pack = VGroup(brace, a_object, b_object)
            new_brace = Brace(new_objects, LEFT, buff=0.1)
            new_pack = VGroup(new_brace, new_a_object, new_b_object)
            self.play(TransformFromCopy(pack, new_pack))

            # complete array
            new_a_var_object = TextMobject(str(a))
            new_a_var_object.move_to([a_var_object.get_x(), a_var_object.get_y(), 0])
            new_a_var_object.shift([hspace, 0, 0])
            new_a_var_object.scale(0.65)
            self.play(TransformFromCopy(a_var_object, new_a_var_object))
            a_var_object = new_a_var_object

            new_b_var_object = TextMobject(str(b))
            new_b_var_object.move_to([b_var_object.get_x(), b_var_object.get_y(), 0])
            new_b_var_object.shift([hspace, 0, 0])
            new_b_var_object.scale(0.65)
            self.play(TransformFromCopy(b_var_object, new_b_var_object))
            b_var_object = new_b_var_object

            self.wait(1)

            # new step
            new_step_line_arrow = step_line_arrow.copy()
            new_step_line_arrow.shift([0, -0.6, 0])
            self.play(ReplacementTransform(step_line_arrow, new_step_line_arrow))
            step_line_arrow = new_step_line_arrow

            a_object = new_a_object
            b_object = new_b_object
            brace = new_brace

            self.wait(1)

            if a != b:
                new_step_line_arrow = step_line_arrow.copy()
                new_step_line_arrow.shift([0, 1.2, 0])
                self.play(ReplacementTransform(step_line_arrow, new_step_line_arrow))
                step_line_arrow = new_step_line_arrow

        self.wait(1)

    def create_table(self, x_start, y_start, vertical_num, horizontal_num, border_mode=False):
        vspace=0.5
        hspace=0.5
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


class Pseudocode(Scene):

    def construct(self):
        ### part 0: Title
        title_l1 = TextMobject("How to write the pseudocode?")
        title_l1.scale(1)
        title_l1.shift([0, 0.5, 0])
        self.add(title_l1)
        self.wait(2)
        sq = Square()
        self.play(
            ReplacementTransform(
                title_l1, sq
            )
        )
        self.wait(1.5)


class Euclidean_example(Scene):

    def construct(self):
        ### part 0: Title
        title = TextMobject("How to write the pseudocode?")
        title.scale(1)
        title.shift([0, 0.5, 0])

        creators = TextMobject("Made by Matin Tavakoli \& Bahar Kaviani")
        creators.scale(0.4)
        creators.move_to([5, -3.7, 0])

        self.play(FadeIn(creators), FadeIn(title))
        self.wait(2)

        algoTitle = TextMobject("Euclidean Algorithm:")
        algoTitle.to_edge(LEFT, buff=0.8)
        algoTitle.shift([-0.5, 2.5, 0])
        algoTitle.scale(0.9)

        self.play(
            ReplacementTransform(
                title, algoTitle
            )
        )
        self.wait(1.5)

        # drawing the new_a_var_object line
        line = Line([-6.3, 2.2, 0], [-6.3, -1.7, 0])

        # drawing the code
        code = VGroup()

        l1 = TextMobject("\\textrm{set}", "\\textrm{ a}", "\\textrm{ to}", "\\textrm{ ?}")
        for i, color in zip(l1, [PURPLE_C, BLUE, WHITE, BLUE]):
            i.set_color(color)
        code.add(l1)

        l2 = TextMobject("\\textrm{set}", "\\textrm{ b}", "\\textrm{ to}", "\\textrm{ ?}")
        for i, color in zip(l2, [PURPLE_C, BLUE, WHITE, BLUE]):
            i.set_color(color)
        code.add(l2)

        l3 = TextMobject("\\textrm{repeat}", "\\textrm{ while}", "\\textrm{ a}", "\\textrm{ !=}", "\\textrm{ b}")
        for i, color in zip(l3, [PURPLE_C, GREEN_E, BLUE, WHITE, BLUE]):
            i.set_color(color)
        code.add(l3)

        l4 = TextMobject("\\textrm{do}", "    \\textrm{if}", "\\textrm{ a}", "\\textrm{ >}", "\\textrm{ b}")
        for i, color in zip(l4, [PURPLE_C, GREEN_E, BLUE, WHITE, BLUE]):
            i.set_color(color)
        code.add(l4)

        l5 = TextMobject("    \\textrm{do}", "\\textrm{  set}", "\\textrm{ a}", "\\textrm{ to}", "\\textrm{ a}",
                         "\\textrm{ -}", "\\textrm{ b}")
        for i, color in zip(l5, [GREEN_E, PURPLE_C, BLUE, WHITE, BLUE, WHITE, BLUE]):
            i.set_color(color)
        code.add(l5)

        l6 = TextMobject("    \\textrm{else}", "\\textrm{ set}", "\\textrm{ b}", "\\textrm{ to}", "\\textrm{ b}",
                         "\\textrm{ -}", "\\textrm{ a}")
        for i, color in zip(l6, [GREEN_E, PURPLE_C, BLUE, WHITE, BLUE, WHITE, BLUE]):
            i.set_color(color)
        code.add(l6)

        l7 = TextMobject("\\textrm{print}", "\\textrm{ a}")
        for i, color in zip(l7, [GREEN_E, BLUE]):
            i.set_color(color)
        code.add(l7)

        for i, l in enumerate(code):
            l.to_edge(LEFT, buff=0.7)
            l.shift([0.2 * (len(l[0].get_tex_string()) - len(l[0].get_tex_string().lstrip())), -0.55 * i + 0.65, 0])

        code.scale(0.85)
        code.shift([0, 1.6, 0])

        l1_x = code[0].get_x() + 0.11  # keeping it as temp value
        l1_y = code[0].get_y()  # keeping it as temp value

        l2_x = code[1].get_x() + 0.11  # keeping it as temp value
        l2_y = code[1].get_y()  # keeping it as temp value

        self.play(FadeInFrom(line, DOWN))

        for l in code:
            self.play(FadeInFrom(l, LEFT), run_time=0.5)
        self.wait(1)

        # result array
        x_start = 0
        y_start = 2.5
        hspace = 0.5
        vspace = 0.5
        vertical_num = 10
        horizontal_num = 2

        Euclidean_example.create_table(self, x_start, y_start, vertical_num, horizontal_num)

        a_var_object = TextMobject("a")
        a_var_object.move_to([x_start - hspace / 2, y_start + vspace / 2 - vspace, 0])
        a_var_object.scale(0.65)
        self.play(Write(a_var_object))

        self.wait(0.4)

        b_var_object = TextMobject("b")
        b_var_object.move_to([x_start - hspace / 2, y_start - vspace / 2 - vspace, 0])
        b_var_object.scale(0.65)
        self.play(Write(b_var_object))

        twins = [(15, 10), (48, 180)]

        for a, b in twins:

            values = VGroup()

            rect = SurroundingRectangle(l1, buff=0.04, color=WHITE)

            # drawing the searched key
            question = TextMobject(f"Let's find the GCD of  {a} \& {b}.")
            question.shift([0, title.get_y() + 0.9, 0])
            question.scale(0.7)
            question.set_color(GREEN)
            self.play(Write(question))
            self.wait(0.5)

            a_val = TextMobject(str(a))
            a_val.move_to([l1[3].get_x(), l1[3].get_y(), 0])
            a_val.scale(0.85)
            a_val.set_color(BLUE)
            new_l1 = TextMobject("\\textrm{set}", "\\textrm{ a}", "\\textrm{ to}", f" \\textrm{a}")
            for i, color in zip(new_l1, [PURPLE_C, BLUE, WHITE, BLUE]):
                i.set_color(color)
            new_l1.move_to([l1_x, l1_y, 0])  # TODO: plot height
            num_len = int(math.log10(a)) + 1
            new_l1.shift([0.11 * (num_len - 2), 0, 0])
            new_l1.scale(0.85)
            self.play(ReplacementTransform(l1, new_l1))
            code.remove(l1)
            code.add(new_l1)
            l1 = new_l1
            rect = SurroundingRectangle(new_l1, buff=0.04, color=WHITE)

            self.wait(0.7)

            b_val = TextMobject(str(b))
            b_val.move_to([l2[3].get_x(), l2[3].get_y(), 0])
            b_val.scale(0.85)
            b_val.set_color(BLUE)
            new_l2 = TextMobject("\\textrm{set}", "\\textrm{ b}", "\\textrm{ to}", f" \\textrm{b}")
            for i, color in zip(new_l2, [PURPLE_C, BLUE, WHITE, BLUE]):
                i.set_color(color)
            new_l2.move_to([l2_x, l2_y, 0])
            num_len = int(math.log10(b)) + 1
            new_l2.shift([0.11 * (num_len - 2), 0, 0])
            new_l2.scale(0.85)
            self.play(ReplacementTransform(l2, new_l2))
            code.remove(l2)
            code.add(new_l2)
            l2 = new_l2
            new_rect = SurroundingRectangle(new_l2, buff=0.04, color=WHITE)

            self.wait(0.5)

            self.play(Write(rect))
            self.wait(0.7)

            a_var_object = TextMobject(str(a))
            a_var_object.move_to([x_start - hspace / 2 + hspace, y_start + vspace / 2 - vspace, 0])
            a_var_object.scale(0.65)
            self.play(Write(a_var_object))
            values.add(a_var_object)

            new_rect = SurroundingRectangle(l2, buff=0.04, color=WHITE)
            self.play(ReplacementTransform(rect, new_rect))
            self.wait(0.7)

            b_var_object = TextMobject(str(b))
            b_var_object.move_to([x_start - hspace / 2 + hspace, y_start - vspace / 2 - vspace, 0])
            b_var_object.scale(0.65)
            self.play(Write(b_var_object))
            values.add(b_var_object)

            rect = new_rect
            new_rect = SurroundingRectangle(l3, buff=0.04, color=WHITE)
            self.play(ReplacementTransform(rect, new_rect))
            self.wait(0.7)

            while a != b:
                rect = new_rect
                new_rect = SurroundingRectangle(l4, buff=0.04, color=GREEN)
                self.play(ReplacementTransform(rect, new_rect))
                self.wait(0.7)

                if a > b:
                    rect = new_rect
                    new_rect = SurroundingRectangle(l5, buff=0.04, color=GREEN)
                    self.play(ReplacementTransform(rect, new_rect))
                    self.wait(0.7)
                    a = a - b
                    new_a_var_object = TextMobject(str(a))
                    new_a_var_object.move_to(
                        [a_var_object.get_x(), a_var_object.get_y(), 0])
                    new_a_var_object.shift([hspace, 0, 0])
                    new_a_var_object.scale(0.65)
                    self.play(TransformFromCopy(a_var_object, new_a_var_object))
                    values.add(new_a_var_object)
                    a_var_object = new_a_var_object
                    self.wait(0.5)
                else:
                    rect = new_rect
                    new_rect = SurroundingRectangle(l6, buff=0.04, color=GREEN)
                    self.play(ReplacementTransform(rect, new_rect))
                    self.wait(0.7)
                    b = b - a
                    new_b_var_object = TextMobject(str(b))
                    new_b_var_object.move_to(
                        [b_var_object.get_x(), b_var_object.get_y(), 0])
                    new_b_var_object.shift([hspace, 0, 0])
                    new_b_var_object.scale(0.65)
                    self.play(TransformFromCopy(b_var_object, new_b_var_object))
                    values.add(new_b_var_object)
                    b_var_object = new_b_var_object
                    self.wait(0.5)

                rect = new_rect
                new_rect = SurroundingRectangle(l3, buff=0.04, color=WHITE)
                self.play(ReplacementTransform(rect, new_rect))
                self.wait(0.7)

            rect = new_rect
            new_rect = SurroundingRectangle(l7, buff=0.04, color=ORANGE)
            self.play(ReplacementTransform(rect, new_rect))
            self.wait(0.7)

            new_a_var_object.save_state()
            # self.play(new_a_var_object.scale, 1.25, new_a_var_object.move_to,
            #           [new_a_var_object.get_x(), new_a_var_object.get_y() + 0.05, 0],
            #           new_a_var_object.set_color,
            #           YELLOW, run_time=1.5)
            self.play(new_a_var_object.animate.scale(1.25),
                      new_a_var_object.animate.move_to([new_a_var_object.get_x(), new_a_var_object.get_y() + 0.05, 0]),
                      new_a_var_object.animate.set_color(YELLOW), run_time=1.5)
            self.wait(0.4)

            answer = TextMobject(str(a))
            answer.set_color(ORANGE)
            answer.scale(0.7)
            answer.next_to(question, RIGHT, buff=0.25)
            self.play(TransformFromCopy(new_a_var_object, answer))

            self.play(Restore(new_a_var_object))

            self.wait(0.7)

            self.play(FadeOut(new_rect))
            self.play(*[FadeOut(value) for value in values])
            self.play(FadeOut(question), FadeOut(answer))

        self.wait(3)

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



class RemoveAllObjectsInScreen(Scene):
    def construct(self):

        creators = TextMobject("Made by Matin Tavakoli \& Bahar Kaviani")
        creators.scale(0.4)
        creators.move_to([5, -3.7, 0])
        self.play(Write(creators))

        self.play(
            *[FadeOut(mob)for mob in self.mobjects if mob != creators]
            # All mobjects in the screen are saved in self.mobjects
        )

        #for mob in self.mobjects:
        #    if mob != creators:
        #        self.play(FadeOut(mob))

        self.wait()

class WhatIsCONFIG(Scene):
    CONFIG={
        "object_1":TextMobject("Object 1"),
        "object_2":Square(),
        "number":3,
        "vector":[1,1,0]
    }
    def construct(self):
        print(self.CONFIG.keys())

        self.play(
            Write(self.CONFIG['object_1'])
        )
        self.play(
            self.object_1.scale,self.number
        )
        self.play(
            ReplacementTransform(
                self.object_1,
                self.object_2
            )
        )
        self.play(
            self.object_2.shift,self.vector
        )
        self.wait()