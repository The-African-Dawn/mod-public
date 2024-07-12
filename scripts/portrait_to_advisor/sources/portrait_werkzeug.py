from PIL import Image
import os

class PortraitWerkzeug:
    def process_image(input_file, output_file):
        """
        A function that processes an image by opening, converting, resizing, and saving it.

        Args:
            input_file (str): The path to the input image file.
            output_file (str): The path to save the processed image.

        Returns:
            None
        """
        img = Image.open(input_file)
        img = img.convert("RGBA")
        img = img.resize((38, 50), resample=Image.LANCZOS if hasattr(Image, 'LANCZOS') else Image.ANTIALIAS)
        img.save(output_file)

    def combine_images(input_file, output_file, new_size, position):
        """
        Combines two images into a single image and saves the result.

        Args:
            input_file (str): The path to the input image file.
            output_file (str): The path to the output image file.
            new_size (tuple): The size of the new image.
            position (tuple): The position of the input image in the new image.

        Returns:
            None
        """
        input_img = Image.open(input_file)
        new_img = Image.new('RGBA', new_size)
        new_img.paste(input_img, position)
        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'base.png')
        base_img = Image.open(base_path).convert('RGBA')
        input_img = input_img.rotate(10)
        new_img.paste(input_img, position)
        base_img.paste(base_img, (0, 0), base_img)
        combined_img = Image.alpha_composite(new_img, base_img)
        combined_img.save(output_file)
        
    def process_and_combine_images(input_file, output_file, new_size, position, combined_file):
        """
        A function that processes and combines images, saves the results, and removes the intermediate image file.

        Args:
            input_file (str): The path to the input image file.
            output_file (str): The path to save the processed image.
            new_size (tuple): The size of the new image.
            position (tuple): The position of the input image in the new image.
            combined_file (str): The path to save the combined image.

        Returns:
            None
        """
        PortraitWerkzeug.process_image(input_file, output_file)
        PortraitWerkzeug.combine_images(output_file, combined_file, new_size, position)
        os.remove(output_file)