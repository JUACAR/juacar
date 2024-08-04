from PIL import Image
import os

def resize_images(input_dir, output_dir):
    # Verificar si el directorio de salida existe, si no, crearlo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Listar archivos en el directorio de entrada
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    for image_file in image_files:
        input_path = os.path.join(input_dir, image_file)
        output_path = os.path.join(output_dir, image_file)

        # Abrir la imagen con Pillow
        with Image.open(input_path) as img:
            # Obtener las dimensiones originales de la imagen
            width, height = img.size

            # Reducir a la mitad el tamaño de la imagen
            new_width = width // 2
            new_height = height // 2

            # Redimensionar la imagen con interpolación bilineal
            resized_img = img.resize((new_width, new_height), Image.BILINEAR)

            # Guardar la imagen redimensionada en el directorio de salida
            resized_img.save(output_path)
            print(f'Imagen redimensionada: {output_path}')

if __name__ == "__main__":
    # Especificar directorio de entrada y salida
    input_directory = 'D:/Me/Projects/juacar/img/juacar-2024'
    output_directory = 'D:/Me/Projects/juacar/img/juacar-2024'

    # Llamar a la función para redimensionar las imágenes
    resize_images(input_directory, output_directory)
