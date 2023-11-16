##contoh 

import cv2
import numpy as np
import os
import math
from skimage import color
from cbircolor import colormethod
import time













def read_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            # Baca gambar
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            if image is not None:
                images.append(image)
            else:
                print(f"Failed to read image: {image_path}")                                    

    return images

images_path = "CBIR\Input"
list_images=read_images_from_folder(images_path)

input_image = cv2.imread("CBIR\Input\input.jpg")
hsv_input_image = colormethod.rgb_to_hsv(input_image)
histogram_input_image = colormethod.calculate_histogram(hsv_input_image)

start_time = time.time()
for image in list_images:
    x=0
    jumlah =0
    data_images=[]
    output_image=[]
    dataset_image = image
    hsv_data_image = colormethod.rgb_to_hsv(dataset_image)
    histogram_dataset_image = colormethod.calculate_histogram(hsv_data_image)
    similarity_image2 =0
    for i in range(16):
        similarity_image2 += colormethod.calculate_cosine_similarity(histogram_input_image[i], histogram_dataset_image[i])
    
    similarity_image2 /=16.0
    print(f"Similarity dengan foto ke-{x}: {similarity_image2}")
    if similarity_image2 >= 0.6:
        output_image.append(image)
        print(f"Foto mirip dengan foto ke-{x}: {similarity_image2}")
        jumlah = jumlah +1
    x = x+1

print(f"Jumlah foto yang mirip: {jumlah}")










                      





end_time = time.time()
execution_time = end_time - start_time

# # Tampilkan hasil similarity
# similarity = cosine_similarity(histogram_input_image.flatten(), histogram_dataset_image.flatten())

# print(f"Cosine Similarity: {similarity}")

print(f"Waktu eksekusi: {execution_time} detik")