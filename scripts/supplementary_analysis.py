# Day 9 补充分析：每人次旅游收入、城乡居民收入对比
# 这些是"顺带看一看"的补充内容，不是研究核心——不能用这里算出的数字去说
# "全市旅游收入证明了泰山旅游拉动了本地经济"这种话，全市数据和景区数据是不同范围。

import pandas as pd

plt = None  # 如果后面要画图再导入，这里先只做数值计算

df = pd.read_csv('../data/cleaned/analysis_data.csv')  # ← 需要改：换成实际路径
CORE_YEARS = [2019, 2020, 2021, 2022, 2023, 2024]

def get_series(name):
    s = df[df['指标名称'] == name].set_index('年份')['数值']
    return pd.to_numeric(s, errors='coerce').reindex(CORE_YEARS)

domestic_visitors = get_series('国内游客人次')          # 万人次
domestic_revenue  = get_series('国内旅游收入')          # 亿元
urban_income      = get_series('城镇居民人均可支配收入')  # 元
rural_income      = get_series('农村居民人均可支配收入')  # 元
income_ratio      = get_series('城乡居民收入比(农村=1)')  # 城镇/农村

# ---------- 第一步：每人次国内旅游收入 ----------
# 公式：收入(亿元) / 人次(万人次) * 10000 = 元/人次
# (亿=10^8, 万=10^4，相除后还差10^4才回到"元"，所以乘10000)
per_capita_revenue = domestic_revenue / domestic_visitors * 10000
print("每人次国内旅游收入(元/人次)：", per_capita_revenue.round(1).to_dict())

# ---------- 第二步：城乡收入的两种看法——倍数 vs 绝对差 ----------
absolute_gap = urban_income - rural_income  # 元
print("\n城乡居民收入比(城镇/农村，表里现成的)：", income_ratio.to_dict())
print("城乡收入绝对差(城镇-农村，元)：", absolute_gap.to_dict())

gap_change_pct = (absolute_gap.loc[2024] / absolute_gap.loc[2019] - 1) * 100
ratio_change = income_ratio.loc[2024] - income_ratio.loc[2019]
print(f"\n2019→2024：收入比从{income_ratio.loc[2019]}降到{income_ratio.loc[2024]}"
      f"(变化{ratio_change:.2f})，但绝对差距从{absolute_gap.loc[2019]}元涨到"
      f"{absolute_gap.loc[2024]}元(涨了{gap_change_pct:.1f}%)")
print("——这说明「倍数缩小」和「绝对差距缩小」是两回事，不能只看比值就说城乡差距在改善。")

# ---------- 第三步：城镇/农村各自的名义增长率 ----------
urban_growth = urban_income.pct_change() * 100
rural_growth = rural_income.pct_change() * 100
print("\n城镇居民收入同比增长率(%,名义)：", urban_growth.round(1).to_dict())
print("农村居民收入同比增长率(%,名义)：", rural_growth.round(1).to_dict())
print("农村每年的增长率都比城镇高，这是收入比逐年缩小的直接原因。")

# ---------- 第四步：这几年CPI很低，名义和实际差别不大 ----------
cpi = get_series('居民消费价格指数CPI涨幅')  # 已经是"涨幅"，不是"上年=100"那种格式
print("\nCPI涨幅(%)：", (cpi*100).round(2).to_dict())
print("2023、2024年CPI涨幅接近0甚至为负，说明这两年名义收入增长和实际购买力增长差别很小，"
      "不需要像其他年份那样特别强调名义/实际的区别。")
