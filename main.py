import subprocess
string = 'sdfsdfdsfg'
with open('chat.txt', 'a', encoding='utf-8') as file:
    file.write(string + '\n')

subprocess.call(['git', 'add', '.'])