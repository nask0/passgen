# passgen
Passgen is an alternative for the random character generator crunch which attempts to solve cracking WPA/WPA2 keys by randomizing the output opposed to generating a list like so, (aaaaaaaa, aaaaaaab, aaaaaac, etc).


example usuage with aircrack-ng (python passgen.py -l | sudo aircrack-ng --bssid 00:11:22:33:44:55 -w- WiFi.cap)

argument switches are as followed
-l lowercase ascii
-l1 lowercase ascii + digits(0-9)
-U uppercase ascii
-U1 uppercase ascii + digits
-lU lowercase + uppercase ascii
-lU1 lowercase + uppercase ascii + digits
