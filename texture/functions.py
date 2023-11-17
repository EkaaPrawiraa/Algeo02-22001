import cv2
import numpy as np

def rgb_to_grayscale(rgb):
    return np.round(0.29 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2])

def make_cooccurrence(path):
    img = cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height, width, _ = img.shape
    matrix_size = (256, 256)
    matrix = np.zeros(matrix_size)

    grayscale_img = rgb_to_grayscale(img_rgb)

    for i in range(height):
        for j in range(width - 1):
            x = int(grayscale_img[i, j])
            y = int(grayscale_img[i, j + 1])
            matrix[x, y] += 1

    matrix += matrix.T  # Transpose in-place
    total = np.sum(matrix)
    comatrix = matrix / total
    return comatrix

def contrast(comatrix):
    i, j = np.ogrid[:256, :256]
    return np.sum(comatrix * ((i - j) ** 2))

def homogeneity(comatrix):
    i, j = np.ogrid[:256, :256]
    return np.sum(comatrix / (1 + (i - j) ** 2))

def entropy(comatrix):
    epsilon = 1e-1000
    comatrix[comatrix == 0] = epsilon
    return -np.sum(comatrix * np.log(comatrix))

def cosine_similarity(vect1, vect2):
    dot_product = np.dot(vect1, vect2)
    norm_vect1 = np.linalg.norm(vect1)
    norm_vect2 = np.linalg.norm(vect2)
    similarity = dot_product / (norm_vect1 * norm_vect2)
    return similarity

def makevector(path):
    comatrix = make_cooccurrence(path)
    vector = np.array([contrast(comatrix), homogeneity(comatrix), entropy(comatrix)])
    return vector

