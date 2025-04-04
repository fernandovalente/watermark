# Watermark Processor

## License and Author

MIT License

Copyright (c) 2024 Fernando Valente

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Author**: Fernando Valente

## Overview

The **Watermark Processor** is a Python project designed to apply watermarks to images in bulk. The watermark can either be a text overlay or a custom image with transparency. The processor resizes the watermark proportionally based on the size of the original image and applies it at the center. The watermark’s opacity can also be controlled.

The project is structured to be reusable and easy to extend. Additionally, it includes unit tests using the `pytest` framework to ensure the processor works as expected.

## Features

- Apply a watermark (text or image) to a batch of images.
- Resize the watermark proportionally to the original image.
- Control the watermark’s opacity.
- Process images in different formats (`.png`, `.jpg`, `.jpeg`).
- Easy configuration for input/output folders and watermark settings.


## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/watermark.git
    cd watermark
    ```

2. Create a Python virtual environment and activate it:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The processor can be configured and executed by editing the main script `watermark_processor.py`. Here’s how you can use it:

1. **Prepare the directories**:
   - Place your original images in the `imgs/original` folder.
   - Place your watermark image (e.g., `logo_horizontal.png`) in the `imgs/` folder.

2. **Configure the processor**:
   - Edit the paths and parameters in the script to suit your needs.

    ```python
    # Define paths and parameters
    input_folder = 'imgs/original'
    output_folder = 'imgs/withwatermark'
    watermark_image_path = 'imgs/logo_horizontal.png'

    # Create and run the processor
    processor = WatermarkProcessor(input_folder, output_folder, watermark_image_path, scale=0.7, opacity=0.3)
    processor.process_images()
    ```

    - **Scale**: Defines how large the watermark will be in relation to the original image (e.g., `scale=0.7` makes the watermark 70% of the original image width).
    - **Opacity**: Controls the transparency of the watermark (e.g., `opacity=0.3` means 30% opacity).

3. **Run the script**:
   
   After configuring the script, run it with:

    ```bash
    python watermark_processor.py
    ```

   Processed images will be saved in the `imgs/withwatermark` folder.

## Testing

The project includes unit tests that use the `pytest` framework. These tests validate the functionality of the watermark processor.

### Running Tests

1. Install the testing dependencies:

    ```bash
    pip install pytest pytest-mock pytest-cov
    ```

2. Run the tests:

    ```bash
    pytest --cov=watermark_processor tests/
    ```

    This will run all unit tests and generate a coverage report.

3. To generate an HTML report of the coverage:

    ```bash
    pytest --cov=watermark_processor --cov-report=html tests/
    ```

    This will create a `htmlcov/` directory containing the report, which you can open in a browser to see the test coverage.

### Test Explanation

The tests are located in the `tests/test_watermark_processor.py` file and cover the following cases:
- **Initialization Test**: Verifies that the processor is initialized correctly.
- **Watermark Application Test**: Mocks the image and watermark to verify that the watermark is applied correctly.
- **Batch Processing Test**: Simulates multiple images and verifies that all are processed.

## Dependencies

- **Python 3.8+**
- **Pillow**: A Python Imaging Library (PIL) fork for working with images.
- **pytest**: A testing framework for writing and running tests.
- **pytest-mock**: Plugin for pytest to mock dependencies in tests.
- **pytest-cov**: Plugin to measure code coverage during test execution.

Feel free to customize this project to suit your needs or contribute to improve it further!
