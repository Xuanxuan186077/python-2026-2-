import class

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        return f"Calling {number} from {self.model}."
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"
    def __call__(self, number):
        return self.call(number)    


class Huawei(Phone):
    def __init__ (self, model, price, HarmonyOS_version):
        super().__init__("Huawei", model, price)
        self.HarmonyOS_version = HarmonyOS_version
    def fingerprint(self):
        return f"{self.model} has a fingerprint sensor."
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}, HarmonyOS version: {self.HarmonyOS_version}"
class SatelliteDevice:
    def __init__(self, satellite = "GPS"):
        self.satellite = satellite
        return None
class HuaweiMate60(Huawei, SatelliteDevice):
    def __init__(self, price, HarmonyOS_version):
        super().__init__("Mate 60", price, HarmonyOS_version)#继承的是Huawei的__init__方法
        SatelliteDevice.__init__(self, "北斗卫星")#继承的是SatelliteDevice的__init__方法