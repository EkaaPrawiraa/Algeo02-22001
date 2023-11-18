import cv2
import numpy as np
import time




class colormethod(object):
    def calculate_histogram(image_matrix):
        # start = time.time()
        (height, width, num_channels) = image_matrix.shape

        # Inisialisasi vektor histogram
        histogram_vector = np.zeros((16,48),dtype=float)

        # Mendefinisikan blok 4x4
        block_size = 4
        num_blocks_height = height // block_size
        num_blocks_width = width // block_size
        
        # Iterasi melalui blok-blok
      
        x=0
        for i in range(block_size):
            for j in range(block_size):
                # Batas blok
                block_start_row = i * num_blocks_height
                block_end_row = (i + 1) * num_blocks_height
                block_start_col = j * num_blocks_width
                block_end_col = (j + 1) * num_blocks_width
                
                # Mendapatkan blok citra
                block = image_matrix[block_start_row : block_end_row, block_start_col:block_end_col]
                Hue = block[:,:,0].flatten()
                Sat = block[:,:,1].flatten()
                Val = block[:,:,2].flatten()
                
                
                block_histogram_hue,_ = np.histogram(Hue, bins=16, range= (0, 180))
                block_histogram_sat,_ = np.histogram(Sat, bins=16, range= (0, 1))
                block_histogram_val,_ = np.histogram(Val, bins=16, range= (0, 1))
                
                if np.linalg.norm(block_histogram_hue) !=0:
                    block_histogram_hue = block_histogram_hue/np.linalg.norm(block_histogram_hue)
                if np.linalg.norm(block_histogram_sat) !=0:
                    block_histogram_sat = block_histogram_sat/np.linalg.norm(block_histogram_sat)
                if np.linalg.norm(block_histogram_val) !=0:
                    block_histogram_val = block_histogram_val/np.linalg.norm(block_histogram_val)
                # print(f"Hasil block_histogram: {np.array(block_histogram_hue)}"
                
                histogram_vector[x] = np.concatenate([block_histogram_hue.flatten(), block_histogram_sat.flatten(), block_histogram_val.flatten()])
                # print(f"Hasil block_histogram: {histogram_vector}")
                x += 1
                
        # end= time.time()  
        # print(f"Lama HISTOGRAM: {end-start}")
        return histogram_vector
   
    def calculate_cosine_similarity(hist1, hist2):
        # Flatten histograms
        result =0;
        
        for i in range(16):
            dot_product = np.dot(hist1[i],hist2[i])
            normal_a = np.linalg.norm(hist1[i])
            normal_b = np.linalg.norm(hist2[i])
            result += dot_product/(normal_a*normal_b)
        result/=16.0
        return result
    



    def rgb_to_hsv(rgbimage_path):
        # Baca gambar
        rgbimage = cv2.imread(rgbimage_path)
        
        
        #  Normalisasi nilai RGB
        normalized_image = rgbimage / 255.0
        
        # Mendapatkan nilai-nilai RGB
        red = normalized_image[:, :, 2]
        green = normalized_image[:, :, 1]
        blue = normalized_image[:, :, 0]
        
        # Mendapatkan nilai maksimum dan minimum dari RGB
        max_rgb = np.maximum(red, np.maximum(green, blue))
        min_rgb = np.minimum(red, np.minimum(green, blue))
        
        # Menghitung delta
        delta = max_rgb - min_rgb
        
        # Mencari nilai hue
        hue = np.where(delta == 0, 0, 
                   60 * np.where(max_rgb == red, (green - blue) / (delta + 1e-9) % 6,
                                np.where(max_rgb == green, (blue - red) / (delta + 1e-9) + 2,
                                         (red - green) / (delta + 1e-9) + 4)))

        # Menghitung nilai saturation
        saturation = np.where(max_rgb == 0, 0, delta / (max_rgb + 1e-9))

        # Menghitung nilai value
        value = max_rgb

        # Menggabungkan nilai H, S, V ke dalam satu array
        hsv_image = np.stack((hue, saturation, value), axis=-1)

        return hsv_image