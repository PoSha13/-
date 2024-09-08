import os
import cv2
import numpy as np

def preprocess_images(input_dir, output_dir, num_parts=4):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            if img is None:
                print(f'Failed to read {img_path}')
                continue

            height, width = img.shape
            part_width = width // num_parts
            
            base_filename = os.path.splitext(filename)[0]
            
            for i in range(num_parts):
                part = img[:, i*part_width:(i+1)*part_width]
                part_filename = f'{base_filename}_part{i}.png'
                part_path = os.path.join(output_dir, part_filename)
                cv2.imwrite(part_path, part)
                print(f'Saved {part_path}')

if __name__ == "__main__":
    input_dir = 'captcha_images'
    output_dir = 'preprocessed_images/parts'
    preprocess_images(input_dir, output_dir)
