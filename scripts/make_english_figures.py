# 生成英文标签版的两张图，供英文版报告使用。
# 计算方法和 plot_core_comparison.py、sensitivity_check.py 完全一样，只有标签、标题、图例是英文。
# 中文版的图和原来两个脚本不受影响。
#
# Make English-labelled versions of the two figures used in the English report.
# The calculations are the same as in plot_core_comparison.py and sensitivity_check.py;
# only the labels are in English. The Chinese figures are not changed.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/cleaned/analysis_data.csv')  # ← 需要改：换成实际路径
CORE_YEARS = [2019, 2020, 2021, 2022, 2023, 2024]

def get_series(name):
    s = df[df['指标名称'] == name].set_index('年份')['数值']
    return pd.to_numeric(s, errors='coerce').reindex(CORE_YEARS)

visitors = get_series('泰山景区进山游客(窄口径)')
tertiary = get_series('第三产业增加值')

# ---------- Figure 1: index and year-on-year growth ----------
visitors_index = visitors / visitors.loc[2019] * 100
tertiary_index = tertiary / tertiary.loc[2019] * 100
visitors_growth = visitors.pct_change() * 100
tertiary_growth = tertiary.pct_change() * 100

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

ax1.plot(CORE_YEARS, visitors_index, marker='o', label='Mount Tai entry visitors', color='#1D9E75')
ax1.plot(CORE_YEARS, tertiary_index, marker='s', label='Tertiary-sector value-added (current prices)', color='#378ADD')
ax1.axhline(100, color='gray', linewidth=0.8, linestyle='--')
ax1.set_ylabel('Index (2019 = 100)')
ax1.set_title("Mount Tai entry visitors and Tai'an tertiary-sector value-added: index (2019 = 100)")
ax1.legend()
ax1.grid(alpha=0.3)

ax2.bar([y - 0.15 for y in CORE_YEARS], visitors_growth, width=0.3,
        label='Entry visitors, year-on-year growth', color='#1D9E75')
ax2.bar([y + 0.15 for y in CORE_YEARS], tertiary_growth, width=0.3,
        label='Tertiary-sector value-added, year-on-year growth (current prices)', color='#378ADD')
ax2.axhline(0, color='black', linewidth=0.8)
ax2.set_ylabel('Year-on-year growth (%)')
ax2.set_xlabel('Year')
ax2.legend(loc='upper left', fontsize=9)  # upper left is empty, so the legend does not cover the 2023 bar
ax2.grid(alpha=0.3)

ax1.annotate('2023: free-admission policy +\nrecovery after the pandemic;\nnote the low base',
             xy=(2023, visitors_index.loc[2023]), xytext=(2019.1, 135),
             fontsize=8, color='#993C1D', ha='left',
             arrowprops=dict(arrowstyle='->', color='#993C1D', lw=0.8,
                              connectionstyle='arc3,rad=0.15'))
ax1.set_ylim(top=max(visitors_index.max(), tertiary_index.max()) * 1.3)  # extra headroom so the legend does not touch the data

plt.tight_layout()
fig.savefig('../analysis/figures/01_core_comparison_en.png', dpi=150, bbox_inches='tight')
print("saved 01_core_comparison_en.png")
plt.close(fig)

# ---------- Figure 2: different base years ----------
def make_index(series, base_year):
    return series / series.loc[base_year] * 100

fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#1D9E75', '#378ADD', '#BA7517']
for base_year, color in zip([2019, 2021, 2022], colors):
    ax.plot(CORE_YEARS, make_index(visitors, base_year), marker='o', color=color,
            label=f'Base year {base_year} = 100')
ax.axhline(100, color='gray', linewidth=0.8, linestyle='--')
ax.set_ylabel('Mount Tai entry-visitor index')
ax.set_xlabel('Year')
ax.set_title('How the entry-visitor index changes with the choice of base year')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
fig.savefig('../analysis/figures/02_sensitivity_base_year_en.png', dpi=150, bbox_inches='tight')
print("saved 02_sensitivity_base_year_en.png")
plt.close(fig)
