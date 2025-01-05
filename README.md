# GDG KLEF Caption Master

**GDG Klef Caption Master** is a web application built with Streamlit that generates catchy and engaging social media captions based on user inputs. The app uses Google's Generative AI model (Gemini) to create captions for various platforms like Instagram, Twitter, Facebook, and LinkedIn. You can also include hashtags and emojis to enhance engagement.

## Features
- **Custom Captions**: Generate captions for different social media platforms.
- **Hashtags & Emojis**: Add relevant hashtags and emojis for better engagement.
- **Platform-Specific Prompts**: Tailored prompts for Instagram, Twitter, Facebook, and LinkedIn.
- **User-Friendly Interface**: Easy-to-use interface with text input and selection options.

## Setup Instructions

To run this app locally, follow these steps:

### Prerequisites

- Python 3.7+
- Google Cloud API Key for Generative AI (Gemini)

### Steps to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository/gdg-klef-Caption-Master.git
   cd gdg-klef-Caption-Master
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google API key:
   - Get your Google Cloud API Key for Generative AI (Gemini).
   - Create a `.env` file in the project root directory and add the following line:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

6. Open the browser at `http://localhost:8501` to use the app.

## How to Use

- **Enter a Description**: In the "Enter the description" box, input the text that you want a caption for.
- **Select Platform**: Choose the social media platform for which you want to generate the caption.
- **Include Hashtags/Emojis**: Check the boxes to include relevant hashtags and emojis in your caption.
- **Generate Caption**: Click the "✨ Generate Caption ✨" button to generate the caption.
- **Output**: The app will display the generated caption based on the inputs.

## Project Structure

```
gdg-klef-Caption-Master/
│
├── app.py                  # Main application file containing Streamlit code
├── requirements.txt        # Project dependencies
└── .streamlit/             
    └── config.toml         # Streamlit configuration file (theme settings)
```

### Configuration

You can customize the theme of the Streamlit app by modifying the `.streamlit/config.toml` file.

Currently, the theme is set to **light mode**. If you want to change the theme to dark mode, you can modify the `base` key in `config.toml` to:

```toml
[theme]
base = "dark"
```

## Dependencies

- `streamlit`: Framework for building the web application.
- `google-generativeai`: Google Generative AI API client.
- `python-dotenv`: For loading environment variables from `.env` file.
- `ipython`: For enhanced interactive shell experience.

