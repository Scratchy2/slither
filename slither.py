def setup():
    app = QApplication([])
    window = QWidget()
    group1 = QGroupBox("Click Interval", window)
    global ulgroup
    ulgroup = None
    return app, window, group1

def hours():
    hrs1 = QLineEdit()
    hrs1.setStyleSheet("border-radius: 10%; background-color: #444; color: #FFF; text-align: bottom;")
    hrs1.setContentsMargins(0, 10, 0, 0)
    hrs1.setAlignment(Qt.AlignCenter)
    hrs2 = QLabel("Hours")
    hrs2.setAlignment(Qt.AlignCenter)
    return hrs1, hrs2

def minutes():
    mins1 = QLineEdit()
    mins1.setStyleSheet("border-radius: 10%; background-color: #444; color: #FFF; text-align: bottom;")
    mins1.setAlignment(Qt.AlignCenter)
    mins1.setContentsMargins(0, 10, 0, 0)
    mins2 = QLabel("Minutes")
    mins2.setAlignment(Qt.AlignCenter)
    return mins1, mins2

def seconds():
    secs1 = QLineEdit()
    secs1.setStyleSheet("border-radius: 10%; background-color: #444; color: #FFF; text-align: bottom;")
    secs1.setAlignment(Qt.AlignCenter)
    secs1.setContentsMargins(0, 10, 0, 0)
    secs2 = QLabel("Seconds")
    secs2.setAlignment(Qt.AlignCenter)
    return secs1, secs2

def milliseconds():
    ms1 = QLineEdit()
    ms1.setStyleSheet("border-radius: 10%; background-color: #444; color: #FFF; text-align: bottom;")
    ms1.setAlignment(Qt.AlignCenter)
    ms1.setContentsMargins(0, 10, 0, 0)
    ms2 = QLabel("Milliseconds")
    ms2.setAlignment(Qt.AlignCenter)
    return ms1, ms2

def vboxes():
    vbox1 = QVBoxLayout()
    vbox1.addWidget(hrs1)
    vbox1.addWidget(hrs2)
    vbox1.addStretch(1)
    vbox2 = QVBoxLayout()
    vbox2.addWidget(mins1)
    vbox2.addWidget(mins2)
    vbox2.addStretch(1)
    vbox3 = QVBoxLayout()
    vbox3.addWidget(secs1)
    vbox3.addWidget(secs2)
    vbox3.addStretch(1)
    vbox4 = QVBoxLayout()
    vbox4.addWidget(ms1)
    vbox4.addWidget(ms2)
    vbox4.addStretch(1)
    vboxs = QHBoxLayout()
    vboxs.addLayout(vbox1)
    vboxs.addLayout(vbox2)
    vboxs.addLayout(vbox3)
    vboxs.addLayout(vbox4)
    vboxs.addStretch(1)
    group1.setLayout(vboxs)
    return vbox1, vbox2, vbox3, vbox4, vboxs

def options():
    group2 = QGroupBox("Options", window)
    group6 = QHBoxLayout()
    group3 = QVBoxLayout()
    group4 = QHBoxLayout()
    group4.addWidget(QLabel("Mouse Button"))
    dropdown1 = QComboBox(window)
    dropdown1.addItems(["Left", "Middle", "Right"])
    dropdown1.setFixedWidth(100)
    group4.addWidget(dropdown1)
    group4.addStretch(1)
    group5 = QHBoxLayout()
    group5.addWidget(QLabel("Click type"))
    dropdown2 = QComboBox(window)
    dropdown2.addItems(["Single", "Double"])
    dropdown2.setFixedWidth(100)
    group5.addWidget(dropdown2)
    group5.addStretch(1)
    group7 = QGroupBox("More Options", window)
    group7.setContentsMargins(0, 10, 0, 0)
    group8 = QVBoxLayout()
    group8.setContentsMargins(15, 30, 15, 0)
    checkbox = QCheckBox("Custom Location", window)
    group8.addWidget(checkbox)
    group9 = QHBoxLayout()
    x = QLineEdit()
    x.setStyleSheet("border-radius: 10%; background-color: #444; color: #FFF; text-align: bottom;")
    x.setAlignment(Qt.AlignCenter)
    x.setPlaceholderText("X")
    y = QLineEdit()
    y.setStyleSheet("border-radius: 10%; background-color: #444; color: #FFF; text-align: bottom;")
    y.setAlignment(Qt.AlignCenter)
    y.setPlaceholderText("Y")
    button = QPushButton("Get")
    group9.addWidget(x)
    group9.addWidget(y)
    group9.addWidget(button)
    group10 = QHBoxLayout()
    checkbox2 = QCheckBox("Random Interval", window)
    group10.addWidget(checkbox2)
    interval = QLineEdit(window)
    interval.setPlaceholderText("+/-")
    interval.setStyleSheet("border-radius: 10%; background-color: #444; color: #FFF; text-align: bottom;")
    interval.setAlignment(Qt.AlignCenter)
    group10.addWidget(interval)
    group8.addLayout(group9)
    group8.addLayout(group10)
    group7.setLayout(group8)
    group3.addLayout(group4)
    group3.addLayout(group5)
    group2.setLayout(group3)
    group6.addWidget(group2, 1)
    group6.addWidget(group7, 1)
    group2.setStyleSheet("border-radius: 4%; background-color: #222; color: #FFF; text-align: bottom; border-color: #000")
    group7.setStyleSheet("border-radius: 4%; background-color: #222; color: #FFF; text-align: bottom; border-color: #000")
    group7.setContentsMargins(0, 10, 0, 0)
    return group6, dropdown1, dropdown2, checkbox, button, x, y, checkbox2, interval

