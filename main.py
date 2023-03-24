import time
import keyboard
import os


#cette fontion vérifie que le tuple entré est au bon format
def my_check_tuple(my_tuple):
    if (type(my_tuple) != tuple):
        return(False)
    if (len(my_tuple) != 3):
        return(False)
    for i in my_tuple:
        if (type(i) !=  int):
            return(False)
    if (my_tuple[0] > 23 or my_tuple[1] > 59 or my_tuple[2] > 59 or my_tuple[0] < 0 or my_tuple[1] < 0 or my_tuple[2] < 0 ):
        return(False)
    return(True)


#foncion pour dupliquer une liste afin de ne pas modifier la liste de base
def my_dup_list(o_list):
    nw_l = []
    for i in o_list:
        nw_l.append(i)
    return(nw_l)

#fonction pour faire passer le format d'heure anglaise a heure francaise
def my_modif_format(my_list):
    my_list[0] = my_list[0] % 12
    if(my_list[0] == 0):
            my_list[0] = 12
    return(my_list)

# fonction d'affichage de l'heure au format demandé
def my_print_heure(time_list, t):
    check = 0
    print_list = my_dup_list(time_list)
    if (t == 2):
        if (time_list[0] >= 12):
            check = 1
        else:
            check = 2
        print_list = my_modif_format(print_list)
    time_str = my_list_to_str(print_list, check)
    print(time_str, end='\r')
    

def my_list_to_str(time_list, mode):
    res = ''
    if (time_list[0] < 10):
        res += '0'
    res += str(time_list[0]) + ':'
    if (time_list[1] < 10):
        res += '0'
    res += str(time_list[1]) + ':'
    if (time_list[2] < 10):
        res += '0'
    res += str(time_list[2])
    if (mode == 1):
        res += ' PM'
    if (mode == 2):
        res += 'AM'
    return(res)

#menu demandant a l'utilisateur si il souhaite creer ou non une alarme
def my_menu_alarm():
    try:
        i = int(input("Voulez vous créer une alarme ? '1' pour oui '2' pour non : "))
    except ValueError:
        print('Saisie incorrecte')
        return(my_menu_alarm())
    if (i == 1):
        return(my_set_alarm(my_get_tuple(2)))
    elif (i == 2):
        return(None)
    else:
        print('Saisie incorrecte')
        return(my_menu_alarm())

def my_get_tuple(i):
    if i == 2:
        print("Renseignez l'heure a laquelle l'alarme doit s'activer : ", end='')
    elif i == 1:
        print("Renseignez l'heure de démarage de l'horloge : ", end='')
    try:
        my_tuple = (int(input()), int(input("Précissez les minutes : ")), int(input("Précisez les secondes : ")))
    except ValueError:
        print('Saisie incorrecte')
        return(my_get_tuple(i))
    if (my_check_tuple(my_tuple) == True):
        return(my_tuple)
    else:
        return(my_get_tuple(i))


#en soit je pourrais m'en passer mais ca permet de simplifier un peu le code
#et de mettre la deuxieme fonction qui doit prendre un tuple
def my_set_alarm(time_tuple):
        
        stop_time = [time_tuple[0], time_tuple[1], time_tuple[2]]
        return(stop_time)

#verifie si l'heure actuelle correspond a celle de l'alarme
def my_check_alarm(act_time, stop_time):
    if (stop_time == None):
        return()
    if (act_time == stop_time):
        print("C'est l'heure")


def my_affichage_mode():
    try:
        i = int(input("Tapez 1 pour un affichage classique ou 2 pour un affichage ''à l'anglaise'' : "))
    except ValueError:
        print('Saisie incorrecte')
        return(my_affichage_mode())
    if (i == 1):
        return(i)
    elif (i == 2):
        return(i)
    else:
        print('Saisie incorrecte')
        return(my_affichage_mode())

def my_pause(pause):
    if (keyboard.read_key(' ') and pause == False):
        pause = True
        return(pause)
    elif (keyboard.read_key(' ') and pause == True):
        pause = False
        return(pause)
    else :
        return(pause)
           
#fonction principale et mandataire du projet
def afficher_heure(my_tuple):
    
    pause = False
    if my_check_tuple(my_tuple) == False:
        return(None)
    alarm_time = my_menu_alarm()
    t = my_affichage_mode()
    time_list = [my_tuple[0], my_tuple[1], my_tuple[2]]
    while True:
        if (pause == False):
            my_check_alarm(time_list, alarm_time)
            my_print_heure(time_list, t)
            time_list[2] += 1
            if (time_list[2] > 59):
                time_list[1] += 1
                time_list[2] = 0
                if (time_list[1] > 59):
                    time_list[0] += 1
                    time_list[1] = 0
                    if (time_list[0] > 23):
                        time_list[0] = 0
            time.sleep(1)

time_tuple = my_get_tuple(1)
afficher_heure(time_tuple)