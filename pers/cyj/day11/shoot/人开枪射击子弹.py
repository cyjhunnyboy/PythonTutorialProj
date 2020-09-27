from pers.cyj.day11.shoot.person import Person
from pers.cyj.day11.shoot.gun import Gun
from pers.cyj.day11.shoot.bulletbox import BulletBox
"""
人
类名：Person
属性：抢
行为：fire

抢
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：BulletBox
属性：bulletCount

"""

if __name__ == "__main__":
    # 弹夹
    bulletBox = BulletBox(5)
    # 抢
    gun = Gun(bulletBox)
    # 人
    per = Person(gun)
    # 开火
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fire()

    per.fillBullet(3)
    per.fire()
