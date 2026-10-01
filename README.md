# 泰山景区客流规模与泰安市经济指标同步性研究
# Tourist Volume of Mount Tai and Synchronicity with Tai'an Municipal Economic Indicators

## 项目简介 / Project Overview

本项目研究泰山景区游客规模(2016-2024,2025年数据待《泰安统计年鉴2026》发布后补充,详见"数据截止说明")与泰安市地方经济指标之间的同步性关系,尝试用相关性分析、回归分析等统计方法,检验旅游规模的变化是否、以及在多大程度上与地方经济指标(GDP、第三产业增加值、社会消费品零售总额、财政收入等)同步波动。

This project investigates the synchronicity between Mount Tai's tourist volume (2016-2024; 2025 data to be added once the *Tai'an Statistical Yearbook 2026* is published — see "Data Cutoff Note") and Tai'an's municipal economic indicators. Using correlation and regression analysis, it examines whether — and to what extent — changes in tourism scale co-move with local economic indicators such as GDP, tertiary sector value-added, retail sales, and fiscal revenue. 

## 研究背景与动机 / Background and Motivation

我在泰山脚下长大。这些年我注意到:尤其是周末和小长假,泰山山门口经常排长队、缆车站十分拥挤。我从身边长辈的闲聊中得到一个尚未核实的印象——本地居民收入似乎没有随游客数量同步增长。这让我很好奇——泰山每年吸引这么多游客,这种旅游规模的增长,是否真的与本地经济指标同步变化?这个问题(以及由此产生的一个尚未验证的猜测:游客数量增长与本地经济价值增长可能并不同步)是我做这项研究最初的动机。详细的观察记录与猜测标注见 [logs/research_log.md](logs/research_log.md)。

I grew up at the foot of Mount Tai. Over the years I've noticed that, especially on weekends and short holidays, the gate to Mount Tai is often crowded with long queues, and the cable car stations get very busy. From conversations among adults around me, I've formed an unverified impression that local residents' incomes haven't grown in step with rising visitor numbers. This made me curious: if Mount Tai attracts so many tourists every year, does this growth in tourism scale actually move in sync with local economic indicators? This question — along with the unverified hypothesis it raises, that growth in tourist volume may not be synchronized with growth in local economic value — is the starting point of this research. Detailed observations and hypothesis notes are logged in [logs/research_log.md](logs/research_log.md).

## 研究范围说明 / Scope and Adjustments

本研究的核心解释变量选用泰山景区进山游客(窄口径),而非全市口径旅游数据,原因有二。其一,研究问题源于对泰山景区本身(山门、缆车站)拥挤程度的直接观察,窄口径客流是与这一观察对应的指标;全市口径数据会混入与泰山无关的区域旅游活动,与研究动机的匹配度反而更低。其二,该指标虽因来源分散(历年统计公报、专项债可行性报告、评级报告等)在原始数据表中一度部分年份标记为"待核实",但经 [docs/data_priority_policy.md](docs/data_priority_policy.md) 案例三、八、九、十、十一、十二记录的多轮独立信源交叉核实,2016-2025年整条序列的口径一致性与数值可信度已得到充分验证。数据表中的"存疑"颜色标记曾滞后于实际核实进度,已于2026-09-17同步更正;该过程(包括此前一度考虑改用全市口径数据、后经核实发现依据不成立的经过)记录于 [logs/reflection_2026-09-17_narrow_gauge_verification_correction.md](logs/reflection_2026-09-17_narrow_gauge_verification_correction.md)。

The core explanatory variable in this study is Mount Tai scenic area's narrow-definition entry visitor count, rather than citywide tourism figures, for two reasons. First, the research question originates from a direct observation of crowding at Mount Tai itself (the gate, the cable car stations); the narrow-gauge visitor count corresponds directly to that observation, whereas citywide figures would mix in tourism activity unrelated to Mount Tai, making them a weaker match for the research motivation. Second, although this indicator was flagged as "unverified" for several years in the raw data table — owing to its scattered sourcing across annual bulletins, bond-issuance feasibility reports, and credit-rating reports — multiple rounds of independent cross-verification documented in [docs/data_priority_policy.md](docs/data_priority_policy.md) (Cases 3, 8, 9, 10, 11, and 12) have since confirmed the definitional consistency and reliability of this series across 2016–2025. The "unverified" color-coding in the data table had lagged behind this completed verification work and was corrected on 2026-09-17; the process — including an earlier, since-abandoned consideration of switching to citywide data — is documented in [logs/reflection_2026-09-17_narrow_gauge_verification_correction.md](logs/reflection_2026-09-17_narrow_gauge_verification_correction.md).

## AI工具使用说明 / AI Tool Assistance

