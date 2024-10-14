
# Text-to-Image Generator

This is a simple web-based prototype that allows users to input a text prompt and generate an image using AI. The project uses the **Stable Diffusion** model to create high-quality images from text.

## Project Overview

-   **Input**: Users enter a text prompt (e.g., "A serene mountain landscape during sunset").
-   **Output**: The AI generates an image based on the text prompt.

The app is hosted on Hugging Face Spaces, making it accessible from any device with an internet connection.

----------

## How to Use

1.  **Enter a Prompt**: Type a description of the image you want to generate in the input box.
2.  **Click "Generate Image"**: Wait a few moments while the AI processes your request.
3.  **View the Image**: The generated image will be displayed below the button.
4.  **Download the Image**: You can right-click on the image to save it.

----------

## Deployment Instructions

This project is deployed on **Hugging Face Spaces**. Below are the steps I followed for deployment:

1.  **Set Up Hugging Face Account**: Created a free account on Hugging Face.
2.  **Clone Repository**: Cloned a pre-trained model (`sam749/Photon-v1`) and used the `stabilityai/sd-vae-ft-mse` VAE for better image quality.
3.  **Develop the Web App**: Built the app using **Streamlit** to create a user-friendly interface for text input and image display.
4.  **Push to Hugging Face**: Uploaded the code to Hugging Face Spaces for deployment.
5.  **Run the Application**: The app runs in the cloud, handling user requests and generating images.

To deploy your own version on Hugging Face Spaces, you can follow these steps:

-   Sign in to your Hugging Face account.
-   Create a new Space and select "Streamlit" as the framework.
-   Upload the code to the repository.
-   Click "Deploy" to run your app live.

----------

## Technical Documentation

-   **Model Used**:
    
    -   The model used is **sam749/Photon-v1**, a fine-tuned version of Stable Diffusion.
    -   The model also uses a **Variational Autoencoder (VAE)** from Stability AI for improved image clarity.
-   **Scheduler**:
    
    -   The app uses the **DPMSolverMultistepScheduler** for better inference speed and quality. The DPM++ 2M Karras sampler is hardcoded to improve the generated image's quality.
-   **Backend**:
    
    -   **Streamlit** is used to handle the frontend and backend, allowing users to input text and see the generated images.
-   **Parameters**:
    
    -   `num_inference_steps`: 24 (controls the number of steps the model takes to generate an image).
    -   `guidance_scale`: 5.5 (higher values result in images closer to the text prompt).
    -   `negative_prompt`: Predefined to remove unwanted characteristics (e.g., low quality, cartoonish images).
    -   `width` and `height`: Set to 512x768 for output image size.

----------

## Challenges Faced

-   **CUDA Support**: Initially, I ran into issues trying to use CUDA in environments like Hugging Face Spaces, but later adjusted the code to work without CUDA when deploying in CPU environments.
-   **Memory Limits**: Fine-tuning the model locally led to memory issues. Instead of fine-tuning, I opted for a pre-finetuned model (`Photon-v1`), which worked well and met the assignment's requirements.
-   **Negative Prompting**: Implementing negative prompts helped to improve image quality by filtering out unwanted styles (e.g., cartoons or illustrations).

----------

## Future Improvements

-   Add more customization options for users (e.g., allowing them to choose image dimensions or quality settings).
-   Explore deploying on GPU-based cloud platforms for faster inference times.
