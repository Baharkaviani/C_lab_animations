from manim import *
import math

class scene(Scene):
    def construct(self):
        Beginning.construct(self)
        CodeAnalyzer.construct(self)

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
        # part 1: draw the code at left side
        codeTitle = TextMobject("Example Program:")
        codeTitle.to_edge(LEFT, buff=0.8)
        codeTitle.shift([-0.5, 3.5, 0])
        codeTitle.scale(0.8)

        self.play(
            Write(codeTitle)
        )
        self.wait(1.5)

        line = Line([-6.3, 3.2, 0], [-6.3, -3.8, 0])

        # start the code
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

        # part 1: draw the memory at right side
        a1 = 20

        m0_text = TextMobject(f"a")
        m0_text.scale(1.5)
        m0 = Rectangle(height=1, width=4)
        m0_val = TextMobject(f"{a1}")
        m0_val.scale(1.5)
        m0.next_to(m0_text, RIGHT)
        m0_val.next_to(m0_text, 4*RIGHT)

        memory0 = VGroup(*[m0_text, m0, m0_val])
        memory0.shift([2, 0, 0])
        memory0.set_color(BLUE_B)

        # second a (inner block of mani)
        a2 = 10

        m1_text = TextMobject(f"a")
        m1_text.scale(1.5)
        m1 = Rectangle(height=1, width=4)
        m1_val = TextMobject(f"{a2}")
        m1_val.scale(1.5)
        m1.next_to(m1_text, RIGHT)
        m1_val.next_to(m1_text, 4*RIGHT)

        memory1 = VGroup(*[m1_text, m1, m1_val])
        memory1.shift([2, 0, 0])
        memory1.set_color(BLUE_B)

        # part 1: start the analyze
        # TODO: organize the memory
        memory = VGroup(
                    *[
                        VGroup(
                            *[
                                TextMobject(f"m{i}"),
                                Rectangle(height=1, width=4, color=BLUE)
                            ]
                        ).arrange_submobjects(RIGHT)
                        for i in range(8)
                    ]
                ).arrange_submobjects(DOWN, buff=0)

        memory.shift([3, 0, 0])
        self.play(FadeInFrom(memory))
        self.wait(2)
        #self.play(FadeOut(memory))
        self.wait(1)

        # global section
        surr = SurroundingRectangle(l1, buff=0.04, color=BLUE)
        self.play(Write(surr))
        self.wait(0.7)

        self.play(FadeInFrom(memory0))
        self.wait(0.7)

        # main block
        m_surr1 = SurroundingRectangle(l5, buff=0.04, color=RED)
        self.play(ReplacementTransform(surr, m_surr1))
        self.wait(0.7)

        m_surr2 = SurroundingRectangle(b3, buff=0.04, color=RED)
        self.play(ReplacementTransform(m_surr1, m_surr2))
        self.wait(0.7)

        m_surr3 = SurroundingRectangle(l6, buff=0.04, color=RED)
        self.play(ReplacementTransform(m_surr2, m_surr3))
        self.wait(0.7)

        memory0.set_color(RED)
        self.wait(1)

        # inner block in main
        mm_surr1 = SurroundingRectangle(b4, buff=0.04, color=GREEN)
        self.play(ReplacementTransform(m_surr3, mm_surr1))
        self.wait(0.7)

        mm_surr2 = SurroundingRectangle(l7, buff=0.04, color=GREEN)
        self.play(ReplacementTransform(mm_surr1, mm_surr2))
        self.wait(0.7)

        self.play(FadeInFrom(memory1))
        self.wait(0.7)

        memory0.set_color(BLUE_B)
        self.wait(1)

        self.wait()