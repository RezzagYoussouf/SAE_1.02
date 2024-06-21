from santa_claus import *

def test_dictionary_cities():
    villes=["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    assert dictionary_cities(villes) == {'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}


    print("TEST OK")

def test_distance_cities():

    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert round(distance_cities("Paris","Lyon",dico),4) == 394.5057
    assert round(distance_cities("Lille","Lyon",dico),4) == 558.5472
    assert distance_cities("Lille1","Lyon",dico) == -1
    print("TEST OK")


def test_tour_length():
    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert tour_length(["Paris", "Lyon", "Marseille", "Lille"],dico) == 1708.0796060895232
    print("TEST OK")

def test_closest_city():
    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert closest_city("Paris",["Marseille", "Lyon"],dico) == 1
    assert closest_city("Paris",["Marseille", "Marseille","Lyon"],dico) == 2
    print("TEST OK")

def test_tour_from_closest_city():

    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert tour_from_closest_city("Marseille",dico) == ["Marseille", "Lyon", "Paris", "Lille"]
    print("TEST OK ")

def test_best_tour_from_closest_city():

    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert best_tour_from_closest_city(dico) == ["Paris", "Lille", "Lyon", "Marseille"] or ["Lyon", "Marseille", "Paris", "Lille"]
    print("Test OK")

def test_reverse_part_tour():
    tour=["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    reverse_part_tour(tour,2,5)
    assert tour == ["Agen", "Belfort", "Fréjus","Épinay", "Dijon", "Cahors", "Grenoble", "Hyères"]
    print("Test OK")

def test_inversion_length_diff():
    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert round(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"],dico,1,2),4) == -740.857
    print('Test OK')

def test_better_inversion():
    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}

    assert better_inversion(["Marseille", "Paris", "Lyon", "Lille"],dico) == True
    assert better_inversion(["Marseille", "Lyon", "Lille", "Paris"],dico) == False
    print("Test OK")

def test_best_obtained_with_inversions():
    dico={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert best_obtained_with_inversions(["Marseille", "Paris", "Lyon", "Lille"],dico) == 2
    assert best_obtained_with_inversions(["Marseille", "Lyon", "Paris", "Lille"],dico) == 1
    assert best_obtained_with_inversions(["Marseille", "Lyon", "Lille", "Paris"],dico) == 0
    print("Test ok ")
