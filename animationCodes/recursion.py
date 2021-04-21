from manim import *
import math


class scene(Scene):
    def construct(self):
        Beginning.construct(self)
        # Tips_Local.construct(self)
        # Tips_Global.construct(self)
        Tips_Static.construct(self)

        # RemoveAllObjectsInScreen.construct(self)


class Beginning(Scene):
    """
    Show the title and first scene context.
    """

    def construct(self):
        ### part 0: Title
        title_l1 = TextMobject("Local, Global and Static")
        title_l2 = TextMobject("Session 9")
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


class CodeAnalyzer(Scene):
    """
    Analyze one code to show differences between local, global and static variables.
    """

    def construct(self):
        ### part 0: introduction
        # TODO: add x svg file as a character

        ### part 1: example code
        codeTitle = TextMobject("Example Program:")
        codeTitle.to_edge(LEFT, buff=0.8)
        codeTitle.shift([-0.5, 3.5, 0])
        codeTitle.scale(0.8)

        self.play(
            Write(codeTitle)
        )
        self.wait(1.5)

        line = Line([-6.3, 3.2, 0], [-6.3, -3.8, 0])

        # draw the code
        code = VGroup()

        l1 = TextMobject("\\textrm{static}", "\\textrm{ int}", "\\textrm{ a}", "\\textrm{ = 20;}")
        for i, color in zip(l1, [YELLOW_C, BLUE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l1)

        l2 = TextMobject("\\textrm{void}", "\\textrm{ func}", "\\textrm{()}")
        for i, color in zip(l2, [BLUE, PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l2)

        b1 = TextMobject("\\textrm{\\{}")
        b1.set_color(color, WHITE)
        code.add(b1)

        l3 = TextMobject("    \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ a}", "\\textrm{ );}")
        for i, color in zip(l3, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l3)

        l4 = TextMobject("    \\textrm{a}", "\\textrm{ = 100;}")
        for i, color in zip(l4, [RED_E, WHITE]):
            i.set_color(color)
        code.add(l4)

        b2 = TextMobject("\\textrm{\\}}")
        b2.set_color(color, WHITE)
        code.add(b2)

        l5 = TextMobject("\\textrm{int}", "\\textrm{ main}", "\\textrm{()}")
        for i, color in zip(l5, [BLUE, PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l5)

        b3 = TextMobject("\\textrm{\\{}")
        b3.set_color(color, WHITE)
        code.add(b3)

        l6 = TextMobject("    \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ a}", "\\textrm{ );}")
        for i, color in zip(l6, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l6)

        b4 = TextMobject("    \\textrm{\\{}")
        b4.set_color(color, WHITE)
        code.add(b4)

        l7 = TextMobject("        \\textrm{static}", "\\textrm{ int}", "\\textrm{ a}", "\\textrm{ = 10;}")
        for i, color in zip(l7, [YELLOW_C, BLUE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l7)

        l8 = TextMobject("        \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ a}", "\\textrm{ );}")
        for i, color in zip(l8, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l8)

        l9 = TextMobject("        \\textrm{func}", "\\textrm{();}")
        for i, color in zip(l9, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l9)

        b5 = TextMobject("    \\textrm{\\}}")
        b5.set_color(color, WHITE)
        code.add(b5)

        l10 = TextMobject("    \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                          "\\textrm{ a}", "\\textrm{ );}")
        for i, color in zip(l10, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l10)

        b6 = TextMobject("\\textrm{\\}}")
        b6.set_color(color, WHITE)
        code.add(b6)

        for i, l in enumerate(code):
            l.to_edge(LEFT, buff=0.7)
            l.shift([0.2 * (len(l[0].get_tex_string()) - len(l[0].get_tex_string().lstrip())), -0.55 * i + 0.65, 0])

        code.scale(0.8)
        code.shift([0, 3, 0])

        l1_x = code[0].get_x() + 0.11  # keeping it as temp value
        l1_y = code[0].get_y()  # keeping it as temp value

        l2_x = code[1].get_x() + 0.11  # keeping it as temp value
        l2_y = code[1].get_y()  # keeping it as temp value

        self.play(FadeInFrom(line, DOWN))

        for l in code:
            self.play(FadeInFrom(l, LEFT), run_time=0.5)
        self.wait(1)


class Factorial(MovingCameraScene):
    """
    Factorial Function.
    """

    def construct(self):
        ### part 0: introduction
        # TODO: add x svg file as a character

        ### part 1: function code

        codetitle = TextMobject("Factorial Function:")
        codetitle.to_edge(LEFT, buff=0.8)
        codetitle.shift([-0.5, 3.5, 0])
        codetitle.scale(0.8)
        self.play(Write(codetitle))
        self.wait(1.5)

        line = Line([-6.3, 3.1, 0], [-6.3, -0.3, 0])

        # draw the code
        code = VGroup()

        l0 = TextMobject("\\# include <stdio.h>")
        l0.set_color(GREY)
        code.add(l0)

        blank = TextMobject("BLANK LINE")
        blank.set_color(WHITE)
        blank.set_opacity(0)
        code.add(blank)

        l1 = TextMobject("\\textrm{ int}", "\\textrm{ factorial}", "\\textrm{(}", "\\textrm{n}", "\\textrm{) \\{}")
        for i, color in zip(l1, [BLUE, GOLD_C, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l1)

        l2 = TextMobject("    \\textrm{ if}", "\\textrm{(}", "\\textrm{n}", "\\textrm{ == 1)}")
        for i, color in zip(l2, [PURPLE_C, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l2)

        l3 = TextMobject("        \\textrm{ return}", "\\textrm{ 1;}")
        for i, color in zip(l3, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l3)

        l4 = TextMobject("    \\textrm{ return}", "\\textrm{ n}", "\\textrm{ ×}", "\\textrm{ factorial}", "\\textrm{(}",
                         "\\textrm{n}", "\\textrm{ - 1);}")
        for i, color in zip(l4, [PURPLE_C, RED_E, WHITE, GOLD_C, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l4)

        b1 = TextMobject("\\textrm{\\}}")
        b1.set_color(color, WHITE)
        code.add(b1)

        for i, l in enumerate(code):
            l.to_edge(LEFT, buff=0.5)
            l.shift([0.2 * (len(l[0].get_tex_string()) - len(l[0].get_tex_string().lstrip())), -0.55 * i + 0.65, 0])

        code.scale(0.8)
        code.shift([0, 2.5, 0])

        pseudo = VGroup(code, codetitle, line)

        self.play(FadeInFrom(line, DOWN))

        for l in code:
            self.play(FadeInFrom(l, LEFT), run_time=0.5)
        self.wait(1)

        ### part 2: executing the code

        self.camera.frame.save_state()

        self.play(
            # self.camera.frame.animate.move_to(text_zoom),
            self.camera.frame.animate.scale(1.7),
            pseudo.animate.shift([-5, 2.5, 0])
        )

        self.wait(1)

        n = 3  # TODO: store it in a list?

        rect = SurroundingRectangle(l1, buff=0.04, color=WHITE)

        self.play(Write(rect))
        self.wait(0.7)

        new_rect = SurroundingRectangle(l2, buff=0.04, color=YELLOW)
        self.play(ReplacementTransform(rect, new_rect))
        rect = new_rect
        self.wait(0.7)

        if n == 1:
            new_rect = SurroundingRectangle(l3, buff=0.04, color=RED)
            self.play(ReplacementTransform(rect, new_rect))
            rect = new_rect
            self.wait(0.7)

        else:
            new_rect = SurroundingRectangle(l4, buff=0.04, color=RED)
            self.play(ReplacementTransform(rect, new_rect))
            rect = new_rect
            self.wait(0.7)

            node = Circle()  # TODO: is circle the best shape?
            node.move_to([3, 4, 0])
            node.scale(0.75)
            node.set_color(GREEN)
            node.set_opacity(0.4)

            val = TextMobject("fact(", str(n), ") = ?")
            val.move_to([3, 4, 0])
            val.scale(0.6)

            self.play(ShowCreation(node), Write(val))

            node_child = Circle()  # TODO: is circle the best shape?
            node_child.move_to([3, 2, 0])
            node_child.scale(0.75)
            node_child.set_color(GREEN)
            node_child.set_fill()
            node_child.set_opacity(0.4)

            val_child = TextMobject("fact(", str(n - 1), ") = ?")
            val_child.move_to([3, 2, 0])
            val_child.scale(0.6)

            edge = Arrow([node.get_x(), node.get_y(), 0],
                         [node_child.get_x(), node_child.get_y(), 0])  # TODO: arrow head is too big!

            edge.scale(0.4)

            self.play(
                Write(node_child),
                Write(val_child),
            )

            self.wait(0.5)

            self.play(
                ShowCreation(edge),
            )

            self.wait()


class Fibonacci(ZoomedScene):
    """
    Fibonacci Function.
    """

    CONFIG = {
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        ### part 0: introduction
        # TODO: add x svg file as a character

        ### part 1: function code

        codetitle = TextMobject("Fibonacci Function:")
        codetitle.to_edge(LEFT, buff=0.8)
        codetitle.shift([-0.5, 3.5, 0])
        codetitle.scale(0.8)
        self.play(Write(codetitle))
        self.wait(1.5)

        line = Line([-6.3, 3.1, 0], [-6.3, -0.3, 0])

        # draw the code
        code = VGroup()

        l0 = TextMobject("\\# include <stdio.h>")
        l0.set_color(GREY)
        code.add(l0)

        blank = TextMobject("BLANK LINE")
        blank.set_color(WHITE)
        blank.set_opacity(0)
        code.add(blank)

        l1 = TextMobject("\\textrm{ int}", "\\textrm{ fibonacci}", "\\textrm{(}", "\\textrm{n}", "\\textrm{) \\{}")
        for i, color in zip(l1, [BLUE, GOLD_C, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l1)

        l2 = TextMobject("    \\textrm{ if}", "\\textrm{(}", "\\textrm{n}", "\\textrm{ == 1 ||}", "\\textrm{ n}",
                         "\\textrm{ == 2)}")
        for i, color in zip(l2, [PURPLE_C, WHITE, RED_E, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l2)

        l3 = TextMobject("        \\textrm{ return}", "\\textrm{ 1;}")
        for i, color in zip(l3, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l3)

        l4 = TextMobject("    \\textrm{ return}", "\\textrm{ fibonacci}", "\\textrm{(}",
                         "\\textrm{n}", "\\textrm{ - 2)}", "\\textrm{ +}", "\\textrm{ fibonacci}", "\\textrm{(}",
                         "\\textrm{n}",
                         "\\textrm{ - 1);}")
        for i, color in zip(l4,
                            [PURPLE_C, GOLD_C, WHITE, RED_E, WHITE, WHITE, GOLD_C, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l4)

        b1 = TextMobject("\\textrm{\\}}")
        b1.set_color(color, WHITE)
        code.add(b1)

        for i, l in enumerate(code):
            l.to_edge(LEFT, buff=0.5)
            l.shift([0.2 * (len(l[0].get_tex_string()) - len(l[0].get_tex_string().lstrip())), -0.55 * i + 0.65, 0])

        code.scale(0.8)
        code.shift([-0.3, 2.5, 0])

        pseudo = VGroup(code, codetitle, line)

        self.play(FadeInFrom(line, DOWN))

        for l in code:
            self.play(FadeInFrom(l, LEFT), run_time=0.5)
        self.wait(1)

        ### part 2: executing the code

        self.camera.frame.save_state()

        self.play(
            # self.camera.frame.animate.move_to(text_zoom),
            self.camera.frame.animate.scale(1.7),
            pseudo.animate.shift([-5, 2.5, 0])
        )

        self.wait(1)

        n = 3  # TODO: store it in a list?

        rect = SurroundingRectangle(l1, buff=0.04, color=WHITE)

        self.play(Write(rect))
        self.wait(0.7)

        new_rect = SurroundingRectangle(l2, buff=0.04, color=YELLOW)
        self.play(ReplacementTransform(rect, new_rect))
        rect = new_rect
        self.wait(0.7)

        if n == 1:
            new_rect = SurroundingRectangle(l3, buff=0.04, color=RED)
            self.play(ReplacementTransform(rect, new_rect))
            rect = new_rect
            self.wait(0.7)

        else:
            new_rect = SurroundingRectangle(l4, buff=0.04, color=RED)
            self.play(ReplacementTransform(rect, new_rect))
            rect = new_rect
            self.wait(0.7)

            node = Circle()  # TODO: is circle the best shape?
            node.move_to([0, 4, 0])
            node.scale(0.25)
            node.set_color(ORANGE)
            node.set_opacity(0.3)

            val = TextMobject("fib(", str(n), ") = ?")
            val.move_to([0, 4, 0])
            val.scale(0.2)

            self.play(ShowCreation(node), Write(val))

            node_child1 = Circle()  # TODO: is circle the best shape?
            node_child1.move_to([-1.5, 3.5, 0])
            node_child1.scale(0.25)
            node_child1.set_color(ORANGE)
            node_child1.set_fill()
            node_child1.set_opacity(0.3)

            node_child2 = Circle()  # TODO: is circle the best shape?
            node_child2.move_to([1.5, 3.5, 0])
            node_child2.scale(0.25)
            node_child2.set_color(ORANGE)
            node_child2.set_opacity(0.3)

            val_child1 = TextMobject("fibo(", str(n - 2), ") = ?")
            val_child1.move_to([-1.5, 3.5, 0])
            val_child1.scale(0.2)

            val_child2 = TextMobject("fibo(", str(n - 1), ") = ?")
            val_child2.move_to([1.5, 3.5, 0])
            val_child2.scale(0.2)

            edge1 = Arrow([node.get_x(), node.get_y(), 0],
                          [node_child1.get_x(), node_child1.get_y(), 0])  # TODO: arrow head is too big!
            edge2 = Arrow([node.get_x(), node.get_y(), 0],
                          [node_child2.get_x(), node_child2.get_y(), 0])  # TODO: arrow head is too big!

            edge1.scale(0.2)
            edge2.scale(0.2)

            self.play(
                Write(node_child1),
                Write(val_child1),
                Write(node_child2),
                Write(val_child2),
            )

            self.wait(0.5)

            self.play(
                ShowCreation(edge1),
                ShowCreation(edge2),
            )

            self.wait()

            ######################################3

            # # Set objects
            # dot = Dot().shift(UL * 2)
            #
            # image = ImageMobject(np.uint8([[0, 100, 30, 200],
            #                                [255, 0, 5, 33]]))
            # image.set_height(7)
            # frame_text = TextMobject("Frame", color=PURPLE).scale(1.4)
            # zoomed_camera_text = TextMobject("Zommed camera", color=RED).scale(1.4)
            #
            # self.add(image, dot)

            # Set camera
            zoomed_camera = self.zoomed_camera
            zoomed_display = self.zoomed_display
            frame = zoomed_camera.frame
            # zoomed_display_frame = zoomed_display.display_frame

            cluster = VGroup(node, node_child1, node_child2)

            frame.move_to(cluster)
            frame.set_color(YELLOW)

            # zoomed_display_frame.set_color(BLACK)
            zoomed_display.shift(2 * RIGHT + 0.5 * UP)

            # background zoomed_display
            zd_rect = BackgroundRectangle(
                zoomed_display,
                fill_opacity=0,
                buff=MED_SMALL_BUFF,
            )

            self.add_foreground_mobject(zd_rect)

            # animation of unfold camera
            unfold_camera = UpdateFromFunc(
                zd_rect,
                lambda rect: rect.replace(zoomed_display)
            )

            # frame_text.next_to(frame, DOWN)

            # Scale in     x   y  z
            # to put it short, the ratios must be exactly the same. Otherwise, the frame will scale like the zoomed display
            frame_scale_factor = [8, 3, 0]
            zd_scale_factor = [2, 0.75, 0]

            zoomed_display.scale(zd_scale_factor)

            self.play(
                ShowCreation(frame),
                frame.animate.scale(frame_scale_factor),
                # zoomed_display.animate.scale(scale_factor),
                # FadeIn(frame_text)
            )

            # Activate zooming
            self.activate_zooming()

            self.play(
                # You have to add this line
                self.get_zoomed_display_pop_out_animation(),
                unfold_camera
            )

            # zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
            # self.play(FadeIn(zoomed_camera_text))

            # # Scale in     x   y  z
            # scale_factor = [0.5, 1.5, 0]
            #
            # # Resize the frame and zoomed camera
            # self.play(
            #     frame.animate.scale(scale_factor),
            #     zoomed_display.animate.scale(scale_factor),
            #     # FadeOut(zoomed_camera_text),
            #     # FadeOut(frame_text)
            # )
            #
            # # Resize the frame
            # self.play(
            #     frame.animate.scale(3),
            #     frame.animate.shift(2.5 * DOWN)
            # )
            #
            # # Resize zoomed camera
            # self.play(
            #     ScaleInPlace(zoomed_display, 2)
            # )
            #
            # self.wait()
            #
            # self.play(
            #     self.get_zoomed_display_pop_out_animation(),
            #     unfold_camera,
            #     # -------> Inverse
            #     rate_func=lambda t: smooth(1 - t),
            # )
            # self.play(
            #     # Uncreate(zoomed_display_frame),
            #     Uncreate(frame),
            # )
            # self.wait()