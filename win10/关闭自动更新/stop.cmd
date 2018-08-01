net stop wuauserv > stop.txt
sc config wuauserv start=disabled >> stop.txt