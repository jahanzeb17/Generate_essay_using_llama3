import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

def get_llama_model_response(input_topic,no_words,student_level):

    llm = ChatGroq(model_name='Llama3-70b-8192')

    template = """
        you are expert in essay writing and write a essay on {input_topic} topic of {no_words} words
        for {student_level} level students.
    """

    prompt = PromptTemplate(
        input_variable=['input_topic','no_words','student_level'],
        template=template,
    )

    formatted_prompt = prompt.format(input_topic=input_topic,no_words=no_words,student_level=student_level)
    response = llm.invoke(formatted_prompt)

    return response


def main():

    st.set_page_config(page_title="Generate Essays", page_icon='books', layout='centered', initial_sidebar_state='collapsed')
    st.header("Generate Essay")

    input_topic = st.text_area("Enter the Essay Topic", height=100)

    no_words = st.slider("Number of words", min_value=100,max_value=1000,value=500,step=50)

    student_level = st.selectbox('writing essay for',('School','College','University'),index=0)

    submit = st.button('Generate')

    if submit and input_topic:

        with st.spinner("Generating your essay"):

            blog_content = get_llama_model_response(input_topic,no_words,student_level)

            st.subheader('Generated essay')
            st.write(blog_content.content)


if __name__=="__main__":
    main()