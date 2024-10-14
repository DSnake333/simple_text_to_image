import streamlit as st
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler, AutoencoderKL
import torch

# Load the model and scheduler
model_id = "sam749/Photon-v1"
vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse", torch_dtype=torch.float16).to("cuda")
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.vae = vae
pipe.to("cuda")

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Streamlit interface
st.title("Text-to-Image Generator")

# Prompt inputs
prompt = st.text_input("Enter the prompt for the image:")
negative_prompt = "cartoon, painting, illustration, (worst quality, low quality, normal quality:2)"

cfg_scale = 5.5
width = 512
height = 768

num_inference_steps = 24

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        # Generate image with the given parameters
        generator = torch.Generator("cuda").manual_seed(0)
        image = pipe(prompt, negative_prompt=negative_prompt, num_inference_steps=num_inference_steps,
                     guidance_scale=cfg_scale, width=width, height=height, generator=generator).images[0]

        # Display the generated image
        st.image(image, caption="Generated Image", use_column_width=True)
        image.save("generated_image.png")