import pandas as pd
from config import FINAL_DATA_PATH


def generate_report():

    df = pd.read_csv(FINAL_DATA_PATH / "grupo_e_summary.csv")

    report = f"""
# Group E - FIFA World Cup 2026 Analysis

## Team Rankings

{df[['Team', 'Power_Score', 'Points_Form', 'Goal_Difference']].to_string(index=False)}

## Key Insights

- Türkiye appears as the strongest team in the group based on recent form and overall Power Score.
- Australia showed balanced performances and solid defensive metrics throughout the analyzed matches.
- United States demonstrated strong attacking capability but less defensive consistency.
- Paraguay produced the lowest Power Score in the group despite maintaining a relatively stable defensive profile.

## Predicted Standings

1. Türkiye
2. Australia
3. United States
4. Paraguay
"""

    output_path = "reports/resumen_grupo_e.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print("Reporte generado en:", output_path)


if __name__ == "__main__":
    generate_report()