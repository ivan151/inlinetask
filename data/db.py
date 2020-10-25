class Fruit:
    def __init__(self, id, name, photo, rating=0):
        self.id = id
        self.name = name
        self.rating = rating
        self.photo = photo

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1


fruits = [Fruit(0, "banana", photo="http://dgdesign.ru/uploads/posts/2018-07/1532339411_545642411.png"),
          Fruit(1, "pineapple",
                photo="https://fruits-exotic.ru/upload/iblock/857/857e9e4d6f7d270ed49aa5920ab93027.jpg"),
          Fruit(2, "Apple", photo="http://magpara.ru/files/products/product_592_2_18902182.jpg")
          ]
