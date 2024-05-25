import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def convert():
    value = float(entry.get())
    from_unit = from_combobox.get()
    to_unit = to_combobox.get()

    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = celsius_to_fahrenheit(value)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = fahrenheit_to_celsius(value)
    elif from_unit == "Kilograms" and to_unit == "Pounds":
        result = kilograms_to_pounds(value)
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        result = pounds_to_kilograms(value)
    elif from_unit == "Meters" and to_unit == "Feet":
        result = meters_to_feet(value)
    elif from_unit == "Feet" and to_unit == "Meters":
        result = feet_to_meters(value)
    else:
        result = "Invalid conversion"

    result_label.config(text=result)

# GUI 생성
root = tk.Tk()
root.title("Unit Converter")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# 입력 레이블과 엔트리
entry_label = ttk.Label(frame, text="Value:")
entry_label.grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)

# 변환할 단위 선택
from_label = ttk.Label(frame, text="From:")
from_label.grid(row=1, column=0, padx=5, pady=5)
from_combobox = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kilograms", "Pounds", "Meters", "Feet"])
from_combobox.grid(row=1, column=1, padx=5, pady=5)
from_combobox.set("Celsius")

to_label = ttk.Label(frame, text="To:")
to_label.grid(row=2, column=0, padx=5, pady=5)
to_combobox = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kilograms", "Pounds", "Meters", "Feet"])
to_combobox.grid(row=2, column=1, padx=5, pady=5)
to_combobox.set("Fahrenheit")

# 변환 버튼
convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=3, columnspan=2, padx=5, pady=5)

# 변환 결과 표시 레이블
result_label = ttk.Label(frame, text="")
result_label.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
