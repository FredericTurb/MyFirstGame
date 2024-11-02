from PIL import Image

def flip_image_horizontally(input_path, output_path):
    # Open the image file
    with Image.open(input_path) as img:
        # Flip the image horizontally
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        # Save the flipped image
        flipped_img.save(output_path)

# Example usage
input_image_path = 'zombie.png'  # Replace with your input image path
output_image_path = 'zombie.png'  # Replace with your desired output path

flip_image_horizontally(input_image_path, output_image_path)
print(f"Flipped image saved as: {output_image_path}")