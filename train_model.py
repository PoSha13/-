import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(36, activation='softmax')  # 36 классов для символов и дефисов
    ])
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model):
    datagen = ImageDataGenerator(rescale=1./255)
    
    train_generator = datagen.flow_from_directory(
        'preprocessed_images/parts',
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical'
    )
    
    # Выводим информацию для отладки
    print(f'Found {train_generator.samples} samples belonging to {train_generator.num_classes} classes.')
    
    if train_generator.samples == 0:
        raise ValueError("No images found in the specified directory.")
    
    model.fit(train_generator, epochs=10)
    model.save('captcha_model.h5')

if __name__ == "__main__":
    model = build_model()
    train_model(model)
