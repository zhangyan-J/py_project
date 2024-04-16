##创建文件夹
import os


# 创建文件夹
def mkdir_multi(path):
    # 判断路径是否存在
    isExists = os.path.exists(path)

    if not isExists:
        # 如果不存在，则创建目录（多层）
        os.makedirs(path)
        print('目录创建成功！')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('目录已存在！')
        return False


if __name__ == "__main__":
    mkdir_multi(r'D:\node_client\li-test-client')
    mkdir_multi(r'D:\node_client\test_script')
    mkdir_multi(r'D:\node_client\ZL')

    mkdir_multi(r'D:\liat_studio')
    mkdir_multi(r'D:\liat_studio\resource')