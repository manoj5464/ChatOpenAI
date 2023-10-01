import os
import langchain
from langchain.embeddings import OpenAIEmbeddings
# from api.constant.constant import OPEN_API_KEY
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
import pinecone
pinecone.init(
	api_key='887ebe6f-7788-4cac-a64d-6d7b68c01eae',
	environment='gcp-starter'
)
index_name = 'learningpinecone'

files = os.listdir("./text")
#
for file in files:
    loader = TextLoader(os.path.join("./text", file))
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(
        openai_api_key='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'
    )
    #First, check if our index already exists. If it doesn't, we create it
    if index_name not in pinecone.list_indexes():
        # we create a new index
        pinecone.create_index(
            name=index_name,
            metric='cosine',
            dimension=1536
        )
    # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
    #docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

    # if you already have an index, you can load it like this
    # docsearch = Pinecone.from_existing_index(index_name, embeddings)
    #query = "Mindler"
    #docs = docsearch.similarity_search(query)
    #print(docs[0].page_content)


print("traing done")
