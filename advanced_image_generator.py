import shutil
import os
from gradio_client import Client

class text_to_image_generator():
    def __init__(self, client, prompt, neg_prompt, stable_diffusion_checkpoints):
        self.prompt = prompt
        self.negPrompt = neg_prompt
        self.stable_diffusion_checkpoints = stable_diffusion_checkpoints
        self.sampling_steps = 20.0
        self.sampling_method = "DPM++ 2M Karras"
        self.cfg_scale = 7.0
        self.width = 512
        self.height = 512
        self.seed = -1.0
        
        print("Generating Your Image")
        self.generateImage()
        
        print("Saving Your Image in the 'Image/' folder!")
        self.changePath()
        
    def generateImage(self):
        self.result = client.predict(self.prompt,
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
        print("The Image is Generated!")
        
    def changePath(self):
        self.org_path = self.result
        self.dest_path = r"Images/image.png"
        shutil.move(self.org_path, self.dest_path)
        print("File moved successfully")
        
    def openImage(self):
        try:
            os.system(f"start {self.dest_path}")
        except Exception as e:
            print(f"Error opening image: {e}")

if __name__ == "__main__":
    c = 0
    infos = [
        {
            "prodia/fast-stable-diffusion": [
                "amIReal_V41.safetensors [0a8a2e61]",
                "absolutereality_v181.safetensors [3d9d4d2b]",
                "cyberrealistic_v33.safetensors [82b0d085]",
                "anythingV5_PrtRE.safetensors [893e49b9]"
            ]
        },
        {
            "prodia/sdxl-stable-diffusion-xl": [
                "juggernautXL_v45.safetensors [e75f5471]", 
                "realismEngineSDXL_v10.safetensors [af771c3f]",
                "turbovisionXL_v431.safetensors [78890989]",
                "dynavisionXL_0411.safetensors [c39cc051]",
                "sd_xl_base_1.0.safetensors [be9edd61]",
            ]
        },
    ]

    print("Choose a model (0 for prodia/fast-stable-diffusion), 1 for prodia/sdxl-stable-diffusion-xl:\n")

    for i, info in enumerate(infos):
        print(f"{i}:", end='')
        for model_name, model_values in info.items():
            print(f"\t{model_name}")
            
    option = int(input("-> "))

    if option == 0:
        model_values = infos[0]["prodia/sdxl-stable-diffusion-xl"]
        client = Client("prodia/sdxl-stable-diffusion-xl")
    elif option == 1:
        model_values = infos[1]["prodia/fast-stable-diffusion"]
        client = Client("prodia/fast-stable-diffusion")
    else:
        print("Exiting...")
        exit()

    print("Choose a model from the list below:")
    for i, value in enumerate(model_values):
        print(f"{i}: {value}")

    model_choice = int(input("-> "))
    if model_choice < 0 or model_choice >= len(model_values):
        print("Invalid choice. Exiting...")
        exit()

    stable_diffusion_checkpoints = model_values[model_choice]
    print(f"Selected model: {stable_diffusion_checkpoints}")
    
    prompt = input("Enter your Prompt here: ")
    negative_prompt = "ugly, deformed eyes, deformed ears, deformed nose, deformed mouth, bad anatony, extra  limbs, low resolution, pixelated, distorted proportion, unnatural colors, unrealistic lighting, excessive noise, unnatural pose, unrealistic shadows"
    
    # Calling the Class
    app = text_to_image_generator(client=client, prompt=prompt, neg_prompt=negative_prompt, stable_diffusion_checkpoints=stable_diffusion_checkpoints)
