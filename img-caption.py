from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def caption_image(image_path):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")

    output = model.generate(**inputs, max_length=30)
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    return caption

def main():
    image_path = "image.jpg"
    
    try:
        caption = caption_image(image_path)
        print(f"Image: {image_path}")
        print(f"Caption: {caption}")
        
        from matplotlib import pyplot as plt
        image = Image.open(image_path)
        plt.imshow(image)
        plt.axis('off')
        plt.title(caption)
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()







































































































'''
# Import necessary libraries
from PIL import Image  # For image handling
from transformers import BlipProcessor, BlipForConditionalGeneration  # For loading BLIP model and processor
from matplotlib import pyplot as plt  # For displaying the image and caption

# Function to generate image caption using BLIP model
def caption_image(image_path):
    # Load the BLIP processor and model (BLIP for image captioning)
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    # Open the image and convert it to RGB format (required by the model)
    image = Image.open(image_path).convert('RGB')
    
    # Use the processor to prepare the image as input for the model (tokenization and feature extraction)
    inputs = processor(image, return_tensors="pt")
    
    # Generate the output caption from the model (max_length=30 limits the caption's length)
    output = model.generate(**inputs, max_length=30)
    
    # Decode the output tokens to generate a readable caption
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    # Return the generated caption
    return caption

# Main function that drives the program
def main():
    # Path to the image that needs captioning
    image_path = "image.jpg"  # Make sure 'image.jpg' is in the same directory
    
    try:
        # Generate caption for the image by calling the caption_image function
        caption = caption_image(image_path)
        
        # Print the image path and the generated caption
        print(f"Image: {image_path}")
        print(f"Caption: {caption}")
        
        # Open the image again for displaying with the caption
        image = Image.open(image_path)
        
        # Display the image using matplotlib
        plt.imshow(image)  # Show the image
        plt.axis('off')  # Hide the axis
        plt.title(caption)  # Set the title of the image as the caption
        plt.show()  # Display the image in a window
        
    except Exception as e:
        # In case of an error (e.g., image file not found, model issues), print the error message
        print(f"Error: {e}")

# If the script is being run directly (not imported), run the main function
if __name__ == "__main__":
    main()
'''