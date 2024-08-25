import streamlit as st
from PIL import Image
from io import BytesIO
from transformers import ViltProcessor, ViltForQuestionAnswering
import torch

# Set page layout to wide
st.set_page_config(layout="wide")

# Load the image processor and model
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def get_answer(image, text):
    try:
        # Load and process the image
        img = Image.open(BytesIO(image)).convert("RGB")
        
        # Prepare inputs
        encoding = processor(images=img, text=text, return_tensors="pt")
        input_ids = encoding['input_ids']
        pixel_values = encoding['pixel_values']

        # Debug: Check shapes of inputs
        print(f"Input IDs shape: {input_ids.shape}")
        print(f"Pixel Values shape: {pixel_values.shape}")

        # Forward pass
        with torch.no_grad():
            outputs = model(input_ids=input_ids, pixel_values=pixel_values)
        
        logits = outputs.logits
        idx = logits.argmax(-1).item()  # Get the index of the highest score
        
        # Retrieve the answer from id2label mapping
        answer = model.config.id2label.get(idx, "Unknown answer")

        return answer

    except Exception as e:
        return str(e)

# Set up the Streamlit app
st.title("Visual Question Answering")
st.write("Upload an image and enter a question to get an answer.")

# Create columns for image upload and input fields
col1, col2 = st.columns(2)

# Image upload
with col1:
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        try:
            # Open and convert the image to RGB before displaying
            img = Image.open(uploaded_file).convert("RGB")
            st.image(img, use_column_width=True)
        except Exception as e:
            st.error(f"Error opening image: {e}")

# Question input
with col2:
    question = st.text_input("Question")

    # Process the image and question when both are provided
    if uploaded_file is not None and question:
        if st.button("Ask Question"):
            try:
                # Convert the uploaded image to byte array
                image_byte_array = BytesIO()
                img = img.convert("RGB")  # Ensure the image is in RGB mode
                img.save(image_byte_array, format='JPEG')
                image_bytes = image_byte_array.getvalue()

                # Get the answer
                answer = get_answer(image_bytes, question)

                # Display the answer
                st.success("Answer: " + answer)
            except Exception as e:
                st.error(f"Error processing image or getting answer: {e}")
