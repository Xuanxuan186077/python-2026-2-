class Mother:
    def __init__(self):
        self.kongfu = '[妈妈煎饼果子技术]'
    def cook_pancake(self):
        print(f'该煎饼制作依靠{self.kongfu}')
class School:
     def __init__(self):
        self.kongfu = '[科班煎饼果子技术]'
     def cook_pancake(self):
        print(f'该煎饼制作依靠{self.kongfu}')
class Son(Mother, School):
    pass
s = Son()
s.cook_pancake()