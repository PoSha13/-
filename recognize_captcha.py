from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

def recognize_captcha(model_path, image_path):
    model = load_model(model_path)
    
    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    
    # Для демонстрации, используем индекс класса как строку
    class_labels = {i: f'char_{i}' for i in range(36)}  # Подставьте правильные метки классов
    predicted_label = class_labels.get(predicted_class, 'Unknown')
    
    return predicted_label

if __name__ == "__main__":
    model_path = 'captcha_model.h5'
    test_image_path = '4RCCCK.png'
    result = recognize_captcha(model_path, test_image_path)
    print(f'Recognized captcha: {result}')
