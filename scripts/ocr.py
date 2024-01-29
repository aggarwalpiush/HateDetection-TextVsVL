import os
import json
from PIL import Image
import pytesseract

# path of dataset
image_folder = '/Users/jawman/IdeaProjects/HateDetection-TextVsVL/confounders/Addo_Trump'

# empty list image data
image_data_list = []

# loop through each image file in the folder
for image_file in os.listdir(image_folder):
    if image_file.endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(image_folder, image_file)

        image_id = os.path.splitext(image_file)[0]
        # load image
        image = Image.open(image_path)

        # perform ocr on the image to extract text
        extracted_text = pytesseract.image_to_string(image)

        # append image data to the list
        image_data = {
            "id": image_id,
            "img": image_file,
            "text": extracted_text.strip()
        }
        image_data_list.append(image_data)

# save data to JSON file
output_file = 'test.jsonl'
with open(output_file, 'w') as jsonl_file:
    for image_data in image_data_list:
        jsonl_file.write(json.dumps(image_data) + '\n')

print(f"Image data saved to {output_file}")
