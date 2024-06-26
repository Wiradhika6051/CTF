#!/usr/bin/python3
FLAG = "FindITCTF{F4k3_fl333g}"

ascii1 = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?**********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?**************?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*******************@@@@@@@@@@@@@@@***?***@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**********@@@?*******@@@@@@@@@@@@*************@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*********@@@@@******@@@@@@@@@******************@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@@*********@********@@@@@@@********?@@@@@@@@****@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@******@@@@@****************@@@@@***********@@@@@@@@@@@***?@
@@@@@@@@@@@@@@@@@@***@@@@@@@@@@********@@@@.************@@@@**************?@@@@@@@@@@@****
@@@@@@@@@@@@@@@@*******@@@****@@********@@@@@*********@@@?******************@@@@@@@@@@@***
@@@@@@@@@@@@@@@***************************@@@@*****@@@@**********************@@@@@@@@@@***
@@@@@@@@@@@@@@@*****************************@@@@@@@@***************************@@@@@@@****
@@@@@@@@@@@@@@@@;*****@@@*******************@@@@@**********************************?******
@@@@@@@@@@@@@@@@@@@@@*;@@@@****************@@@*******************************************@
@@@@@@@@@@@@@@@@@@******@@@@********@@@@@@@@***************@@***************************@@
@@@@@@@@@@@@@@*?@@*******@@@@@*******@@@@****************@@@@@@**********************@@@@@
@@@@@@@@@@@******@@@*******@@@@****@@@********************+@@********************@@@@@@@@@
@@@@@@@@*********+@@@@*******@@@@@@******************************************@@@@@@@@@@@@@
@@@@@@@************@@@@*****+@@@@******************?+********************@@@@@@@@@@@@@@@@@
@@@@@@@************@@@@@**@@@@***************************************@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@********@@@@@@@@@@**************************************%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@********@@@@@@*************************************?@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@******@@@@*************@@@@*******************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@**@@@@***********************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@?*********************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@***********************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@************************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@************************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@******?@@@@@@*********************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@***********@@@@**+**********@@@@****************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
**************?@@**********@@@@@@@***********@@***@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
***************@@@@@@@@@@@@@@@@@@@****************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
***************@@@@@@@@@@@@@@@@@@@****************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
***************@@@@@@@@@@@@@@@@@@@****************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
**************@@@@@@@@@@@@@@@@@@@@****************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@***********@@@@@@*****@@@@@@@@@@****************@@@@@@@@@@@@****@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@*****@@@@@@***********@@@@@@@****************@@@@@@@@?**********@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@**************@@@@@@****************@@@@@@@************@*+@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@****************@@@@@@**************@@@@@@@****************?@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@*******************@@@@@@***********@@@@@@*******************@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@********@@************@@@@@@@+*@@@@@@@@**********************@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@***************************@@@@@@@***************************@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@**********************************************************@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@******************************************@@***********@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@****************************************************@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@?****************@@@*****************************@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@?***************@@***************************@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@****************************************@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@**********+***********************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*************************+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***********+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

ascii2 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠉⠉⠉⠉⠉⠉⠉⠙⠻⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠙⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⣠⣶⠛⠛⠛⠛⠛⠛⠳⣦⡀⠀⠘⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⢹⣿⣦⣀⣀⣀⣀⣀⣠⣼⡇⠀⠀⠸⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠉⠛⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⣿
       ⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀
       ⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀
⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⣠⡶⠶⠿⠿⠿⠿⢷⣦⠀⠀⠀⠀⠀    ⣿⠀
⠀⠀⣀⣀⣀⠀⣸⡇⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⠀
⣠⡿⠛⠛⠛⠛⠻⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀ ⠀⣿⠀
⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⢀⣤⣤⣴⣿⠀⠀⠀⠀⠀⠀  ⠀⣿⠀
⠈⠙⢷⣶⣦⣤⣤⣤⣴⣶⣾⠿⠛⠁⢀⣶⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀
             ⠀⠀⠀⠀⠈⣿⣆⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡾⠃⠀
                  ⠀⠈⠛⠻⢿⣿⣾⣿⡿⠿⠟⠋⠁⠀⠀⠀
"""


block = [
    ";",
    '"',
    "os",
    "_",
    "\\",
    "`",
    " ",
    "-",
    "!",
    "[",
    "]",
    "*",
    "import",
    "eval",
    "banner",
    "echo",
    "cat",
    "%",
    "&",
    ">",
    "<",
    "+",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "b",
    "s",
    "lower",
    "upper",
    "system",
    "}",
    "{",
    ".py",
]

#REDACTED :) to make this challenge more interesting