import time

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

#la fonction ne sert a rien mais il etait demandé dans le sujet qu'il y ai une autre fonction prenant en parametre un tuple pour regler l'alarme
def my_reglage_alarme(tuple):
    list = [tuple[0], tuple[1], tuple[2]]
    return(list)

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
    if (print_list[0] < 10):
        print('0', end= '')
    print(print_list[0], ':',sep='', end='')
    if (print_list[1] < 10):
        print('0', end= '')
    print(print_list[1], ':', sep = '',end='')
    if (print_list[2] < 10):
        print('0', end= '')
    print(print_list[2], end='')
    if (t == 2 and check == 1):
        print(' PM')
    elif (t == 2 and check == 2):
        print(' AM')

#menu demandant a l'utilisateur si il souhaite creer ou non une alarme
def my_menu_alarm():
    try:
        i = int(input("Voulez vous créer une alarme ? '1' pour oui '2' pour non : "))
    except ValueError:
        print('Saisie incorrecte')
        return(my_menu_alarm())
    if (i == 1):
        return(my_set_alarm())
    elif (i == 2):
        return(None)
    else:
        print('Saisie incorrecte')
        return(my_menu_alarm())

#fonction pour determiner l'heure de l'alarme avec securité du format
def my_set_alarm():
        
        stop_time = []
        try:
            stop_time += [int(input("Renseignez l'heure a laquelle l'alarme doit s'activer : "))]
            stop_time += [int(input("Précissez les minutes : "))]
            stop_time += [int(input("Précisez les secondes : "))]
        except ValueError:
            print("Saisie incorrecte")
            return(my_set_alarm())
        if (my_check_tuple((stop_time[0], stop_time[1], stop_time[2])) == False):
            print("Saisie incorrecte")
            return(my_set_alarm())
        else:
            return(my_reglage_alarme((stop_time[0], stop_time[1], stop_time[2])))

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

#fonction principale et mandataire du projet
def afficher_heure(my_tuple):
    
    if my_check_tuple(my_tuple) == False:
        return(None)
    alarm_time = my_menu_alarm()
    t = my_affichage_mode()
    time_list = [my_tuple[0], my_tuple[1], my_tuple[2]]
    while True:
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



afficher_heure((12, 59, 45))