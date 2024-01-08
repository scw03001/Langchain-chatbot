from langchain.vectorstores import FAISS

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from langchain.chat_models import ChatOpenAI


from dotenv import load_dotenv

import streamlit as st

from get_dataset import make_chunks
from get_dataset import get_vector_store

from cssTemplates import bot, user, css

# conversation chain for langchain & chatbot
def get_conversation_chain(vector_store: FAISS):
    # Use gpt-4 model
    llm = ChatOpenAI(model="gpt-4")
    # memory for store message & extract msgs in variables
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_retrieval_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vector_store.as_retriever(),
        memory = memory
    )

    return conversation_retrieval_chain

# Manage chat history + render the msgs to the webpage
def handle_inputs(question: str) -> None:
    response = st.session_state.conversation({"question": question})
    
    # manage chat history to keep show the previous chats
    if st.session_state.chat_history is not None:
        st.session_state.chat_history.extend(response["chat_history"])
    else:
        st.session_state.chat_history = response["chat_history"]


    for i, msg in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user.replace("{{MSG}}", msg.content), unsafe_allow_html=True)
        else:
            st.write(bot.replace("{{MSG}}", msg.content), unsafe_allow_html=True)

def main():
    load_dotenv()

    st.set_page_config(page_title='Hanwha chatbot', page_icon='🤖')

    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header('Ask any questions related to 2022 State of the Union Address')
    question = st.text_input("Write your question")

    # If the question exists
    if question:
        handle_inputs(question)
    # Load texts from pdf
    texts = make_chunks()
    # load or create vector store
    vector_store = get_vector_store(texts)
    # Start session
    st.session_state.conversation =  get_conversation_chain(vector_store)



if __name__ == "__main__":
    main()