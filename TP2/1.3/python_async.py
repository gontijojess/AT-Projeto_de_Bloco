import os
import time
import asyncio
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

async def process_image(image_path, output_dir):
    img = Image.open(image_path)
    img = img.filter(ImageFilter.BLUR)
    img.save(os.path.join(output_dir, os.path.basename(image_path)))

async def main_image_processing(input_dir, output_dir, num_threads):
    os.makedirs(output_dir, exist_ok=True)

    images = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]

    chunks = [images[i:i + num_threads] for i in range(0, len(images), num_threads)]

    for chunk in chunks:
        await asyncio.gather(*(process_image(img, output_dir) for img in chunk))

def measure_image_processing_time(input_dir, output_dir, max_threads=10):
    times = []

    for num_threads in range(1, max_threads + 1):
        start_time = time.time()
        asyncio.run(main_image_processing(input_dir, output_dir, num_threads))
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)
        print(f"Threads: {num_threads}, Tempo: {elapsed_time:.2f} segundos")

    plt.plot(range(1, max_threads + 1), times, marker='o')
    plt.title("Número de Threads vs Tempo de Processamento")
    plt.xlabel("Número de Threads")
    plt.ylabel("Tempo (segundos)")
    plt.savefig('grafico_processing_inages.png')
    print('Grafico salvo como grafico_processing_inages.png')

input_dir = "input_inages"
output_dir = "output_inages"

measure_image_processing_time(input_dir, output_dir, max_threads=5)