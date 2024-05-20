from PIL import Image
from utility import *
from htmltemplates import css

# --- PAGE SETUP ---
# Initialize streamlit app
page_title = "Image Genie"
page_icon = ":robot_face:"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

# Apply CSS styles to title and subheading
st.markdown(css, unsafe_allow_html=True)
st.markdown("<span class=styled-span> Image Genie </span>", unsafe_allow_html=True)

st.write(" ")
st.write("")
st.markdown("<div class=text-with-line> <p><b><i>This app reads the image (in JPG or PNG format)"
            " and respond to user queries regarding the image.  "
            "This application makes use of gemini-1.5-pro-latest model from Google.</b></i></p></div>",
            unsafe_allow_html=True)

# ---- SETUP SIDEBAR ----
st.sidebar.title("Configuration")
api_key, file_uploader = configure_apikey_sidebar()

# Input Prompt
input_prompt = """
You are a proficient image reader. 
We will upload an image. Respond to the question asked by the user. If user question is not related to the image,
your should response "Not related to the image" or similar.

"""
st.header("Upload Image")
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], disabled=not file_uploader,
                                  label_visibility='collapsed')

col1, col2 = st.columns(2)

with col2:
    container1 = st.container(height=500, border=True)
    with container1:
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.subheader("Uploaded Image")
            st.image(image, use_column_width='auto')
with col1:
    container2 = st.container(height=500, border=True)

    question = st.chat_input("Enter your question related to the image. ",
                             key="question_number", disabled=not uploaded_image)

    # if submit:
    if question:
        with container2:
            st.subheader("Question:")
            st.write(question)
            st.subheader("Response: ")
            with st.spinner(":blue[Processing...]"):
                response = get_gemini_response(api_key, input_prompt, uploaded_image, question)
                st.write(response)
