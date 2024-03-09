# Text to Image Generator

This Streamlit application allows users to generate images from text prompts using pre-trained models. It leverages the Stable Diffusion models provided by Prodia for generating ultra-realistic images based on user-provided text descriptions.

## Features

- Choose from a variety of pre-trained models including fast-stable-diffusion and sdxl-stable-diffusion-xl.
- Select specific checkpoints within each model for generating images.
- Input custom prompts to describe the desired image content.
- Adjust the width and height of the generated images using sliders.
- Download the generated images directly from the application.

## Usage

### Requirements

```
streamlit
gradio
gradio-client
shutil
os
pillow
```

### Installation

- Clone this repository to your local machine

  ```
  git clone `https://github.com/SP85691/Text_To_Image_Generator_Stable_Diffusion.git`

  ```
- Navigate to the project directory:

  ```
  cd text-to-image-generator

  ```
- Install the required dependencies:

  ```
  pip install -r requirements.txt
  ```

### Running the Application

- Run the Streamlit application by executing the following command:
  ```
  streamlit run app.py
  ```

This will start the Streamlit server locally, and you can access the application in your web browser at http://localhost:8501.

## Usage Instructions

1. Choose one or more models from the available options.
2. Select a checkpoint within each model for image generation.
3. Input your desired prompt to describe the image content.
4. Adjust the width and height sliders to customize the size of the generated image.
5. Click the "Generate Image" button to create the image based on your inputs.
6. Download the generated image using the provided button.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on the GitHub repository.
License

#### This project is licensed under the `<a href="https://opensource.org/license/mit">`MIT License `</a>`.
