import os
import tkinter as tk
from tkinter import messagebox
import requests
import subprocess

API_URL = os.getenv("API_URL", "http://172.16.1.220:8000/api/register-mac")


def normalize_mac(mac):
    """Chuẩn hóa MAC về định dạng A:B:C:D:E:F."""
    if not mac:
        return ""
    mac = str(mac).strip().replace('-', ':').replace('.', '').replace(' ', '')
    if len(mac) == 12:
        mac = ':'.join(mac[i:i+2] for i in range(0, 12, 2))
    return mac.upper()


def disable_random_mac_windows():
    """Cố gắng tắt tính năng Random MAC trên Windows (Cần quyền Admin)."""
    try:
        cmd_get_profile = 'netsh wlan show interfaces | findstr "Profile"'
        output = subprocess.check_output(cmd_get_profile, shell=True, text=True)
        profile_name = None
        for line in output.splitlines():
            if ':' in line and 'Profile' in line:
                profile_name = line.split(':', 1)[1].strip()
                break

        if profile_name:
            cmd_disable = f'netsh wlan set profileparameter name="{profile_name}" connectionMode=auto macRandomization=disable'
            subprocess.run(cmd_disable, shell=True, capture_output=True)
            print(f"Đã gửi lệnh tắt Random MAC cho profile: {profile_name}")
            return True
        return False
    except Exception as e:
        print(f"Không thể can thiệp Random MAC: {e}")
        return False


def scan_wifi_macs():
    try:
        output = subprocess.check_output('netsh wlan show interfaces', shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return []
    except Exception:
        return []

    interfaces = []
    current_name = None
    current_mac = None
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("Name"):
            parts = line.split(" : ", 1)
            current_name = parts[1].strip() if len(parts) == 2 else None
        elif line.startswith("Physical address") or line.startswith("Physical Address"):
            parts = line.split(" : ", 1)
            if len(parts) == 2:
                current_mac = normalize_mac(parts[1].strip())
        elif line == "" and current_mac:
            interfaces.append({
                "name": current_name or "WiFi Interface",
                "mac": current_mac,
            })
            current_name = None
            current_mac = None

    if current_mac:
        interfaces.append({"name": current_name or "WiFi Interface", "mac": current_mac})

    return interfaces


def get_selected_mac():
    selected = listbox.curselection()
    if not selected:
        return None
    text = listbox.get(selected[0])
    parts = text.split(" | ")
    return parts[-1] if len(parts) >= 2 else None


def refresh_network_list():
    networks = scan_wifi_macs()
    listbox.delete(0, tk.END)
    if not networks:
        listbox.insert(tk.END, "Không tìm thấy mạng WiFi. Hãy kiểm tra WiFi và thử lại.")
        return
    for net in networks:
        label = f"{net['name']} | {net['mac']}"
        listbox.insert(tk.END, label)


def submit_data():
    user_id = entry_userid.get().strip()
    mac_address = get_selected_mac()

    if not user_id:
        messagebox.showwarning("Lỗi", "Vui lòng nhập Mã học sinh!")
        return
    if not mac_address:
        messagebox.showwarning("Lỗi", "Vui lòng chọn một địa chỉ MAC card WiFi để đăng ký!")
        return

    payload = {
        "user_id": user_id,
        "mac_address": mac_address,
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=15)
        if response.status_code == 200:
            message = response.json().get("message", "Đăng ký thành công!")
            messagebox.showinfo("Thành công", message)
        else:
            error_msg = response.json().get('detail', 'Có lỗi xảy ra')
            messagebox.showerror("Thất bại", error_msg)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Lỗi Kết Nối", f"Không thể kết nối đến Server:\n{e}")


root = tk.Tk()
root.title("Đăng ký Thiết bị Mạng - School Network")
root.geometry("560x520")
root.eval('tk::PlaceWindow . center')

frame = tk.Frame(root, padx=16, pady=12)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="HỆ THỐNG ĐĂNG KÝ TRUY CẬP MẠNG", font=("Arial", 14, "bold")).pack(pady=(0, 12))

form_frame = tk.Frame(frame)
form_frame.pack(fill=tk.X, pady=(0, 12))

tk.Label(form_frame, text="Mã học sinh:").grid(row=0, column=0, sticky="w")
entry_userid = tk.Entry(form_frame, width=35, font=("Arial", 11))
entry_userid.grid(row=0, column=1, pady=4, sticky="w")

list_frame = tk.LabelFrame(frame, text="Danh sách MAC card WiFi trên máy", padx=8, pady=8)
list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 12))

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=70, height=10, yscrollcommand=scrollbar.set, font=("Arial", 10))
listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

button_frame = tk.Frame(frame)
button_frame.pack(fill=tk.X, pady=(0, 8))

btn_refresh = tk.Button(button_frame, text="Làm mới danh sách MAC WiFi", command=refresh_network_list, bg="#1976d2", fg="white", font=("Arial", 10, "bold"))
btn_refresh.pack(side=tk.LEFT, padx=(0, 4))

btn_submit = tk.Button(button_frame, text="Đăng ký MAC đã chọn", command=submit_data, bg="#388e3c", fg="white", font=("Arial", 10, "bold"))
btn_submit.pack(side=tk.LEFT, padx=(4, 0))

lbl_hint = tk.Label(frame, text="Chọn một MAC card WiFi từ danh sách bên trên rồi nhấn Đăng ký.", fg="#333333", wraplength=520, justify="left")
lbl_hint.pack(pady=(4, 0))

refresh_network_list()
root.mainloop()