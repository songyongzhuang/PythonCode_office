import pytest


@pytest.fixture(scope='function', autouse=True)
def login():
    print('登录系统')


def test_01():
    print('测试用例一')


class TestCase:

    def test_03(self):
        print('测试用例三')

    def test04(self):
        print('测试用例四')

#
# if __name__ == '__main__':
#     pytest.main(['-s', 'pytest-demo.py'])
