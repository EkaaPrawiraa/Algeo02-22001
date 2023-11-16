import cv2
import numpy as np
import time




class colormethod(object):
    def rgb_to_hsv(rgbimage):
        #tinggi dan lebar image
        start = time.time()
        (height, width) = rgbimage.shape[:2] 
        #3 dimensi untuk H S V
        fitur=np.zeros((height,width,3),dtype=float)
        # Normalisasi nilai RGB
        normalized_image = rgbimage/255.0
       
        # calculating cmax,cmin,delta
        red = normalized_image[:,:,2]
        green = normalized_image[:,:,1]
        blue = normalized_image[:,:,0]
        # print(f"Hasil red: {red}")
        # print(f"Hasil green: {green}")
        # print(f"Hasil blue: {blue}")

        result = np.zeros((height,width,2),dtype=float)
        for i in range(height):
            for j in range(width):
                # array of max rgb
                result[i][j][0]=colormethod.maxvalue(red[i][j],green[i][j],blue[i][j])
                #array of min
                result[i][j][1]=colormethod.minvalue(red[i][j],green[i][j],blue[i][j])
                delta = result[i][j][0]-result[i][j][1]

                #mencari nilai H
                if delta ==0:
                    fitur[i][j][0]=0
                elif result[i][j][0]==red[i][j]:
                    fitur[i][j][0] = 60 * ( (green[i][j]-blue[i][j])/delta %6)
                elif result[i][j][0]==green[i][j]:
                    fitur[i][j][0] = 60 * ( (green[i][j]-blue[i][j])/delta +2)
                else:
                    fitur[i][j][0] = 60 * ( (green[i][j]-blue[i][j])/delta +4)

                #mencari nilai S
                if result[i][j][0] == 0:
                    fitur[i][j][1]=0
                elif result[i][j][0] != 0:
                    fitur[i][j][1]=delta/result[i][j][0]
                
                #mencari nilai V
                fitur[i][j][2]=result[i][j][0]
        end = time.time()

        # print(f"Lama RGB: {end-start}")
        return fitur
        
    

  





    

    def maxvalue(a,b,c):
        max_value = a  # Inisialisasi dengan nilai pertama

    
        if b > max_value:
            max_value = b

        if c > max_value:
            max_value = c

        return max_value
    def minvalue(a,b,c):
        min_value = a  # Inisialisasi dengan nilai pertama

    
        if b < min_value:
            min_value = b

        if c < min_value:
            min_value = c

        return min_value
    

    
    
    def calculate_histogram(image_matrix):
        start = time.time()
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
                
        end= time.time()  
        # print(f"Lama HISTOGRAM: {end-start}")
        return histogram_vector
   


    def calculate_cosine_similarity(hist1, hist2):
        # Flatten histograms
        dot_product = np.dot(hist1,hist2)
        normal_a = np.linalg.norm(hist1)
        normal_b = np.linalg.norm(hist2)
        similarity = dot_product/(normal_a*normal_b)

        return similarity