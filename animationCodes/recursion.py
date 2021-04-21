from manim import *
import math

fibo_n = 5
size = (2 ** fibo_n - 1)
func_call_arr = [-1] * size


class Node:
    def __init__(self, index, key, x, y, node_color, function_name, scaling_factor=0.25, opacity=0.3):
        self.key = key
        self.index = index

        self.left_edge = None
        self.right_edge = None

        self.node_obj = Circle()
        self.node_obj.move_to([x, y, 0])
        self.node_obj.scale(scaling_factor)
        self.node_obj.set_color(node_color)
        self.node_obj.set_fill()
        self.node_obj.set_opacity(opacity)

        self.key_obj = TextMobject(function_name + "(", str(key), ") = ?")
        self.key_obj.move_to([x, y, 0])
        self.key_obj.scale(scaling_factor * 0.8)

        # TODO this shit must be set and updated in heap operations
        self.index_obj = TextMobject(str(index))
        self.index_obj.set_color(RED)
        self.index_obj.move_to([x, y, 0])
        self.index_obj.scale(0.7)
        self.index_obj.shift([-0.5, 0, 0])


class Tree:

    def __init__(self, arr, x, y, node_color, function_name, hspace=4, vspace=-1):

        self.x = x
        self.y = y
        self.size = len(arr)
        if self.size != 0:
            self.height = math.floor(math.log2(self.size))
        else:
            self.height = 0

        self.hspace = hspace
        self.vspace = vspace
        self.node_color = node_color

        self.node_objs = VGroup()
        self.key_objs = VGroup()
        self.edges = VGroup()

        self.arr = []

        for i, key in enumerate(arr):

            if i == 0:
                node = Node(i, key, self.x, self.y, node_color, function_name)
                self.node_objs.add(node.node_obj)
                self.key_objs.add(node.key_obj)

            elif key != -1:

                node_height = math.floor(math.log2(i + 1))
                delta_x = 0.5 ** node_height * hspace
                node_parent = self.arr[self.parent(i)]

                if self.left(node_parent.index) == i:
                    delta_x *= -1

                delta_y = self.vspace
                node = None
                node = Node(i, key, node_parent.node_obj.get_x() + delta_x, node_parent.node_obj.get_y() + delta_y,
                            node_color, function_name)

                self.node_objs.add(node.node_obj)
                self.key_objs.add(node.key_obj)

                edge = Arrow([node_parent.node_obj.get_x(), node_parent.node_obj.get_y(), 0],
                             [node.node_obj.get_x(), node.node_obj.get_y(), 0])
                edge.scale(0.83)
                if self.left(node_parent.index) == i:
                    node_parent.left_edge = edge
                else:
                    node_parent.right_edge = edge

                self.edges.add(edge)

            self.arr.append(node)

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        if 2 * index + 1 < self.size:
            return 2 * index + 1
        else:
            return None

    def right(self, index):
        if 2 * index + 2 < self.size:
            return 2 * index + 2
        else:
            return None

    def sketch_tree(self, scene):
        for node_obj, key_obj in zip(self.node_objs, self.key_objs):
            scene.play(
                Write(node_obj),
                Write(key_obj),
                run_time=0.3
            )
        scene.play(*[Write(e) for e in self.edges], run_time=1.5)

    # sketch part of the nodes
    def sketch_nodes(self, scene, node_objs, key_objs):
        for node_obj, key_obj in zip(node_objs, key_objs):
            scene.play(
                Write(node_obj),
                Write(key_obj),
                run_time=0.3
            )
        scene.play(*[Write(e) for e in self.edges], run_time=1.5)


class scene(Scene):
    def construct(self):
        Beginning.construct(self)


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


def parent_func(index, size):
    return (index - 1) // 2


def left_func(index, size):
    if 2 * index + 1 < size:
        return 2 * index + 1
    else:
        return None


