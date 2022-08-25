# About this Module
I volunteer in an office where I'm often calling people on my personal cell phone, but others in the office can't see when I am, so sometimes try to talk with me over the partition or walk over to chat only to find I'm on a call.

I needed something to alert them, so I made a simple device that lights up when I'm making or taking a phone call.

1) Wire the Arduino and Bluetooth module.

2) Upload the sketch to listen for Bluetooth notifications.

3) Upload the phone app to MIT AppInventor 2.

4) Pair your phone with the Bluetooth module, usually named HC-05. (Don't skip this part.) Note the Bluetooth device number. You may want to add it to your phone app (top right block).

5) Load it into your phone (using the MIT AI2 Companion or download the app and send it to the phone to install).

6) Launch the phone app & test. The phone code contains a hidden pair of buttons for testing. Tap on the red phone icon and they appear (as seen in the video in the beginning).

This app has code (top right) that automatically selects the Bluetooth module when it turns on. You can change the number so it automatically connects to yours, or you can delete that set of blocks entirely and just do a scan each time. The device number can usually be seen when you pair the phone with the module for the first time, or when you scan for the module within the app.

7) I printed a case for the device using my 3D printer, but any little project box will work, or it can be left open.

When it's all done, power up the Arduino, start the phone app, scan for the HC-05 Bluetooth module (if you didn't put the device number in the code), and then any time you're taking or making a call, the led lights up.


![wiring_bb_MgBK9p5aTU](https://user-images.githubusercontent.com/81805145/186573753-11ae64cd-6d3c-44c5-b184-180c289302bb.png)
