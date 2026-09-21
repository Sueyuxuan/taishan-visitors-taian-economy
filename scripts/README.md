# scripts/ 文件夹说明

这里的 Python 脚本对应研究计划 Day 7（核心对比图）和 Day 8（换基期敏感性检查）。
每个脚本都有两个版本：`.py`（普通脚本）和 `.ipynb`（notebook，可以一格一格运行，方便看中间结果）。

## 环境准备（只需要做一次）

```
pip install pandas matplotlib
```

如果要用 notebook 版本，还需要：
```
pip install jupyter
```

如果电脑上还没有 Python，直接装 Anaconda 最省事——pandas、matplotlib、jupyter 都自带，不用分开装。

## 怎么运行

**用普通脚本**：在终端里进入 `scripts/` 文件夹，然后：
```
python plot_core_comparison.py
python sensitivity_check.py
```

**用 notebook**（推荐，方便逐步核对）：打开 Jupyter Notebook，导航到 `scripts/` 文件夹，
打开对应的 `.ipynb` 文件，从上到下依次运行每个格子。

脚本会自动读取 `../data/cleaned/analysis_data.csv`，把图保存到 `../analysis/figures/`（这个文件夹要提前手动建好，脚本不会自动创建）。

## 用之前必须做的事

1. 脚本里标了 `# ← 需要改` 的地方，换成你电脑上实际的文件路径。
2. **2026-09-20起，这两个脚本的计算不再用Excel交叉核对**（原因见 `docs/research_plan.md` 变更记录）。
   取而代之的是：自己必须能不看代码、用大白话讲清楚每一行在算什么、为什么这么算——
   这个要求比之前更严格，因为少了Excel这一道独立验证。
3. 运行完之后，把输出的数字和 `docs/methodology_notes.md` 里记录的参考值对一下，确认一致。
4. 在 `docs/methodology_notes.md` 里补一段说明这两个脚本是用来做什么的、用了什么方法、
   AI 起草代码后本人做了哪些修改和核对（比如 CSV 数字被读成文字这个bug，是怎么发现并修好的，
   这本身就是一个值得写进方法笔记的"调试过程"）。
