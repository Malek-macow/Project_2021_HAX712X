import numpy as np
import pandas as pd
import time
import networkx as nx


start = time.time()


def average_cost(data_price, data_dist):
    """
    Calcule de la matrice du prix moyen au kilomètre.
    
    Paramètres
    ----------
    data_price : DataFrame.
    	Tableau des prix.
    
    data_dist : DataFrame.
    	Tableau des distances.
    
    Return
    ------
    M : array.
    	Retourne la matrice des prix moyens.
    """
    n = len(data_price)
    p = np.array(data_price)
    d = np.array(data_dist) + np.diag(np.ones(n))
    return p/d

end = time.time()
print("Temps passé pour exécuter average_cost: {0:.5f} s.".format(end - start))


start = time.time()


def average_cost_list(data_price, data_dist):
    """
    Calcule de la liste du prix moyen au kilomètre.
    
    Paramètres
    ----------
    data_price : DataFrame.
    	Tableau des prix.
    
    data_dist : DataFrame.
    	Tableau des distances.
    
    Return
    ------
    L : list.
    	Retourne la partie diagonale inférieure (ou supérieure par 
    	symétrie) de la matrice des prix moyens sous forme de liste.
    """
    n = len(data_price)
    p = np.array(data_price)[np.triu_indices(n, k=1)]
    d = np.array(data_dist)[np.triu_indices(n, k=1)]
    return p/d

end = time.time()
print("Temps passé pour exécuter average_cost_list: {0:.5f} s.".format(end - start))


start = time.time()


def get_index(data, name):
    """
    Retourne la valeur de la position de name en tant qu'index.
    
    Paramètres
    ----------
    data : pd.DataFrame.
    
    name : str ou list, 
    	Nom(s) d'index du tableau de données data.
    
    Return
    ------
    I : int or list.
    	Donne la/les positions(s) de name dans l'index de data.
    """
    if type(name) == str:
        i = 0
        while i < len(data) and name != data.index[i]:
            i += 1
        return i
    elif type(name) == list:
        ind = []
        for j in range(len(name)):
            i = 0
            while i < len(data) and name[j] != data.index[i]:
                i += 1
            ind.append(i)
        return ind
end = time.time()
print("Temps passé pour exécuter get_index: {0:.5f} s.".format(end - start))

start = time.time()


def get_way(data_dist, start, target):
    """
    Renvoie une liste contenant les péages entre start et target.
    Notre méthode se base sur le fait que l'algorithme de Kruskal nous
    fournit un graphe du réseau routier avec seulement des arêtes
    entre deux gares successives dont on déduit trivialement la liste
    avec un algorithme du plus court chemin (ici Dijkstra).
    
    Paramètres
    ----------
    data_dist : DataFrame.
    	Tableau de données sous forme de matrice 
    	de distance entre toutes les gares.
    
    start : str.
    	La gare de départ (doit être une élément de 
    	data_dist.columns).
    
    target : str.
    	La gare d'arrivée (doit être une élément de
    	data_dist.columns).
    
    Return
    ------
    L : list.
    	Liste des péages situé sur le trajet autoroutier le plus court
    	de start à target.
    """
    G = nx.Graph(incoming_graph_data=data_dist)
    a = nx.minimum_spanning_tree(G, weight='weight')
    return nx.shortest_path(a, start, target, weight='weight')

end = time.time()
print("Temps passé pour exécuter get_way : {0:.5f} s.".format(end - start))

