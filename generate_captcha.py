from captcha.image import ImageCaptcha
import random
import os

def generate_captchas(output_dir, num_samples):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    image = ImageCaptcha(width=160, height=60)
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    for i in range(num_samples):
        code = ''.join([random.choice(characters) for _ in range(6)])  # Генерация кода капчи
        image_file = os.path.join(output_dir, f'{code}.png')
        image.generate_image(code).save(image_file)
        print(f'Generated {image_file}')

if __name__ == "__main__":
    output_dir = 'captcha_images'
    num_samples = 1000
    generate_captchas(output_dir, num_samples)
