# Visual Question-and-Answering System

This project is a **Visual Question-and-Answering (VQA) System** developed using the **VILT model**. The system takes an image and a corresponding question as input and generates an accurate textual answer. The project is implemented using Streamlit, making it easy to use and deploy.

## Features

- **Visual Question Answering**: Input an image and a related question to get an accurate answer.
- **User-Friendly Interface**: Built with Streamlit, providing a simple and interactive UI.
- **Real-time Processing**: Quickly processes images and questions for instant results.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mohammedazif/visual_Question-and-Answering_system.git
   cd visual_Question-and-Answering_system

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv vqa_env
   source vqa_env/bin/activate  # On Windows: vqa_env\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload an image using the provided interface.
2. Enter a question related to the image.
3. Press the "Submit" button to get an answer.

## Snapshots

Here are some snapshots of the project in action:

1. **Home Page**

   ![image](https://github.com/user-attachments/assets/69006b9d-0081-49ff-9500-27eee9b601e7)


2. **Image Upload**

   ![image](https://github.com/user-attachments/assets/8327c680-eeba-4b88-a401-47efc4020642)

3. **Question Input and Generated Answer**

   ![image](https://github.com/user-attachments/assets/db625029-c968-418d-a90f-1df17183d3bb)
   
## Technologies Used

- **Python**: Programming language
- **Streamlit**: Web application framework
- **VILT (Vision-and-Language Transformer)**: Model for Visual Question Answering
- **PIL**: Image processing library
- **NumPy**: Numerical computing library

## Acknowledgements

This project utilizes the [VILT model](https://github.com/dandelin/vilt) for visual question answering. Special thanks to the open-source community for their invaluable contributions.
