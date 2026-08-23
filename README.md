# 泰山景区客流规模与泰安市经济指标同步性研究
# Tourist Volume of Mount Tai and Synchronicity with Tai'an Municipal Economic Indicators

## 项目简介 / Project Overview

本项目研究泰山景区游客规模(2016-2025)与泰安市地方经济指标之间的同步性关系,尝试用相关性分析、回归分析等统计方法,检验旅游规模的变化是否、以及在多大程度上与地方经济指标(GDP、第三产业增加值、社会消费品零售总额、财政收入等)同步波动。

This project investigates the synchronicity between Mount Tai's tourist volume (2016-2025) and Tai'an's municipal economic indicators. Using correlation and regression analysis, it examines whether — and to what extent — changes in tourism scale co-move with local economic indicators such as GDP, tertiary sector value-added, retail sales, and fiscal revenue. 

## 研究背景与动机 / Background and Motivation

我在泰山脚下长大。这些年我注意到:尤其是周末和小长假,泰山山门口经常排长队、缆车站十分拥挤。我从身边长辈的闲聊中得到的印象是,本地居民收入似乎没有随游客数量同步增长——但这只是转述印象,并非我核实过的数据。这让我很好奇——泰山每年吸引这么多游客,这种旅游规模的增长,是否真的与本地经济指标同步变化?这个问题(以及由此产生的一个尚未验证的猜测:游客数量增长与本地经济价值增长可能并不同步)是我做这项研究最初的动机。详细的观察记录与猜测标注见 [logs/research_log.md](logs/research_log.md)。

I grew up at the foot of Mount Tai. Over the years I've noticed that, especially on weekends and short holidays, the gate to Mount Tai is often crowded with long queues, and the cable car stations get very busy. From conversations among adults around me, I've gotten the impression that local residents' incomes haven't grown in step with rising visitor numbers — but this is only a secondhand impression, not data I have verified myself. This made me curious: if Mount Tai attracts so many tourists every year, does this growth in tourism scale actually move in sync with local economic indicators? This question — along with the unverified hypothesis it raises, that growth in tourist volume may not be synchronized with growth in local economic value — is the starting point of this research. Detailed observations and hypothesis notes are logged in [logs/research_log.md](logs/research_log.md).

## 研究范围说明 / Scope and Adjustments

最初的研究计划以"泰安市全市旅游规模"作为核心变量,但在数据收集过程中发现,全市口径的游客数据在部分年份(如2017、2025)存在缺失或统计口径不一致(境内外游客 vs 国内游客)。相比之下,泰山景区"进山人数"这一指标的时间序列更为完整。因此,本研究将核心解释变量调整为泰山景区进山人数,并计划通过稳健性检验(即用全市口径数据重复分析),验证这一替代变量的合理性。

The initial research plan used "Tai'an's citywide tourist volume" as the core variable. However, during data collection it became clear that citywide figures were missing or used inconsistent definitions in several years (e.g. 2017, 2025 — domestic-only vs. domestic-plus-inbound visitors). In contrast, the "Mount Tai scenic area entry visitor count" has a more complete time series. The research therefore shifted its core explanatory variable to Mount Tai's entry visitor count, with a robustness check (repeating the analysis using citywide data) planned to validate this substitution.

## 研究方法概述 / Methodology Overview

*(待补充 / To be expanded)* 本节将在完成理论框架部分后补充,预计包含:相关性分析(PMCC、Spearman等级相关)、显著性假设检验、最小二乘回归、移动平均趋势分解等,所用方法均在A-level考纲范围内。

*(To be expanded)* This section will be filled in after the theoretical framework is drafted. It is expected to cover: correlation analysis (PMCC, Spearman's rank correlation), significance hypothesis testing, least-squares regression, and moving-average trend decomposition — all within the A-level syllabus.

## 仓库结构 / Repository Structure

```
├── README.md
├── logs/           # 研究日志:观察、猜测与决策过程 / Research log: observations, hypotheses, decisions
├── data/           # 原始数据与清理后的分析数据 / Raw and cleaned datasets
├── docs/           # 研究方案说明、数据来源记录 / Research plan and data source documentation
├── analysis/       # 分析过程、图表、计算结果 / Analysis workbooks, charts, and results
└── archive/        # 关键网页存档记录 / Archived copies of key source links
```

## 数据来源 / Data Sources

详见 [docs/data_sources.md](docs/data_sources.md)(文件待建立 / to be added)

## 当前研究进度 / Current Progress

- [x] 确定研究主题与仓库搭建 / Defined research topic and set up repository
- [ ] 数据收集与来源核实 / Data collection and source verification
- [ ] 数据清理 / Data cleaning
- [ ] 相关性与回归分析 / Correlation and regression analysis
- [ ] 报告撰写 / Report writing

## 关于本仓库 / About This Repository

这是一个个人科研项目,所有数据均来自公开的政府统计资料。

This is a personal research project. All data are drawn from publicly available government statistics.

---
最后更新 / Last updated: 2026-08-23
