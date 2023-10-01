from langchain.embeddings import OpenAIEmbeddings
from constant.constant import OPEN_API_KEY
from langchain.vectorstores import Pinecone
import pinecone
pinecone.init(
	api_key='887ebe6f-7788-4cac-a64d-6d7b68c01eae',
	environment='gcp-starter'
)
index_name = 'learningpinecone'
embeddings = OpenAIEmbeddings(
    openai_api_key=OPEN_API_KEY
)

docsearch = Pinecone.from_existing_index(index_name, embeddings)
while(True):
    prompt = input("Human: ")
    if(prompt == "stop"):
        break;
    docs = docsearch.similarity_search(query=prompt,k=2)

    print(docs[0].page_content)
    # print(docs)