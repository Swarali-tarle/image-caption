# import requests
# API_TOKEN = "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"
# headers = {
#     "Authorization": f"Bearer {API_TOKEN}"
# }
# prompt = input("Enter a description for the image you'd like to generate: ")
# data = {
#     "inputs": prompt
# }
# response = requests.post(
#     "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
#     headers=headers, json=data
# )
# if response.status_code == 200:
#     with open("generated_image.png", "wb") as f:
#         f.write(response.content)
#     print("Image saved as 'generated_image.png'")
# else:
#     print("Failed:", response.status_code)
#     print(response.text)

import requests
import io
from PIL import Image

#API_TOKEN = "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"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

prompt = input("Enter a description for the image you'd like to generate: ")

# Using Stable Diffusion XL model which is known to work with the API
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

# Make the request
response = requests.post(
    API_URL,
    headers=headers,
    json={"inputs": prompt}
)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response content to an image
    image = Image.open(io.BytesIO(response.content))
    # Save the image
    image.save("generated_image.png")
    print("Image successfully generated and saved as 'generated_image.png'")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
















































































































    '''
    # Import necessary libraries
import requests  # For making HTTP requests to the Hugging Face API
import io        # To handle byte streams
from PIL import Image  # For image processing (opening, saving images)

# Your Hugging Face API token (keep this secure, don't expose it publicly)
API_TOKEN = "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"

# Set the authorization header using your API token
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Ask the user to enter a description of the image they want to generate
prompt = input("Enter a description for the image you'd like to generate: ")

# URL for the Stable Diffusion XL model hosted on Hugging Face
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

# Send a POST request to the Hugging Face API with the user's prompt
response = requests.post(
    API_URL,
    headers=headers,
    json={"inputs": prompt}  # Pass the text prompt in JSON format
)

# Check if the API request was successful (HTTP 200 = OK)
if response.status_code == 200:
    # Read the binary image data from the response
    image = Image.open(io.BytesIO(response.content))
    # Save the generated image to a file
    image.save("generated_image.png")
    print("Image successfully generated and saved as 'generated_image.png'")
else:
    # If the request failed, print the error code and message
    print(f"Error: {response.status_code}")
    print(response.text)

    '''