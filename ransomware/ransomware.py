import os
import shutil
from cryptography.fernet import Fernet

with open('./key.txt', 'rb') as key_file:
    key = key_file.read()

f = Fernet(key)


path_to_target = input("enter the path to folder you want to encrypt: ")

if path_to_target[-1] != '/':
    path_to_target += '/'

path_to_encrypted = input("enter the path to folder you want to save encrypted files: ")

if path_to_encrypted[-1] != '/':
    path_to_encrypted += '/'


# recursive function to delete file including directories
def delete_directories(now_path):
    objects = os.listdir(now_path)

    for object in objects:
        print(now_path+object)
        if os.path.isdir(now_path+object):
            print("this file is directory")
            delete_directories(now_path+object+'/')
            os.rmdir(now_path+object)
        else:
            os.remove(now_path+object)
            print("deleted: "+now_path+object)


# copy original folder to encrpyted folder
try:
    shutil.copytree(path_to_target, path_to_encrypted)
except:
    # delete directory if it already exists
    delete_directories(path_to_encrypted)
    os.rmdir(path_to_encrypted)
    shutil.copytree(path_to_target, path_to_encrypted)

# file encrypting fucnction
def encrypt(original_path, encrypt_path):
    with open(original_path, 'rb') as file:
        original_file = file.read()

    encrypted_file = f.encrypt(original_file)

    with open(encrypt_path, 'wb') as file:
        file.write(encrypted_file)
    
    os.rename(encrypt_path, encrypt_path+'.lmao')

# searching for the file to encrypt
def encrypt_files(now_path):
    targets = os.listdir(path_to_target+now_path)

    for target in targets:
        if os.path.isdir(path_to_target+now_path+target):
            encrypt_files(now_path+target+'/')
        else:
            encrypt(path_to_target+now_path+target, path_to_encrypted+now_path+target)



target_files = os.listdir(path_to_target)

for target in target_files:
    encrypt_files('')