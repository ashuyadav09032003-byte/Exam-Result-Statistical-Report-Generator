import os
import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr

def analyze_exam(csv_file):
    # Read CSV
    df = pd.read_csv(csv_file.name)

    # Statistics
    mean_marks = df["Marks"].mean()
    std_marks = df["Marks"].std()

    df["Z_Score"] = (df["Marks"] - mean_marks) / std_marks

    # Plot
    plt.figure()
    plt.hist(df["Marks"])
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Students")

    plot_path = "output.png"
    plt.savefig(plot_path)
    plt.close()

    summary = f"""
    Mean Marks: {mean_marks:.2f}
    Standard Deviation: {std_marks:.2f}
    """

    return df, summary, plot_path


interface = gr.Interface(
    fn=analyze_exam,
    inputs=gr.File(label="Upload Exam CSV File"),
    outputs=[
        gr.Dataframe(label="Exam Result Analysis"),
        gr.Textbox(label="Statistical Summary"),
        gr.Image(label="Marks Distribution Graph")
    ],
    title="Exam Result Statistical Report Generator",
    description="Upload exam result CSV to generate statistical analysis"
)

interface.launch()
