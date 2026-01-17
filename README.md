## Description
This project uses ChatGroq chat model and perform web search in wikipedia on the given topic

## Prerequisites
- Python 3.8+
- uv package manager
- Groq API key to be added in .env file


## Installation of Packages
Run this command to install the packages/dependencies
```bash
uv sync
```
and Run 
```bash
.venv/scripts/activate
```

## Run the APP
```bash
streamlit run app.py
```
App will run on 
```bash
http://localhost:8501/
```

1. Give the topic that you want the search.
2. Click search button.
3. The content will be displayed in the page.