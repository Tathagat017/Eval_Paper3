from langchain_core.documents import Document
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

file_path = "../data/data.csv"

loader = CSVLoader(file_path=file_path)
data = loader.load()

for record in data[:2]:
    print(record)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=200,
    add_start_index=True
)
all_splits = splitter.split_documents(data)

_ = vector_store.add_documents(documents=data)

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful assistant. Answer the question using only the provided context. "
     "If the answer isn't in the context, say you don't know.\n\n"
     "Context:\n{context}"),
    ("human", "{question}")
])

retriever = vector_store.as_retriever(search_kwargs={"k": 4})


rag_chain = (
    {
        "context": retriever ,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

rag_chain.invoke("What is the nutritional value of cheese?")
