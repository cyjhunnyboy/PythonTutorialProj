import time


class Admin(object):

    admin = "admin"
    password = "admin123"

    def printAdminView(self):
        print("*****************************************************")
        print("*                                                   *")
        print("*                                                   *")
        print("*                 欢迎登录凯哥银行                    *")
        print("*                                                   *")
        print("*                                                   *")
        print("*****************************************************")

    def printSysFunctionView(self):
        print("*****************************************************")
        print("*  开户(A)  查询(B)  取款(C)  存款(D)  *")
        print("*  转账(E)  改密(F)  锁定(G)  解锁(H)  *")
        print("*  补卡(K)  销户(J)  退出(K)                         *")
        print("*****************************************************")

    def adminOption(self):
        inputAdmin = input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账户输入有误！")
            return -1
        inputPassword = input("请输入管理员密码：")
        if self.password != inputPassword:
            print("密码输入有误！")
            return -1

        # 能执行到这里说明账户密码正确
        print("操作成功！请稍后......")
        time.sleep(2)
        return 0
