# Natural Language to SQL Query Executor

A Streamlit application that allows users to upload CSV files and query them using natural language. The application uses Google's Gemini AI model to convert natural language queries into SQL queries.

## Features

- Upload CSV files
- Automatic schema extraction
- Natural language to SQL query conversion using Gemini AI
- Interactive query execution and results display
- Real-time database updates

## Prerequisites

- Python 3.7+
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nlp-sql-query-executor.git
cd nlp-sql-query-executor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Replace the API key in `app.py` with your own key

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (usually http://localhost:8501)

3. Upload a CSV file and start querying using natural language!

## Project Structure

- `app.py` - Main application file containing the Streamlit interface and core functionality
- `requirements.txt` - List of Python dependencies
- `README.md` - Project documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 