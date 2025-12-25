import os
import pandas as pd
import matplotlib.pyplot as plt

# Find project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to CSV file
data_path = os.path.join(BASE_DIR, "data", "exam_data.csv")

print("Reading data from:", data_path)

# Load data
df = pd.read_csv(data_path)
print("\nStudent Data:")
print(df)

# Statistical calculations
mean_marks = df["Marks"].mean()
std_marks = df["Marks"].std()

print("\nMean Marks:", mean_marks)
print("Standard Deviation:", std_marks)

# Z-score
df["Z_Score"] = (df["Marks"] - mean_marks) / std_marks
print("\nZ-Score Analysis:")
print(df)

# Visualization
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
