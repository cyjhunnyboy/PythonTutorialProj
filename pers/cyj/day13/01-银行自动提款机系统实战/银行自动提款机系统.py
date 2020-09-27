"""
人
类：User
属性：姓名、身份证号、电话号、卡
行为：

卡
类名：IDCard
属性：卡号、密码、余额

提款机
类名：ATM
属性：用户字典
行为：开户、查询、取款、存款、转账、改密、锁定、解锁、补卡、销户、退出

管理员
类名：Admin
属性：
行为：管理员界面、管理员验证、系统功能界面

"""
import os
import pickle
import time

from pers.cyj.day13.bank.admin import Admin
from pers.cyj.day13.bank.atm import ATM

filePath = os.path.join(os.getcwd(), "allUsers.txt")


def main():
    # 管理员开机
    admin = Admin()
    admin.printAdminView()
    if admin.adminOption():
        return -1

    # 提款机对象
    with open(filePath, "rb") as fRead:
        allUsers = pickle.load(fRead)
    print(allUsers)
    atm = ATM(allUsers)

    while True:
        admin.printSysFunctionView()
        # 等待用户操作
        option = input("请输入您的操作：")
        if option == "A":
            # 开户
            atm.createUser()
        elif option == "B":
            # 查询
            atm.searchUserInfo()
        elif option == "C":
            # 取款
            atm.withdrawal()
        elif option == "D":
            # 存款
            atm.deposit()
        elif option == "E":
            # 转账
            atm.transferAcc()
        elif option == "F":
            # 改密
            atm.modifyPwd()
        elif option == "G":
            # 锁定
            atm.lockUser()
        elif option == "H":
            # 解锁
            atm.unlockUser()
        elif option == "I":
            # 补卡
            atm.reissueCard()
        elif option == "J":
            # 销户
            atm.cancleAcc()
        elif option == "K":
            # 退出
            if not admin.adminOption():
                # 将当前系统中的用户信息保存到文件中
                with open(filePath, "wb") as fWrite:
                    pickle.dump(atm.allUsers, fWrite)
                return -1

        time.sleep(2)


if __name__ == '__main__':
    main()
