##contoh 

import cv2
import numpy as np
from skimage import color

def rgb_to_hsv(rgb_image):
    # Normalisasi nilai RGB
    normalized_image = rgb_image/255.0
    #Mencari Cmax, Cmin, dan ∆
    Cmax = np.max(normalized_image, axis=2)
    Cmin = np.min(normalized_image, axis=2)
    delta = Cmax - Cmin

     # Mendapatkan nilai Hue
    hue = np.zeros_like(delta)
    hue[delta != 0] = np.where(Cmax == normalized_image[:,:,0], (60 * ((normalized_image[:,:,1] - normalized_image[:,:,2]) / delta) % 6),
                             np.where(Cmax == normalized_image[:,:,1], (60 * ((normalized_image[:,:,2] - normalized_image[:,:,0]) / delta) + 2),
                                      (60 * ((normalized_image[:,:,0] - normalized_image[:,:,1]) / delta) + 4)))
    
    # Mendapatkan nilai Saturation
    saturation = np.zeros_like(delta)
    saturation[delta != 0] = delta / Cmax
    
    # Mendapatkan nilai Value
    value = Cmax
    
    # Menggabungkan nilai Hue, Saturation, dan Value
    hsv_image = np.stack((hue, saturation, value), axis=-1)
    
    return hsv_image

def cosine_similarity(hist1, hist2):
    dot_product = np.dot(hist1, hist2)
    norm_hist1 = np.linalg.norm(hist1)
    norm_hist2 = np.linalg.norm(hist2)
    
    similarity = dot_product / (norm_hist1 * norm_hist2)
    
    return similarity

# Fungsi untuk menghitung histogram
def calculate_histogram(image):
    # Menghitung histogram menggunakan np.histogramdd
    histogram, _ = np.histogramdd(image.reshape(-1, 3), bins=(180, 256, 256), range=[(0, 180), (0, 1), (0, 1)])
    
    # Normalisasi histogram
    histogram /= np.sum(histogram)
    
    return histogram.flatten()

# Load image dataset (contoh: Anda memiliki dataset berisi beberapa gambar)
dataset_image1 = cv2.imread('C:\ITB\SEM 3\Alstrukdat\C\TUBES 1\Algeo001\CBIR\Dataset\est0.jpg')
dataset_image2 = cv2.imread('C:\ITB\SEM 3\Alstrukdat\C\TUBES 1\Algeo001\CBIR\Dataset\est1.jpg')

# Konversi warna dari RGB ke HSV untuk dataset
hsv_dataset_image1 = rgb_to_hsv(dataset_image1)
hsv_dataset_image2 = rgb_to_hsv(dataset_image2)

# Hitung histogram dari dataset
histogram_dataset_image1 = calculate_histogram(hsv_dataset_image1)
histogram_dataset_image2 = calculate_histogram(hsv_dataset_image2)

# Load input image
input_image = cv2.imread('C:\ITB\SEM 3\Alstrukdat\C\TUBES 1\Algeo001\CBIR\Input\in.jpg')

# Konversi warna dari RGB ke HSV untuk input image
hsv_input_image = rgb_to_hsv(input_image)

# Hitung histogram dari input image
histogram_input_image = calculate_histogram(hsv_input_image)

# Bandingkan histogram menggunakan cosine similarity
similarity_image1 = cosine_similarity(histogram_input_image, histogram_dataset_image1)
similarity_image2 = cosine_similarity(histogram_input_image, histogram_dataset_image2)

# Tampilkan hasil similarity
print(f"Similarity with dataset_image1: {similarity_image1}")
print(f"Similarity with dataset_image2: {similarity_image2}")