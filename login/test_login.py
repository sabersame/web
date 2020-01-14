import pytest
from case.case_login import Case_Login
from public.Data_Unit import Data_Base


class Test_login:
    """
    GitHub GUI测试的运行
    """
    data_list = Data_Base("login").result

    def setup_class(self):
        # 初始化浏览器实例并且打开被测页面
        self.d = Case_Login()
        self.d.start_log()
        self.d.start_operation("http://jfzy.eastedu.test/#/login")

    def teardown_class(self):
        self.d.end_log()
        self.d.close_operation()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(argnames="username", argvalues=data_list["e_username"])
    @pytest.mark.parametrize(argnames="passwd", argvalues=data_list["e_passwd"])
    def test_error_login(self, username, passwd, case_name="login_error"):
        self.d.username_input_input(case_name, username)
        self.d.passwd_input_input(case_name, passwd)
        self.d.signup_button_click(case_name)

        # 错误断言
        self.d.errorlogin_text_assertion(case_name)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(argnames="username", argvalues=data_list["c_username"])
    @pytest.mark.parametrize(argnames="passwd", argvalues=data_list["c_passwd"])
    def test_correct_login(self, username, passwd, case_name="login_correct"):
        self.d.username_input_input(case_name, username)
        self.d.passwd_input_input(case_name, passwd)
        self.d.signup_button_click(case_name)

        # 正确断言
        self.d.userinfo_text_assertion(case_name)
