# GenAI for Comics

Work alongside an AI model of your choice to create your favourite visual comics!
Please visit https://friendly-spoon-65oeqxj4lj56emjfnokuay.streamlit.app/ to access the app.

### Considerations

- Using both text and drawing inputs from user to generate a beautiful comic image

### Steps to use the app


1. Type in a text prompt to describe the image you want generated.
<img src="./img/text_prompt.png" style="width: 75%">

2. Draw an image that you want the generated image to be similar to. 
<img src="./img/generated_img.png" style="width: 75%">

3. Click on download button to trigger generating of image by stable diffusion AI model. The generated image should be visible below the canvas board.

<img src="./img/buttons.jpg" style="width: 75%">

4. Click the delete button to clear canvas and try again

Future improvements:
- Adding more refined drawing tools 
- Experiment with more models to make it more comic looking
- Panel templates for placing generated images

### Steps to replicate project locally

#### Install dependencies
```
pip install -r requirements.txt
```

#### Replace lines 34 and 35 with the below statements
```
config = toml.load("config.toml")
# config = st.secrets
```

#### Add environment variables for APIs in config.toml file:
- cloudinary and 
- replicate

#### Run app with the following command
```
python -m streamlit run streamlit_app.py
```

Dependencies:
- streamlit>=0.88
- streamlit-drawable-canvas>=0.8
- svgpathtools
- svgwrite


https://replicate.com/fofr/image-prompts/examples
https://replicate.com/fofr/llama2-prompter/examples
https://replicate.com/tstramer/midjourney-diffusion