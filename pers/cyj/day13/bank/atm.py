from pers.cyj.day13.bank.user import User
from pers.cyj.day13.bank.idcard import IDCard
import random


class ATM(object):

    def __init__(self, allUsers):
        # 卡号-用户
        self.allUsers = allUsers

    # 开户
    def createUser(self):
        # 目标：向用户字典中添加一对键值对(卡号-用户)
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")

        advanceDeposit = int(input("请输入预存款金额："))
        if advanceDeposit < 0:
            print("预存款输入有误！开户失败...")
            return -1
        onePwd = input("请设置密码：")
        # 验证密码
        if not self.checkPwd(onePwd):
            print("密码输入错误！开户失败...")
            return -1

        # 所有需要的信息就全了
        carId = self.randomCardId()
        card = IDCard(carId, onePwd, advanceDeposit)
        user = User(name, idCard, phone, card)
        # 存入字典
        self.allUsers[carId] = user
        print("开户成功！请牢记卡号（%s）..." % carId)

    # 查询
    def searchUserInfo(self):
        cardId = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardId)
        if not user:
            print("该卡号不存在！查询失败...")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再使用其他功能...")
            return -1
        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("密码输入错误！该卡已被锁定，请解锁后再使用其他功能...")
            user.card.cardLock = True
            return -1
        print("账号：%s  余额：%d" % (user.card.cardId, user.card.cardMoney))


    # 取款
    def withdrawal(self):
        cardId = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardId)
        if not user:
            print("该卡号不存在！取款失败...")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再使用其他功能...")
            return -1
        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("密码输入错误！该卡已被锁定，请解锁后再使用其他功能...")
            user.card.cardLock = True
            return -1
        # 取款
        money = int(input("请输入取款金额："))
        while True:
            if money <= 0:
                print("输入取款金额不能小于或等于0，请重新输入...")
                money = int(input("请输入取款金额："))
            break
        if money > user.card.cardMoney:
            print("余额不足！取款失败...")
            return -1
        user.card.cardMoney -= money
        print("取款成功！余额： %d" % user.card.cardMoney)

    # 存款
    def deposit(self):
        cardId = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardId)
        if not user:
            print("该卡号不存在！存款失败...")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再使用其他功能...")
            return -1
        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("密码输入错误！该卡已被锁定，请解锁后再使用其他功能...")
            user.card.cardLock = True
            return -1
        # 存款
        money = int(input("请输入存款金额："))
        while True:
            if money <= 0:
                print("输入存款金额不能小于或等于0，请重新输入...")
                money = int(input("请输入存款金额："))
            break
        user.card.cardMoney += money
        print("存款成功！余额： %d" % user.card.cardMoney)

    # 转账
    def transferAcc(self):
        pass

    # 改密
    def modifyPwd(self):
        pass

    # 锁定
    def lockUser(self):
        cardId = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardId)
        if not user:
            print("该卡号不存在！锁定失败...")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再使用其他功能...")
            return -1
        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("密码输入错误，锁定失败...")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号输入错误，锁定失败...")
            return -1
        # 锁定
        user.card.cardLock = True
        print("锁定成功...")

    # 解锁
    def unlockUser(self):
        cardId = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardId)
        if not user:
            print("该卡号不存在！解锁失败...")
            return -1
        if not user.card.cardLock:
            print("该卡没有被锁定！无需解锁...")
            return -1
        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("密码输入错误，解锁失败...")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号输入错误，解锁失败...")
            return -1
        # 解锁
        user.card.cardLock = False
        print("解锁成功...")

    # 补卡
    def reissueCard(self):
        pass

    # 销户
    def cancleAcc(self):
        pass

    # 验证密码
    def checkPwd(self, realPwd):
        for i in range(3):
            tempPwd = input("请输入密码：")
            if tempPwd == realPwd:
                return True
        return False

    # 生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(12):
                # 随机生成一个数字
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            # 判断是否重复
            if not self.allUsers.get(str):
                return str