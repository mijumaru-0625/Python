class Robot:
    """ お手伝いロボ """
    def __init__(self, name, battery) -> None:
        # どんなデータをもつのか
        self._job = "お手伝い"
        self._name = name
        self._battery = battery

    # プロパティ:値を返すのみ
    @property
    def job(self):
        return self._job
    
    @property
    def name(self):
        return self._name
    
    @property
    def battery(self):
        return self._battery
    
    @battery.setter
    def battery(self, value):
        if 0 <= value <= 100:
            self._battery = value
        else:
            print("注意: batteryの値は、0～100にしてください。")


    # メソッド:どんな処理をするのか
    def show_info(self):
        print(f"私は「{self._name}」です。仕事は{self._job}で、充電残量は{self._battery}です。")

    def do_work(self):
        self._battery -= 10
        print(f"{self._name}は、お手伝いをしました。充電残量は{self._battery}です。")



robot1 = Robot("ココア", 100)
robot2 = Robot("ラテ", 80)
robot1.battery = 10000
robot1.show_info()
robot2.show_info()
print("【仕事を命令】")
robot1.do_work()
robot2.do_work()