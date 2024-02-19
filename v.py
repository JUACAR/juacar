import cv2
import random

def capture_frames(video_path, output_folder, num_frames=200):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error al abrir el video.")
        return

    # Obtiene la información del video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Selecciona 200 fotogramas al azar
    selected_frames = random.sample(range(total_frames), num_frames)

    # Captura y guarda los fotogramas seleccionados
    for frame_number in selected_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()

        if not ret:
            print(f"No se pudo leer el fotograma {frame_number}")
            continue

        frame_filename = f"{output_folder}/frame_{frame_number}.jpg"
        cv2.imwrite(frame_filename, frame)

    cap.release()
    print(f"Se capturaron {num_frames} fotogramas al azar y se guardaron en {output_folder}.")

if __name__ == "__main__":
    video_path = "D:/Me/Projects/juacar/img/juacar-2023/directora/Video de WhatsApp 2024-02-15 a las 11.39.36_58a340ec.mp4"
    output_folder = "D:/Me/Projects/juacar/img/juacar-2023/directora"  # Carpeta de salida para los fotogramas

    capture_frames(video_path, output_folder)
