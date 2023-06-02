import streamlit as st
import os
from llama_index import StorageContext, load_index_from_storage, GPTVectorStoreIndex

#os.environ['OPENAI_API_KEY'] = 'OPEN AI API KEY HERE'
st.title("Query ISLR with Llama Index")
st.subheader("Code is hosted here: ")
         
storage_context = StorageContext.from_defaults(persist_dir="./storage")

# load index
index = load_index_from_storage(storage_context)

islr_query = index.as_query_engine()
question = st.text_input("Ask a question about ISLR")
if question == '':
    st.stop()
response = islr_query.query(question)
st.markdown(f'''<h3>{response}</h3>''', unsafe_allow_html=True)