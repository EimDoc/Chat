import subprocess

name = 'Caня'
while True:
    string = input('Сообщение: ')
    with open('chat.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} - {string}\n')
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', "'some'"])
    subprocess.call(['git', 'pull', 'https://github.com/EimDoc/Chat.git'])
    subprocess.call(['git', 'push', 'https://github.com/EimDoc/Chat.git'])