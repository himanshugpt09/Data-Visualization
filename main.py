"""
Employee Performance Analysis with 100 Employees
Email: 24f1002302@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employee_performance_100.csv")
# -------------------------------
# Step 2: Frequency count for R&D department
# -------------------------------
rd_count = (df["department"] == "R&D").sum()
print("Frequency count for R&D department:", rd_count)

# -------------------------------
# Step 3: Histogram of department distribution
# -------------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="department", palette="viridis")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")

# -------------------------------
# Step 4: Save visualization as HTML
# -------------------------------
from matplotlib.backends.backend_svg import FigureCanvasSVG

# Export plot as SVG, then embed into HTML
canvas = FigureCanvasSVG(plt.gcf())
svg_output = "employee_department_distribution.svg"
canvas.print_svg(svg_output)

html_content = f"""
<html>
<head><title>Employee Performance Analysis</title></head>
<body>
<h2>Employee Performance Analysis (100 Employees)</h2>
<p><b>Email:</b> 24f1002302@ds.study.iitm.ac.in</p>
<p>Frequency count for R&D department: {rd_count}</p>
<object type="image/svg+xml" data="{svg_output}" width="600" height="450"></object>
</body>
</html>
"""

with open("employee_performance_analysis.html", "w") as f:
    f.write(html_content)

print("Analysis complete! File saved as employee_performance_analysis.html")
