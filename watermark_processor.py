import os
from dataclasses import dataclass
from PIL import Image, ImageEnhance


@dataclass
class WatermarkProcessor:
    input_folder: str
    output_folder: str
    watermark_image_path: str
    scale: float = 0.2
    opacity: float = 0.5

    def __post_init__(self):
        # Check if the output folder exists, create it if it doesn't
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def apply_watermark(self, input_image_path: str, output_image_path: str):
        # Open the original image
        image = Image.open(input_image_path).convert("RGBA")
        width, height = image.size

        # Open the watermark image with transparent background
        watermark = Image.open(self.watermark_image_path).convert("RGBA")

        # Resize the watermark to be proportional to the original image
        watermark_width = int(width * self.scale)
        watermark_height = int(watermark.size[1] * (watermark_width / watermark.size[0]))
        watermark = watermark.resize((watermark_width, watermark_height), Image.LANCZOS)

        # Adjust the opacity of the watermark
        if self.opacity < 1:
            alpha = watermark.split()[3]  # Extract the alpha channel
            alpha = ImageEnhance.Brightness(alpha).enhance(self.opacity)  # Adjust the opacity
            watermark.putalpha(alpha)

        # Calculate the position to center the watermark
        watermark_position = ((width - watermark_width) // 2, (height - watermark_height) // 2)

        # Create a new image with the watermark overlayed
        watermarked_image = Image.new("RGBA", image.size)
        watermarked_image = Image.alpha_composite(image, Image.new("RGBA", image.size))
        watermarked_image.paste(watermark, watermark_position, watermark)

        # Save the final image
        watermarked_image = watermarked_image.convert("RGB")  # Remove alpha channel to save as JPEG
        watermarked_image.save(output_image_path, quality=95)

        print(f"Watermark (image) applied and image saved at {output_image_path}")

    def process_images(self):
        # Iterate over all files in the input folder
        for filename in os.listdir(self.input_folder):
            input_image_path = os.path.join(self.input_folder, filename)
            output_image_path = os.path.join(self.output_folder, filename)

            # Only process image files
            if input_image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                self.apply_watermark(input_image_path, output_image_path)
            else:
                print(f"File {filename} is not an image. Skipping...")

# Define paths and parameters
input_folder = 'imgs/original'
output_folder = 'imgs/withwatermark'
watermark_image_path = 'imgs/logo_horizontal.png'  # Replace with the path to your watermark image

# Instantiate the class and process the images
processor = WatermarkProcessor(input_folder, output_folder, watermark_image_path, scale=0.7, opacity=0.3)
processor.process_images()
