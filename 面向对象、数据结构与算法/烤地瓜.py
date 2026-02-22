'''
类的应用：案例一：烤地瓜
需求主线：地瓜被烤时间      对应地瓜生熟状态
        0-3分钟           生的
        3-7分钟           半生不熟
        7-12分钟           熟的
        >12分钟          烤糊了
    添加的调料          用户按照自己的意愿添加调料
'''
class SweetPotato:
    def __init__(self):
        self.cooked_time = 0
        self.cooked_string = '生的'
        self.condiments = []
    def cook(self, time):
        self.cooked_time += time
        if self.cooked_time < 0:
            print('时间不能为负数')
        elif self.cooked_time >= 0 and self.cooked_time < 3:
            self.cooked_string = '生的'
        elif self.cooked_time >= 3 and self.cooked_time < 7:
            self.cooked_string = '半生不熟'
        elif self.cooked_time >= 7 and self.cooked_time < 12:
            self.cooked_string = '熟的'
        else:
            self.cooked_string = '烤糊了'
    def add_condiments(self, condiment):
        self.condiments.append(condiment)
    def __str__(self):
        return f'地瓜已经烤了{self.cooked_time}分钟了，现在是{self.cooked_string}的状态，添加的调料有{self.condiments}'
if __name__ == '__main__':
    sweet_potato = SweetPotato()
    print(sweet_potato)
    sweet_potato.cook(2)
    print(sweet_potato)
    sweet_potato.cook(2)
    print(sweet_potato)
    sweet_potato.cook(4)
    print(sweet_potato)
    sweet_potato.cook(5)
    print(sweet_potato)
    sweet_potato.add_condiments('番茄酱')
    sweet_potato.add_condiments('辣椒面')
    print(sweet_potato)