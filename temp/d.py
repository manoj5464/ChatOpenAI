from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
# from constant.constant import OPEN_API_KEY
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
# chat completion llm
llm = ChatOpenAI(
    openai_api_key='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',
    model_name='gpt-3.5-turbo',
    temperature=0.0
)
import pinecone
pinecone.init(
	api_key='887ebe6f-7788-4cac-a64d-6d7b68c01eae',
	environment='gcp-starter'
)
index_name = 'learningpinecone'
embeddings = OpenAIEmbeddings(
    openai_api_key='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'
)

vectorstore = Pinecone.from_existing_index(index_name, embeddings)
# conversational memory
conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)
# retrieval qa chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

while(True):
    prompt = input("Human: ")
    if(prompt == "stop"):
        break;
    docs = qa.run(prompt)

    print(docs)

