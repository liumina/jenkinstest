import allure


def test_01():
    print("111")
    assert 1

@allure.step('登录功能测试')
def test_login():
    allure.attach('登录', '输入用户名')
    print("aaa")
    allure.attach('登录', '输入密码')
    print("bbb")
    allure.attach('登录', '点击登录')
    print("登录")
    assert 0