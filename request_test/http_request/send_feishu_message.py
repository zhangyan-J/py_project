import requests
import json


def send_message_to_feishu(webhook_url, message):
    """
    向飞书机器人发送消息。

    :param webhook_url: 飞书机器人的 Webhook URL
    :param message: 要发送的消息内容（字典格式）
    :return: 请求的状态码和响应内容
    """
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(
            webhook_url,
            headers=headers,
            data=json.dumps(message)
        )
        # 返回状态码和响应内容
        return response.status_code, response.text
    except requests.RequestException as e:
        # 如果发生请求异常，输出异常信息
        print(f"请求失败: {e}")
        return None, str(e)


# 示例用法
if __name__ == "__main__":
    # 替换成你的飞书机器人 Webhook URL
    webhook_url = ''

    # 示例消息
    message = {
        "msg_type": "text",
        "content": {
            "text": "Hello, this is a test message, please ignore!"
        }
    }

    # 发送消息
    status_code, response_text = send_message_to_feishu(webhook_url, message)

    # 打印结果
    print(f"状态码: {status_code}")
    print(f"响应内容: {response_text}")
