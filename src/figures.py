import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# --- 日本語フォントの設定（Windows標準） ---
plt.rcParams['font.family'] = 'MS Gothic'

# =====================================================================
# エピソード 1 (ep010) の図生成
# =====================================================================
def create_ep010_figs():
    output_dir = Path("output/ep010")
    output_dir.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------
    # ep010 - fig1: AI/機械学習の全体像
    # --------------------------------------------------
    output_file = output_dir / "fig1.png"
    fig, ax = plt.subplots(figsize=(16, 9.5))
    fig.patch.set_facecolor('white') # 背景白
    ax.set_xlim(0, 1600)
    ax.set_ylim(0, 950)
    ax.invert_yaxis() # (0,0)を左上に
    ax.axis('off')

    boxes = [
        (170, 85, 1370, 830, "#1E90FF"), # AI
        (10, 190, 1240, 600, "#E8651E"),  # 統計処理
        (455, 265, 1050, 595, "#7FB800"), # 機械学習
        (660, 350, 810, 490, "#A040C0"),  # 深層学習
        (1130, 385, 320, 430, "#FF0000"), # Transformer
        (1190, 615, 240, 140, "#E8B800")  # LLM
    ]

    for x, y, w, h, color in boxes:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=10", 
                                      linewidth=2, edgecolor=color, facecolor=color, alpha=0.2)
        ax.add_patch(rect)

    texts = [
        (800, 45, "AI/機械学習の全体像", 30, "#555555"),
        (1330, 135, "ルールベースシステム", 20, "#555555"),
        (430, 135, "AI(人工知能)", 28, "#1E90FF"),
        (300, 235, "統計処理", 26, "#E8651E"),
        (90, 410, "平均", 18, "#555555"), (90, 485, "分散", 18, "#555555"), (90, 560, "最大/最小", 18, "#555555"),
        (335, 335, "検定", 18, "#555555"), (335, 410, "区間推定", 18, "#555555"), (335, 500, "相関分析", 18, "#555555"),
        (700, 310, "機械学習", 26, "#7FB800"),
        (565, 430, "ベイズ", 18, "#555555"), (565, 525, "ガウス推定", 18, "#555555"),
        (845, 405, "深層学習", 24, "#A040C0"),
        (850, 525, "MLP", 18, "#555555"), (920, 615, "CNN", 18, "#555555"), (860, 700, "RNN", 18, "#555555"),
        (1260, 445, "Transformer", 24, "#FF0000"),
        (1350, 505, "Attention", 18, "#555555"), (1350, 555, "BERT", 18, "#555555"),
        (1350, 670, "LLM", 24, "#E8B800"), (1350, 720, "ChatGPT", 18, "#555555")
    ]

    for x, y, text, size, color in texts:
        ax.text(x, y, text, fontsize=size, color=color, ha='center', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Saved: {output_file}")


    # --------------------------------------------------
    # ep010 - fig2: 回帰と分類のベン図風
    # --------------------------------------------------
    output_file = output_dir / "fig2.png"
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 600)
    ax.invert_yaxis()
    ax.axis('off')

    rect1 = patches.FancyBboxPatch((50, 100), 750, 450, boxstyle="round,pad=0,rounding_size=30", 
                                   linewidth=2, edgecolor="#FFD700", facecolor="#FFEDAA")
    ax.add_patch(rect1)

    rect2 = patches.FancyBboxPatch((850, 100), 300, 450, boxstyle="round,pad=0,rounding_size=30", 
                                   linewidth=2, edgecolor="#8FBC8F", facecolor="#C1E1C1")
    ax.add_patch(rect2)

    circle1 = patches.Circle((250, 350), 150, facecolor="#95A5A6", edgecolor="#2C3E50", linewidth=2)
    ax.add_patch(circle1)
    circle2 = patches.Circle((550, 350), 150, facecolor="#F39C12", edgecolor="#D35400", linewidth=2, alpha=0.7)
    ax.add_patch(circle2)

    texts = [
        (600, 50, "機械（深層）学習", 35),
        (425, 150, "教師あり学習", 25),
        (1000, 150, "教師なし学習", 25),
        (250, 350, "回帰", 40),
        (550, 350, "分類", 40),
        (1000, 350, "クラスタ\n自己回帰", 25)
    ]

    for x, y, text, size in texts:
        ax.text(x, y, text, fontsize=size, ha='center', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Saved: {output_file}")


    # --------------------------------------------------
    # ep010 - fig3: 3つの理由（箇条書き）
    # --------------------------------------------------
    output_file = output_dir / "fig3.png"
    fig, ax = plt.subplots(figsize=(12, 6.75))
    fig.patch.set_facecolor('#F8F9FA')
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 675)
    ax.invert_yaxis()
    ax.axis('off')

    rect_title = patches.FancyBboxPatch((80, 40), 1040, 80, boxstyle="round,pad=0,rounding_size=15", 
                                        linewidth=0, facecolor="#2C3E50")
    ax.add_patch(rect_title)
    ax.text(600, 80, "AIが近年急激に進化した3つの理由（三種の神器）", fontsize=30, color="white", ha='center', va='center', fontweight='bold')

    items = [
        ("① データ量 ［学習教材］", "インターネットとスマホの普及により、テキストや画像など\nAIの教材となる「ビッグデータ」が無限に手に入るようになった。"),
        ("② 計算力 ［学習環境］", "ゲーム用だった「GPU」が深層学習の並列計算にドンピシャでハマり、\n以前は何年もかかっていた計算が、現実的な時間で終わるようになった。"),
        ("③ アルゴリズムの進化 ［学習法］", "画期的なアルゴリズム「Transformer」の発明により、離れた単語同士の\n関係性（Attention）を効率よく学習でき、言語の理解力が飛躍した。")
    ]

    y_start = 160
    y_step = 150
    colors = ["#3498DB", "#E67E22", "#27AE60"]

    for i, (title, desc) in enumerate(items):
        y_base = y_start + i * y_step
        
        rect_bg = patches.FancyBboxPatch((80, y_base), 1040, 120, boxstyle="round,pad=0,rounding_size=10", 
                                         linewidth=1, edgecolor="#DDDDDD", facecolor="white")
        ax.add_patch(rect_bg)
        
        rect_accent = patches.FancyBboxPatch((80, y_base), 20, 120, boxstyle="round,pad=0,rounding_size=10", 
                                             linewidth=0, facecolor=colors[i])
        ax.add_patch(rect_accent)
        rect_cover = patches.Rectangle((90, y_base), 10, 120, facecolor=colors[i], edgecolor="none")
        ax.add_patch(rect_cover)

        # テキストの間隔を微調整 (見出しを30、説明文を90に)
        ax.text(130, y_base + 30, title, fontsize=22, color=colors[i], fontweight='bold', va='center')
        ax.text(130, y_base + 90, desc, fontsize=18, color="#333333", va='center', linespacing=1.6)

    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Saved: {output_file}")