本项目在不同阶段使用了 AI 工具,具体分工如下,以便读者判断每一项结论的责任归属:

| 环节 | 谁做的 | 说明 |
|---|---|---|
| 研究问题的提出与调整 | 本人 | 包括最初的观察、猜测,以及2026-08-28对研究问题的收窄 |
| 数据来源检索、定位 | AI 工具(Google NotebookLM、Claude)辅助 + 本人 | AI 帮助搜索和定位可能的官方文件链接;是否采用、如何解读由本人判断 |
| 原文逐项核对 | 本人亲自完成 | 所有标注"已核实"的数据,均由本人打开官方原文(统计公报、统计年鉴、评级报告等)逐项对照后确认,过程记录于 [logs/research_log.md](logs/research_log.md) |
| 数据冲突的判断与取舍(如口径优先级、候选值排除) | 本人 | 判断依据记录于 [docs/data_priority_policy.md](docs/data_priority_policy.md) |
| 研究日志的格式整理、文字润色 | AI 工具(Claude)辅助 | 日志的观察内容、猜测、判断均为本人原始记录;AI 协助统一格式、精简重复表述,不改变记录的事实内容 |
| 最终报告的分析与写作（中文版） | AI起草初稿 + 本人重写 | AI依据研究提纲起草中文初稿；本人重写全文表述、独立撰写个人经历部分，并在审阅过程中发现并更正了游客数量单位（万人→万人次）标注错误；完整分工说明见两份报告末尾的"写作辅助说明"（[中文版](reports/research_report_zh.md)、[英文版](reports/research_report.md)） |
| 报告英文版 | AI翻译自中文版 | 英文版 [reports/research_report.md](reports/research_report.md) 由AI从中文版翻译，两者有出入时以中文版为准 |

所有数据结论均经过本人逐项核实官方原文后确认,不存在未经本人核实、仅凭 AI 输出即采信的数据。过程记录见 [logs/research_log.md](logs/research_log.md)。

This project used AI tools at different stages; the division of labor is listed above so readers can judge where responsibility for each conclusion sits. In short: framing the research question, verifying primary sources, and judging data conflicts were done by me personally; AI tools (Google NotebookLM, Claude) assisted with locating candidate sources and with formatting/copyediting the research log. No data point was adopted solely on the basis of an AI-generated claim without my own check against the original source. The process is documented in [logs/research_log.md](logs/research_log.md).

## 数据截止说明 / Data Cutoff Note

本研究的核心分析目前以 **2024 年** 为终点。2025 年数据存在两个限制:(1)《泰安统计年鉴2026》(通常于次年下半年发布,**预计2026年11月左右**公布,将收录2025年经普查/年报核实后的正式数据)尚未公布,当前v4表格中的2025年数值均来自统计公报或专题解读文章的**初步/快报数**,未来可能被年鉴修订;(2)"全市接待游客总人次""旅游总收入"两项2025年官方数据截至本文档更新时尚未发布。因此:

- 正文的核心图表与结论以 2019-2024 年为准
- 2025 年数据在图表中标注为 **provisional(初步数)**,不纳入核心结论的支撑证据,仅作参考展示
- 待《泰安统计年鉴2026》发布后,将重新核实2025年数据并更新本仓库,更新记录将写入 [logs/research_log.md](logs/research_log.md),不做静默覆盖

This study's core analysis currently ends at **2024**. 2025 data is limited because: (1) the *Tai'an Statistical Yearbook 2026* (which will contain the officially verified 2025 figures) has not yet been published — it is **expected around November 2026** — and current 2025 values in the v4 dataset are preliminary/flash figures from bulletins or thematic articles, and may be revised; (2) citywide visitor arrivals and tourism revenue for 2025 had not been officially released as of this update. Accordingly, core charts and conclusions are based on 2019–2024; 2025 figures are marked **provisional** and shown for reference only. This will be revisited once the 2026 yearbook is published, with the update logged (not silently overwritten) in [logs/research_log.md](logs/research_log.md).

## 研究方法概述 / Methodology Overview

本研究用到的方法都比较基础，以我在 CIE Economics (9708) 与 Mathematics 课程中学过的内容为主。下面分两组列出：本报告实际用到的，以及学过或考虑过、但这份报告没有用的。

**本报告实际使用的方法**

| 方法 | 用途 |
|---|---|
| 指数化（2019年=100） | 让单位不同的两个指标，可以比较各自相对2019年的变化 |
| 同比增长率 | 观察逐年变化 |
| 换基期比较（基期敏感性展示） | 展示增长率数字对比较起点有多敏感；这不是独立的稳健性检验 |
| 比值与绝对差额 | 比较城乡居民收入的相对差距和金额差距 |
| 每人次收入（收入÷人次） | 延伸讨论中的补充观察，全市口径 |
| 图表与描述性比较 | 呈现趋势，不做因果推断 |

