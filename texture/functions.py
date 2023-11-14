import cv2
import numpy as np
def rgbtograyscale(rgb):
    return round(0.29*rgb[0]+0.587*rgb[1]+0.114*rgb[2])

def makecooccurance(path):
    img=cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width, _=img.shape
    matrix_size = (256, 256)
    matrix = np.zeros(matrix_size)
    for i in range(height):
        for j in range(width-1):
            x=rgbtograyscale(img_rgb[i,j])
            y=rgbtograyscale(img_rgb[i,j+1])
            matrix[x,y]+=1
    return matrix

def contrast(comatrix):
    hasil=0
    for i in range(256):
        for j in range(256):
            hasil+=comatrix[i,j]*((i-j)**2)
    return hasil
def homogeneity(comatrix):
    hasil=0
    for i in range(256):
        for j in range(256):
            hasil += comatrix[i, j] / (1 + (i - j) ** 2)
    return hasil
def entropy(comatrix):
    epsilon = 1e-10
    comatrix[comatrix == 0] = epsilon
    entropy = -np.sum(comatrix * np.log(comatrix))
    return entropy

def cosine_similarity(vect1, vect2):
    dot_product = np.dot(vect1, vect2)
    norm_vect1 = np.linalg.norm(vect1)
    norm_vect2 = np.linalg.norm(vect2)
    
    similarity = dot_product / (norm_vect1 * norm_vect2)
    
    return similarity
def makevector(path):
    comatrix=makecooccurance(path)
    vector=np.array([contrast(comatrix), homogeneity(comatrix), entropy(comatrix)])
    return vector
print(cosine_similarity(makevector('../media/uploaded_images/402773.jpg'), makevector('../media/uploaded_images/402773_XXyzSc7.jpg')))