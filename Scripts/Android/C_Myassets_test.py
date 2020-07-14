from appium import webdriver
from PO.Android.MyassetsPage import Myassets
from PO.getconfig import setup_method
from PO.Base import Base
from libs.ShareModules import Getdata
import pytest,time

Transaction_pwd = Getdata('Login_tc','Transaction_pwd') # 交易密码
code = Getdata('Login_tc','code')  # 验证码

class TestMyassets:
    """
    我的资产
    """
    def setup_method(self):
        setup_method.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', setup_method.android_driver_caps)  # 串联
        self.myassets_page = Myassets(self.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成
        self.myassets_page.getinto_Myassets_page()

    def test_001_Myassets_scan(self):
        """
        用例一： 扫码界面
        """
        try:
            assert None == self.myassets_page.Myassets_scan()
        except (Exception, AssertionError):
            self.myassets_page.Allure_save_img("001_assets_scan_fail")
            raise Exception

    def test_002_Myassets_setting(self):
        """
        用例二：设置界面
        """
        try:
            assert "设置" == self.myassets_page.Myassets_setting()
        except (Exception, AssertionError):
            self.myassets_page.Allure_save_img("002_assets_setting_fail")
            raise Exception

    def test_003_Myassets_records(self):
        """
        用例三: 资产记录界面
        """
        try:
            assert "资产记录" == self.myassets_page.Myassets_records()
        except (Exception, AssertionError):
            self.myassets_page.Allure_save_img("002_assets_records_fail")
            raise Exception

    def test_004_Assets_receive(self):
        """
        用例四: 充值二维码界面
        """
        try:
            symbol = "BTC"
            assert "扫描二维码进行充值" == self.myassets_page.Assets_receive(symbol)
        except (Exception, AssertionError):
            self.myassets_page.Allure_save_img("004_assets_receive_fail")
            raise Exception

    def test_005_Assets_withdrawal(self,symbol,address,quantity,code,Transaction_pwd):
        """
        用例五: 提现流程
        :param symbol: 提现币种
        :param address: 提现地址
        :param quantity:  验证码
        :param code:  验证码
        :param Transaction_pwd:  交易密码
        """
        try:
            symbol = "BTC"
            address = '3KK4ioGAUs53tScfyRbEdfhhGugYa6x6t9'
            self.myassets_page.Assets_withdrawal(symbol,address,'0.5',code,Transaction_pwd)
        except (Exception, AssertionError):
            self.myassets_page.Allure_save_img("005_assets_withdrawal_fail")
            raise Exception

    def test_006_Assets_transfer(self,symbol,amount):
        """
        用例六: 划转流程
        :param symbol: 划转币种
        :param amount: 划转金额
        """
        try:
            symbol = "BTC"
            self.myassets_page.Assets_transfer(symbol,'0.5')
        except (Exception, AssertionError):
            self.myassets_page.Allure_save_img("006_assets_transfer_fail")
            raise Exception


    def teardown_method(self):
        self.driver.quit()


if __name__ == '__main__':
    # pytest.main(['-s', 'C:/Users/HP/Desktop/HooApp/Scripts/Android/A_Register_test.py
    # ::TestRigister::test_003_switch_nation_register'])
    pytest.main()