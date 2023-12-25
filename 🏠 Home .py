import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Research Buddy",
    page_icon=":books:",
)

# Apply styles
main_bg_color = "#f0f6f7"
main_text_color = "#001f3f"
sidebar_bg_color = "#003366"
sidebar_text_color = "#ffffff"

# Apply styles to the page
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {main_bg_color};
            color: {main_text_color};
        }}
        .sidebar .sidebar-content {{
            background-color: {sidebar_bg_color};
            color: {sidebar_text_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and content
st.title("Welcome to Research Buddy :books:")
st.write("""
This research paper presents the development of a user-trained conversational model tailored for processing PDF files using OpenAI's API and large language models. The implemented system, named seamlessly integrates into a Streamlit interface, enabling users to pose natural language questions about uploaded PDF documents. The code leverages PyPDF2 for PDF parsing, character-based text splitting, and vectorization using OpenAIEmbeddings and FAISS. The conversational aspect is powered by ChatOpenAI, forming a ConversationalRetrievalChain. The model exhibits dynamic learning through a ConversationBufferMemory, refining responses over interactions. The system's architecture is designed for adaptability, accommodating various language models. With an intuitive user interface, this model empowers researchers to interactively explore and extract knowledge from their PDF documents, demonstrating the practicality of user-trained models in real-world applications.
""")

# Sidebar message
st.sidebar.success("Select a page above.")
