 #Обязательно установите все модули!!!

import minecraft_launcher_lib #pip install minecraft_launcher_lib
import subprocess #pip install subprocess

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('Minecraft', 'Данное творение лаунчеров под GNU/Linux создан челом под псевдонимом Temmie!')

print('████████╗███████╗███╗   ███╗██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗███████╗██╗  ██╗██████╗ ') 
print('╚══██╔══╝██╔════╝████╗ ████║██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██╔════╝██║  ██║██╔══██╗')
print('   ██║   █████╗  ██╔████╔██║██║     ███████║██║   ██║██╔██╗ ██║██║     █████╗  ███████║██████╔╝')
print('   ██║   ██╔══╝  ██║╚██╔╝██║██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██║██╔══██╗') #/dev/sdb2/home/administrator/MClauncher.py (Ubuntu)
print('   ██║   ███████╗██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗███████╗██║  ██║██║  ██║') #/dev/sda2/home/fuckel/TemmieLauncher.py 
print('   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝')
print('    __  ____                            ______     __                           __                 ____           __    _                 ')
print('   /  |/  (_)___  ___  ______________ _/ __/ /_   / /   ____ ___  ______  _____/ /_  ___  _____   / __ \____     / /   (_)___  __  ___  __')
print('  / /|_/ / / __ \/ _ \/ ___/ ___/ __ `/ /_/ __/  / /   / __ `/ / / / __ \/ ___/ __ \/ _ \/ ___/  / / / / __ \   / /   / / __ \/ / / / |/_/')
print(' / /  / / / / / /  __/ /__/ /  / /_/ / __/ /_   / /___/ /_/ / /_/ / / / / /__/ / / /  __/ /     / /_/ / / / /  / /___/ / / / / /_/ />  <  ')
print('/_/  /_/_/_/ /_/\___/\___/_/   \__,_/_/  \__/  /_____/\__,_/\__,_/_/ /_/\___/_/ /_/\___/_/      \____/_/ /_/  /_____/_/_/ /_/\__,_/_/|_|  ')
print('The creator of this programming miracle: Temmie ')

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    if iteration == total:
        print()

def maximum(max_value, value):
    max_value[0] = value

version = input('Какая тебе нужна версия?: ')
username = input('Какой твой никнейм?: ')
modloader = input('(BETA) Какой тебе нужен ModLoader?: ')


print('=======================================================================================')

max_value = [0]

callback = {
        "setStatus": lambda text: print(text, end='r'),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
}

minecraft_launcher_lib.install.install_minecraft_version(version=version, minecraft_directory=minecraft_directory, callback=callback, modloader=modloader)

options = {
    'username': username,
}

subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))
#ура, я клутоииии! если не будет запускаться, Wine в помощь =) (НЕ ВИНО, А ПРОГА ДЛЯ ЗАПУСКА ШЫНДА-ПРОГ НА LINUX)
#           .-/+oossssoo+/-.               root@administrator 
#       `:+ssssssssssssssssss+:`           --------------------------- 
#     -+ssssssssssssssssssyyssss+-         OS: Ubuntu 24.04.2 LTS x86_64 
#   .ossssssssssssssssssdMMMNysssso.       Host: MS-7721 9.0 
#  /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 6.11.0-25-generic 
# +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 1 hour, 17 mins 
#/sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 2137 (dpkg), 19 (snap) 
#.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.2.21 
#+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Resolution: 1360x768 
#ossyNMMMNyMMhsssssssssssssshmmmhssssssso   DE: GNOME 46.0 
#ssyNMMMNyMMhsssssssssssssshmmmhssssssso   WM: Mutter 
#+sssshhhyNMMNyssssssssssssyNMMMysssssss+   WM Theme: Adwaita 
#.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Theme: Yaru-dark [GTK2/3] 
#/sssssssshNMMMyhhyyyyhdNMMMNhssssssss/    Icons: Yaru [GTK2/3] 
# +sssssssssdmydMMMMMMMMddddyssssssss+     Terminal: gnome-terminal 
#  /ssssssssssshdmNNNNmyNMMMMhssssss/      CPU: AMD Athlon X4 860K Quad (4) @ 3 
#   .ossssssssssssssssssdMMMNysssso.       GPU: NVIDIA GeForce GTX 1050 
#     -+sssssssssssssssssyyyssss+-         Memory: 5360MiB / 15951MiB 
#       `:+ssssssssssssssssss+:`
#           .-/+oossssoo+/-.                                       
# УСТАРЕЛО! Я ща сижу на EndeavourOS, а это так - пасхалко о моей системе на которой я делал впервые этот лаунчер, так еще и выиграл с ним конкурс. 
                                                                   










                                                                   