**学过或考虑过，但本报告没有使用的方法**

| 方法 | 说明 |
|---|---|
| 名义值/实际值换算（CPI平减） | 只看过CPI涨幅（2023、2024年接近0），没有用来换算报告里的数字；报告里只说明了第三产业增加值是现价 |
| 人均化处理 | 没有使用 |
| 平均消费倾向（APC） | 没有做 |
| 占比与结构份额分析（如泰山游客占全市游客的比重） | 没有做 |
| 均值、标准差 | 没有计算 |
| 显著性检验、回归 | 刻意不做，原因见下 |

本研究使用的是年度时间序列数据(如GDP、游客量逐年数值),同一变量相邻年份之间高度相关,不满足显著性假设检验(如t检验、卡方检验)所要求的"观测值相互独立"这一前提;样本量也有限(n=6–10),统计功效不足。因此本研究没有采用显著性检验或回归分析,而是以描述性比较为核心方法。

以描述性比较为核心方法,是基于对可用工具边界的判断,而非能力局限——详见[docs/methodology_notes.md](docs/methodology_notes.md)。

The methods used in this study are fairly basic and mostly drawn from what I learned in CIE Economics (9708) and Mathematics. They are listed in two groups below: methods actually used in the report, and methods I have learned or considered but did not use here.

**Methods actually used in the report**

| Method | Purpose |
|---|---|
| Indexing (2019 = 100) | Compare two indicators with different units by their change relative to 2019 |
| Year-on-year growth rate | Track year-by-year change |
| Changing the base year (base-year sensitivity display) | Show how sensitive growth figures are to the comparison year; this is not an independent robustness check |
| Ratio and absolute gap | Compare the relative and absolute urban–rural income gaps |
| Revenue per visit (revenue ÷ visits) | Supplementary observation in the extended discussion; citywide scope |
| Charts and descriptive comparison | Present trends without causal inference |

**Methods learned or considered, but not used in this report**

| Method | Note |
|---|---|
| Nominal/real conversion (CPI deflation) | CPI inflation was looked at (close to zero in 2023 and 2024) but not used to convert figures in the report; the report only notes that tertiary-sector value-added is at current prices |
| Per-capita adjustment | Not used |
| Average propensity to consume (APC) | Not done |
| Share / structure analysis (e.g. Mount Tai visitors as a share of citywide visitors) | Not done |
| Mean, standard deviation | Not computed |
| Significance testing, regression | Deliberately not used; see below |

The data used here are annual time series (e.g. yearly GDP and visitor-volume figures), where adjacent years for the same variable are highly correlated — this violates the independence assumption required by significance tests (e.g. t-tests, chi-squared tests); the sample size is also limited (n=6–10), giving insufficient statistical power. This study therefore does not use significance testing or regression analysis, relying instead on descriptive comparison as its core method.

## 仓库结构 / Repository Structure

```
├── README.md
├── .gitattributes
├── archive/                # 关键网页/文件存档记录 / Archived copies of key sources
│   ├── archive_index.md
│   └── ...(共4份存档文件,详见 archive_index.md)
├── data/
│   ├── raw/
│   │   ├── taian_indicators.xlsx   # 当前使用版本(数据源) / current version in use
│   │   └── archive/                # 历史版本存档,按版本号+日期保留,不覆盖 / archived historical versions, kept by version+date, never overwritten
│   ├── cleaned/            # 清洗后的分析用数据 / Cleaned data for analysis
│   │   ├── analysis_data.xlsx
│   │   └── analysis_data.csv
│   └── data_conflict_audit.csv     # 数字冲突清单 / List of conflicting figures
├── analysis/               # 分析笔记与图表 / Analysis notes and figures
│   ├── core_comparison_analysis.md
│   ├── sensitivity_analysis.md
│   ├── supplementary_analysis_notes.md
│   └── figures/            # 图(中文标签;英文标签版以 _en 结尾) / Figures (Chinese labels; English-labelled versions end in _en)
├── scripts/                # Python 计算与作图脚本(含 .ipynb) / Python scripts for calculation and charts (with .ipynb)
├── reports/
│   ├── research_report.md      # 英文正式版 / English version (formal)
│   └── research_report_zh.md   # 中文版(原文) / Chinese version (original)
├── docs/                   # 数据来源、方法与计划文档 / Data, method and planning documents
│   ├── data_sources.md
│   ├── data_priority_policy.md
│   ├── data_dictionary.md
│   ├── methodology_notes.md
│   ├── research_plan.md
│   └── future_directions.md
└── logs/                   # 研究日志:观察、猜测与决策过程 / Research log: observations, hypotheses, decisions
    ├── research_log.md
    ├── reflection_2026-08-24_data_rebuild.md
    └── reflection_2026-08-28_research_question_pivot.md
```

