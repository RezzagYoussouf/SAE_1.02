from math import radians, sin, cos, acos
from time import time 
def distance(long1, lat1, long2, lat2):
    
    long1 = radians(long1)
    lat1 = radians(lat1)
    long2 = radians(long2)
    lat2 = radians(lat2)
    
    R = 6370.7

    d = (R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long2-long1)))
    return d

def distance_noms(nom1, nom2, villes):
    long1, lat1 = villes[nom1]
    long2, lat2 = villes[nom2]
    return distance(long1, lat1, long2, lat2)
def long_tour(villes, tournee) :
    """
    Prend en paramètre une liste "villes" et une liste "tournée". Détermine la distance totale qu'il faut pour parcourir les villes dans l'ordre donné de la liste. Puis de la dernière a la première.
    """
    distanceT = 0 
    for i in range(len(tournee) - 1): 

        d2 = distance_noms(tournee[i], tournee[i + 1], villes)
        distanceT += d2
    distanceT += distance_noms(tournee[len(tournee) - 1], tournee[0], villes)
    return distanceT

def dictionary_cities(villes):
    """
    Crée un dictionnaire de distances entre des villes données. La liste des villes 
    doit être structurée comme suit: [nom_ville1, long1, lat1, nom_ville2, long2, lat2, ...].
    """
   
    distance_dict = {}
    i = 0
    while i < len(villes):
        ville1 = villes[i]
        long1, lat1 = villes[i + 1], villes[i + 2]
        distance_dict[ville1] = {}
        j = 0
        while j < len(villes):
            if j != i:
                ville2 = villes[j]
                long2, lat2 = villes[j + 1], villes[j + 2]
                dist = distance(long1, lat1, long2, lat2)
                distance_dict[ville1][ville2] = dist
            j += 3
        i += 3
    return distance_dict

#QUESTION 2

def distance_cities(ville1, ville2, dictio_dist):
     """
     Prends en paramètre 2 villes et un dictionnaire de distance. Retourne la distance entre les 2 villes 
     passées en paramètre si cette valeur est stockée dans le dictionnaire de villes, et -1 sinon.
     """
     if ville1 in dictio_dist and ville2 in dictio_dist[ville1]:
        return dictio_dist[ville1][ville2]
     else:
        return -1

dictio_dist = {
    'Paris': {
        'Lyon': 394.5056834297657, 
        'Marseille': 661.8616554466852, 
        'Lille': 203.67224282542662
    }, 
    'Lyon': {
        'Paris': 394.5056834297657, 
        'Marseille': 275.87965367431525, 
        'Lille': 558.5472363339435
    }, 
    'Marseille': {
        'Paris': 661.8616554466852, 
        'Lyon': 275.87965367431525, 
        'Lille': 834.0220261600157
    }, 
    'Lille': {
        'Paris': 203.67224282542662, 
        'Lyon': 558.5472363339435, 
        'Marseille': 834.0220261600157
    }
}

#QUESTION 3 
def tour_length(tour,dictio_dist) :
    """
    Prend en paramètre un tour et un dictionnaire de distances.Et retourne la longueur du tour.
    """
    
    d = 0
    i = 0
    while i < len(tour)-1 :
        ville1 = tour[i]
        ville2 = tour[i+1]
        d += distance_cities(ville1,ville2,dictio_dist)
        i+=1
    d += distance_cities(ville2, tour[0],dictio_dist )
    return d 

        
        
#QUESTION 4 : Theoriquement ; 
# Long_tourtour() est quadratique O(n²) car on appelle une fonction linéaire dans une boucle qui parcourt n fois un tableau, 
# et tour_length est linéaire O(n) car dans la boucle qui parcourt n élement on appelle une fonction constante

#Experimentalement longtour : 
tic = time()
tour  = ["Paris", "Lyon", "Marseille", "Lille"]
"long_tour(villes, dictio_dist)"
tac = time()

#Experimentalement tour_length :
tic = time()
tour  = ["Paris", "Lyon", "Marseille", "Lille"]
tour_length(tour, dictio_dist)
tac = time()

#QUESTION 5 


def closest_city(city, cities, dictio_dist) :
    """
    Prend en paramètre un nom de ville, un tableau de noms de villes et un dictionnaire de distances, 
    et retournant l'indice de la ville du tableau la plus proche de "city".
    """
    i = 0
    d = 0
    while i < len(cities) -1 :
        
        d1 = distance_cities(city, cities[i], dictio_dist)
        d2 = distance_cities(city, cities[i+1], dictio_dist)
        if d1 < d2 :
            d = cities[i]
        else:
            d = cities[i+1]
        i += 1
    return d 

        

#QUESTION 6 

def tour_from_closest_city(ville_depart, dictio_dist):
    """
    Prend en paramètre un nom de ville et un dictionnaire de distances et retourne le tour obtenu . 
    """
    ville_actu = ville_depart
    tour = [ville_depart]
    visited = [ville_depart]

    while len(visited) < len(dictio_dist):
        ville_pro = '' 
        min_dist = float('inf')

        cities = list(dictio_dist[ville_actu].keys())
        i = 0
        while i < len(cities):
            city = cities[i]
            if city not in visited:
                dist = dictio_dist[ville_actu][city]
                if dist < min_dist:
                    ville_pro = city
                    min_dist = dist
            i += 1

        if ville_pro:
            tour.append(ville_pro)
            visited.append(ville_pro)
            ville_actu = ville_pro

    return tour



