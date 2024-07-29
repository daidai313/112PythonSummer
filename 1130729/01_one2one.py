import requests
URL = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': 'Bearer lY7VQ8OGXvyXiTqGyIC65Qz8mD3tWjc4gSxOPL7fg7T'}
payload = {'message': 'hello'}
response = requests.post(URL, headers=headers, params=payload)
print(response.status_code)
print(response.text)

import tkinter as tk
from tkinter import messagebox
import requests

def send_message():
    message = message_entry.get()
    if not message:
        messagebox.showwarning("警告", "訊息不能為空")
        return
    
    URL = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer lY7VQ8OGXvyXiTqGyIC65Qz8mD3tWjc4gSxOPL7fg7T'
    }
    payload = {
        'message': message
    }
    
    try:
        print("Sending request to LINE Notify API...")  # 日誌輸出
        response = requests.post(URL, headers=headers, params=payload)
        print(f"Response Status Code: {response.status_code}")  # 日誌輸出
        print(f"Response Text: {response.text}")  # 日誌輸出

        if response.status_code == 200:
            messagebox.showinfo("成功", "訊息已傳送")
        else:
            messagebox.showerror("錯誤", f"傳送失敗，狀態碼: {response.status_code}\n{response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("錯誤", f"發送請求時出現錯誤: {e}")

# 建立主視窗
root = tk.Tk()
root.title("LINE Notify 訊息發送器")

# 訊息輸入框
tk.Label(root, text="輸入訊息:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

# 送出按鈕
send_button = tk.Button(root, text="送出", command=send_message)
send_button.pack(pady=20)

# 運行主循環
root.mainloop()



