import scipy.stats as stats

# Data for unit density based on die temperature and diameter
# Replace with your actual data
data = {
    'Unit_Density': [73.28, 54.57, 48.01, 70.51, 63.94, 55.60,
                     57.31, 66.03, 50.03, 43.93, 58.03, 53.21,
                     56.55, 54.85, 72.83, 92.04, 86.77, 81.28,
                     64.00, 46.30, 59.14, 46.33, 42.95, 56.75],
    'Die_Temperature': [145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145,
                        155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155],
    'Die_Diameter': [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]
}

# Convert data to DataFrame
import pandas as pd
df = pd.DataFrame(data)
# Perform ANOVA
model = stats.f_oneway(df[df['Die_Diameter'] == 3]['Unit_Density'],
                       df[df['Die_Diameter'] == 4]['Unit_Density'])

# Extract F-statistic and p-value
F_statistic = model.statistic
p_value = model.pvalue

print(f"F-statistic: {F_statistic:.2f}")
print(f"P-value: {p_value:.3f}")