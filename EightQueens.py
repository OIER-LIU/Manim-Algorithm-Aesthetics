from manim import *

class EightQueens(Scene):
    def construct(self):
        # ====================
        # 第一幕：标题与引入 (约 12 秒)
        # ====================
        title = Text("算法解析：八皇后问题", font_size=48)
        subtitle = Text("The Eight Queens Puzzle", font_size=32, color=GRAY).next_to(title, DOWN)
        
        self.play(Write(title), run_time=3)
        self.play(FadeIn(subtitle), run_time=2)
        self.wait(3)
        
        self.play(
            title.animate.scale(0.7).to_edge(UP).shift(LEFT*3),
            FadeOut(subtitle),
            run_time=2
        )
        self.wait(2)

        # ====================
        # 第二幕：规则说明 (约 30 秒)
        # ====================
        # 创建 8x8 棋盘 (放置在左侧)
        board8 = self.create_board(8, 8, square_size=0.6).move_to(LEFT * 3 + DOWN * 0.5)
        
        intro_text_1 = Text("目标：在8×8的棋盘上放置8个皇后", font_size=24).move_to(RIGHT * 3 + UP * 2)
        intro_text_2 = Text("要求：任何两个皇后不能互相攻击", font_size=24).next_to(intro_text_1, DOWN, buff=0.5)
        
        self.play(FadeIn(board8), run_time=3)
        self.wait(1)
        self.play(Write(intro_text_1), run_time=2)
        self.play(Write(intro_text_2), run_time=2)
        self.wait(3)

        rule_title = Text("攻击范围包含：", font_size=24, color=YELLOW).next_to(intro_text_2, DOWN, buff=0.8, aligned_edge=LEFT)
        rule_group = VGroup(
            Text("1. 同一行 (Row)", font_size=22),
            Text("2. 同一列 (Column)", font_size=22),
            Text("3. 对角线 (Diagonal)", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(rule_title, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Write(rule_title), run_time=1.5)
        self.play(Write(rule_group), run_time=4)
        self.wait(4)

        # ====================
        # 第三幕：数学公式表达 (约 18 秒)
        # ====================
        self.play(
            FadeOut(intro_text_1), FadeOut(intro_text_2), 
            FadeOut(rule_title), FadeOut(rule_group)
        )
        
        math_intro = Text("约束条件的数学化表示：", font_size=26).move_to(RIGHT * 3 + UP * 2)
        # 纯公式，无中文字符
        eq_def = MathTex(r"Q_i = (r_i, c_i)", font_size=36)
        eq1 = MathTex(r"r_i \neq r_j", font_size=36)
        eq2 = MathTex(r"c_i \neq c_j", font_size=36)
        eq3 = MathTex(r"|r_i - r_j| \neq |c_i - c_j|", font_size=36)
        
        math_group = VGroup(eq_def, eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(math_intro, DOWN, buff=0.8, aligned_edge=LEFT)

        self.play(Write(math_intro), run_time=2)
        self.play(Write(eq_def), run_time=1.5)
        self.play(Write(eq1), run_time=1.5)
        self.play(Write(eq2), run_time=1.5)
        self.play(Write(eq3), run_time=2)
        self.wait(5)

        # ====================
        # 第四幕：回溯算法演示 - 4皇后 (约 65 秒)
        # ====================
        self.play(FadeOut(board8), FadeOut(math_intro), FadeOut(math_group))
        
        # 使用 4x4 演示以保证过程可被直观理解
        board4 = self.create_board(4, 4, square_size=1.0).move_to(LEFT * 3 + DOWN * 0.5)
        
        trans_text1 = Text("为了直观演示核心的回溯思想", font_size=26).move_to(RIGHT * 3 + UP * 2)
        trans_text2 = Text("我们先来看 4×4 棋盘的推导过程", font_size=26).next_to(trans_text1, DOWN, buff=0.3)
        status_text = Text("开始尝试放置第一行", font_size=24, color=YELLOW).next_to(trans_text2, DOWN, buff=1.0)
        
        self.play(FadeIn(board4), run_time=2)
        self.play(Write(trans_text1), Write(trans_text2), run_time=3)
        self.play(Write(status_text), run_time=1.5)
        self.wait(2)

        # 回溯演示开始
        # 放(0,0)
        q00 = self.get_q(0, 0, board4, size=1.0)
        self.play(FadeIn(q00), run_time=1.5)
        self.wait(2)

        self.play(Transform(status_text, Text("第二行：第1、2列冲突，放置于第3列", font_size=24, color=GREEN).move_to(status_text.get_center())))
        q12 = self.get_q(1, 2, board4, size=1.0)
        self.play(FadeIn(q12), run_time=1.5)
        self.wait(2.5)

        self.play(Transform(status_text, Text("第三行：所有位置均冲突！(死胡同)", font_size=24, color=RED).move_to(status_text.get_center())))
        self.wait(3)

        self.play(Transform(status_text, Text("触发回溯 (Backtracking) : 撤销并尝试新分支", font_size=24, color=YELLOW).move_to(status_text.get_center())))
        self.play(FadeOut(q12), run_time=1.5)
        self.wait(2)

        self.play(Transform(status_text, Text("第二行：改放置于第4列", font_size=24, color=GREEN).move_to(status_text.get_center())))
        q13 = self.get_q(1, 3, board4, size=1.0)
        self.play(FadeIn(q13), run_time=1.5)
        self.wait(2)

        self.play(Transform(status_text, Text("第三行：放置于第2列", font_size=24, color=GREEN).move_to(status_text.get_center())))
        q21 = self.get_q(2, 1, board4, size=1.0)
        self.play(FadeIn(q21), run_time=1.5)
        self.wait(2)

        self.play(Transform(status_text, Text("第四行：无可用位置！再次回溯", font_size=24, color=RED).move_to(status_text.get_center())))
        self.wait(3)

        self.play(Transform(status_text, Text("彻底回溯至第一行，调整初始位置", font_size=24, color=YELLOW).move_to(status_text.get_center())))
        self.play(FadeOut(q21), FadeOut(q13), run_time=2)
        self.play(q00.animate.move_to(board4[0*4 + 1].get_center()), run_time=2)
        self.wait(2)

        self.play(Transform(status_text, Text("加速寻找：最终得到有效解", font_size=24, color=GREEN).move_to(status_text.get_center())))
        q13_new = self.get_q(1, 3, board4, size=1.0)
        q20_new = self.get_q(2, 0, board4, size=1.0)
        q32_new = self.get_q(3, 2, board4, size=1.0)
        self.play(FadeIn(q13_new), FadeIn(q20_new), FadeIn(q32_new), run_time=3)
        self.wait(5)

        # ====================
        # 第五幕：回归8皇后与总结 (约 30 秒)
        # ====================
        self.play(
            FadeOut(board4), FadeOut(q00), FadeOut(q13_new), 
            FadeOut(q20_new), FadeOut(q32_new), 
            FadeOut(trans_text1), FadeOut(trans_text2), FadeOut(status_text)
        )
        
        self.play(FadeIn(board8), run_time=2)

        final_text1 = Text("运用相同的深度优先搜索 (DFS)", font_size=26).move_to(RIGHT * 3 + UP * 2)
        final_text2 = Text("即可解决标准的 8×8 皇后问题", font_size=26).next_to(final_text1, DOWN, buff=0.3)
        final_text3 = Text("共有 92 种合法解法！", font_size=32, color=YELLOW).next_to(final_text2, DOWN, buff=1.0)
        
        self.play(Write(final_text1), Write(final_text2), run_time=3)
        self.wait(2)
        self.play(Write(final_text3), run_time=2)
        self.wait(3)

        # 填入一个标准的八皇后解
        sol_cols = [0, 4, 7, 5, 2, 6, 1, 3]
        qs_8 = VGroup()
        for r, c in enumerate(sol_cols):
            q = self.get_q(r, c, board8, size=0.6)
            qs_8.add(q)
        
        self.play(FadeIn(qs_8), run_time=4)
        self.wait(4)
        
        outro = Text("感谢您的观看", font_size=40).next_to(final_text3, DOWN, buff=1.5)
        self.play(Write(outro), run_time=2)
        self.wait(6)

    # 辅助函数：绘制棋盘
    def create_board(self, rows, cols, square_size):
        board = VGroup()
        for r in range(rows):
            for c in range(cols):
                color = "#DDDDDD" if (r + c) % 2 == 0 else "#666666"
                sq = Square(side_length=square_size, fill_color=color, fill_opacity=1, stroke_width=0.5)
                # 左上角为起点排列
                sq.move_to(RIGHT * c * square_size + DOWN * r * square_size)
                board.add(sq)
        # 整体居中调整，方便后续移动
        board.move_to(ORIGIN)
        return board

    # 辅助函数：生成皇后的图形
    def get_q(self, r, c, board, size=1.0):
        # 使用圆形里面带 Q 字母来代替复杂的矢量图，兼容性最好且不会受限于字体
        dim = int((len(board))**0.5)
        q_icon = VGroup(
            Circle(radius=size*0.35, color=YELLOW, fill_opacity=0.8, stroke_width=2),
            MathTex("Q", color=BLACK, font_size=size*36)
        )
        q_icon.move_to(board[r * dim + c].get_center())
        return q_icon
