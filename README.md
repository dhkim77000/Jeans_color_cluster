# Jeans_color_cluster
---
Cluster jeans by its colors.(Currently undergoing)

## Motivation
---
Finding the right jeans that you want is difficult. Since the subtle differences in colors and its combination make huge different, recommending by just its price, brand, fit is not enough. The basic idea is to find the color components of the jeans and measured the distance between two jeans. The similar the colors and its combination is, the closer the distance will be. The image data of jeans are in https://github.com/dhkim77000/Farfetch_crawler/tree/master/img/jeans

#### Can we say those jeans are similar? It seems heavily weighted on brands
![image](https://user-images.githubusercontent.com/89527573/174465967-b865d069-961e-4c5d-a897-42a65c52a1be.png)


## Example
---
### Jeans 1

![image](https://user-images.githubusercontent.com/89527573/174426391-5d03eb07-afad-4a84-8205-3114185a0363.png)
![image](https://user-images.githubusercontent.com/89527573/174426386-ba82cacb-50b1-480a-9222-e260d26b50e6.png)

### Jeans 2

![image](https://user-images.githubusercontent.com/89527573/174426409-b333241d-594c-452d-a035-bd709e0186b4.png)
![image](https://user-images.githubusercontent.com/89527573/174426414-1ab6e0c2-7c77-4c70-8de2-d3b95545e72f.png)


# Measure similarity
---

The color data of the jeans if given like this.
![image](https://user-images.githubusercontent.com/89527573/174465994-28437ea2-c8a7-47e3-962a-b9a606534dd5.png)

Then we measure the distance between two jeans(I used Delta E1994). About ~15 seems acceptable distance.
The distance is weighted by its percentage calculated above.

![image](https://user-images.githubusercontent.com/89527573/174466169-8b71f740-aead-4a4a-b994-89fdac13e5ed.png)

