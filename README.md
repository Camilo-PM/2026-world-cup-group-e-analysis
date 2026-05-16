# FIFA World Cup 2026 – Group E Team Performance Analysis

## Project Overview

This project analyzes the projected FIFA World Cup 2026 Group E teams using data from each national team's last 10 matches. The analysis focuses on team form, offensive and defensive efficiency, consistency, and overall performance trends ahead of the tournament.

The project combines Python-based data analysis, automated reporting, and Tableau visualizations to generate data-driven insights about the teams competing in Group E.

---

## Teams Analyzed

* Germany
* Ecuador
* Ivory Coast
* Curacao

---

## Objectives

* Analyze recent team performance before the FIFA World Cup 2026
* Compare offensive and defensive efficiency between teams
* Create custom performance indicators and rankings
* Visualize team trends using Tableau dashboards
* Generate reproducible sports analytics workflows

---

## Data Sources

* FBref match logs and national team statistics
* Manually downloaded HTML files for local parsing
* Last 10 matches per national team

---

## Methodology

The project pipeline includes:

1. Data Collection

   * Local FBref HTML parsing using pandas

2. Data Cleaning

   * Match filtering
   * Standardization of results and metrics
   * Goal difference calculations

3. Statistical Analysis

   * Win rate
   * Goals scored and conceded
   * Attack and defense indexes
   * Form index
   * Custom Power Score metric

4. Visualization

   * Team rankings
   * Offensive vs defensive efficiency
   * Goal difference analysis
   * Tableau interactive dashboard

5. Automated Reporting

   * Markdown report generation

---

## Key Metrics

* Matches Played
* Wins / Draws / Losses
* Goals For
* Goals Against
* Goal Difference
* Goals Per Game
* Defensive Efficiency
* Form Index
* Power Score

---

## Key Findings

* Ivory Coast emerged as the most balanced team statistically
* Germany showed the strongest offensive output but weaker defensive stability
* Ecuador demonstrated elite defensive organization but limited offensive production
* Curacao produced strong numbers, although partially influenced by weaker opposition quality

---

## Tableau Dashboard

View the interactive Tableau dashboard here:

https://public.tableau.com/app/profile/camilo.perez5892/viz/GroupETeamPerformanceAnalysisFIFAWorldCup2026/Dashboard1?publish=yes

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Tableau Public
* VS Code
* Git & GitHub

---

## Project Structure

```plaintext
Group E/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── reports/
│   └── figures/
│
├── src/
│
├── dashboard/
│
├── README.md
└── requirements.txt
```

---

## How to Run the Project

```bash
python src/collect_data.py
python src/clean_data.py
python src/analysis.py
python src/visualize.py
python src/report.py
```

---

## Future Improvements

* Full tournament simulation
* Opponent strength weighting
* Expected goals (xG) integration
* Streamlit dashboard deployment
* Multi-group comparative analysis

GitHub
