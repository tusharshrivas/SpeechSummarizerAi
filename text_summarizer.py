import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(groq_api_key=api_key, model="Gemma-7b-It")

# ------------------------ Manual Speech Summary ------------------------ #
speech = """
People across the country, involved in government, political, and social activities, are dedicating their time to make the ‘Viksit Bharat Sankalp Yatra’ (Developed India Resolution Journey) successful...
"""

# Simple summary interaction
chat_message = [
    SystemMessage(content="You are expert with expertise in summarizing speeches."),
    HumanMessage(content=f"Please provide a short and concise summary of the following speech:\nText: {speech}")
]

# Get token count and response
print("Tokens in speech:", llm.get_num_tokens(speech))
print("LLM Summary:\n", llm(chat_message))

# ------------------------ Translate Summary ------------------------ #
generictemplate = """
Write a summary of the following speech:
Speech: {speech}
Translate the precise summary to {language}
"""
prompt = PromptTemplate(input_variables=['speech', 'language'], template=generictemplate)
llm_chain = LLMChain(llm=llm, prompt=prompt)
summary = llm_chain.run({'speech': speech, 'language': 'hindi'})
print("\nTranslated Summary in Hindi:\n", summary)

# ------------------------ PDF Summary ------------------------ #
loader = PyPDFLoader("apjspeech.pdf")
docs = loader.load_and_split()

# Simple prompt
template = "Write a concise and short summary of the following speech,\nSpeech :{text}\n"
prompt = PromptTemplate(input_variables=['text'], template=template)
chain = load_summarize_chain(llm, chain_type='stuff', prompt=prompt, verbose=True)
output_summary = chain.run(docs)
print("\nStuff Chain Summary:\n", output_summary)

# ------------------------ Chunked Map-Reduce Summary ------------------------ #
final_documents = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100).split_documents(docs)

chunks_prompt = """Please summarize the below speech:\nSpeech:`{text}`\nSummary:\n"""
map_prompt_template = PromptTemplate(input_variables=['text'], template=chunks_prompt)

final_prompt = '''
Provide the final summary of the entire speech with these important points.
Add a Motivation Title, start the precise summary with an introduction, and provide the summary in numbered points.
Speech: {text}
'''
final_prompt_template = PromptTemplate(input_variables=['text'], template=final_prompt)

summary_chain = load_summarize_chain(
    llm=llm,
    chain_type="map_reduce",
    map_prompt=map_prompt_template,
    combine_prompt=final_prompt_template,
    verbose=True
)

output = summary_chain.run(final_documents)
print("\nMap-Reduce Summary:\n", output)

# ------------------------ Refine Summary ------------------------ #
refine_chain = load_summarize_chain(
    llm=llm,
    chain_type="refine",
    verbose=True
)
refined_summary = refine_chain.run(final_documents)
print("\nRefined Summary:\n", refined_summary)
