from PIL import Image

def apply_grayscale_filter(input_image_path, output_image_path):
    try:
        # input image
        with Image.open(input_image_path) as img:
            # Convert the image to grayscale
            grayscale_img = img.convert("L")

            # Save grayscale image
            grayscale_img.save(output_image_path)
            print("Grayscale filter applied and saved as", output_image_path)
    except FileNotFoundError:
        print("Input image not found.")

if __name__ == "__main__":
    input_path = "input_image.jpg"  # Provide the path to your input image
    output_path = "output_grayscale.jpg"  # Output path for the grayscale image
    apply_grayscale_filter(input_path, output_path)
