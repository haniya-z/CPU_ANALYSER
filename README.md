
⚡ CPU Pipeline Analyzer
📌 Problem Statement

Modern CPU architectures use pipelines to improve instruction throughput. However, visualizing and analyzing the pipeline execution stages (Fetch, Decode, Execute, etc.) can be challenging.

This project provides an interactive dashboard to simulate and analyze CPU pipeline behavior in real-time, while also tracking performance metrics like CPI (Cycles Per Instruction) and IPC (Instructions Per Cycle).

🛠 Tech Stack

Backend: Dash (Python)

Graphs & Visualization: Plotly

Styling: Bootswatch (Darkly Theme)

Languages: Python, HTML (via Dash components)

Simulation: Randomized pipeline instruction execution with stalls

🚀 Features

Real-time visualization of CPU Pipeline stages:

Fetch

Decode

Execute

Memory

WriteBack

Heatmap showing instruction execution & stalls

Live calculation and plotting of:

CPI (Cycles Per Instruction)

IPC (Instructions Per Cycle)

Interactive graphs powered by Plotly

Lightweight and runs in the browser

📂 Project Structure
cpu-analyser/
│── backend/
│   └── app.py          # Main application code  
│── requirements.txt     # Dependencies  
│── README.md            # Documentation  

⚙️ Usage
1️⃣ Clone this repository
git clone https://github.com/your-username/cpu-analyser.git  
cd cpu-analyser  

2️⃣ Install dependencies
pip install -r requirements.txt  

3️⃣ Run the app
python backend/app.py  


Then open your browser at:
👉 http://127.0.0.1:8050

📦 Requirements

All dependencies are listed in requirements.txt.
Key packages include:

dash

plotly

numpy

🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss proposed changes.

📄 License

This project is licensed under the MIT License.
