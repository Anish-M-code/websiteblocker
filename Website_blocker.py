
# Simple Website Blocker
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

#ABOUT
'''This Program helps user to unblock and block websites on windows using hosts file '''

import platform
import os

url=''

 
#Function to check if program is running on windows os or not.
def check_w():
    if platform.system().lower()!='windows':
       return 1
    return 0
 
#Function to pause program.
def pause():
   x=input('\nPress any key to continue...')
   if check_w()==0:
      os.system('cls')
   else:
      os.system('clear')
      
#Function to get website URL as input from user.
def get_url():
    x=input('\nEnter website to block:')
    return x
    
#Function to delete all Blocking Rules for websites.
def unblockall():
    if check_w()==0:
    
       #Creating windows batch file to truncate hosts file.
       with open('script.bat','w') as f:
           f.write('echo #>C:\Windows\System32\drivers\etc\hosts')
       print('Please run script.bat generated as administrator to delete all blocked websites.')
    else:
       print('\nPlatform not yet supported!')
    pause()
    menu()
    exit()
 
#Function to block given website.
def block():
    url=get_url()
 
    #Code to obtain domain from website.
    if url.startswith('https://'):
               url=url.strip('https://')
    elif url.startswith('http://'):
               url=url.strip('http://')
               
    if check_w()==0:
      
       #Creating batch file to block website by pointing it to local host using hosts file.
       with open('script.bat','w') as f:
          f.write('echo 127.0.0.1 '+url+' >>C:\Windows\System32\drivers\etc\hosts\n')
       print('please run script.bat generated as administrator to block website.')
    else:
       print('\nPlatform not yet supported!')
    pause()
    menu()
    exit()

#Function to unblock blocked website.
def unblock():
    flag=0
    blocklist=[]
    url=input('\nEnter website to unblock:')
    if url.startswith('https://'):
               url=url.strip('https://')
    elif url.startswith('http://'):
               url=url.strip('http://')
    
    if check_w()==0:
     with open('C:\Windows\System32\drivers\etc\hosts','r') as f:
       for line in f:
           if len(line.strip())>9:
              if len(line.strip())>9:
                 blocklist.append(line.split()[1])
                 
     with open('script.bat','w') as f:
           f.write('echo #>C:\Windows\System32\drivers\etc\hosts\n')
     for i in blocklist:
       if url!=i:
          flag+=1
          with open('script.bat','a') as f:
             f.write('echo 127.0.0.1 '+i+' >>C:\Windows\System32\drivers\etc\hosts\n')
     if flag==len(blocklist):
         print('Entered website is not blocked!')
         if os.path.exists('script.bat'):
            os.remove('script.bat')
            pause()
            menu()
            exit()
             
     print('Please run script.bat script as administrator to continue...')
    else:
      x=input('Platform not currently supported!\nPress any key to continue...')
      exit()
    pause()
    menu()
    exit()
       
              
#Function to display currently blocked domains.
def display():
    print('\n===Currently Blocked Websites===\n')
    
    if check_w()==0:
       
     with open('C:\Windows\System32\drivers\etc\hosts','r') as f:
        for line in f:
            if len(line.strip())>9:
                print(line.split()[1])
    else:
      x=input('Platform not supported!\nPress any key to continue...')
      exit()
    pause()
    menu()
    exit()
                  
#Function to display menu.
def menu():
    print('\n\t===Simple Website Blocker===')
    print('\n\n1)Block A website')
    print('2)Unblock blocked website')
    print('3)Display blocked websites')
    print('4)Delete all Rules to block Websites')
    while(1):
       try:
        x=int(input('\nEnter choice:'))
        break
       except ValueError:
        print('Please Enter either 1,2,3 or 4 as choice!')
    if x==1:
       block()
    elif x==2:
       unblock()
    elif x==3:
       display()
    elif x==4:
       unblockall()
    else:
        x=input('press any key to continue...')
        exit()
 
menu()
       
