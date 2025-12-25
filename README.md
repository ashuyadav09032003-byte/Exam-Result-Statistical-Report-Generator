📊 Exam Result Statistical Report Generator

An AI/ML-based statistical analysis project that automatically analyzes exam results and generates a complete statistical report using Python, Pandas, and Gradio.
The project also provides an interactive web interface for easy usage.

⸻

🚀 Features
	•	Upload exam result CSV file
	•	Calculate:
	•	Mean (Average)
	•	Standard Deviation
	•	Z-Score analysis
	•	Visualize marks distribution using graphs
	•	Interactive web interface using Gradio
	•	Beginner-friendly & easy to extend

⸻

🧠 Project Objective

To automate the analysis of exam results using statistical techniques and provide an easy-to-use system for evaluating student performance.

⸻

🛠️ Technologies Used
	•	Python 3
	•	Pandas – Data analysis
	•	NumPy – Numerical computations
	•	Matplotlib – Data visualization
	•	Gradio – Web interface


📁 Project Structure

Exam_Result_Project/
│
├── data/
│   └── exam_data.csv
│
├── src/
│   ├── main.py        # Core statistical analysis
│   └── app.py         # Gradio web app
│
├── .gitignore
└── README.md

📄 Sample CSV Format


0      6605563  Ashutosh     78
1      6605516     Rahul     85
2      6605342     Priya     92
3      6605523      Neha     60
4      6605687      Aman     55
5      6605761     Karan     40

▶️ How to Run the Project (macOS)

1️⃣ Clone the Repository
git clone https://github.com/ashuyadav09032003-byte/Exam-Result-Statistical-Report-Generator.git
cd Exam-Result-Statistical-Report-Generator

2️⃣ Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install pandas numpy matplotlib gradio

4️⃣ Run Statistical Analysis (Terminal Output)

📊 Output
	•	Student performance table with Z-scores
	•	Mean & standard deviation values
	•	Histogram of marks distribution
	•	Interactive web UI
