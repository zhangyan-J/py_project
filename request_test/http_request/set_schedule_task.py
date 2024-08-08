import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler

# 替换成你的飞书机器人 Webhook URL
webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-id'

def send_message_to_feishu():
    """
    向飞书机器人发送消息
    """
    message = {
        "msg_type": "text",
        "content": {
            "text": "这是一条定时发送的消息！"
        }
    }
    
    try:
        response = requests.post(
            webhook_url,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(message)
        )
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
    except requests.RequestException as e:
        print(f"请求失败: {e}")

def main():
    # 创建一个调度器
    scheduler = BackgroundScheduler()
    
    # 添加定时任务
    scheduler.add_job(send_message_to_feishu, 'interval', hours=1)  # 每小时执行一次
    
    # 启动调度器
    scheduler.start()
    
    try:
        # 保持程序运行
        print("定时任务已启动。按 Ctrl+C 退出程序。")
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # 关闭调度器
        scheduler.shutdown()
        print("定时任务已停止。")

if __name__ == "__main__":
    main()
