## Will learn here
## Reading files
## Writing to files
## Opening and closing files
## File objects
## String methods
## Reading files, one line at a time
## Files modes
## Line endings (Unix vs WIndows)
## Exceptions

## open() Built-in function that opens a file returns a file object.


# hosts = open("C:/ProgramData/Cognizant/AutomationCenter/Scripts/eyethon_script/EyethonV2-Application\AWS_Server/eyethon/invoke.ps1") #C:\Windows\System32\drivers\etc
# hosts_file_contents = hosts.read()
# print(hosts_file_contents)

### called the any file for read ###

# hosts = open("C:\Windows\System32\drivers\etc\hosts") #C:\Windows\System32\drivers\etc
# hosts_file_contents = hosts.read()
# print(hosts_file_contents)

# client_path = r"C:/ProgramData/Cognizant/AutomationCenter/Scripts/eyethon_script/EyethonV2-Application\AWS_Server/eyethon/invoke.ps1"
# print(client_path)

## reade the content of the file ###

# hosts = open("C:\Windows\System32\drivers\etc\hosts") #C:\Windows\System32\drivers\etc
# hosts.seek(20)
# print('current position:{}'.format(hosts.tell()))
# print(hosts.read(3))
# print(hosts.tell())

### closed method for close a file ###

# hosts = open("C:\Windows\System32\drivers\etc\hosts")
# hosts_file_contents = hosts.read()
# print(hosts_file_contents)
# hosts.close()
# print('started reading the file.')
# with open('C:\Windows\System32\drivers\etc\hosts') as hosts:
#     print('File closed? {}'.format(hosts.closed))
#     print(hosts.read())
# print('Finished reading the file.')
# print('File closed?{}'.format(hosts.closed))


#### Mode         ### Description

## r           open for reading (default)
## w           open for writing, truncating first
## x           create a new file and open it for writing
## a           open for writing, apending to file


# with open('file2.txt', 'w') as the_file:
#     the_file.write('This text will be written to the file.')
#     the_file.write('Here is more text.')
# with open('file2.txt') as the_file:
#     print(the_file.read())


## \r   carriage return
## \n   new line

## \n  unix/linux/mac line ending
## \r\n windows style line endings.


# with open('file2.txt', 'w') as the_file:
#     the_file.write('This text will be written to the file.')
#     the_file.write('Here is more text.')
# with open('file2.txt') as the_file:
#     print(the_file.read())


# Open a file and assign its contacts tto a variable.
# If the file is unavailable, create an emty variable.

try:
    contacts = open('contacts.txt').read()
except:
    contacts = 'C:\Windows\System32\drivers\etc\hosts'
print(len(contacts))