def right_func(index, size):
    if 2 * index + 2 < size:
        return 2 * index + 2
    else:
        return None


def function_call_arr(n, size, i):
    global func_call_arr
    if i is not None:
        func_call_arr[i] = n
        if n >= 2:
            function_call_arr(n - 1, size, left_func(i, size))
            function_call_arr(n - 2, size, right_func(i, size))
        # print(arr)
    return func_call_arr


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

        l2 = TextMobject("    \\textrm{ if}", "\\textrm{(}", "\\textrm{n}", "\\textrm{ == }", "1", "\\textrm{ ||}",
                         "\\textrm{ n}",
                         "\\textrm{ == }", "2", ")")
        for i, color in zip(l2, [PURPLE_C, WHITE, RED_E, WHITE, BLUE, WHITE, RED_E, WHITE, BLUE, WHITE]):
            i.set_color(color)
        code.add(l2)

        l3 = TextMobject("        \\textrm{ return}", " 1", "\\textrm{;}")
        for i, color in zip(l3, [PURPLE_C, BLUE, WHITE]):
            i.set_color(color)
        code.add(l3)

        l4 = TextMobject("    \\textrm{ return}", "\\textrm{ fibonacci}", "\\textrm{(}",
                         "\\textrm{n}", "\\textrm{ - }", "1", "\\textrm{) +}", "\\textrm{ fibonacci}", "\\textrm{(}",
                         "\\textrm{n}",
                         "\\textrm{ - }", "2", ");")
        for i, color in zip(l4,
                            [PURPLE_C, GOLD_C, WHITE, RED_E, WHITE, BLUE, WHITE, GOLD_C, WHITE, RED_E, WHITE, BLUE,
                             WHITE]):
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

        rect = SurroundingRectangle(l1, buff=0.04, color=WHITE)

        self.play(Write(rect))
        self.wait(0.7)

        new_rect = SurroundingRectangle(l2, buff=0.04, color=YELLOW)
        self.play(ReplacementTransform(rect, new_rect))
        rect = new_rect
        self.wait(0.7)

        # n = 4  # TODO: store it in a list?

        # calls = [3, 2, 1, 1, 0, -1, -1]
        # calls = [6, 5, 4, 4, 3, 3, 2, 3, 2, 2, 1, 2, 1, 1, 0, 2, 1, 1, 0, 1, 0, -1, -1, 1, 0, -1, -1, -1, -1, -1, -1, 1, 0]

        calls = function_call_arr(fibo_n, size, 0)  # generalized!

        function_name = "fibo"
        fibo_tree = Tree(calls, -2, 1, ORANGE, function_name, hspace=6)

        # node_objs = fibo_tree.node_objs[:1]
        # key_objs = fibo_tree.key_objs[:1]

        # fibo_tree.sketch_tree(self)
        # fibo_tree.sketch_nodes(self, node_objs, key_objs)

        if fibo_n == 1:
            new_rect = SurroundingRectangle(l3, buff=0.04, color=RED)
            self.play(ReplacementTransform(rect, new_rect))
            rect = new_rect
            self.wait(0.7)

        else:
            new_rect = SurroundingRectangle(l4, buff=0.04, color=RED)
            self.play(ReplacementTransform(rect, new_rect))
            rect = new_rect
            self.wait(0.7)

            # keeping scaling values
            frame_scale_factor_list = [[16, 4, 0], [8 / 16, 4, 0], [5 / 8, 4, 0], [3 / 5, 4, 0]]
            zd_scale_factor_list = [[4, 1, 0], [2 / 4, 1, 0], [2 / 2, 1.6, 0], [1.5 / 2, 2, 0]]

            # indices = [0, 1, 3, 7, 4, 2, 5]  # indices that extraction occurs (TODO: function for this? :) )
            indices = [0, 1, 3]  # indices that extraction occurs (TODO: function for this? :) )

            for i, index in enumerate(indices):
                root = fibo_tree.arr[index]  # TODO: is circle the best shape?

                if index == 0:
                    self.play(
                        Write(root.node_obj),
                        Write(root.key_obj),
                    )

                left_child = fibo_tree.arr[fibo_tree.left(index)]
                right_child = fibo_tree.arr[fibo_tree.right(index)]

                cluster = VGroup(root.node_obj, left_child.node_obj, right_child.node_obj)

                # Set camera
                zoomed_camera = self.zoomed_camera
                zoomed_display = self.zoomed_display
                frame = zoomed_camera.frame
                zoomed_display_frame = zoomed_display.display_frame

                zoomed_display_shift_list = [[2 * UP], [RIGHT], [0 * RIGHT], [-1 * UP]]

                frame.move_to(cluster)
                frame.set_color(YELLOW)

                zoomed_display_frame.set_color(YELLOW)
                zoomed_display.shift(zoomed_display_shift_list[i])  # TODO: test and check propagating effect

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

                # Scale in     x   y  z
                # to put it short, the ratios must be exactly the same. Otherwise, the frame will scale like the zoomed display
                frame_scale_factor = frame_scale_factor_list[i]  # TODO: test and check propagating effect
                zd_scale_factor = zd_scale_factor_list[i]  # TODO: test and check propagating effect

                zoomed_display.scale(zd_scale_factor)

                self.play(
                    ShowCreation(frame),
                    frame.animate.scale(frame_scale_factor),
                    # zoomed_display.animate.scale(scale_factor),
                )

                # Activate zooming
                self.activate_zooming()

                self.play(
                    # You have to add this line
                    self.get_zoomed_display_pop_out_animation(),
                    unfold_camera
                )

                self.wait()

                self.play(
                    Write(left_child.node_obj),
                    Write(left_child.key_obj),
                    Write(right_child.node_obj),
                    Write(right_child.key_obj),
                )

                self.wait(0.5)

                self.play(
                    Write(root.left_edge),
                    Write(root.right_edge),
                )

                self.wait()

                # flickering_edge = edge1.copy()
                # flickering_edge.set_color(GREEN_SCREEN)
                #
                # self.play(ShowCreation(flickering_edge), rate_func=lambda t: smooth(t), run_time=0.5)
                #
                # self.wait(0.2)
                #
                # # self.play(Uncreate(flickering_edge), rate_func=lambda t: smooth(1 - t))
                # self.play(
                #     Uncreate(flickering_edge.set_points(flickering_edge.get_points()[::-1])),
                #           rate_func=lambda t: smooth(1 - t), run_time=0.5)
                #
                # self.wait(0.2)
                #
                # self.play(
                #     frame.animate.move_to(node)
                # )
                #
                # # zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
                # # self.play(FadeIn(zoomed_camera_text))
                #
                # # # Scale in     x   y  z
                # # scale_factor = [0.5, 1.5, 0]
                # #
                # # # Resize the frame and zoomed camera
                # # self.play(
                # #     frame.animate.scale(scale_factor),
                # #     zoomed_display.animate.scale(scale_factor),
                # #     # FadeOut(zoomed_camera_text),
                # #     # FadeOut(frame_text)
                # # )
                # #
                # # # Resize the frame
                # # self.play(
                # #     frame.animate.scale(3),
                # #     frame.animate.shift(2.5 * DOWN)
                # # )
                # #
                # # # Resize zoomed camera
                # # self.play(
                # #     ScaleInPlace(zoomed_display, 2)
                # # )
                # #
                # # self.wait()
                # #
                # # self.play(
                # #     self.get_zoomed_display_pop_out_animation(),
                # #     unfold_camera,
                # #     # -------> Inverse
                # #     rate_func=lambda t: smooth(1 - t),
                # # )
                # # self.play(
                # #     Uncreate(zoomed_display_frame),
                # #     Uncreate(frame),
                # # )
                # # self.wait()
