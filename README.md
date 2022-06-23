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

Then we measure the distance between two jeans(I used Delta E1994)
#### Color Space
![image](https://user-images.githubusercontent.com/89527573/175081709-c048973e-4bf8-4241-88d8-7ba141f2f5f2.png)

The distance is weighted by its percentage calculated above.

![image](https://user-images.githubusercontent.com/89527573/174468409-56406fd2-c337-4f76-8225-62151b56258e.png)

#### Distance = 25.051756135932177(Pretty Close)

![3](https://user-images.githubusercontent.com/89527573/174489847-7181a63a-8f59-47cd-9d8d-ca07248c4919.jpg)
![4](https://user-images.githubusercontent.com/89527573/174489860-e9dd5de8-76f7-4e46-bb33-342955a7781c.jpg)

#### Distance = 91.66139599425614(Pretty far)

![image](https://user-images.githubusercontent.com/89527573/174490568-eecef2e2-aa9c-4f74-836a-e6e869678a41.png)
![4](https://user-images.githubusercontent.com/89527573/174489860-e9dd5de8-76f7-4e46-bb33-342955a7781c.jpg)

#### Since the matrix is symmetric, code only calculates upper triangle of the matrix.
![image](https://user-images.githubusercontent.com/89527573/175212714-515c007f-c336-4a86-a0a6-057b84ce3c68.png)


# Expected Output
---
Color distance Matrix
![image](https://user-images.githubusercontent.com/89527573/174491104-0bbbff35-6e94-4121-953f-ff967eb17a5a.png)


