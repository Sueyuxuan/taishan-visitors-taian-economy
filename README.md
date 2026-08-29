# 泰山景区客流规模与泰安市经济指标同步性研究
# Tourist Volume of Mount Tai and Synchronicity with Tai'an Municipal Economic Indicators

## 项目简介 / Project Overview

本项目研究泰山景区游客规模(2016-2025)与泰安市地方经济指标之间的同步性关系,尝试用相关性分析、回归分析等统计方法,检验旅游规模的变化是否、以及在多大程度上与地方经济指标(GDP、第三产业增加值、社会消费品零售总额、财政收入等)同步波动。

This project investigates the synchronicity between Mount Tai's tourist volume (2016-2025) and Tai'an's municipal economic indicators. Using correlation and regression analysis, it examines whether — and to what extent — changes in tourism scale co-move with local economic indicators such as GDP, tertiary sector value-added, retail sales, and fiscal revenue. 

## 研究背景与动机 / Background and Motivation

我在泰山脚下长大。这些年我注意到:尤其是周末和小长假,泰山山门口经常排长队、缆车站十分拥挤。我从身边长辈的闲聊中得到一个尚未核实的印象——本地居民收入似乎没有随游客数量同步增长。这让我很好奇——泰山每年吸引这么多游客,这种旅游规模的增长,是否真的与本地经济指标同步变化?这个问题(以及由此产生的一个尚未验证的猜测:游客数量增长与本地经济价值增长可能并不同步)是我做这项研究最初的动机。详细的观察记录与猜测标注见 [logs/research_log.md](logs/research_log.md)。

I grew up at the foot of Mount Tai. Over the years I've noticed that, especially on weekends and short holidays, the gate to Mount Tai is often crowded with long queues, and the cable car stations get very busy. From conversations among adults around me, I've formed an unverified impression that local residents' incomes haven't grown in step with rising visitor numbers. This made me curious: if Mount Tai attracts so many tourists every year, does this growth in tourism scale actually move in sync with local economic indicators? This question — along with the unverified hypothesis it raises, that growth in tourist volume may not be synchronized with growth in local economic value — is the starting point of this research. Detailed observations and hypothesis notes are logged in [logs/research_log.md](logs/research_log.md).

## 研究范围说明 / Scope and Adjustments

最初的研究计划以"泰安市全市旅游规模"作为核心变量,但在数据收集过程中发现,全市口径的游客数据在部分年份(如2017、2025)存在缺失或统计口径不一致(境内外游客 vs 国内游客)。相比之下,泰山景区"进山人数"这一指标的时间序列更为完整。因此,本研究将核心解释变量调整为泰山景区进山人数,并计划通过稳健性检验(即用全市口径数据重复分析),验证这一替代变量的合理性。

The initial research plan used "Tai'an's citywide tourist volume" as the core variable. However, during data collection it became clear that citywide figures were missing or used inconsistent definitions in several years (e.g. 2017, 2025 — domestic-only vs. domestic-plus-inbound visitors). In contrast, the "Mount Tai scenic area entry visitor count" has a more complete time series. The research therefore shifted its core explanatory variable to Mount Tai's entry visitor count, with a robustness check (repeating the analysis using citywide data) planned to validate this substitution.

## AI工具使用说明 / AI Tool Assistance

本项目在不同阶段使用了 AI 工具,具体分工如下,以便读者判断每一项结论的责任归属:

| 环节 | 谁做的 | 说明 |
|---|---|---|
| 研究问题的提出与调整 | 本人 | 包括最初的观察、猜测,以及2026-08-28对研究问题的收窄 |
| 数据来源检索、定位 | AI 工具(Google NotebookLM、Claude)辅助 + 本人 | AI 帮助搜索和定位可能的官方文件链接;是否采用、如何解读由本人判断 |
| 原文逐项核对 | 本人亲自完成 | 所有标注"已核实"的数据,均由本人打开官方原文(统计公报、统计年鉴、评级报告等)逐项对照后确认,过程记录于 [logs/research_log.md](logs/research_log.md) |
| 数据冲突的判断与取舍(如口径优先级、候选值排除) | 本人 | 判断依据记录于 [docs/data_priority_policy.md](docs/data_priority_policy.md) |
| 研究日志的格式整理、文字润色 | AI 工具(Claude)辅助 | 日志的观察内容、猜测、判断均为本人原始记录;AI 协助统一格式、精简重复表述,不改变记录的事实内容 |
| 最终报告的分析与写作 | 本人独立完成 | 待补充 |

