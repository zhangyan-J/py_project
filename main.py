from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
import sys

import requests
import json

def get_feishu_sheet_data(spreadsheet_token, range_name, app_id, app_secret):
    # 获取 tenant_access_token
    token_url = "https://li.feishu.cn/sheets/Xp7MslzpYhN7fzt88FucjPFcn7L"
    token_data = {
        "app_id": app_id,
        "app_secret": app_secret
    }
    token_response = requests.post(token_url, json=token_data)
    tenant_access_token = token_response.json().get("tenant_access_token")

    # 获取表格数据
    sheet_url = f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{spreadsheet_token}/values/{range_name}"
    headers = {
        "Authorization": f"Bearer {tenant_access_token}",
        "Content-Type": "application/json"
    }
    sheet_response = requests.get(sheet_url, headers=headers)
    return sheet_response.json()
import subprocess

def run_adb_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

class FeishuADBTool(QWidget):
    def __init__(self):
        super().__init__()
        self.adb_result_display = None
        self.run_adb_button = None
        self.fetch_button = None
        self.sheet_token_input = None
        self.sheet_content_display = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("飞书表格 ADB 工具")
        layout = QVBoxLayout()

        # 输入框：飞书表格 Token
        self.sheet_token_input = QLineEdit(self)
        self.sheet_token_input.setPlaceholderText("输入飞书表格 Token")
        layout.addWidget(self.sheet_token_input)

        # 按钮：获取表格内容
        self.fetch_button = QPushButton("获取表格内容", self)
        self.fetch_button.clicked.connect(self.fetch_sheet_data)
        layout.addWidget(self.fetch_button)

        # 文本框：显示表格内容
        self.sheet_content_display = QTextEdit(self)
        self.sheet_content_display.setReadOnly(True)
        layout.addWidget(self.sheet_content_display)

        # 按钮：执行 ADB 命令
        self.run_adb_button = QPushButton("执行 ADB 命令", self)
        self.run_adb_button.clicked.connect(self.run_adb_commands)
        layout.addWidget(self.run_adb_button)

        # 文本框：显示 ADB 命令执行结果
        self.adb_result_display = QTextEdit(self)
        self.adb_result_display.setReadOnly(True)
        layout.addWidget(self.adb_result_display)

        self.setLayout(layout)

    def fetch_sheet_data(self):
        spreadsheet_token = self.sheet_token_input.text()
        app_id = "your_app_id"
        app_secret = "your_app_secret"
        range_name = "Sheet1!A1:B10"  # 示例范围
        data = get_feishu_sheet_data(spreadsheet_token, range_name, app_id, app_secret)
        self.sheet_content_display.setText(json.dumps(data, indent=2))

    def run_adb_commands(self):
        commands = [
            ["adb devices"],
            ["adb shell ls"]
        ]
        results = []
        for cmd in commands:
            result = run_adb_command(cmd)
            results.append(result)
        self.adb_result_display.setText("\n".join(results))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FeishuADBTool()
    window.show()
    sys.exit(app.exec_())