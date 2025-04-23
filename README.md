🧠 Natural Language to SQL Query Executor
A Streamlit web application that enables users to upload CSV files and interact with them using natural language queries. The app uses Google's Gemini AI to translate user input into SQL queries, execute them, and display the results — all in real-time.

✨ Features
📁 Upload and explore CSV files

🧠 Convert natural language into SQL using Gemini AI

🗂️ Automatic schema extraction from uploaded data

⚙️ Real-time SQL query execution

📊 Interactive table views of query results

🔄 Reflect changes with live updates to the in-memory database

⚙️ Prerequisites
Python 3.7 or above

A valid Google Gemini API key

🚀 Installation
1. Clone the repository

```bash git clone https://github.com/yourusername/nlp-sql-query-executor.git cd nlp-sql-query-executor```

2. Install dependencies

```bash pip install -r requirements.txt```

3. Set your Gemini API key

Visit Google AI Studio to get your API key.

Replace the placeholder key in app.py with your actual API key.

🧪 Usage
Launch the app

```bash streamlit run app.py```
Open the web browser

Navigate to http://localhost:8501

Upload a CSV file

Start asking natural language queries like:

"Show all rows where revenue is greater than 10,000"

"What is the average age of customers?"

📁 Project Structure
graphql
Copy
Edit
nlp-sql-query-executor/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🤝 Contributing
Contributions are welcome! Feel free to fork the repo, make your changes, and submit a Pull Request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
