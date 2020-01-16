from common.Base_Unit import Base_Base


class Case_Login(Base_Base):
    """
    闻道作业测评测试的流程动作
    """
    def __init__(self):
        super().__init__()

    def start_operation(self, url):
        # 开启浏览器
        self._start(url)

    def username_input_input(self, case_name, username):
        # 用户名
        self._input(case_name, 'xpath', '//*[@id="app-el"]/div/div/div/div[2]/div/div[2]/input', username)

    def passwd_input_input(self, case_name, passwd):
        # 密码
        self._input(case_name, 'xpath', '//*[@id="app-el"]/div/div/div/div[2]/div/div[3]/input', passwd)

    def signup_button_click(self, case_name):
        # 登陆按钮
        self._click(case_name, 'xpath', '//*[@id="app-el"]/div/div/div/div[2]/div/div[4]/button')

    def userinfo_text_assertion(self, case_name):
        self._assertion(case_name, 'xpath', '//*[@id="app-el"]/div/div/div/div/div[1]/div[3]/div/div/div', "狗狗")

    def errorlogin_text_assertion(self, case_name):
        self._assertion(case_name, 'xpath', '//*[@id="app-el"]/div/div/div/div[2]/div/div[4]/div', '密码错误!')

    # 启动时日志记录
    def start_log(self):
        self.log(self.Set.operation_history_log, "info", "正在执行登录脚本......")

    # 结束时日志记录
    def end_log(self):
        self.log(self.Set.operation_history_log, "info", "登陆脚本执行完毕.")

    def sleep_operation(self, case_name):
        # 暂停操作
        self._delay(case_name)

    def close_operation(self):
        # 关闭浏览器
        self._quit()
