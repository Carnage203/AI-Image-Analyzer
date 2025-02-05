# dependencies
import os
import base64
import httpx
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from constants import GOOGLE_API_KEY

# API key 
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.8
)

# system prompt to instruct the assistant
system_message = SystemMessage(content="""
    You are a smart vision assistant who will analyze the provided images
    and answer the provided questions/queries.
""")

#For URL
# fruits = ['https://storage.googleapis.com/vectrix-public/fruit/apple.jpeg',
#           'https://storage.googleapis.com/vectrix-public/fruit/banana.jpeg',
#           'https://storage.googleapis.com/vectrix-public/fruit/kiwi.jpeg',
#           'https://storage.googleapis.com/vectrix-public/fruit/peach.jpeg',
#           'https://storage.googleapis.com/vectrix-public/fruit/plum.jpeg'
# ]

# # download the image from the URL and encode it in Base64
# response_img = httpx.get(fruits[0])
# if response_img.status_code == 200:
#     image_data = base64.b64encode(response_img.content).decode("utf-8")
# else:
#     raise Exception(f"Failed to download image from {fruits[0]}: Status {response_img.status_code}")

# For Local
local_image_path = r".\messi.png"

# open and encode the local image in Base64
try:
    with open(local_image_path, "rb") as image_file:
        image_bytes = image_file.read()
        image_data = base64.b64encode(image_bytes).decode("utf-8")
except FileNotFoundError:
    raise Exception(f"Local image file not found: {local_image_path}")

# --- Streamlit UI code begins here ---
st.title("Smart Vision Assistant")
st.write("Upload an image or provide an image URL to analyze and answer your queries.")

# Allow the user to choose the image input method
input_method = st.radio("Choose image input method:", ("Upload Image", "Image URL"))

# Initialize variables for image bytes and Base64-encoded data
final_image_bytes = None
final_image_data = None

if input_method == "Upload Image":
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        final_image_bytes = uploaded_file.read()
        final_image_data = base64.b64encode(final_image_bytes).decode("utf-8")
        st.image(final_image_bytes, caption="Uploaded Image", use_container_width=True)
elif input_method == "Image URL":
    image_url = st.text_input("Enter image URL:")
    if image_url:
        try:
            response_img = httpx.get(image_url)
            if response_img.status_code == 200:
                final_image_bytes = response_img.content
                final_image_data = base64.b64encode(final_image_bytes).decode("utf-8")
                st.image(final_image_bytes, caption="Image from URL", use_container_width=True)
            else:
                st.error(f"Failed to download image from URL: Status {response_img.status_code}")
        except Exception as e:
            st.error(f"Error fetching image: {e}")

query = st.text_input("Enter your question:")

if st.button("Submit"):
    if final_image_data and query:
        human_message = HumanMessage(
            content=[
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{final_image_data}"},
                },
            ],
        )
        # Show spinner while generating answer
        with st.spinner("Generating answer..."):
            response = llm.invoke([system_message, human_message])
        st.write("### LLM Response")
        st.write(response.content)
    else:
        st.error("Please provide both an image and your question.")
