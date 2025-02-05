# Smart Vision Assistant

**Smart Vision Assistant** is a multi-modal application built with Streamlit that leverages Google's Gemini model (via the `ChatGoogleGenerativeAI` class) to analyze images and answer user queries. Users can either upload an image from their local machine or provide an image URL. The app then encodes the image in Base64, sends it along with the user’s query to the model, and displays both the image and the generated response.

## Features

- **Multi-Modal Input:**  
  Users can choose between uploading an image file directly or providing an image URL.

- **LLM Integration:**  
  Utilizes the `ChatGoogleGenerativeAI` model (`gemini-1.5-flash`) to process images and text queries, providing intelligent responses based on the image analysis.

- **User-Friendly Interface:**  
  Built with Streamlit, offering an intuitive UI where users can interact with the app easily.

- **Loading Spinner:**  
  Displays a spinner while the model is generating a response to improve user experience.

## Demo
![](https://github.com/Carnage203/AI-Image-Analyzer/blob/a31d8d8a01f2297f7e71ba87cb72ce63c5a2a1a9/home%20page.png)
![](https://github.com/Carnage203/AI-Image-Analyzer/blob/a31d8d8a01f2297f7e71ba87cb72ce63c5a2a1a9/wp1855659-messi-suarez-neymar-wallpapers.jpg)
![](https://github.com/Carnage203/AI-Image-Analyzer/blob/a31d8d8a01f2297f7e71ba87cb72ce63c5a2a1a9/response.png)

## Installation

### Prerequisites

- requirements.txt

 **Set Up API Key:**

   Create a file named `constants.py` in the project root and add your Google API key:

   ```python
   GOOGLE_API_KEY = "your-google-api-key-here"
   ```

## Code Overview

The main code is structured as follows:

- **Dependencies and Setup:**  
  The script imports necessary libraries, sets the Google API key, and initializes the `ChatGoogleGenerativeAI` model.

- **Existing Comments (Unchanged):**  
  The code retains comments for handling image URLs and local images.

- **Streamlit UI Enhancements:**  
  - **Image Input Options:**  
    Users choose between uploading an image or providing an image URL via a radio button.
  
  - **Image Encoding:**  
    The selected image is read and encoded in Base64.
  
  - **User Query and Submission:**  
    The user enters their question and submits the form. A loading spinner is displayed while the LLM processes the input.
  
  - **Display of Results:**  
    The uploaded image and the LLM-generated answer are both displayed on the page.
