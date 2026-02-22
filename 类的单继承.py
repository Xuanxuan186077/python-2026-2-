import random
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
class Iphone(Phone):
    def __init__(self, model, price, iOS_version):
        super().__init__("Iphone", model, price)
        self.iOS_version = iOS_version
    def face_id(self):
        return f"{self.model} has Face ID."
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}, iOS version: {self.iOS_version}"
    
Huawei_P40 = Huawei("P40", 799, "10.1")
Iphone_12 = Iphone("12", 999, "14.1")
print(Huawei_P40.call("123-456-7890"))
print(Iphone_12)