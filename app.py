from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide social media captions
def generate_caption(description, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], description])
    return response.text.strip()

# Custom CSS for styling
st.markdown(
    """
   <style>
    /* Base Styles */
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #F5F5F5;
        color: #000000;
        margin: 0;
        padding: 0;
        transition: background-color 0.3s, color 0.3s;
    }

    @media (prefers-color-scheme: dark) {
        body {
            background-color: #121212;
            color: #FFFFFF;
        }
    }

    /* Header Styling */
    .main-header {
        font-family: 'Arial', sans-serif;  /* Updated font */
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 1.5rem;
        color: inherit; /* Inherit color from body */
        padding-top: 1rem;
        transition: all 0.3s ease;
    }

    /* Subheader Styling */
    .sub-header {
        font-size: 1.2rem;
        margin-top: 1rem;
        text-align: center;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        color: inherit; /* Inherit color from body */
        line-height: 1.6;
    }

    /* Text Input Area */
    .stTextArea > div > div > textarea {
        border-radius: 8px;
        padding: 12px;
        font-size: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        width: 100%;
        resize: vertical;
        background-color: #FFFFFF;
        border: 2px solid #BDBDBD;
        color: #333333;
    }

    .stTextArea > div > div > textarea:focus {
        border-color: #6200EE;
        box-shadow: 0 0 0 2px rgba(98, 0, 238, 0.3);
    }

    @media (prefers-color-scheme: dark) {
        .stTextArea > div > div > textarea {
            background-color: #1E1E1E;
            color: #F8F8F2;
            border: 2px solid #6272A4;
        }
        .stTextArea > div > div > textarea:focus {
            border-color: #FF79C6;
            box-shadow: 0 0 0 2px rgba(255, 121, 198, 0.3);
        }
    }

    /* Buttons */
    .stButton > button {
        border-radius: 20px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        background-color: #6200EE;
        color: #FFFFFF;
        box-shadow: 0 4px 6px rgba(98, 0, 238, 0.1);
    }

    .stButton > button:hover {
        background-color: #3700B3;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(55, 0, 179, 0.2);
    }

    .stButton > button:active {
        transform: translateY(1px);
    }

    @media (prefers-color-scheme: dark) {
        .stButton > button {
            background-color: #50FA7B;
            color: #282A36;
            box-shadow: 0 4px 6px rgba(80, 250, 123, 0.1);
        }
        .stButton > button:hover {
            background-color: #FF79C6;
            color: #F8F8F2;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(255, 121, 198, 0.2);
        }
    }

    /* Checkbox and Radio Buttons */
    .stRadio > label, .stCheckbox > label {
        font-size: 1rem;
        padding-left: 0.5rem;
        cursor: pointer;
    }
    .stRadio > div, .stCheckbox > div {
        margin-top: 0.5rem;
    }

    /* Caption Output */
    .caption-output {
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: #FFFFFF;
        color: #333333;
        border-left: 4px solid #6200EE;
    }

    @media (prefers-color-scheme: dark) {
        .caption-output {
            background-color: #282A36;
            color: #F8F8F2;
            border-left: 4px solid #FF79C6;
        }
    }

    /* Additional Styling for Selectbox */
    .stSelectbox > div > div {
        border-radius: 8px;
        padding: 8px;
        background-color: #FFFFFF;
        transition: all 0.3s ease;
    }

    .stSelectbox > div > div:focus {
        border-color: #6200EE;
        box-shadow: 0 0 0 2px rgba(98, 0, 238, 0.3);
    }

    @media (prefers-color-scheme: dark) {
        .stSelectbox > div > div {
            background-color: #1E1E1E;
            color: #F8F8F2;
        }
        .stSelectbox > div > div > div {
            background-color: #282A36;
        }
    }

    @media (prefers-color-scheme: light) {
        .stSelectbox > div > div {
            background-color: #FFFFFF;
            color: #333333;
        }
        .stSelectbox > div > div > div {
            background-color: #F5F5F5;
        }
    }
</style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App Header
st.markdown('<h1 class="main-header">🎉 Caption Master: Create Your Perfect Post!</h1>', unsafe_allow_html=True)

# Description Section
st.markdown('<p class="sub-header">Enter a description, choose a platform, and we\'ll generate a catchy caption for your social media post.</p>', unsafe_allow_html=True)

description = st.text_area("Enter the description:", key="description", height=200)

# Social Media Platform Selection
platforms = {
    "Instagram": "Create an engaging and visually appealing caption, use hashtags and emojis for Instagram.",
    "Twitter": "Craft a concise and witty caption, adhering to Twitter's character limit.",
    "Facebook": "Write a friendly and engaging caption suitable for Facebook.",
    "LinkedIn": "Generate a professional and insightful caption tailored for LinkedIn.",
}
selected_platform = st.radio("Select the social media platform:", list(platforms.keys()))

# Additional options checkboxes
col1, col2 = st.columns(2)
with col1:
    include_hashtags = st.checkbox("Include relevant hashtags")
with col2:
    add_emojis = st.checkbox("Add emojis for engagement")

# Generate the prompt based on user choices
if description.strip():
    platform_prompt = platforms[selected_platform]
    prompt = [
        f"""
        You are an expert in creating social media captions. Your task is to create a caption based on the provided description.
        {platform_prompt}
        """
    ]
    if include_hashtags:
        prompt[0] += " Include relevant and trending hashtags."
    if add_emojis:
        prompt[0] += " Add emojis to enhance engagement."
else:
    prompt = []

# Submit Button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
submit = st.button("✨ Generate Caption ✨")
st.markdown("</div>", unsafe_allow_html=True)

# Caption Output
if submit:
    if description.strip():
        caption = generate_caption(description, prompt)
        st.markdown("<div class='caption-output'>", unsafe_allow_html=True)
        st.subheader("Generated Caption:")
        st.write(caption)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter a valid description to generate a caption.")
