
# Website Blocker
# Copyright (C) 2020-2021 M.Anish <aneesh25861@gmail.com> 

# This program is free software: you can redistribute it and/or modify
# it under GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU  General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
 
This Program helps user to unblock and block websites on windows using hosts file.

'''

import platform
import os
import sys

### BEGIN Windows Functions ###

url=''
 
# Function to check if program is running on windows os or not.
def windows():

  # Function to pause program.
  def pause():
     x = input('\nPress any key to continue...')
     os.system('cls')
      
  # Function to get website URL as input from user.
  def get_url():
      x = input('\nEnter website to block:')
      return x
 

  # Function to block url given as input.
  def engine(url):
 
      # Code to obtain domain from website.
      if url.startswith('https://'):
                 url = url[8:]
      elif url.startswith('http://'):
                 url = url[7:]
               
          
      # Creating batch file to block website by pointing it to local host using hosts file.
      with open('script.bat','a') as f:
            f.write('echo 127.0.0.1 '+url+' >>C:\\Windows\\System32\\drivers\\etc\\hosts \n')


  # Function to import blocklisted urls from text file.
  def import_text_file():
    if os.path.exists('script.bat'):
      os.remove("script.bat")
    file = input('\nEnter File:')
    if os.path.exists(file):
      with open(file) as f:
        for line in f:
          engine(line.strip())
      print('Please run script.bat generated as administrator ...')
    else:
      print('File Not Found!\n')
    pause()
    menu()
    sys.exit()
 

  # Block internet.
  def internetblock():
      os.system('ipconfig /release')
      os.system('cls')
      print('\nInternet is now blocked...')
      pause()
      menu()
      sys.exit()

 
  # Unblock Internet
  def internetunblock():
      os.system('ipconfig /renew')
      os.system('cls')
      print('\nInternet is now unblocked...')
      pause()
      menu()
      sys.exit()
 
 
  # Function to delete all Blocking Rules for websites.
  def unblockall():

      # Creating windows batch file to truncate hosts file.
      with open('script.bat','w') as f:
             f.write('echo #>C:\\Windows\\System32\\drivers\\etc\\hosts')
      print('Please run script.bat generated as administrator to delete all blocked websites.')
      pause()
      menu()
      sys.exit()

 
  # Function to block given website.
  def block():
      url = get_url()
 
      # Code to obtain domain from website.
      if url.startswith('https://'):
                 url = url[8:]
      elif url.startswith('http://'):
                 url = url[7:]
                 
      # Creating batch file to block website by pointing it to local host using hosts file.
      with open('script.bat','w') as f:
            f.write('echo 127.0.0.1 '+url+' >>C:\\Windows\\System32\\drivers\\etc\\hosts\n')
      print('please run script.bat generated as administrator to block website.')
      pause()
      menu()
      sys.exit()


  # Function to unblock blocked website.
  def unblock():
      flag = 0
      blocklist = []
      url = input('\nEnter website to unblock:')
      if url.startswith('https://'):
                 url = url[8:]
      elif url.startswith('http://'):
                 url = url[7:]
       
      with open('C:\\Windows\\System32\\drivers\\etc\\hosts','r') as f:
         for line in f:
             if len(line.strip())>9:
                   blocklist.append(line.split()[1])
                 
      with open('script.bat','w') as f:
             f.write('echo #>C:\\Windows\\System32\\drivers\\etc\\hosts\n')
      for i in blocklist:
         if url !=i :
            flag += 1
            with open('script.bat','a') as f:
               f.write('echo 127.0.0.1 '+i+' >>C:\\Windows\\System32\\drivers\\etc\\hosts\n')
      if flag == len(blocklist):
           print('Entered website is not blocked!')
           if os.path.exists('script.bat'):
              os.remove('script.bat')
              pause()
              menu()
              sys.exit()
             
      print('\nPlease run script.bat script as administrator to continue...')
      pause()
      menu()
      sys.exit()
       
              
  # Function to display currently blocked domains.
  def display():
      mark=0
      print('\n===Currently Blocked Websites===\n')
      with open('C:\\Windows\\System32\\drivers\\etc\\hosts','r') as f:
          for line in f:
              if line.startswith('#') is False and len(line.strip()) > 9:
                  print(line.split()[1])
                  mark=1

      if mark==0:
         print(" No Websites Blocked!")
      pause()
      menu()
      sys.exit()


  # Function to import hostfile.
  def import_hostfile():
    print('\nWarning: Please Ensure that you trust the hostfile you import they may contain malware\n\n')
    file=input('Enter hostfile Location to be imported:')
    if os.path.exists(file):
      with open('script.bat','w') as f:
        f.write('move \"'+os.getcwd()+'\\'+file+'\" C:\\Windows\\System32\\drivers\\etc\\hosts')
      print('\nPlease run script.bat script as administrator to continue...')
    else:
      print('File Not Found!\n')
    pause()
    menu()
    sys.exit()


  # Function to export hostile to current working directory.    
  def export_hostfile():
    with open('script.bat','w') as f:
       f.write('copy C:\\Windows\\System32\\drivers\\etc\\hosts \"'+os.getcwd()+'\"')
    print('\nPlease run script.bat script as administrator to continue...')
    pause()
    menu()
    sys.exit()

       
  # Function to display menu.
  def menu():
      os.system('cls')
      print('\n\t===Simple Website Blocker===')
      print('\n\n1)Block A website')
      print('2)Unblock blocked website')
      print('3)Display blocked websites')
      print('4)Delete all Rules to block Websites')
      print('5)Block Internet Connection')
      print('6)Unblock Internet Connection')
      print('7)Import Website Blocklist from text File')
      print('8)Import Hostfile')
      print('9)Export Hostfile')
    
      x = input('\nEnter choice:')
      if x == '1':
         block()
      elif x == '2':
         unblock()
      elif x == '3':
         display()
      elif x == '4':
         unblockall()
      elif x == '5':
         internetblock()
      elif x == '6':
         internetunblock()
      elif x == '7':
         import_text_file()
      elif x == '8':
         import_hostfile()
      elif x == '9':
         export_hostfile()
      elif x.lower() == 'c' or x.lower() == 'close':
         sys.exit()
      else:
          print('Wrong choice!')
          x = input('press any key to continue...')
          menu()
  menu() 
### END OF WINDOWS FUNCTIONS ###
       
### BEGIN OF POSIX FUNCTIONS ###

def posix():
  sudo_status = os.system("sudo --help >/dev/null")

  def sudo(x):
     if sudo_status==0:
        return 'sudo '+x
     elif os.getuid() != 0:
        print('Please Run this Program with Administrative Rights ( Superuser/ Root) ...')
        sys.exit(1)
     return x

  # Take backup of current hosts file.
  if os.path.exists("/etc/hostsbackup") is False:
     os.system(sudo("cp /etc/hosts /etc/hostsbackup"))

  # Function to pause program.
  def pause():
     x = input('\nPress any key to continue...')
     os.system('clear')
      
  # Function to get website URL as input from user.
  def get_url():
      x = input('\nEnter website to block:')
      return x
 
  # Function to block url given as input.
  def engine(url):
 
      # Code to obtain domain from website.
      if url.startswith('https://'):
                 url = url[8:]
      elif url.startswith('http://'):
                 url = url[7:]
               
          
      # Creating script to block website by pointing it to local host using hosts file.
      with open('script.sh','a') as f:
            f.write('echo 127.0.0.1 '+url+' >>/etc/hosts \n')

  # Function to import blocklisted urls from text file.
  def import_text_file():
    file = input('\nEnter File:')
    if os.path.exists(file):
      with open(file) as f:
        for line in f:
          engine(line.strip())
      print('Done!')
    else:
      print('File Not Found!\n')
    pause()
    menu()
    sys.exit()
   
  # Function to run script.
  def run():
      os.system('chmod +x script.sh')
      os.system(sudo('./script.sh'))
      os.remove("script.sh")
       
  # Function to delete all Blocking Rules for websites.
  def unblockall():

      # Creating windows batch file to truncate hosts file.
      with open('script.sh','w') as f:
             f.write('echo 127.0.0.1  localhost>/etc/hosts\n')
             f.write('cat /etc/hostsbackup>>/etc/hosts')
      run()
      pause()
      menu()
      sys.exit()

  # Function to block given website.
  def block():
      url = get_url()
      engine(url)
      run()
      pause()
      menu()
      sys.exit()


  # Function to unblock blocked website.
  def unblock():
      flag = 0
      blocklist = []
      url = input('\nEnter website to unblock:')
      if url.startswith('https://'):
                 url = url[8:]
      elif url.startswith('http://'):
                 url = url[7:]
       
      with open('/etc/hosts','r') as f:
         for line in f:
             if len(line.strip())>9:
                   if '.' in line.split()[1] and ''.join(line.split()[1].split('.')).isalpha()==True:
                      blocklist.append(line.split()[1])
                 
      with open('script.sh','w') as f:
             f.write('echo 127.0.0.1 localhost>/etc/hosts\n')
   
      for i in blocklist:
         if url !=i :
            flag += 1
            with open('script.sh','a') as f:
               f.write('echo 127.0.0.1 '+i+' >>/etc/hosts\n')
      if flag == len(blocklist):
           print('Entered website is not blocked!')
           if os.path.exists('script.sh'):
              os.remove('script.sh')
              pause()
              menu()
              sys.exit()
             
      run()
      pause()
      menu()
      sys.exit()
       
              
  # Function to display currently blocked domains.
  def display():
      mark=0
      print('\n===Currently Blocked Websites===\n')
      with open('/etc/hosts','r') as f:
          for line in f:
              if line.startswith('#') is False and len(line.strip()) > 9:
                 if ('.' in line.split()[1]) and ''.join(line.split()[1].split('.')).isalpha()==True:
                    print(line.split()[1])
                    mark=1

      if mark==0:
         print(" No Websites Blocked!")
      pause()
      menu()
      sys.exit()


  # Function to import hostfile.
  def import_hostfile():
    print('\nWarning: Please Ensure that you trust the hostfile you import they may contain malware\n\n')
    file=input('Enter hostfile Location to be imported:')
    if os.path.exists(file):
      with open('script.sh','w') as f:
        f.write('mv \"'+os.getcwd()+'/'+file+'\" /etc/hosts')
      run()
    else:
      print('File Not Found!\n')
    pause()
    menu()
    sys.exit()


  # Function to export hostile to current working directory.    
  def export_hostfile():
    with open('script.sh','w') as f:
       f.write('cp /etc/hosts \"'+os.getcwd()+'\"')
    run()
    pause()
    menu()
    sys.exit()

       
  # Function to display menu.
  def menu():
      os.system('clear')
      print('\n\t===Simple Website Blocker===')
      print('\n\n1)Block A website')
      print('2)Unblock blocked website')
      print('3)Display blocked websites')
      print('4)Delete all Rules to block Websites')
      print('5)Import Website Blocklist from text File')
      print('6)Import Hostfile')
      print('7)Export Hostfile')
    
      x = input('\nEnter choice:')
      if x == '1':
         block()
      elif x == '2':
         unblock()
      elif x == '3':
         display()
      elif x == '4':
         unblockall()
      elif x == '5':
         import_text_file()
      elif x == '6':
         import_hostfile()
      elif x == '7':
         export_hostfile()
      elif x.lower() == 'c' or x.lower() == 'close':
         sys.exit()
      else:
          print('Wrong choice!')
          x = input('press any key to continue...')
          menu()
  menu()

### END OF POSIX FUNCTIONS ###

if platform.system().lower() == 'windows':
   windows()
else:
   posix()