def interval():
    global hrs, mins, secs, ms
    try:
        hrs = int(hrs1.text())
    except:
        hrs = 0
    try:
        mins = int(mins1.text())
    except:
        mins = 0
    try:
        secs = int(secs1.text())
    except:
        secs = 0
    try:
        ms = int(ms1.text())
    except:
        ms = 0

def mbutton():
    global button
    button = dropdown1.currentText().lower()
    if button == "left":
        button = Button.left
    elif button == "middle":
        button = Button.middle
    else:
        button = Button.right

def clicks():
    global click
    click = dropdown2.currentIndex() + 1

def hotkey():
    global ulgroup
    bg = QGroupBox("Hotkeys", window)
    bg.setStyleSheet("border-radius: 4%; background-color: #222; color: #FFF; text-align: bottom;")
    vgroup = QVBoxLayout()
    hgroup = QHBoxLayout()
    startstop = QLabel("Start/stop key:")
    vgroup.setContentsMargins(15, 25, 0, 15)
    sequence = QLineEdit()
    sequence.setPlaceholderText("Key")
    hgroup.addWidget(startstop)
    hgroup.addWidget(sequence)
    vgroup.addLayout(hgroup)
    hgroup2 = QHBoxLayout()
    endlabel = QLabel("End key:", window)
    endsequence = QLineEdit()
    endsequence.setPlaceholderText("Key")
    hgroup2.addWidget(endlabel)
    hgroup2.addWidget(endsequence)
    vgroup.addLayout(hgroup2)
    button3 = QPushButton("Click to remove the text cursor")
    vgroup.addWidget(button3)
    bg.setLayout(vgroup)
    ulgroup.addWidget(bg)
    return sequence, endsequence

def main():
    global running
    running = 0
    while running == 0:
        sleep = 3600 * hrs + 60 * mins + secs + 0.001 * ms
        if keyboard.is_pressed(sequence.text()):
            time.sleep(0.5)
            running = 1
        elif keyboard.is_pressed(endsequence.text()):
            window.close()
            sys.exit()
    if checkbox2.isChecked() and interval2.text() != "":
        random2 = float(interval2.text())
    else:
        random2 = 0
    while running == 1:
        if checkbox.isChecked() and x.text() != "" and y.text() != "":
            pyautogui.moveTo(int(x.text()), int(y.text()))
        Controller().click(button)
        time.sleep(max(sleep - 0.004 + (random.random() * 2 - 1) * random2, 0.016))
        if click == 2:
            Controller().click(button)
        if keyboard.is_pressed(sequence.text()):
            running = 0
            time.sleep(0.5)
            run()
            sys.exit()
        elif keyboard.is_pressed(endsequence.text()):
            running = 0
            window.close()
            sys.exit()

def run():
    if sequence.text() != "" and endsequence.text() != "":
        threading.Thread(target=main).start()

def clickedthread():
    def on_click(*args):
        x.setText(str(pyautogui.position().x))
        y.setText(str(pyautogui.position().y))
        listener.stop()
    listener = Listener(on_click=on_click)
    listener.start()

def clicked():
    threading.Thread(target=clickedthread).start()

import sys, time, threading, pyautogui, keyboard, random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QCheckBox, QPushButton
from pynput.mouse import Button, Controller, Listener
running = 0
app, window, group1 = setup()
group1.setStyleSheet("border-radius: 4%; background-color: #222; color: #FFF; text-align: bottom;")
group1.setContentsMargins(0, 10, 0, 0)
hrs1, hrs2 = hours()
mins1, mins2 = minutes()
secs1, secs2 = seconds()
ms1, ms2 = milliseconds()
vbox1, vbox2, vbox3, vbox4, vboxs = vboxes()
group6, dropdown1, dropdown2, checkbox, button2, x, y, checkbox2, interval2 = options()
global ulgroup
ulgroup = QVBoxLayout(window)
ulgroup.addWidget(group1)
ulgroup.addLayout(group6)
sequence, endsequence = hotkey()
hrs = 0
hrs1.textEdited.connect(interval)
mins = 0
mins1.textEdited.connect(interval)
secs = 0
secs1.textEdited.connect(interval)
ms = 20
ms1.textEdited.connect(interval)
ms1.setText("20")
dropdown1.currentTextChanged.connect(mbutton)
click = 1
dropdown2.currentIndexChanged.connect(clicks)
checkbox.clicked.connect(clicks)
button2.clicked.connect(clicked)
sequence.textEdited.connect(run)
endsequence.textEdited.connect(run)
button = Button.left
window.setWindowTitle("Slither Autoclicker")
window.setStyleSheet("background-color: #000;")
window.show()
sys.exit(app.exec())