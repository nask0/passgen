# Passgen 0.1
Passgen is an alternative for the random character generator crunch which attempts to solve cracking WPA/WPA2 keys by randomizing the output opposed to generating a list like so, (aaaaaaaa, aaaaaaab, aaaaaac, etc).


example usuage with aircrack-ng (python passgen.py -l | sudo aircrack-ng --bssid 00:11:22:33:44:55 -w- WiFi.cap)

argument switches are as followed
<br>
-l lowercase ascii
<br>
-l1 lowercase ascii + digits(0-9)
<br>
-U uppercase ascii
<br>
-U1 uppercase ascii + digits
<br>
-lU lowercase + uppercase ascii
<br>
-lU1 lowercase + uppercase ascii + digits
