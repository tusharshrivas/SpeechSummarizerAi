# SpeechSummarizerAi

This project allows you to summarize speeches, YouTube video transcripts, website content, and PDF documents using the Groq Gemma LLM integrated with LangChain. It supports multiple summary strategies like simple summary, map-reduce, and refinement chains for better results.

Features
Summarize plain text speeches with detailed prompts

Summarize PDF documents by loading and chunking content

Summarize YouTube video transcripts and web page text via URL input

Supports Groq Gemma-7b-It language model via Groq API

Supports translation of summaries to other languages (e.g., Hindi)

Multiple summarization techniques: stuff, map-reduce, refine

Streamlit app interface for summarizing URLs (YouTube or web pages)

Getting Started
Prerequisites
Python 3.8 or above

Groq API Key (sign up at Groq to get your API key)

PyCharm or any Python IDE (optional)

Installation
Clone this repository or copy the project files to your local machine.

Create and activate a Python virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies from requirements.txt or manually:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not provided, install these packages:

bash
Copy
Edit
pip install langchain langchain-groq python-dotenv langchain-community pypdf validators streamlit youtube_transcript_api unstructured pytube
Setup .env file
Create a .env file in your project root directory with the following content:

ini
Copy
Edit
GROQ_API_KEY=your_actual_groq_api_key_here
Replace your_actual_groq_api_key_here with your Groq API key.

How to Run
1. Summarize a speech or text
In your Python script (e.g. text_summarizer.py), load your speech text in the speech variable.

Run the script to see simple, translated, and advanced summary outputs in your console.

bash
Copy
Edit
python text_summarizer.py
2. Summarize a PDF document
Place your PDF speech document (e.g., apjspeech.pdf) in the project folder.

The script will load and chunk the PDF content automatically and generate summaries.

3. Summarize YouTube videos or website content via Streamlit app
Run the Streamlit app:

bash
Copy
Edit
streamlit run streamlit_app.py
Enter your Groq API key and URL (YouTube or website) in the sidebar.

Click Summarize the Content from YT or Website to get a 300-word summary displayed on the page.

Project Structure
bash
Copy
Edit
├── apjspeech.pdf                  # Sample speech PDF file
├── text_summarizer.py             # Main script for speech and PDF summarization
├── streamlit_app.py               # Streamlit app to summarize URLs (YouTube & web pages)
├── .env                          # Environment variables (API key)
├── requirements.txt              # Required packages (optional)
└── README.md                     # This README file
Notes
Make sure to keep your .env file private and never upload your API keys to public repos.

The project uses the Groq Gemma-7b-It model, ensure your Groq API key has access.

The summarization quality depends on your prompt design and the Groq model performance. You can customize prompt templates in the code.

The project does NOT include or relate to any app.py files that may exist elsewhere.

Troubleshooting
ModuleNotFoundError or import errors:
Ensure you installed all dependencies properly in the same Python environment you run your script.

API key errors:
Confirm your .env file is correctly placed and the key is valid. Use print(api_key) in your code to debug.

Streamlit app issues:
Make sure you installed streamlit and run streamlit run streamlit_app.py from the project root.

Future Improvements
Add GUI interface to summarize local text or PDFs without coding

Support more languages for translation summary

Add caching for repeated URL summarizations

Extend to support audio/video speech input files

License
This project is open source and free to use for personal and educational purposes.

