import tkinter as tk
from tkinter import filedialog, messagebox
import requests

# 發送 LINE Notify 通知的函數
def send_line_notify(data, files=None):
    URL = 'https://notify-api.line.me/api/notify'
    H = {'Authorization': 'Bearer RJ8ZEmHu1TDQb7CGkW2mYZlxT1qyXg6cWVmFElc87zf'}
    response = requests.post(URL, headers=H, data=data, files=files)
    if response.status_code == 200:
        messagebox.showinfo("成功", "通知發送成功！")
    else:
        messagebox.showerror("錯誤", f"發送失敗！\n{response.text}")

# 處理按鈕點擊事件
def on_send_button_click():
    option = option_var.get()
    message = message_entry.get()
    group_id = group_id_entry.get()
    
    if not group_id:
        messagebox.showwarning("警告", "請輸入群組 ID。")
        return

    if option == 'LINE Sticker':
        sticker_package_id = sticker_package_id_entry.get()
        sticker_id = sticker_id_entry.get()
        if not sticker_package_id or not sticker_id:
            messagebox.showwarning("警告", "請填寫所有貼圖資訊。")
            return
        data = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            'to': group_id
        }
        send_line_notify(data)
    
    elif option == 'Local Image File':
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if not file_path:
            return
        data = {'message': message, 'to': group_id}
        with open(file_path, 'rb') as image_file:
            files = {'imageFile': (file_path, image_file, 'image/jpeg')}
            send_line_notify(data, files)
    
    elif option == 'Web Image File':
        image_url = image_url_entry.get()
        if not image_url:
            messagebox.showwarning("警告", "請輸入圖片 URL。")
            return
        data = {'message': message, 'to': group_id}
        response_img = requests.get(image_url)
        files = {'imageFile': ('image.jpg', response_img.content, 'image/jpeg')}
        send_line_notify(data, files)

# 創建主窗口
root = tk.Tk()
root.title("LINE Notify 發送工具")

# 創建選擇框
option_var = tk.StringVar(value='LINE Sticker')
tk.Label(root, text="選擇發送方式:").pack(pady=5)
tk.Radiobutton(root, text="LINE Sticker", variable=option_var, value='LINE Sticker').pack()
tk.Radiobutton(root, text="Local Image File", variable=option_var, value='Local Image File').pack()
tk.Radiobutton(root, text="Web Image File", variable=option_var, value='Web Image File').pack()

# 創建輸入框
tk.Label(root, text="群組 ID:").pack(pady=5)
group_id_entry = tk.Entry(root, width=50)
group_id_entry.pack(pady=5)

tk.Label(root, text="訊息:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="貼圖包 ID:").pack(pady=5)
sticker_package_id_entry = tk.Entry(root, width=50)
sticker_package_id_entry.pack(pady=5)

tk.Label(root, text="貼圖 ID:").pack(pady=5)
sticker_id_entry = tk.Entry(root, width=50)
sticker_id_entry.pack(pady=5)

tk.Label(root, text="圖片 URL:").pack(pady=5)
image_url_entry = tk.Entry(root, width=50)
image_url_entry.pack(pady=5)

# 創建發送按鈕
send_button = tk.Button(root, text="發送", command=on_send_button_click)
send_button.pack(pady=20)

# 運行主循環
root.mainloop()