所有数据结论均经过本人逐项核实官方原文后确认,不存在未经本人核实、仅凭 AI 输出即采信的数据。过程记录见 [logs/research_log.md](logs/research_log.md)。

This project used AI tools at different stages; the division of labor is listed above so readers can judge where responsibility for each conclusion sits. In short: framing the research question, verifying primary sources, and judging data conflicts were done by me personally; AI tools (Google NotebookLM, Claude) assisted with locating candidate sources and with formatting/copyediting the research log. No data point was adopted solely on the basis of an AI-generated claim without my own check against the original source. The process is documented in [logs/research_log.md](logs/research_log.md).

## 数据截止说明 / Data Cutoff Note

本研究的核心分析目前以 **2024 年** 为终点。2025 年数据存在两个限制:(1)《泰安统计年鉴2026》(通常于次年下半年发布,将收录2025年经普查/年报核实后的正式数据)尚未公布,当前v4表格中的2025年数值均来自统计公报或专题解读文章的**初步/快报数**,未来可能被年鉴修订;(2)"全市接待游客总人次""旅游总收入"两项2025年官方数据截至本文档更新时尚未发布。因此:

- 正文的核心图表与结论以 2019-2024 年为准
- 2025 年数据在图表中标注为 **provisional(初步数)**,不纳入核心结论的支撑证据,仅作参考展示
- 待《泰安统计年鉴2026》发布后,将重新核实2025年数据并更新本仓库,更新记录将写入 [logs/research_log.md](logs/research_log.md),不做静默覆盖

This study's core analysis currently ends at **2024**. 2025 data is limited because: (1) the *Tai'an Statistical Yearbook 2026* (which will contain the officially verified 2025 figures) has not yet been published — current 2025 values in the v4 dataset are preliminary/flash figures from bulletins or thematic articles, and may be revised; (2) citywide visitor arrivals and tourism revenue for 2025 had not been officially released as of this update. Accordingly, core charts and conclusions are based on 2019–2024; 2025 figures are marked **provisional** and shown for reference only. This will be revisited once the 2026 yearbook is published, with the update logged (not silently overwritten) in [logs/research_log.md](logs/research_log.md).

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

详见 [docs/data_sources.md](docs/data_sources.md)、[docs/data_priority_policy.md](docs/data_priority_policy.md)(数据来源冲突时的优先级判定规则)

## 当前研究进度 / Current Progress

- [x] 确定研究主题与仓库搭建 / Defined research topic and set up repository
- [x] 数据收集与来源核实(核心变量2016-2024已完整核实;2025年为初步数,详见"数据截止说明") / Data collection and source verification (2016–2024 fully verified; 2025 is provisional — see "Data Cutoff Note")
- [x] 研究问题调整(2026-08-28,详见 [logs/reflection_2026-08-28_research_question_pivot.md](logs/reflection_2026-08-28_research_question_pivot.md)) / Research question revised
- [ ] 描述性分析(指数化对比、比值分析;不做回归,理由见方法论部分) / Descriptive analysis (indexed comparison, ratio analysis; regression intentionally omitted — see methodology)
- [ ] 报告撰写 / Report writing
- [ ] 2025年数据更新(待《泰安统计年鉴2026》发布) / 2025 data update (pending *Tai'an Statistical Yearbook 2026*)

## 关于本仓库 / About This Repository

这是一个个人科研项目,所有数据均来自公开的政府统计资料。

This is a personal research project. All data are drawn from publicly available government statistics.

---
最后更新 / Last updated: 2026-08-24