> `data/raw/` 下只保留一份"当前使用版本"(干净命名,不带版本号/日期),每次更新前先把被替换的旧文件移入 `data/raw/archive/`(保留其原有版本号+日期文件名),不做静默覆盖;更新过程记录于 [logs/research_log.md](logs/research_log.md)。
>
> `data/raw/` keeps only one "current" file (clean name, no version/date suffix). Before each update, the file being replaced is moved into `data/raw/archive/` under its original versioned filename rather than being overwritten; the update is logged in [logs/research_log.md](logs/research_log.md).
>
> `reports/` 里的英文版 `research_report.md` 是正式版，由中文版 `research_report_zh.md` 翻译而来；两者有出入时以中文版为准。配套的分析笔记、数据字典等文档为中文。
>
> In `reports/`, `research_report.md` is the formal English version, translated from the Chinese `research_report_zh.md`; if they differ, the Chinese version is the reference. The supporting notes and the data dictionary are in Chinese.

## 数据来源 / Data Sources

详见 [docs/data_sources.md](docs/data_sources.md)、[docs/data_priority_policy.md](docs/data_priority_policy.md)(数据来源冲突时的优先级判定规则)

## 当前研究进度 / Current Progress

- [x] 确定研究主题与仓库搭建 / Defined research topic and set up repository
- [x] 数据收集与来源核实(核心变量2016-2024已完整核实;2025年为初步数,详见"数据截止说明";2026-09-17核实状态更正、2026-09-29单位标注由"万人"更正为"万人次",详见 [docs/data_conflict_audit.csv](docs/data_conflict_audit.csv)) / Data collection and source verification (2016–2024 fully verified; 2025 is provisional — see "Data Cutoff Note"; verification status corrected 2026-09-17, unit label corrected 2026-09-29 — see [docs/data_conflict_audit.csv](docs/data_conflict_audit.csv))
- [x] 研究问题调整(2026-08-28提出收窄方向,2026-09-15正式定稿最终版本,详见 [logs/reflection_2026-08-28_research_question_pivot.md](logs/reflection_2026-08-28_research_question_pivot.md)) / Research question revised (narrowed 2026-08-28, finalized 2026-09-15)
- [x] 描述性分析(指数化对比、同比增长率、基期敏感性检查、补充分析;不做回归,理由见 [docs/methodology_notes.md](docs/methodology_notes.md)) / Descriptive analysis (indexed comparison, YoY growth, base-year sensitivity check, supplementary analysis; regression intentionally omitted — see [docs/methodology_notes.md](docs/methodology_notes.md))
- [x] 报告撰写与本人理解检查(中文版为原文,初稿完成、交叉复核、本人理解检查均已完成,详见 [reports/research_report_zh.md](reports/research_report_zh.md);英文正式版由中文版翻译而来,详见 [reports/research_report.md](reports/research_report.md)) / Report writing and self-understanding check (the Chinese version is the original; draft, cross-review and self-check all completed — see [reports/research_report_zh.md](reports/research_report_zh.md); the formal English version is translated from it — see [reports/research_report.md](reports/research_report.md))
- [ ] 2025年数据更新(待《泰安统计年鉴2026》发布,预计2026年11月左右) / 2025 data update (pending *Tai'an Statistical Yearbook 2026*, expected around November 2026)
- [ ] 后续研究方向(月度数据、行业细分、跨城市对比等,详见 [docs/future_directions.md](docs/future_directions.md),不计入本轮15天计划) / Future research directions (monthly data, industry breakdown, cross-city comparison, etc. — see [docs/future_directions.md](docs/future_directions.md); not part of this 15-day cycle)

> 项目曾于 2026-09-03 至 2026-09-14 期间因学校考试暂停更新,未发生数据变更,详见 [logs/research_log.md](logs/research_log.md)。原计划2026-10-01至11-12也安排了考试季暂停,但实际因材料提交截止日期优先级更高,未按计划暂停,Day12至Day15连续完成,详见 [docs/research_plan.md](docs/research_plan.md) 变更记录。
>
> Project updates were paused 2026-09-03 to 2026-09-14 for school examinations; no data changes occurred during this period — see [logs/research_log.md](logs/research_log.md). A second pause was originally planned for 2026-10-01 to 11-12, but did not occur in practice because a material-submission deadline took priority; Day 12 through Day 15 were completed without interruption — see the changelog in [docs/research_plan.md](docs/research_plan.md).

## 关于本仓库 / About This Repository

这是一个个人科研项目,所有数据均来自公开的政府统计资料。

This is a personal research project. All data are drawn from publicly available government statistics.

---
最后更新 / Last updated: 2026-10-01
