import yaml
import os


def read_yaml_data(yaml_file):
    # "获取yaml的数据"
    yaml_file_temp = r"C:\Users\kk\PycharmProjects\yqhk-Project\config\user.yaml"
    yaml_data = open(yaml_file, 'r', encoding='utf-8')
    data = yaml.safe_load(yaml_data)
    yaml_data.close()
    print(data)
    return data


# noinspection PyInterpreter
def yaml_user():
    yaml_name = "user.yaml"
    # 获取当前脚本所在文件夹路径
    os_path = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yaml_path = os.path.join(os_path, yaml_name)
    return read_yaml_data(yaml_path)


# print(yaml_user()['user_test_01']['user'])
