"""
Evaluation of genetic algorithm on knapsack problem

"""

"""
Size of population : Plus on augmente la taille de la population, l'algorithme resous le probleme plus vote mais 
on utilise plus de memoire ==> Compromis temps-memoire
Ex : num_generations = 1 loop for 200 pop against 7 loops for 100 pop

"""

"""
Selection influence le resultat de la recherche. Avec un type de selection adéquate on arrive plus vite au bon résultat alors
qu'avec un autre type on prendra plus de temps ou on n'arrivera meme pas au bon résultat
Ex : 7 loops for 100 pop selTournament; selAutomaticEpsilonLexicase 8 loops for 100 pop; selRoulette pas le bon résultat

"""