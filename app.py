import streamlit as st
import os
import shutil
from gradio_client import Client
from PIL import Image

class TextToImageGenerator:
    def __init__(self, client, prompt, neg_prompt, stable_diffusion_checkpoints, width, height):
        self.client = client
        self.prompt = prompt
        self.negPrompt = neg_prompt
        self.stable_diffusion_checkpoints = stable_diffusion_checkpoints
        self.sampling_steps = 20.0
        self.sampling_method = "DPM++ 2M Karras"
        self.cfg_scale = 7.0
        self.width = width
        self.height = height
        self.seed = -1.0
        self.result = None

    def generate_image(self):
        self.result = self.client.predict(self.prompt,
                                self.negPrompt,
                                self.stable_diffusion_checkpoints,
                                self.sampling_steps,
                                self.sampling_method,
                                self.cfg_scale,
                                self.width,
                                self.height,
                                self.seed,
                                fn_index = 0
                            )
        self.change_path()
        self.open_image()

    def change_path(self):
        self.org_path = self.result
        self.dest_path = "Images/image.png"
        shutil.move(self.org_path, self.dest_path)
        print("File moved successfully")
        
    def open_image(self):
        try:
            image = Image.open(self.dest_path)
            st.image(image, caption='Generated Image', use_column_width=True)
            if st.button("Download Image"):
                with open(self.dest_path, "rb") as f:
                    bytes = f.read()
                    st.download_button(label="Download", data=bytes, file_name="generated_image.png", mime="image/png")
        except Exception as e:
            st.write(f"Error opening image: {e}")

    
def main():
    st.title("Text to Image Generator")

    model_options = {
        "prodia/fast-stable-diffusion": [
            "amIReal_V41.safetensors [0a8a2e61]",
            "absolutereality_v181.safetensors [3d9d4d2b]",
            "cyberrealistic_v33.safetensors [82b0d085]",
            "anythingV5_PrtRE.safetensors [893e49b9]"
        ],
        "prodia/sdxl-stable-diffusion-xl": [
            "juggernautXL_v45.safetensors [e75f5471]", 
            "realismEngineSDXL_v10.safetensors [af771c3f]",
            "turbovisionXL_v431.safetensors [78890989]",
            "dynavisionXL_0411.safetensors [c39cc051]",
            "sd_xl_base_1.0.safetensors [be9edd61]",
        ]
    }

    selected_models = st.multiselect("Choose models", list(model_options.keys()))

    for selected_model in selected_models:
        st.sidebar.write(f"Selected Model: {selected_model}")
        model_values = model_options[selected_model]
        selected_checkpoint = st.sidebar.selectbox("Choose a checkpoint", model_values)

        width = st.sidebar.slider("Width", min_value=100, max_value=1000, value=512, step=1)
        height = st.sidebar.slider("Height", min_value=100, max_value=1000, value=512, step=1)

        prompt = st.sidebar.text_input("Enter your Prompt here: ")
        negative_prompt = "ugly, deformed eyes, deformed ears, deformed nose, deformed mouth, bad anatony, extra  limbs, low resolution, pixelated, distorted proportion, unnatural colors, unrealistic lighting, excessive noise, unnatural pose, unrealistic shadows"

        if st.sidebar.button("Generate Image"):
            client = Client(selected_model)
            app = TextToImageGenerator(client=client, prompt=prompt, neg_prompt=negative_prompt, stable_diffusion_checkpoints=selected_checkpoint, width=width, height=height)
            app.generate_image()
            
if __name__ == "__main__":
    main()
