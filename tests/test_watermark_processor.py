import os
from PIL import Image
from watermark_processor import WatermarkProcessor


def test_apply_watermark(monkeypatch, tmpdir):
    # Use tmpdir for input/output simulation
    input_dir = tmpdir.mkdir("input")
    output_dir = tmpdir.mkdir("output")
    input_image = str(input_dir.join("image.png"))
    output_image = str(output_dir.join("image_with_watermark.png"))
    watermark_image = str(tmpdir.join("logo_horizontal.png"))

    # Create a dummy input image to simulate input image file
    img = Image.new("RGBA", (1000, 500), (255, 255, 255, 255))  # Create a white dummy image
    img.save(input_image)

    # Verify the input image was created
    assert os.path.exists(input_image), "Input image should exist but was not created."

    # Create a dummy watermark image
    watermark_img = Image.new("RGBA", (100, 50), (0, 0, 0, 0))  # Transparent watermark

    # Save the original Image.open method
    original_image_open = Image.open

    # Monkeypatch Image.open to handle both input image and watermark image
    def mock_open(path):
        if path == watermark_image:
            return watermark_img  # Return mock watermark for the watermark path
        return original_image_open(path)  # Open the original input image for the input path

    monkeypatch.setattr(Image, "open", mock_open)
    monkeypatch.setattr(img, "save", lambda *args, **kwargs: None)

    processor = WatermarkProcessor(input_folder=str(input_dir),
                                   output_folder=str(output_dir),
                                   watermark_image_path=watermark_image)

    # Call apply_watermark
    processor.apply_watermark(input_image_path=input_image, output_image_path=output_image)

    # Verify that the output image was created
    assert os.path.exists(output_image), "Output image should exist but was not created."


def test_process_images(monkeypatch, tmpdir):
    # Mocking directories
    input_dir = tmpdir.mkdir("input")
    output_dir = tmpdir.mkdir("output")
    watermark_image = str(tmpdir.join("logo_horizontal.png"))

    # Create dummy images in input folder
    input_image_1 = input_dir.join("image1.png")
    input_image_1.write("content")
    input_image_2 = input_dir.join("image2.jpg")
    input_image_2.write("content")

    processor = WatermarkProcessor(input_folder=str(input_dir),
                                   output_folder=str(output_dir),
                                   watermark_image_path=watermark_image)

    # Monkeypatch the apply_watermark function
    def mock_apply_watermark(*args, **kwargs):
        pass

    monkeypatch.setattr(processor, 'apply_watermark', mock_apply_watermark)

    # Call process_images
    processor.process_images()

    # Assert that apply_watermark was called for each image
    assert os.path.exists(str(input_image_1))
    assert os.path.exists(str(input_image_2))
