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


class Tips_Local(Scene):
    """
    Show the important tips of local variables.
    """

    def construct(self):
        ### part 0: introduction
        # TODO: add x svg file as a character

        ### part 1: explaining the 3 tips as bullet points
        title = TextMobject("A Few Tips:")
        title.to_edge(LEFT, buff=0.8)
        title.shift([-0.5, 3.5, 0])
        title.scale(0.8)
        self.play(Write(title))
        self.wait(1.5)

        bp1 = TextMobject("local variable", " keyword", ":", " auto")
        bp2 = TextMobject("local variable", " scope", ":", " available in the block which it's declared")
        bp3 = TextMobject("local variable", " default value", ":", " garbage value")
        bp1[0].set_color(ORANGE)
        bp1[3].set_color(BLUE)
        bp2[0].set_color(ORANGE)
        bp2[3].set_color(BLUE)
        bp3[0].set_color(ORANGE)
        bp3[3].set_color(BLUE)
        bp1.scale(0.7)
        bp2.scale(0.7)
        bp3.scale(0.7)
        bp1.to_edge(LEFT, buff=0.8)
        bp2.to_edge(LEFT, buff=0.8)
        bp3.to_edge(LEFT, buff=0.8)
        bp1.shift([0, 2.5, 0])
        bp2.shift([0, 2, 0])
        bp3.shift([0, 1.5, 0])
        self.play(Write(bp1))
        self.wait(1.5)
        self.play(Write(bp2), run_time=2.5)
        self.wait(1.5)
        self.play(Write(bp3))
        self.wait(1.5)

        local_tip_pack = VGroup(bp1, bp2, bp3)

        rect = SurroundingRectangle(local_tip_pack, buff=0.2)
        rect.set_color(ORANGE)
        self.play(Write(rect))
        self.wait(1)

        rect_pack = VGroup(local_tip_pack, rect)

        mini_title = TextMobject("local variable tips")
        bp1_small = TextMobject(" keyword", ":", " auto")
        bp2_small = TextMobject(" scope", ":", " available in the block")
        bp22_small = TextMobject("which it's declared")
        bp3_small = TextMobject(" default value", ":", " garbage value")
        mini_title.set_color(ORANGE)
        bp1_small[2].set_color(BLUE)
        bp2_small[2].set_color(BLUE)
        bp22_small.set_color(BLUE)
        bp3_small[2].set_color(BLUE)
        mini_title.scale(0.75)
        bp1_small.scale(0.6)
        bp2_small.scale(0.6)
        bp22_small.scale(0.6)
        bp3_small.scale(0.6)
        mini_title.to_edge(LEFT, buff=9)
        bp1_small.to_edge(LEFT, buff=9.2)
        bp2_small.to_edge(LEFT, buff=9.2)
        bp22_small.to_edge(LEFT, buff=10.1)
        bp3_small.to_edge(LEFT, buff=9.2)
        mini_title.shift([0, 3, 0])
        bp1_small.shift([0, 2.5, 0])
        bp2_small.shift([0, 2.15, 0])
        bp22_small.shift([0, 1.8, 0])
        bp3_small.shift([0, 1.45, 0])

        local_tip_pack_small = VGroup(mini_title, bp1_small, bp2_small, bp22_small, bp3_small)
        rect_small = SurroundingRectangle(local_tip_pack_small, buff=0.2)
        rect_small.set_color(ORANGE)
        rect_pack_small = VGroup(local_tip_pack_small, rect_small)

        self.play(Transform(rect_pack, rect_pack_small))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(2)

        ### part 2: example code

        codetitle = TextMobject("Example Program:")
        codetitle.to_edge(LEFT, buff=0.8)
        codetitle.shift([-0.5, 3.5, 0])
        codetitle.scale(0.8)
        self.play(Write(codetitle))
        self.wait(1.5)

        line = Line([-6.3, 3.2, 0], [-6.3, -3.6, 0])

        # draw the code
        code = VGroup()

        l0 = TextMobject("hashtag include <stdio.h>")  # TODO: what's wrong with #?
        l0.set_color(GREY)
        code.add(l0)

        blank = TextMobject("BLANK LINE")
        blank.set_color(WHITE)
        blank.set_opacity(0)
        code.add(blank)

        l1 = TextMobject("\\textrm{ main}", "\\textrm{()}")
        for i, color in zip(l1, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l1)

        b1 = TextMobject("\\textrm{\\{}")
        b1.set_color(color, WHITE)
        code.add(b1)

        l2 = TextMobject("    \\textrm{auto}", "\\textrm{ int}", "\\textrm{ i}", "\\textrm{ = 1;}")
        for i, color in zip(l2, [ORANGE, BLUE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l2)

        b2 = TextMobject("        \\textrm{\\{}")
        b2.set_color(color, WHITE)
        code.add(b2)

        l3 = TextMobject("            \\textrm{auto}", "\\textrm{ int}", "\\textrm{ i}", "\\textrm{ = 2;}")
        for i, color in zip(l3, [ORANGE, BLUE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l3)

        b3 = TextMobject("                \\textrm{\\{}")
        b3.set_color(color, WHITE)
        code.add(b3)

        l4 = TextMobject("                    \\textrm{auto}", "\\textrm{ int}", "\\textrm{ i}", "\\textrm{ = 3;}")
        for i, color in zip(l4, [ORANGE, BLUE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l4)

        l5 = TextMobject("                    \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ i}", "\\textrm{ );}")
        for i, color in zip(l5, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l5)

        b4 = TextMobject("                \\textrm{\\}}")
        b4.set_color(color, WHITE)
        code.add(b4)

        l6 = TextMobject("            \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ i}", "\\textrm{ );}")
        for i, color in zip(l6, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l6)

        b5 = TextMobject("        \\textrm{\\}}")
        b5.set_color(color, WHITE)
        code.add(b5)

        l7 = TextMobject("    \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ i}", "\\textrm{ );}")
        for i, color in zip(l7, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l7)

        b6 = TextMobject("\\textrm{\\}}")
        b6.set_color(color, WHITE)
        code.add(b6)

        for i, l in enumerate(code):
            l.to_edge(LEFT, buff=0.5)
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


class Tips_Global(Scene):
    """
    Show the important tips of global variables.
    """

    def construct(self):
        ### part 0: introduction
        # TODO: add x svg file as a character

        ### part 1: explaining the 3 tips as bullet points
        title = TextMobject("A Few Tips:")
        title.to_edge(LEFT, buff=0.8)
        title.shift([-0.5, 3.5, 0])
        title.scale(0.8)
        self.play(Write(title))
        self.wait(1.5)

        bp1 = TextMobject("global variable", " keyword", ":", " extern")
        bp2 = TextMobject("global variable", " scope", ":", " available throughout the program")
        bp3 = TextMobject("global variable", " default value", ":", " zero")
        bp1[0].set_color(GREEN)
        bp1[3].set_color(BLUE)
        bp2[0].set_color(GREEN)
        bp2[3].set_color(BLUE)
        bp3[0].set_color(GREEN)
        bp3[3].set_color(BLUE)
        bp1.scale(0.7)
        bp2.scale(0.7)
        bp3.scale(0.7)
        bp1.to_edge(LEFT, buff=0.8)
        bp2.to_edge(LEFT, buff=0.8)
        bp3.to_edge(LEFT, buff=0.8)
        bp1.shift([0, 2.5, 0])
        bp2.shift([0, 2, 0])
        bp3.shift([0, 1.5, 0])
        self.play(Write(bp1))
        self.wait(1.5)
        self.play(Write(bp2), run_time=2.5)
        self.wait(1.5)
        self.play(Write(bp3))
        self.wait(1.5)

        local_tip_pack = VGroup(bp1, bp2, bp3)

        rect = SurroundingRectangle(local_tip_pack, buff=0.2)
        rect.set_color(GREEN)
        self.play(Write(rect))
        self.wait(1)

        rect_pack = VGroup(local_tip_pack, rect)

        mini_title = TextMobject("global variable tips")
        bp1_small = TextMobject(" keyword", ":", " extern")
        bp2_small = TextMobject(" scope", ":", " available throughout the program")
        bp3_small = TextMobject(" default value", ":", " zero")
        mini_title.set_color(GREEN)
        bp1_small[2].set_color(BLUE)
        bp2_small[2].set_color(BLUE)
        bp3_small[2].set_color(BLUE)
        mini_title.scale(0.75)
        bp1_small.scale(0.55)
        bp2_small.scale(0.55)
        bp3_small.scale(0.55)
        mini_title.to_edge(LEFT, buff=8.8)
        bp1_small.to_edge(LEFT, buff=9)
        bp2_small.to_edge(LEFT, buff=9)
        bp3_small.to_edge(LEFT, buff=9)
        mini_title.shift([0, 1, 0])
        bp1_small.shift([0, 0.5, 0])
        bp2_small.shift([0, 0.1, 0])
        bp3_small.shift([0, -0.3, 0])

        local_tip_pack_small = VGroup(mini_title, bp1_small, bp2_small, bp3_small)
        rect_small = SurroundingRectangle(local_tip_pack_small, buff=0.2)
        rect_small.set_color(GREEN)
        rect_pack_small = VGroup(local_tip_pack_small, rect_small)

        self.play(Transform(rect_pack, rect_pack_small))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(2)

        ### part 2: example code

        codetitle = TextMobject("Example Program:")
        codetitle.to_edge(LEFT, buff=0.8)
        codetitle.shift([-0.5, 3.5, 0])
        codetitle.scale(0.8)
        self.play(Write(codetitle))
        self.wait(1.5)

        line = Line([-6.3, 3, 0], [-6.3, -1, 0])

        # draw the code
        code = VGroup()

        l0 = TextMobject("hashtag include <stdio.h>")  # TODO: what's wrong with #?
        l0.set_color(GREY)
        code.add(l0)

        blank = TextMobject("BLANK LINE")
        blank.set_color(WHITE)
        blank.set_opacity(0)
        code.add(blank)

        l1 = TextMobject("\\textrm{ int}", "\\textrm{ var}", ";")
        for i, color in zip(l1, [BLUE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l1)

        l2 = TextMobject("\\textrm{ int}", "\\textrm{ main}", "\\textrm{()}")
        for i, color in zip(l2, [BLUE, PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l2)

        b1 = TextMobject("\\textrm{\\{}")
        b1.set_color(color, WHITE)
        code.add(b1)

        l3 = TextMobject("    \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ var}", "\\textrm{);}")
        for i, color in zip(l3, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l3)

        l4 = TextMobject("    \\textrm{return}", " 0;")
        for i, color in zip(l4, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l4)

        b2 = TextMobject("\\textrm{\\}}")
        b2.set_color(color, WHITE)
        code.add(b2)

        for i, l in enumerate(code):
            l.to_edge(LEFT, buff=0.7)
            l.shift([0.2 * (len(l[0].get_tex_string()) - len(l[0].get_tex_string().lstrip())), -0.55 * i + 0.65, 0])

        code.scale(0.8)
        code.shift([0, 2.5, 0])

        l1_x = code[0].get_x() + 0.11  # keeping it as temp value
        l1_y = code[0].get_y()  # keeping it as temp value

        l2_x = code[1].get_x() + 0.11  # keeping it as temp value
        l2_y = code[1].get_y()  # keeping it as temp value

        self.play(FadeInFrom(line, DOWN))

        for l in code:
            self.play(FadeInFrom(l, LEFT), run_time=0.5)
        self.wait(1)


class Tips_Static(Scene):
    """
    Show the important tips of static variables.
    """

    def construct(self):
        ### part 0: introduction
        # TODO: add x svg file as a character

        ### part 1: explaining the 3 tips as bullet points
        title = TextMobject("A Few Tips:")
        title.to_edge(LEFT, buff=0.8)
        title.shift([-0.5, 3.5, 0])
        title.scale(0.8)
        self.play(Write(title))
        self.wait(1.5)

        bp1 = TextMobject("static variable", " keyword", ":", " static")
        bp2 = TextMobject("static variable", " scope", ":"," keeps its value throughout the program and in between")
        bp22 = TextMobject("function calls")
        bp3 = TextMobject("static variable", " default value", ":", " zero")
        bp1[0].set_color(YELLOW_C)
        bp1[3].set_color(BLUE)
        bp2[0].set_color(YELLOW_C)
        bp2[3].set_color(BLUE)
        bp22.set_color(BLUE)
        bp3[0].set_color(YELLOW_C)
        bp3[3].set_color(BLUE)
        bp1.scale(0.7)
        bp2.scale(0.7)
        bp22.scale(0.7)
        bp3.scale(0.7)
        bp1.to_edge(LEFT, buff=0.8)
        bp2.to_edge(LEFT, buff=0.8)
        bp22.to_edge(LEFT, buff=0.8)
        bp3.to_edge(LEFT, buff=0.8)
        bp1.shift([0, 2.5, 0])
        bp2.shift([0, 2, 0])
        bp22.shift([3.35, 1.5, 0])
        bp3.shift([0, 1, 0])
        self.play(Write(bp1))
        self.wait(1.5)
        self.play(Write(bp2), run_time=2.5)
        self.play(Write(bp22))
        self.wait(1.5)
        self.play(Write(bp3))
        self.wait(1.5)

        local_tip_pack = VGroup(bp1, bp2, bp22, bp3)

        rect = SurroundingRectangle(local_tip_pack, buff=0.2)
        rect.set_color(YELLOW_C)
        self.play(Write(rect))
        self.wait(1)

        rect_pack = VGroup(local_tip_pack, rect)

        mini_title = TextMobject("static variable tips")
        bp1_small = TextMobject(" keyword", ":", " static")
        bp2_small = TextMobject(" scope", ":", " available throughout the program")
        bp22_small = TextMobject("and in between function calls")
        bp3_small = TextMobject(" default value", ":", " zero")
        mini_title.set_color(YELLOW_C)
        bp1_small[2].set_color(BLUE)
        bp2_small[2].set_color(BLUE)
        bp22_small.set_color(BLUE)
        bp3_small[2].set_color(BLUE)
        mini_title.scale(0.75)
        bp1_small.scale(0.55)
        bp2_small.scale(0.55)
        bp22_small.scale(0.55)
        bp3_small.scale(0.55)
        mini_title.to_edge(LEFT, buff=8.8)
        bp1_small.to_edge(LEFT, buff=9)
        bp2_small.to_edge(LEFT, buff=9)
        bp22_small.to_edge(LEFT, buff=9)
        bp3_small.to_edge(LEFT, buff=9)
        mini_title.shift([0, -1, 0])
        bp1_small.shift([0, -1.5, 0])
        bp2_small.shift([0, -1.9, 0])
        bp22_small.shift([0, -2.3, 0])
        bp3_small.shift([0, -2.7, 0])

        local_tip_pack_small = VGroup(mini_title, bp1_small, bp2_small, bp22_small, bp3_small)
        rect_small = SurroundingRectangle(local_tip_pack_small, buff=0.2)
        rect_small.set_color(YELLOW_C)
        rect_pack_small = VGroup(local_tip_pack_small, rect_small)

        self.play(Transform(rect_pack, rect_pack_small))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(2)

        ### part 2: example code

        codetitle = TextMobject("Example Program:")
        codetitle.to_edge(LEFT, buff=0.8)
        codetitle.shift([-0.5, 3.5, 0])
        codetitle.scale(0.8)
        self.play(Write(codetitle))
        self.wait(1.5)

        line = Line([-6.3, 3, 0], [-6.3, -3.3, 0])

        # draw the code
        code = VGroup()

        l0 = TextMobject("hashtag include <stdio.h>")  # TODO: what's wrong with #?
        l0.set_color(GREY)
        code.add(l0)

        blank = TextMobject("BLANK LINE")
        blank.set_color(WHITE)
        blank.set_opacity(0)
        code.add(blank)

        l1 = TextMobject("\\textrm{ int}", "\\textrm{ main}", "\\textrm{()}")
        for i, color in zip(l1, [BLUE, PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l1)

        b1 = TextMobject("\\textrm{\\{}")
        b1.set_color(color, WHITE)
        code.add(b1)

        l2 = TextMobject("    \\textrm{ inc}", "\\textrm{();}")
        for i, color in zip(l2, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l2)

        l3 = TextMobject("    \\textrm{ inc}", "\\textrm{();}")
        for i, color in zip(l3, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l3)

        l4 = TextMobject("    \\textrm{ inc}", "\\textrm{();}")
        for i, color in zip(l4, [PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l4)

        b2 = TextMobject("\\textrm{\\}}")
        b2.set_color(color, WHITE)
        code.add(b2)

        l5 = TextMobject("\\textrm{void}", "\\textrm{ inc}", "\\textrm{()}")
        for i, color in zip(l5, [BLUE, PURPLE_C, WHITE]):
            i.set_color(color)
        code.add(l5)

        b3 = TextMobject("\\textrm{\\{}")
        b3.set_color(color, WHITE)
        code.add(b3)

        l6 = TextMobject("    \\textrm{static}", "\\textrm{ int}", "\\textrm{ i}", "\\textrm{ = 1;}")
        for i, color in zip(l6, [YELLOW_C, BLUE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l6)

        l7 = TextMobject("    \\textrm{printf}", "\\textrm{(}", "\\textrm{ \"\%d, \"}", "\\textrm{,}",
                         "\\textrm{ i}", "\\textrm{);}")
        for i, color in zip(l7, [PURPLE_C, WHITE, GREEN, WHITE, RED_E, WHITE]):
            i.set_color(color)
        code.add(l7)

        l8 = TextMobject("    \\textrm{i}", "++;")
        for i, color in zip(l8, [RED_E, WHITE]):
            i.set_color(color)
        code.add(l8)

        b4 = TextMobject("\\textrm{\\}}")
        b4.set_color(color, WHITE)
        code.add(b4)

        for i, l in enumerate(code):
            l.to_edge(LEFT, buff=0.7)
            l.shift([0.2 * (len(l[0].get_tex_string()) - len(l[0].get_tex_string().lstrip())), -0.55 * i + 0.65, 0])

        code.scale(0.8)
        code.shift([0, 2.8, 0])

        l1_x = code[0].get_x() + 0.11  # keeping it as temp value
        l1_y = code[0].get_y()  # keeping it as temp value

        l2_x = code[1].get_x() + 0.11  # keeping it as temp value
        l2_y = code[1].get_y()  # keeping it as temp value

        self.play(FadeInFrom(line, DOWN))

        for l in code:
            self.play(FadeInFrom(l, LEFT), run_time=0.5)
        self.wait(1)
