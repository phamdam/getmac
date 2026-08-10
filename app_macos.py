import os
import tkinter as tk
from tkinter import messagebox
import requests
import subprocess

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api/register-mac")


def normalize_mac(mac):
    if not mac:
        return ""
    mac = str(mac).strip().replace('-', ':').replace('.', '').replace(' ', '')
    if len(mac) == 12:
        mac = ':'.join(mac[i:i+2] for i in range(0, 12, 2))
    return mac.upper()


def is_private_mac(mac):
    mac = normalize_mac(mac)
    if len(mac) != 17:
        return False
    first_octet = int(mac.split(':')[0], 16)
    return bool(first_octet & 0x02)


def get_macos_wifi_ports():
    try:
        output = subprocess.check_output(
            ["/usr/sbin/networksetup", "-listallhardwareports"],
            text=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        return []
    except FileNotFoundError:
        return []

    ports = []
    current = {}
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("Hardware Port:"):
            if current:
                ports.append(current)
                current = {}
            current["port"] = line.split(":", 1)[1].strip()
        elif line.startswith("Device:"):
            current["device"] = line.split(":", 1)[1].strip()
        elif line.startswith("Ethernet Address:"):
            current["mac"] = normalize_mac(line.split(":", 1)[1].strip())

    if current:
        ports.append(current)
    return ports


def get_wifi_interface_device():
    for port in get_macos_wifi_ports():
        if "wifi" in port.get("port", "").lower() or "airport" in port.get("port", "").lower():
            return port.get("device")
    return None


def scan_wifi_macs():
    ports = get_macos_wifi_ports()
    wifi_ports = [p for p in ports if "wifi" in p.get("port", "").lower() or "airport" in p.get("port", "").lower()]
    if not wifi_ports:
        return ports
    return wifi_ports


def disable_private_mac():
    device = get_wifi_interface_device()
    if not device:
        messagebox.showwarning(
            "Không tìm thấy Wi-Fi",
            "Không thể xác định thiết bị Wi-Fi trên máy này.",
        )
        return

    try:
        subprocess.check_call(["/usr/sbin/networksetup", "-setairportpower", device, "off"])
        subprocess.check_call(["/usr/sbin/networksetup", "-setairportpower", device, "on"])
        messagebox.showinfo(
            "Đã tắt/mở lại Wi-Fi",
            "Wi-Fi đã được tắt và bật lại. Nếu mac vẫn là địa chỉ private, hãy tắt tính năng Private Address trong System Settings > Wi-Fi.",
        )
        refresh_network_list()
    except subprocess.CalledProcessError as e:
        messagebox.showerror(
            "Lỗi",
            f"Không thể tắt/mở lại Wi-Fi: {e}\nHãy chạy app với quyền administrator và thử lại.",
        )


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
        listbox.insert(tk.END, "Không tìm thấy giao diện Wi-Fi. Hãy kiểm tra Wi-Fi và thử lại.")
        return

    for net in networks:
        label = f"{net.get('port', 'Wi-Fi')} | {net.get('mac', 'Không có MAC')}"
        if is_private_mac(net.get('mac', '')):
            label += " (Private MAC)"
        listbox.insert(tk.END, label)



def submit_data():
    user_id = entry_userid.get().strip()
    mac_address = get_selected_mac()

    if not user_id:
        messagebox.showwarning("Lỗi", "Vui lòng nhập Mã học sinh!")
        return
    if not mac_address:
        messagebox.showwarning("Lỗi", "Vui lòng chọn một địa chỉ MAC Wi-Fi để đăng ký!")
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
root.title("Đăng ký Thiết bị Mạng - macOS")
root.geometry("560x520")
root.eval('tk::PlaceWindow . center')

frame = tk.Frame(root, padx=16, pady=12)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="HỆ THỐNG ĐĂNG KÝ TRUY CẬP MẠNG (macOS)", font=("Arial", 14, "bold")).pack(pady=(0, 12))

form_frame = tk.Frame(frame)
form_frame.pack(fill=tk.X, pady=(0, 12))

tk.Label(form_frame, text="Mã học sinh:").grid(row=0, column=0, sticky="w")
entry_userid = tk.Entry(form_frame, width=35, font=("Arial", 11))
entry_userid.grid(row=0, column=1, pady=4, sticky="w")

list_frame = tk.LabelFrame(frame, text="Danh sách giao diện Wi-Fi và MAC", padx=8, pady=8)
list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 12))

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=70, height=10, yscrollcommand=scrollbar.set, font=("Arial", 10))
listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

button_frame = tk.Frame(frame)
button_frame.pack(fill=tk.X, pady=(0, 8))

btn_refresh = tk.Button(
    button_frame,
    text="Làm mới danh sách MAC Wi-Fi",
    command=refresh_network_list,
    bg="#1976d2",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_refresh.pack(side=tk.LEFT, padx=(0, 4))

btn_disable = tk.Button(
    button_frame,
    text="Tắt/Mở lại Wi-Fi (Private MAC)",
    command=disable_private_mac,
    bg="#f57c00",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_disable.pack(side=tk.LEFT, padx=(4, 4))

btn_submit = tk.Button(
    button_frame,
    text="Đăng ký MAC đã chọn",
    command=submit_data,
    bg="#388e3c",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_submit.pack(side=tk.LEFT, padx=(4, 0))

lbl_hint = tk.Label(
    frame,
    text="Chọn một MAC Wi-Fi thật từ danh sách và nhấn Đăng ký. Nếu MAC là Private, dùng nút tắt/mở Wi-Fi để làm mới.",
    fg="#333333",
    wraplength=520,
    justify="left",
)
lbl_hint.pack(pady=(4, 0))

refresh_network_list()
root.mainloop()
