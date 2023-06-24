# import os, shutil, pickle

# f = open('file2.txt', 'wb')

# d = pickle.dump("Hello world", f)

# f = open('file2.txt', 'rb')

# print(f.read())

# l = pickle.load(f)

# print(l)

# f.close()

# Package / Module / Library / Python File

# Classes -> methods

# Environment Variables

# print(os.environ)

# Get current working directory

# print(os.getcwd())

# Make Directory

# os.mkdir('OS')

# Make multiple directory inside a directory

# os.makedirs('OS/methods')

# Check whether a directory exists or not

# print(os.path.exists('OS'))

# print(os.path.exists('OS/methods'))

# print(os.path.exists('OS/methods/test.py'))

# if not os.path.exists('OS'):
#     os.mkdir('OS')

# else:
#     print('Directory already exists.')

# if not os.path.exists('OS/methods'):
#     os.makedirs('OS/methods')

# else:
#     print('Directories already exists.')

# Make a file -

# Write & append mode -

# f = open('file1.txt', 'w')
# f = open('file1.txt', 'a')
# f = open('file1.txt', 'a+')

# Read mode -

# f = open('file1.txt', 'r')
# f = open('file1.txt')

# print(f.read()) # str
# print(f.readline()) # str
# print(f.readlines()) # List of str

# f.close()

# print(os.listdir('OS'))

# obj = os.walk('OS')

# for path, directory, file in obj:
#     print(f'Current Path: {path}')
#     print(f'Folders: {directory}')
#     print(f'Files: {file}')

# remove a empty directory

# os.rmdir('OS')

# Remove non empty directory

# shutil.rmtree('OS')

# copy directory

# shutil.copytree('OS/classes', 'Shutil/classes')

# copy file

# shutil.copyfile('file1.txt', 'OS/file1.txt')

# shutil.move('file1.txt', 'Shutil')

# shutil.move('file1.txt', 'Shutil/file1.txt')