tour = tour_from_closest_city("Marseille", dictio_dist)


#QUESTION 7 

def total_distance(tour, dictio_dist):
    """
    Prend en paramètre un tour et un dictionnaire de distance et calcul la distance totale du tour.
    
    """
    distance = 0
    i = 0
    while i < len(tour) - 1:
        distance += dictio_dist[tour[i]][tour[i + 1]]
        i += 1
    distance += dictio_dist[tour[-1]][tour[0]] 
    return distance

def best_tour_from_closest_city(dictio_dist):
    """
    Prend en paramètre un dictionnaire de distances. Et retourne le meilleur tour parmi ceux obtenus avec 
    l'algorithme "tour_from_closest_city" en prenant chaque ville comme ville de départ
    """
    best_tour = []
    shortest_distance = float('inf')

    cities = list(dictio_dist.keys())
    i = 0

    while i < len(cities):
        start_city = cities[i]
        tour = tour_from_closest_city(start_city, dictio_dist)
        tour_distance = total_distance(tour, dictio_dist)

        if tour_distance < shortest_distance:
            best_tour = tour
            shortest_distance = tour_distance

        i += 1

    return best_tour




#QUESTION 8 : Cubique car on appelle n fois une fonction quadratique dans une boucle 

#QUESTION 9

def reverse_part_tour(tour, ind_b, ind_e):
    """
    Inverse une partie d'un tour entre les indices ind_b et ind_e inclus.

    """
    tour[ind_b:ind_e+1] = reversed(tour[ind_b:ind_e+1])


#QUESTION 10 

def inversion_length_diff(dictio_dist, tour, ind_b, ind_e):
    """
    Prend en paramètre un dictionnaire de distances, un tour et deux indices ind_b et ind_e. 
    Et retourne la différence entre la distance du tour passé en paramètre et celui obtenu en inversant la partie du tour entre les ind_b et ind_e inclus.
    """
    original_distance = total_distance(tour, dictio_dist)


    modified_tour = tour[:]
  
    i, j = ind_b, ind_e
    while i < j:
        modified_tour[i], modified_tour[j] = modified_tour[j], modified_tour[i]
        i += 1
        j -= 1

    modified_distance = total_distance(modified_tour, dictio_dist)

    # Calcul de la différence de longueur
    length_diff = modified_distance - original_distance
    return length_diff

# Exemple d'utilisation
dictio_dist = {
    'Marseille': {'Lyon': 275.9, 'Paris': 661.9, 'Lille': 834.0},
    'Lyon': {'Marseille': 275.9, 'Paris': 394.5, 'Lille': 558.5},
    'Paris': {'Marseille': 661.9, 'Lyon': 394.5, 'Lille': 203.7},
    'Lille': {'Marseille': 834.0, 'Lyon': 558.5, 'Paris': 203.7}
}









#QUESTION 11
def better_inversion(tour, dictio_dist):
    """
    Prend en paramètre un tour et un dictionnaire de distances et appliquant cette amélioration au tour si elle existe. 
    La fonction renvoie True si une inversion du tour a été faite, et False sinon.
    """
    best_diff = 0
    best_inversion = (0, 0)

    i = 0
    while i < len(tour) - 1:
        j = i + 1
        while j < len(tour):
            current_diff = inversion_length_diff(dictio_dist, tour, i, j)
            if current_diff < best_diff:
                best_diff = current_diff
                best_inversion = (i, j)
            j += 1
        i += 1

    if best_diff < 0:
        ind_b, ind_e = best_inversion
        tour[ind_b:ind_e + 1] = reversed(tour[ind_b:ind_e + 1])
        return True

    return False


dictio_dist = {
    'Marseille': {'Lyon': 275.9, 'Paris': 661.9, 'Lille': 834.0},
    'Lyon': {'Marseille': 275.9, 'Paris': 394.5, 'Lille': 558.5},
    'Paris': {'Marseille': 661.9, 'Lyon': 394.5, 'Lille': 203.7},
    'Lille': {'Marseille': 834.0, 'Lyon': 558.5, 'Paris': 203.7}
}





#QUESTION 12

def best_obtained_with_inversions(tour, dictio_dist):
    """
    Prend en paramètre un tour et un dictionnaire de distances. La fonction effectue successivement des améliorations par inversion. 
    Elle s'arrête lorsque aucune inversion ne peut améliorer le tour. La fonction retournera le nombre d'inversions effectuées.
    """
    inversions_count = 0

    while True:
        if better_inversion(tour, dictio_dist):
            inversions_count += 1
        else:
            break

    return inversions_count



#QUESTION 13 : 

tic = time()
i = 0
while i < 500 :

    tour_from_closest_city("Marseille", dictio_dist)
    i+=1
tac = time()
print(tac - tic )

tic = time()
i = 0
while i < 500 :

    best_tour_from_closest_city(dictio_dist)
    i+=1
tac = time()
print(tac - tic)

tic = time()
i = 0
while i < 500 :

    best_obtained_with_inversions(tour, dictio_dist)
    i+=1
tac = time()
print(tac - tic )

#Le programme le plus rapide est best_obtained_with_inversion; On ne prend pas en compte le tour_from_closest_city car il ne donne pas le meilleur tour assurement.
