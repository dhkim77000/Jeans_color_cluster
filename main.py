from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import numpy as np
import cv2
import pandas as pd
from tqdm import tqdm
import operator
from PIL import ImageColor

def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color
def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (1400, 1000), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img

def color_analysis(img):
    total = img.shape[0] * img.shape[1]
    clf = KMeans(n_clusters = 6)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    counts = sorted(counts.items(), key=operator.itemgetter(1))
    
    ordered_colors = []
    ordered_values = []
    
    for data in counts:
        color = data[0]
        counts = data[1]
        ordered_colors.append(center_colors[color])
        ordered_values.append(counts)
    

    hex_colors = [rgb_to_hex(color) for color in ordered_colors]
    
    data ={}
    
    for i in range(len(ordered_colors)):
        RGB = ordered_colors[i]
        if np.mean(RGB) < 240:
            data[hex_colors[i]] = ordered_values[i]
        
    del ordered_colors
    del ordered_values
    del hex_colors

    data = Normalize(data)

    return data

def Normalize(data):
    total = np.sum(list(data.values()))
    for i,color in enumerate(data.keys()):
        data[color] = list(data.values())[i] / total
    return data
    


if __name__ == "__main__":

    jeans_df = pd.read_csv("/home/dhkim/Farfetch_Crawler/data/data.csv", encoding = "ISO-8859-1")
    jeans_df = jeans_df.loc[jeans_df['Category'] == 'jeans']
    jeans_df['Color Components'] = None

    for i in tqdm(range(len(jeans_df))):
        image_id = str(jeans_df.loc[i,'Unnamed: 0.1.1'])
        image = cv2.imread("/home/dhkim/Farfetch_Crawler/img/jeans/"+ image_id + '.jpg')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        modified_image = prep_image(image)
        data = color_analysis(modified_image)
        

        
        jeans_df.loc[i,'Color Components'] = str(data)  ##save as string, use eval() to convert to dict

    jeans_df.to_csv('/home/dhkim/Jeans_cluster/jeans_color_data.csv')
    
