import os

def print_header():
    logo = """
\033[43m\033[30m  __________________________________________________________________________  \033[0m
\033[43m\033[30m |                                                                          | \033[0m
\033[43m\033[30m |         ###    ###    ####    ####    ### ###   ####  #########          | \033[0m
\033[43m\033[30m |         ###    ###   ######   #####   ### ###  ####  ###                 | \033[0m
\033[43m\033[30m |         ###    ###  ###  ###  ######  ### ### ####    ####               | \033[0m
\033[43m\033[30m |         ########## ########## ### ### ### #######      #####             | \033[0m
\033[43m\033[30m |         ###    ### ###    ### ###  ###### ### ####        ####           | \033[0m
\033[43m\033[30m |         ###    ### ###    ### ###   ##### ###  ####        ####          | \033[0m
\033[43m\033[30m |         ###    ### ###    ### ###    #### ###   #### #########           | \033[0m
\033[43m\033[30m |__________________________________________________________________________| \033[0m
\033[43m\033[30m                                                                              \033[0m
                          \033[43m\033[30m  macOS Post-Install Script  \033[0m
                          \033[43m\033[30m                             \033[0m
"""
    logoSmall = """\033[43m\033[30m                                                         \033[0m
\033[43m\033[30m ###    ###    ####    ####    ### ###   ####  ######### \033[0m
\033[43m\033[30m ###    ###   ######   #####   ### ###  ####  ###        \033[0m
\033[43m\033[30m ###    ###  ###  ###  ######  ### ### ####    ####      \033[0m
\033[43m\033[30m ########## ########## ### ### ### #######      #####    \033[0m
\033[43m\033[30m ###    ### ###    ### ###  ###### ### ####        ####  \033[0m
\033[43m\033[30m ###    ### ###    ### ###   ##### ###  ####        #### \033[0m
\033[43m\033[30m ###    ### ###    ### ###    #### ###   #### #########  \033[0m
\033[43m\033[30m                                                         \033[0m
"""


    width = int(os.popen('stty size', 'r').read().split()[1])
    logoWidth = len(logo.split('\n')[1]) - len("\033[43m\033[30m\033[0m")

    if width < logoWidth:
        logo = logoSmall
        logoWidth = len(logo.split('\n')[1])- len("\033[43m\033[30m\033[0m")


    string_start = int(int(logoWidth)/2 - (width/2))

    padding_x = int(width/2 - logoWidth/2) * ' '
    for i in logo.split('\n'):
        print("\033[0m" + padding_x + i)