# =====================================================================
# エピソード 2 (ep020) の図生成
# =====================================================================
def create_ep020_figs():
    OUTPUT_DIR = Path('output/ep020')
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    np.random.seed(42)
    N = 30
    x = np.random.uniform(0, 10, N)
    TRUE_W, TRUE_B = 0.8, 1.0
    y = TRUE_W * x + TRUE_B + np.random.normal(0, 0.8, N)

    BLUE   = '#1f77b4'
    RED    = '#d62728'
    ORANGE = '#ff7f0e'
    DARK   = '#1a2332'

    def base_ax(ax, xlabel='x', ylabel='y', xlim=(0,10), ylim=(0,10)):
        ax.set_xlabel(xlabel, fontsize=13, labelpad=10)
        ax.set_ylabel(ylabel, fontsize=13, labelpad=15, rotation=90)
        ax.set_xlim(*xlim)
        if ylim is not None:
            ax.set_ylim(*ylim)
        ax.grid(True, linestyle='--', alpha=0.4, zorder=0)
        ax.set_axisbelow(True)

    def scatter(ax):
        ax.scatter(x, y, color=BLUE, s=60, alpha=0.8,
                   edgecolors='white', linewidths=1.2, zorder=3)

    def save(fig, name):
        path = OUTPUT_DIR / name
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f'Saved: {path}')

    # ════════════════════════════════════════════════════════
    # 図1：散布図
    # ════════════════════════════════════════════════════════
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter(ax)
    base_ax(ax)
    plt.tight_layout()
    save(fig, 'fig1.png')

    # ════════════════════════════════════════════════════════
    # 図2：散布図 ＋ 赤い直線（w・b 凡例）
    # ════════════════════════════════════════════════════════
    W_INIT, B_INIT = 0.5, 2.5
    x_line = np.array([0, 10])

    fig, ax = plt.subplots(figsize=(8, 6))
    scatter(ax)
    ax.plot(x_line, W_INIT * x_line + B_INIT, color=RED, linewidth=2.2, zorder=4)
    ax.text(0.04, 0.96, f'w = {W_INIT}\nb = {B_INIT}',
            transform=ax.transAxes, fontsize=12, color=RED, fontweight='bold',
            va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=RED, alpha=0.85))
    base_ax(ax)
    plt.tight_layout()
    save(fig, 'fig2.png')

    # ════════════════════════════════════════════════════════
    # 図3：最小二乗法（誤差補助線 ＋ Loss 表示）
    # ════════════════════════════════════════════════════════
    y_pred2 = W_INIT * x + B_INIT
    loss3   = np.sum((y - y_pred2) ** 2)

    fig, ax = plt.subplots(figsize=(8, 6))
    for xi, yi, ypi in zip(x, y, y_pred2):
        ax.plot([xi, xi], [yi, ypi], color=ORANGE, linestyle='dotted',
                linewidth=1.5, zorder=2)
    ax.plot(x_line, W_INIT * x_line + B_INIT, color=RED, linewidth=2.2, zorder=4)
    scatter(ax)
    ax.text(0.04, 0.96, f'w = {W_INIT}\nb = {B_INIT}',
            transform=ax.transAxes, fontsize=12, color=RED, fontweight='bold',
            va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=RED, alpha=0.85))
    ax.text(0.97, 0.04,
            r'L = $\sum_i\,(y_i - (w\cdot x_i + b))^2$' + f'\nLoss = {loss3:.2f}',
            transform=ax.transAxes, fontsize=11, color='#333333', fontweight='bold',
            va='bottom', ha='right',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor='#888888', alpha=0.85))
    base_ax(ax)
    plt.tight_layout()
    save(fig, 'fig3.png')

    # ════════════════════════════════════════════════════════
    # 図4：w–Loss 二次曲線 ＋ 接線（勾配）
    # ════════════════════════════════════════════════════════
    B_FIXED = 2.5
    w_range = np.linspace(-1.5, 1.0, 300)

    def compute_loss(w, b):
        return np.sum((y - (w * x + b)) ** 2)

    loss_vals = np.array([compute_loss(w, B_FIXED) for w in w_range])

    W_CUR   = -0.5
    L_CUR   = compute_loss(W_CUR, B_FIXED)
    dw      = 1e-5
    grad    = (compute_loss(W_CUR + dw, B_FIXED) -
               compute_loss(W_CUR - dw, B_FIXED)) / (2 * dw)
    t_half  = 0.25
    w_tan   = np.array([W_CUR - t_half, W_CUR + t_half])
    l_tan   = L_CUR + grad * (w_tan - W_CUR)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(w_range, loss_vals, color=BLUE, linewidth=2.5, zorder=3)
    ax.plot(w_tan, l_tan, color=RED, linewidth=2.0, linestyle='--', zorder=4)
    ax.text(w_tan[0] - 0.18, l_tan[0] - 80, 'dL/dw',
            fontsize=12, color=RED, fontweight='bold', va='top', ha='left')
    ax.plot(W_CUR, L_CUR, 'o', color=RED, markersize=9, zorder=5)
    base_ax(ax, xlabel='w', ylabel='Loss', xlim=(-1.5, 1.0), ylim=(0, None))
    plt.tight_layout()
    save(fig, 'fig4.png')

    # ════════════════════════════════════════════════════════
    # 図8：学習前（破線）→ 学習後（実線）
    # ════════════════════════════════════════════════════════
    W_PRE, B_PRE   = 0.1, 0.3
    W_POST, B_POST = TRUE_W, TRUE_B

    fig, ax = plt.subplots(figsize=(8, 6))
    scatter(ax)
    ax.plot(x_line, W_PRE  * x_line + B_PRE,  color=RED, linewidth=2.2,
            linestyle='--', zorder=4)
    ax.plot(x_line, W_POST * x_line + B_POST, color=RED, linewidth=2.2,
            linestyle='-',  zorder=4)

    x_arr = 5.0
    ax.annotate('',
                xy=(x_arr, W_POST * x_arr + B_POST - 0.15),
                xytext=(x_arr, W_PRE  * x_arr + B_PRE  + 0.15),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.8))

    x_lbl = 8.0
    ax.text(x_lbl, W_PRE  * x_lbl + B_PRE  + 0.2, 'pre learning',
            fontsize=11, color=RED, fontweight='bold', va='bottom', ha='left')
    ax.text(x_lbl, W_POST * x_lbl + B_POST + 0.2, 'post learning',
            fontsize=11, color=RED, fontweight='bold', va='bottom', ha='left')

    base_ax(ax)
    plt.tight_layout()
    save(fig, 'fig8.png')


# =====================================================================
# メイン実行処理
# =====================================================================
if __name__ == "__main__":
    print("--- ep010 の画像を出力します ---")
    create_ep010_figs()
    
    print("\n--- ep020 の画像を出力します ---")
    create_ep020_figs()
    
    print("\nすべての画像の出力が完了しました！")