import zipfile
import os
import pickle

def compress_data():
    with zipfile.ZipFile('student.dat', 'wb') as zipf:
        zipf.write("C:\CODE IA\pyhton\pw6\student.pkl","student.pkl")
        zipf.write("C:\CODE IA\pyhton\pw6\course.pkl","course.pkl")
        zipf.write("C:\CODE IA\pyhton\pw6\mark.pkl","mark.pkl")

def decompress_data():
    with zipfile.ZipFile('student.dat', 'r') as zipf:
        zipf.extractall()

def check_data_file():
    return "student.dat" in os.listdir()