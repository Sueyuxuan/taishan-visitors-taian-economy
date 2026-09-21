# 低基数/换基期敏感性检查
# 要检验的问题：核心图里"这两条线像不像"这个结论，会不会只是因为选了2019年当基期才这样，
# 换一个基期结论会不会完全变样？
# 这是为了检验旧结论站不站得住脚——如果换个基期图形完全变样，说明原来的结论对基期选择很敏感。

import pandas as pd
import matplotlib.pyplot as plt

# ---------- 第一步：字体设置 + 读取数据 ----------
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'PingFang SC', 'Heiti TC',
                                     'Noto Sans CJK SC', 'Noto Sans CJK JP', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('../data/cleaned/analysis_data.csv')  # ← 需要改：换成实际路径

name_visitors = '泰山景区进山游客(窄口径)'
name_tertiary = '第三产业增加值'
CORE_YEARS = [2019, 2020, 2021, 2022, 2023, 2024]

visitors = pd.to_numeric(
    df[df['指标名称'] == name_visitors].set_index('年份')['数值'], errors='coerce'
).reindex(CORE_YEARS)
tertiary = pd.to_numeric(
    df[df['指标名称'] == name_tertiary].set_index('年份')['数值'], errors='coerce'
).reindex(CORE_YEARS)

print("进山游客(万人)：", visitors.to_dict())

# ---------- 第二步：定义"换基期算指数"的函数 ----------
# 公式和 Day 6/7 用的是同一个：该年数值 / 基期年数值 * 100，只是基期年可以换。
def make_index(series, base_year):
    """以 base_year 为 100，重新算一遍指数。跟 Day 6/7 用的是同一个公式。"""
    return series / series.loc[base_year] * 100

# 试三个不同的基期，看结论稳不稳
BASE_YEARS_TO_TRY = [2019, 2021, 2022]
print("函数定义完成，准备试算三个基期：", BASE_YEARS_TO_TRY)

# ---------- 第三步：画图——三条不同基期的指数曲线放一起比 ----------
fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#1D9E75', '#378ADD', '#BA7517']

for base_year, color in zip(BASE_YEARS_TO_TRY, colors):
    idx = make_index(visitors, base_year)
    ax.plot(CORE_YEARS, idx, marker='o', color=color,
            label=f'以{base_year}年=100')

ax.axhline(100, color='gray', linewidth=0.8, linestyle='--')
ax.set_ylabel('泰山景区进山游客指数')
ax.set_xlabel('年份')
ax.set_title('换不同基期年份，"进山游客"这条线的形状会不会变')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()  # 运行到这里会弹出图片窗口，看完关掉窗口，代码才会继续往下走

# ---------- 第四步：保存图片 ----------
output_path = '../analysis/figures/02_sensitivity_base_year.png'  # ← 需要改
plt.savefig(output_path, dpi=150)
print(f"图已保存到：{output_path}")

# ---------- 第五步：把"低基数效应"量化出来 ----------
# 2023年相对2022年（低基数）涨了多少？相对2019年（疫情前）又涨了多少？
# 这两个数字差很多，就是"低基数效应"最直接的数字证据。
print("2023年游客数相对不同基期的涨幅：")
print(f"  相对2022年(低基数): {(visitors.loc[2023]/visitors.loc[2022]-1)*100:.1f}%")
print(f"  相对2019年(疫情前): {(visitors.loc[2023]/visitors.loc[2019]-1)*100:.1f}%")
print("这两个数字差很多，就是\"低基数效应\"的直接证据——报告里两个都要提，不能只挑一个说。")
