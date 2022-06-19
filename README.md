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

![image](https://user-images.githubusercontent.com/89527573/174468429-0b41349e-7bdf-418b-bd31-78deceb0f639.png)
![image](https://user-images.githubusercontent.com/89527573/174468427-5b4faedf-b09b-4fdf-b8b2-2835fc5914c9.png)

### Jeans 2

![image](https://user-images.githubusercontent.com/89527573/174468435-d9aa4a04-4243-4099-89d2-ab0c8d5ab457.png)
![image](https://user-images.githubusercontent.com/89527573/174468436-21451931-5724-44f4-9684-287f09301d35.png)


# Measure similarity
---

The color data of the jeans if given like this.
![image](https://user-images.githubusercontent.com/89527573/174468417-0c016865-01bd-4c54-abd4-a26a9f43d32b.png)

Then we measure the distance between two jeans(I used Delta E1994). About ~15 seems acceptable distance.
The distance is weighted by its percentage calculated above.

![image](https://user-images.githubusercontent.com/89527573/174468409-56406fd2-c337-4f76-8225-62151b56258e.png)

