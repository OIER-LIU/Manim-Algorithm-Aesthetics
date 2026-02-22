from manim import *

class Knapsack(Scene):
    def construct(self):
        # ====================
        # 第一幕：标题与引言
        # ====================
        title = Text("算法解析：背包问题", font_size=42)
        subtitle = Text("Knapsack Problem", font_size=28, color=GRAY).next_to(title, DOWN)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=2)
        self.wait(2)
        
        # 移至左上角
        self.play(
            title.animate.scale(0.7).to_edge(UP).shift(LEFT * 3.5),
            FadeOut(subtitle),
            run_time=2
        )
        self.wait(1)

        # ====================
        # 第二幕：问题定义 (左侧动画，右侧说明)
        # ====================
        # --- 左侧：视觉元素 ---
        bag = VGroup(
            Rectangle(width=3, height=3.5, color=BLUE, stroke_width=4),
            Text("背包容量 W = 5", font_size=24, color=BLUE).move_to(DOWN * 2)
        )
        
        items = VGroup(
            self.create_item(1, 2, 3), # 物品1: 重量2, 价值3
            self.create_item(2, 3, 4), # 物品2: 重量3, 价值4
            self.create_item(3, 4, 5)  # 物品3: 重量4, 价值5
        ).arrange(RIGHT, buff=0.4).next_to(bag, UP, buff=0.8)
        
        visual_group = VGroup(bag, items).move_to(LEFT * 3.5)

        # --- 右侧：文字描述 ---
        desc_group = VGroup(
            Text("给定一组物品，每种物品都有", font_size=22),
            Text("自己的重量 (w) 和价值 (v)。", font_size=22),
            Text("目标：在不超过背包总容量的前提下，", font_size=22),
            Text("使得背包中物品的总价值最大化。", font_size=22, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # 强制限制最大宽度并放置在右侧半区
        desc_group.set_max_width(6).move_to(RIGHT * 3.5)

        self.play(FadeIn(bag), run_time=2)
        self.play(FadeIn(items), run_time=3)
        self.wait(1)
        self.play(Write(desc_group), run_time=5)
        self.wait(5)

        # ====================
        # 第三幕：数学建模
        # ====================
        self.play(FadeOut(desc_group))
        
        math_title = Text("数学模型：", font_size=24, color=GREEN)
        eq_obj = MathTex(r"\max \sum_{i=1}^{n} v_i x_i", font_size=32)
        eq_cond = MathTex(r"\text{s.t.} \sum_{i=1}^{n} w_i x_i \le W", font_size=32)
        eq_x = MathTex(r"x_i \in \{0, 1\}", font_size=32)
        
        math_group = VGroup(math_title, eq_obj, eq_cond, eq_x).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        math_group.set_max_width(6).move_to(RIGHT * 3.5)

        self.play(Write(math_group[0]), run_time=1)
        self.play(Write(math_group[1]), run_time=2)
        self.wait(3)
        self.play(Write(math_group[2]), Write(math_group[3]), run_time=3)
        self.wait(5)

        # ====================
        # 第四幕：动态规划方程 (严格防止超宽与重叠)
        # ====================
        self.play(FadeOut(math_group))
        
        dp_title = Text("动态规划 (Dynamic Programming)", font_size=22, color=GREEN)
        
        dp_def = Text("状态定义：", font_size=20)
        dp_state = MathTex(r"dp[i][j]", font_size=26)
        dp_def2 = Text("前i个物品，容量为j时的最大价值", font_size=18, color=GRAY)
        state_group = VGroup(dp_state, dp_def2).arrange(RIGHT, buff=0.2)
        
        dp_eq_title = Text("状态转移方程：", font_size=20)
        
        dp_eq1 = MathTex(r"dp[i][j] = dp[i-1][j]", font_size=24)
        dp_eq_cond1 = MathTex(r"(j < w_i)", font_size=20, color=RED)
        eq1_group = VGroup(dp_eq1, dp_eq_cond1).arrange(RIGHT, buff=0.2)
        
        # 拆分或缩小长公式防止溢出屏幕边界
        dp_eq2 = MathTex(r"dp[i][j] = \max(dp[i-1][j], dp[i-1][j-w_i] + v_i)", font_size=24)
        dp_eq_cond2 = MathTex(r"(j \ge w_i)", font_size=20, color=GREEN)
        eq2_group = VGroup(dp_eq2, dp_eq_cond2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        dp_group = VGroup(
            dp_title, dp_def, state_group, 
            dp_eq_title, eq1_group, eq2_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # 核心防溢出设定：不论多长，强制缩放到右半边宽度(6单位)以内
        dp_group.set_max_width(6.2).move_to(RIGHT * 3.5)

        self.play(Write(dp_group[0:3]), run_time=4)
        self.wait(4)
        self.play(Write(dp_group[3:5]), run_time=3)
        self.wait(3)
        self.play(Write(dp_group[5]), run_time=3)
        self.wait(5)

        # ====================
        # 第五幕：推导表格 (逻辑彻底分离)
        # ====================
        # 必须同时淡出左侧图形和右侧所有公式，保证画布干净
        self.play(FadeOut(visual_group), FadeOut(dp_group))
        
        # 左侧：构建表格
        table = Table(
            [["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"]],
            row_labels=[Text("i=0", font_size=20), Text("i=1", font_size=20), Text("i=2", font_size=20), Text("i=3", font_size=20)],
            col_labels=[Text("j=0", font_size=20), Text("j=1", font_size=20), Text("j=2", font_size=20), Text("j=3", font_size=20), Text("j=4", font_size=20), Text("j=5", font_size=20)],
            include_outer_lines=True
        ).scale(0.5)
        
        table.set_max_width(6).move_to(LEFT * 3.5 + DOWN * 0.5)
        table_title = Text("推导过程图解：", font_size=24, color=YELLOW).next_to(table, UP, buff=0.5)
        
        self.play(FadeIn(table_title), Create(table), run_time=3)
        self.wait(2)

        dp_matrix = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 3, 3, 3, 3],
            [0, 0, 3, 4, 4, 7],
            [0, 0, 3, 4, 5, 7]
        ]
        
        for r in range(2, 6):
            for c in range(3, 8):
                self.remove(table.get_entries((r, c)))

        # 右侧动态信息区 (不再和原本的公式挤在一起)
        right_panel_center = RIGHT * 3.5 + UP * 1
        
        for i in range(1, 4):
            w_i = [0, 2, 3, 4][i]
            v_i = [0, 3, 4, 5][i]
            
            hint = Text(f"当前推导物品 {i}: w={w_i}, v={v_i}", font_size=24, color=YELLOW)
            hint.move_to(right_panel_center)
            
            self.play(FadeIn(hint), run_time=1)

            for j in range(1, 6):
                val = dp_matrix[i][j]
                new_entry = Text(str(val), font_size=20).move_to(table.get_cell((i+2, j+2)).get_center())
                
                cell_box = SurroundingRectangle(table.get_cell((i+2, j+2)), color=YELLOW, stroke_width=2)
                self.play(Create(cell_box), run_time=0.4)
                self.wait(0.5)
                self.play(Write(new_entry), run_time=0.5)
                self.play(FadeOut(cell_box), run_time=0.4)
                
            self.wait(2)
            self.play(FadeOut(hint), run_time=1)

        # ====================
        # 第六幕：结论
        # ====================
        final_ans_box = SurroundingRectangle(table.get_cell((5, 7)), color=RED, stroke_width=3)
        self.play(Create(final_ans_box), run_time=1.5)
        
        concl_group = VGroup(
            Text("最优解为：7", font_size=32, color=RED),
            Text("选择了物品 1 和 物品 2", font_size=24)
        ).arrange(DOWN, buff=0.5).move_to(RIGHT * 3.5 + DOWN * 0.5)
        
        self.play(Write(concl_group), run_time=2)
        self.wait(5)
        
        outro = Text("感谢您的观看", font_size=32).move_to(RIGHT * 3.5 + DOWN * 3)
        self.play(Write(outro), run_time=2)
        self.wait(4)

    def create_item(self, idx, weight, value):
        box = Rectangle(width=0.8, height=0.8, fill_color=ORANGE, fill_opacity=0.6, stroke_width=2)
        i_text = Text(f"#{idx}", font_size=16).move_to(box.get_top() + DOWN * 0.2)
        w_text = Text(f"w:{weight}", font_size=14).next_to(i_text, DOWN, buff=0.1)
        v_text = Text(f"v:{value}", font_size=14).next_to(w_text, DOWN, buff=0.1)
        return VGroup(box, i_text, w_text, v_text)
