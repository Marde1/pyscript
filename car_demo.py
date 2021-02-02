class Car():
    def __init__(self,make,model,year): #
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def update_odoment(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止讲里程表度数往回调
        :param mileage:
        :return:
        """

class ElectricCar(Car):
    