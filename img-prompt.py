from google import genai

client = genai.Client(api_key="AIzaSyA7qeUzFDzTALg3sjIaN5931nG690b5TvE") 
idea = input("What kind of image do you want to generate?\n")

# Creating a more specific prompt to generate an optimized image prompt
prompt_engineering_request = f"""
Create a detailed, optimized prompt for generating an AI image based on this idea: '{idea}'

The prompt should:
- Be specific about style, composition, lighting, colors, and mood
- Include relevant technical specifications (aspect ratio, quality level)
- Use descriptive language that AI image generators respond well to
- Be structured in a way that prioritizes the most important elements
- Be between 50-150 words for optimal results

Just provide the final prompt without explanations.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt_engineering_request
)

print("\nOptimized Image Prompt:\n")
print(response.text.strip())
print("\nYou can now use this prompt with your preferred image generation tool.")









































































































'''
# Import the Google Generative AI client library
from google import genai

# Create a client instance using your API key (⚠️ Do NOT expose API keys publicly)
client = genai.Client(api_key="AIzaSyCuoc3r4G8g69BIZsM6RmdX4XEayPBNizU")

# Ask the user for a basic idea of the image they want to generate
idea = input("What kind of image do you want to generate?\n")

# Construct a detailed prompt for prompt engineering
# This will guide the model to create a high-quality image prompt based on the user's idea
prompt_engineering_request = f"""
Create a detailed, optimized prompt for generating an AI image based on this idea: '{idea}'

The prompt should:
- Be specific about style, composition, lighting, colors, and mood
- Include relevant technical specifications (aspect ratio, quality level)
- Use descriptive language that AI image generators respond well to
- Be structured in a way that prioritizes the most important elements
- Be between 50-150 words for optimal results

Just provide the final prompt without explanations.
"""

# Send the prompt request to the Gemini 2.0 Flash model
# The model will generate a detailed prompt for image generation
response = client.models.generate_content(
    model="gemini-2.0-flash",  # Specify the model name
    contents=prompt_engineering_request  # The prompt we want the model to process
)

# Output the optimized image prompt returned by the model
print("\nOptimized Image Prompt:\n")
print(response.text.strip())

# Inform the user that they can now use the prompt in any image generation tool
print("\nYou can now use this prompt with your preferred image generation tool.")

#image generation
from diffusers import StableDiffusionPipeline
import torch
# Load the Stable Diffusion model from Hugging Face
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Use the optimized prompt you got from Gemini
prompt = "Stunning nature landscape, vibrant and breathtaking. **Subject:** Majestic snow-capped mountain range reflected in a pristine alpine lake. **Style:** Hyperrealistic landscape painting, reminiscent of Thomas Cole's Hudson River School. **Composition:** Wide-angle, emphasizing depth and scale; rule of thirds, placing the mountains slightly off-center. **Lighting:** Golden hour, soft warm light illuminating the mountain peaks and casting long, cool shadows across the foreground. **Colors:** Deep blues and greens in the lake, contrasted with warm oranges and yellows on the mountains. Hints of purple and pink in the sky. **Mood:** Serene, awe-inspiring, peaceful. **Details:** Crisp, clear reflections, detailed textures of rocks and trees. **Technical:** Aspect ratio 16:9, high resolution, photorealistic rendering, ultra-detailed."

# Generate the image
image = pipe(prompt).images[0]

# Display or save the image
image.show()  # Or use image.save("output.png")
'''