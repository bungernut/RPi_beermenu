* To make the RPi display rotate
edit /boot/config.txt
Add/Edit one of these lines:
display_rotate=0 #Normal
display_rotate=1 #90
display_rotate=2 #180
display_rotate=3 #270
display_rotate=0x10000 # horizontal flip
display_rotate=0x20000 # vertical flip

