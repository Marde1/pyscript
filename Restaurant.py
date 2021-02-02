class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        # self.describe_restaurant()
        # self.open_restaurant()

    def describe_restaurant(self):
        """酒店名称和菜肴类型"""
        print("The Restaurant Name Is ",self.restaurant_name.title())
        print("The cuisine type is ",self.cuisine_type.title())

    def open_restaurant(self):
        print("The Restaurant is opening")

if __name__ =="__main__":
    restaurant1 = Restaurant("quanjude","chinese food")
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    restaurant2 = Restaurant("jiangjiacaiguan","chinese food")
    restaurant2.describe_restaurant()
    restaurant3 = Restaurant("kendeji", "快餐")
    restaurant3.describe_restaurant()
