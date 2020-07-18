# snapchat-snap-sender
Snapchat bot that keeps your streaks alive for you.

This project requires ADB (Android Debugging Bridge) to be installed on your computer.
Check out this article https://www.xda-developers.com/install-adb-windows-macos-linux/
on xda-developers.com, it shows how to download ADB on Windows, MacOS and Linux.

Unfortunately, because this project was originally written just for personal use, the script may not work on a screen
with a resolution bigger/smaller than 1080x2340 pixels. You will also have to add a 🟩
in front of all of your friends' names on Snapchat. Like this:

![Imgur](https://i.imgur.com/l2vGSzs.jpg)

After carefully going through all the steps given in the article and installing ADB,
open CMD in the directory you installed ADB in.
Type the following command and press enter: adb devices

Now open Snapchat. 
Take a picture and press send the button.
In the search bar on top of the screen enter the 🟩 emoji and close the keyboard.
Now you can run the script on your computer.
When the script finishes selecting your friends, it will ask for your
permission to send the snap.

Please note that receiving notifications while running the script can mess the script up.
