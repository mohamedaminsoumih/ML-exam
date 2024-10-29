# -*- coding: utf-8 -*-
"""solution_template.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hdFpevy1RD_3ijLUbeR1XM9Imp947rSU

## IFT6390 — PROGRAMMING MIDTERM, FALL 2024

This exam is for students registered in IFT6390A/B only. Please prepare your ID. We will pass by to check it and take attendance.

We will start the session by helping you set up and answering questions. The exam will start 15 minutes after the start of the session. At that time we will upload the exam files into the Resources page on Piazza, and the Gradescope entry will open for you to start submitting. As in our simulation exam, you are welcome to work either on the Jupyter notebook provided (.ipynb) or the Python script (.py). In any case you will have to submit your code for autoevaluation in the form of a python script named solution.py.

The exam will last 1 hour and 15 minutes. After that the Gradescope will stop accepting solutions and you will not be able to submit your unsubmitted code. Important: You are strongly advised to start submitting early and to submit frequently. Do not wait until the end of the session to submit your code; it will not go well. This exam is not graded manually and you will only receive the points given to you by the autograder.

The questions are ordered approximately from easy to hard, however depending on your background, you might find that Question 4 or Question 5 are easier than Question 3. You can work on the questions in any order you prefer.

When you are finished with the exam, close your laptop and stay quietly at your seat. If at least one hour has passed from the start of the exam, you will be allowed to leave the room. At the end of the allocated time for the exam you must exit the room quietly, without making any noise. Other people might still be working.

Good luck!

____________________


## IFT6390 — EXAMEN DE PROGRAMMATION, AUTOMNE 2024

Cet examen est réservé aux étudiants inscrits dans IFT6390A/B uniquement. Veuillez préparer votre carte d'identité. Nous passerons pour la vérifier et faire l'appel.

Nous commencerons la session en vous aidant à configurer et en répondant aux questions. L'examen commencera 15 minutes après le début de la session. À ce moment-là, nous téléchargerons les fichiers de l'examen dans la page Ressources sur Piazza, et l'entrée Gradescope s'ouvrira pour que vous puissiez commencer à soumettre. Comme lors de notre examen de simulation, vous êtes libre de travailler soit sur le notebook Jupyter fourni (.ipynb) soit sur le script Python (.py). Dans tous les cas, vous devrez soumettre votre code pour l'évaluation automatique sous la forme d'un script Python nommé solution.py.

L'examen durera 1 heure et 15 minutes. Après cela, Gradescope cessera d'accepter les solutions et vous ne pourrez plus soumettre votre code non soumis. Important : Il est fortement conseillé de commencer à soumettre tôt et de soumettre fréquemment. Ne pas attendre la fin de la session pour soumettre votre code ; cela ne se passera pas bien. Cet examen n'est pas corrigé manuellement et vous recevrez uniquement les points attribués par l'auto-correcteur.

Les questions sont ordonnées approximativement de la plus facile à la plus difficile ; cependant, en fonction de votre parcours, vous pourriez trouver que la Question 4 ou la Question 5 est plus facile que la Question 3. Vous pouvez travailler sur les questions dans l'ordre que vous préférez.

Lorsque vous avez terminé l'examen, fermez votre ordinateur portable et restez tranquillement à votre place. Si au moins une heure s'est écoulée depuis le début de l'examen, vous serez autorisé à quitter la salle. À la fin du temps alloué pour l'examen, vous devez quitter la salle en silence, sans faire de bruit. D'autres personnes pourraient encore être en train de travailler.

Bonne chance !
"""

import numpy as np
import random
import collections
import sys
import copy
import matplotlib.pyplot as plt
from datetime import datetime

"""## Question 1: Support Vector Machine (SVM) Classifier with the Polynomial Kernel (6 points)

In this question, you are required to implement a Support Vector Machine (SVM) classifier using a Polynomial Kernel. SVM is a supervised machine learning model commonly used for classification tasks. The Polynomial Kernel is a non-linear kernel that computes the similarity between two vectors in a higher-dimensional space using the following formula:

$$ K(x, y) = (k \cdot \langle x, y \rangle + c)^d $$

Where:

- $\langle x, y \rangle$ is the dot product between vectors x and y.
- $k$, $c$, and $d$ are kernel parameters.

You will need to:

1. Implement the Polynomial Kernel function.
2. Implement the SVM classifier using the polynomial kernel.
3. Return the predicted class label for a new data point.


## Steps:

- Assume that the training data consists of feature vectors X and corresponding labels Y.
- Implement the function to compute the polynomial kernel.
- Implement the SVM classifier using the polynomial kernel.
- Make predictions for a test dataset using the trained SVM model.


## Part 1: Implement the Polynomial Kernel (3 points)

-----------------------

## Question 1 : Classificateur SVM (Support Vector Machine) avec le noyau polynomial (6 points)

Dans cette question, vous devez implémenter un classificateur SVM (Support Vector Machine) en utilisant un noyau polynomial. Le SVM est un modèle d'apprentissage supervisé couramment utilisé pour des tâches de classification. Le noyau polynomial est un noyau non linéaire qui calcule la similarité entre deux vecteurs dans un espace de dimension supérieure à l'aide de la formule suivante :

$$ K(x, y) = (k \cdot \langle x, y \rangle + c)^d $$

Où :

- $\langle x, y \rangle$ est le produit scalaire entre les vecteurs x et y.
- \(k\), \(c\), et \(d\) sont les paramètres du noyau.

Vous devrez :

1. Implémenter la fonction du noyau polynomial.
2. Implémenter le classificateur SVM en utilisant le noyau polynomial.
3. Retourner l'étiquette de classe prédite pour un nouveau point de données.


## Étapes :

- Supposons que les données d'entraînement se composent de vecteurs de caractéristiques \(X\) et des étiquettes correspondantes \(Y\).
- Implémentez la fonction pour calculer le noyau polynomial.
- Implémentez le classificateur SVM en utilisant le noyau polynomial.
- Faites des prédictions pour un ensemble de données de test en utilisant le modèle SVM entraîné.


## Partie 1 : Implémenter le noyau polynomial (3 points)
"""
 # J'ai utilisé ChatGPT pour m'aider à répondre à cette question.

class SVM_PolynomialKernel:
    def __init__(self):
        pass

    @staticmethod
    def polynomial_kernel(x, y, kernel_scale=1, c=0, d=2):
        """
        Calcule la valeur du noyau polynomial entre deux vecteurs x et y.
        
        :param x: List[float]
        :param y: List[float]
        :param kernel_scale: float - Facteur de mise à l'échelle pour le produit scalaire dans la fonction noyau
        :param c: float
        :param d: int
        :return: float - Valeur du noyau
        """
        dot_product = sum(xi * yi for xi, yi in zip(x, y))
        return (kernel_scale * dot_product + c) ** d



        # END SOLUTION -- FIN SOLUTION

"""## Part 2: Implement the SVM Classifier (3 points)

To simplify the implementation, assume you are given:

- $lagrange\_multipliers(\alpha_i \text{ values})$: An array of learned weights from the SVM optimization.
- $b$ : The bias term.
- support_vectors: The support vectors that define the decision boundary.
- support_labels: The labels of the support vectors.

The mathematical formula for the decision value is given by:

  $$\text{decision_value} = \sum_{i=1}^{n} \alpha_i \times y_i \times K(\mathbf{x}_i, \mathbf{x}{\text{new}}) + b$$

Return 1 if decision_value > 0 and -1 if decision_value $\leq$ 0. $x_i$ refers to the support vectors and that $i$ indexes these.

You are required to implement the decision function and predict the class label for a new point $x_{\text{new}}$.

-----------------------

## Partie 2 : Implémenter le classificateur SVM (3 points)

Pour simplifier l'implémentation, supposons que vous disposez des éléments suivants :

- $lagrange\_multipliers(\text{valeurs de } \alpha_i)$: Un tableau de poids appris à partir de l'optimisation du SVM.
- $b$ : Le terme de biais.
- support_vectors: Les vecteurs supports qui définissent la frontière de décision.
- support_labels: Les étiquettes des vecteurs supports.

La formule mathématique pour la valeur de décision est donnée par :

  $$\text{decision_value} = \sum_{i=1}^{n} \alpha_i \times y_i \times K(\mathbf{x}_i, \mathbf{x}_{\text{new}}) + b$$

Retourner 1 si decision_value > 0 et -1 si decision_value $\leq$ 0. $x_i$ fait référence aux vecteurs supports et $i$ est l'indice de ceux-ci.

Vous devez implémenter la fonction de décision et prédire l'étiquette de classe pour un nouveau point $x_{\text{new}}$.
"""
# J'ai utilisé ChatGPT pour m'aider à répondre à cette question.

class SVM_Classifier:
    def __init__(self):
        pass

    def svm_predict(self, support_vectors, support_labels, lagrange_multipliers, b, x_new, kernel_function=SVM_PolynomialKernel.polynomial_kernel):
        """
        Prédit la classe pour un nouveau point de données x_new en utilisant le SVM avec noyau polynomial.
        
        :param support_vectors: List[List[float]] - Liste des vecteurs supports
        :param support_labels: List[int] - Liste des étiquettes des vecteurs supports
        :param lagrange_multipliers: List[float] - Multiplicateurs de Lagrange trouvés pendant l'entraînement
        :param b: float - Terme de biais
        :param x_new: List[float] - Nouveau point de données à classifier
        :param kernel_function: callable - Fonction noyau à utiliser (par défaut, noyau polynomial)
        :return: int - Classe prédite (-1 ou 1)
        """
        decision_value = sum(alpha * y * kernel_function(x, x_new) 
                             for alpha, y, x in zip(lagrange_multipliers, support_labels, support_vectors)) + b
        return 1 if decision_value > 0 else -1


"""## Question 2: Implementing a Gaussian Probability Density Function (PDF) (6 points)

A Gaussian Probability Density Function (PDF), also known as the Normal Distribution, describes the probability distribution of a continuous random variable that follows a normal distribution. The goal of this question is to implement a Gaussian PDF.

You will need to:

1. Implement the Multivariate Gaussian PDF.
2. Infer the log probability of a new data point.

## Part 1: Implementation of the Multivariate Gaussian PDF (3 points)

The probability density function (PDF) of the multivariate Gaussian distribution is given by:

$$ P(x | \mu, \Sigma) = \frac{1}{\sqrt{(2\pi)^k |\Sigma|}} \exp\left( -\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu) \right) $$

Where:

- $x$ is the data point.
- $\mu$ is the mean vector.
- $\Sigma$ is the covariance matrix.
- $k$ is the dimensionality of the data.

------------

## Question 2: Implémentation d'une fonction de densité de probabilité (PDF) gaussienne (6 points)

Une fonction de densité de probabilité (PDF) gaussienne, également connue sous le nom de distribution normale, décrit la distribution de probabilité d'une variable aléatoire continue qui suit une distribution normale. L'objectif de cette question est d'implémenter une PDF gaussienne.

Vous devrez :

1. Implémenter la PDF gaussienne multivariée.
2. Inférer la probabilité logarithmique d'un nouveau point de données.

## Partie 1 : Implémentation de la PDF gaussienne multivariée (3 points)

La fonction de densité de probabilité (PDF) de la distribution gaussienne multivariée est donnée par :

$$ P(x | \mu, \Sigma) = \frac{1}{\sqrt{(2\pi)^k |\Sigma|}} \exp\left( -\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu) \right) $$

Où :

- $x$ est le point de données.
- $\mu$ est le vecteur moyen.
- $\Sigma$ est la matrice de covariance.
- $k$ est la dimension des données.
"""
# J'ai utilisé ChatGPT pour m'aider à répondre à cette question.


class MultivariateGaussianPDF:
    def __init__(self):
        pass

    def multivariate_gaussian_pdf(self, x, mu, sigma):
        """
        Calcule la densité de probabilité pour un point de données x dans une distribution gaussienne multivariée.
        
        :param x: List[float] OU 1D numpy.ndarray - Point de données (vecteur de caractéristiques)
        :param mu: List[float] OU 1D numpy.ndarray - Vecteur moyen
        :param sigma: Matrice 2D OU 2D numpy.ndarray - Matrice de covariance
        :return: float - Densité de probabilité de x donnée par la distribution gaussienne
        """
        x = np.array(x)
        mu = np.array(mu)
        sigma = np.array(sigma)
        
        k = len(mu)
        sigma_det = np.linalg.det(sigma)
        sigma_inv = np.linalg.inv(sigma)
        diff = x - mu
        
        exponent = -0.5 * np.dot(diff.T, np.dot(sigma_inv, diff))
        coefficient = 1 / (np.sqrt((2 * np.pi) ** k * sigma_det))
        
        return coefficient * np.exp(exponent)


"""## Part 2: Inference Problem (3 points)

Let the mean vector be $\mu$ and the covariance matrix be $\Sigma$. You are given a n-dimensional data point  $\mathbf{x}$.


Using the given mean vector ($\mu$) and covariance matrix ($\Sigma$), implement the log probability of a data point  $\mathbf{x}$  under the n-dimensional Gaussian distribution. The log probability is obtained after deriving the Gaussian PDF and is given by:


$$\log P(\mathbf{x} | \mu, \Sigma) = -\frac{1}{2} \left( (x - \mu)^T \Sigma^{-1} (x - \mu) \right) - \frac{1}{2} \log \left( (2\pi)^k |\Sigma| \right)$$

----------

## Partie 2 : Problème d'inférence (3 points)

Soit le vecteur moyen $\mu$ et la matrice de covariance $\Sigma$. On vous donne un point de données n-dimensionnel $\mathbf{x}$.

En utilisant le vecteur moyen donné ($\mu$) et la matrice de covariance ($\Sigma$), implémentez la probabilité logarithmique d'un point de données $\mathbf{x}$ sous la distribution gaussienne n-dimensionnelle. La probabilité logarithmique est obtenue après avoir dérivé la PDF gaussienne et est donnée par :

$$\log P(\mathbf{x} | \mu, \Sigma) = -\frac{1}{2} \left( (x - \mu)^T \Sigma^{-1} (x - \mu) \right) - \frac{1}{2} \log \left( (2\pi)^k |\Sigma| \right)$$
"""

# J'ai utilisé ChatGPT pour m'aider à répondre à cette question.


class Inference:
    def __init__(self):
        pass

    def log_multivariate_gaussian_pdf(self, x, mu, sigma):
        """
        Calcule le logarithme de la densité de probabilité pour un point de données x dans une distribution gaussienne multivariée.
        
        :param x: List[float] OU 1D numpy.ndarray - Point de données (vecteur de caractéristiques)
        :param mu: List[float] OU 1D numpy.ndarray - Vecteur moyen
        :param sigma: Matrice 2D OU 2D numpy.ndarray - Matrice de covariance
        :return: float - Logarithme de la densité de probabilité de x donnée par la distribution gaussienne
        """
        x = np.array(x)
        mu = np.array(mu)
        sigma = np.array(sigma)
        
        k = len(mu)
        sigma_det = np.linalg.det(sigma)
        sigma_inv = np.linalg.inv(sigma)
        diff = x - mu
        
        exponent_term = -0.5 * np.dot(diff.T, np.dot(sigma_inv, diff))
        log_coefficient = -0.5 * (k * np.log(2 * np.pi) + np.log(sigma_det))
        
        return exponent_term + log_coefficient


"""## Question 3: Adjacent characters problem (2 point)

Given a string of lowercase English letters, write a function that checks if it is possible to rearrange the string such that no two adjacent characters are the same.

Example 1:

Input:
word = "aabbcc"

Output:
True

Explanation: One possible rearrangement is "abcabc", where no two adjacent characters are the same.

Example 2:

Input:
word = "aaaabb"

Output:
False

Explanation: It is impossible to rearrange the string such that no two 'a' characters are adjacent.

Hint: To solve this question, you only need to use a vector of letter frequencies (counts), and the total length of the word. Try to play with simple examples on a piece of paper to find out the simple rule.

-----------------------

## Question 3: Problème des caractères adjacents (2 point)

Étant donné une chaîne de lettres minuscules anglaises, écrivez une fonction qui vérifie s'il est possible de réorganiser la chaîne de telle sorte que deux caractères adjacents ne soient jamais les mêmes.

Exemple 1 :

Entrée :
word = "aabbcc"

Sortie :
True

Explication : Une réorganisation possible est "abcabc", où aucun caractère adjacent n'est identique.

Exemple 2 :

Entrée :
word = "aaaabb"

Sortie :
False

Explication : Il est impossible de réorganiser la chaîne de manière à ce que deux caractères 'a' ne soient pas adjacents.

Indice : Pour résoudre cette question, vous n'avez besoin que d'un vecteur de fréquences des lettres (comptes) et de la longueur totale du mot. Essayez de jouer avec des exemples simples sur une feuille de papier pour découvrir la règle simple.
"""

# J'ai utilisé ChatGPT pour m'aider à répondre à cette question.

class AdjacentCharactersProblem:
    def __init__(self):
        pass

    def can_rearrange(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Compter les occurrences de chaque caractère
        counts = {}
        for char in word:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        # Trouver la fréquence maximale et la longueur du mot
        max_count = max(counts.values())
        word_length = len(word)

        # Vérifie si le caractère le plus fréquent peut être réorganisé sans être adjacent
        return max_count <= (word_length + 1) // 2



"""## Question 4: Length of the longest subarray of an array (3 points)

Given an array of integers called nums, write a function that returns the length of the longest subarray where the absolute difference between any two elements is less than or equal to 1. Each subarray consists of a subset of elements of the original array. For example, for the array A = [1, 8, 4, 0], the lists [1, 8], [8, 4, 0], and [1, 0] are all possible subarrays of A.
Example 1:

Input:
nums = [1, 2, 2, 3, 1, 2]

Output:
5

Explanation: The longest subarray is [1, 2, 2, 1, 2] with a length of 5.

Example 2:

Input:
nums = [4, 6, 5, 3, 3, 1]

Output:
3

Explanation: The longest subarray is [4, 3, 3] with a length of 3.

-----------------------

## Question 4: Longueur du plus long sous-tableau d'un tableau (3 points)

Étant donné un tableau d'entiers appelé nums, écrivez une fonction qui renvoie la longueur du plus long sous-tableau où la différence absolue entre deux éléments quelconques est inférieure ou égale à 1. Chaque sous-tableau consiste en un sous-ensemble d'éléments du tableau d'origine. Par exemple, pour le tableau A = [1, 8, 4, 0], les listes [1, 8], [8, 4, 0], et [1, 0] sont tous des sous-tableaux possibles de A.
Exemple 1 :

Entrée :
nums = [1, 2, 2, 3, 1, 2]

Sortie :
5

Explication : Le plus long sous-tableau est [1, 2, 2, 1, 2] avec une longueur de 5.

Exemple 2 :

Entrée :
nums = [4, 6, 5, 3, 3, 1]

Sortie :
3

Explication : Le plus long sous-tableau est [4, 3, 3] avec une longueur de 3.
"""
# J'ai utilisé ChatGPT pour m'aider à répondre à cette question, avec des majeures modifications que j'ai faites moi-même.

class LengthLongestSubarray:
    def __init__(self):
        pass

    def longest_subarray(self, nums):
        # Compter les occurrences de chaque nombre
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        max_length = 0

        # Calculer la longueur maximale en vérifiant chaque nombre et son voisin
        for num in counts:
            adjacent_count = counts[num] + counts.get(num + 1, 0)
            max_length = max(max_length, adjacent_count)

        return max_length





"""## Question 5: Maximum sum of the values along the path  (3 points)

You are given a matrix grid of size m x n where each cell contains a positive integer. Starting from the top-left cell, your task is to traverse to the bottom-right cell, and you can only move either right or down. Write a function that returns the maximum sum of the values along the path you take.

Example 1:

Input:
$
\text{grid} =
\begin{bmatrix}
    5 & 3 & 2 & 1 \\
    1 & 2 & 1 & 1 \\
    4 & 3 & 2 & 2
\end{bmatrix}
$

Output:
16

Explanation: The path with the maximum sum is 5 -> 3 -> 2 -> 3 -> 2 -> 2, with a total sum of 17.

Example 2:

Input:
$
\text{grid} =
\begin{bmatrix}
    1 & 2 & 5 \\
    3 & 2 & 1 \\
    4 & 3 & 1
\end{bmatrix}$

Output:
12

Explanation: The path with the maximum sum is 1 -> 3 -> 4 -> 3 -> 1, with a total sum of 12.

## Hint:

For a grid with $n$ rows and $m$ columns, you can enumerate all paths that start at grid position $(0,0)$ and end at $(m,n)$. You can enumerate paths with algorithms like depth-first search. You can alternately notice the repeated subproblems and use dynamic programming.

--------

## Question 5: Somme maximale des valeurs le long du chemin (3 points)

On vous donne une grille de taille m x n où chaque cellule contient un entier positif. En partant de la cellule en haut à gauche, votre tâche est de traverser jusqu'à la cellule en bas à droite, et vous ne pouvez vous déplacer que vers la droite ou vers le bas. Écrivez une fonction qui renvoie la somme maximale des valeurs le long du chemin que vous empruntez.

Exemple 1 :

Entrée :
$
\text{grid} =
\begin{bmatrix}
    5 & 3 & 2 & 1 \\
    1 & 2 & 1 & 1 \\
    4 & 3 & 2 & 2
\end{bmatrix}
$

Sortie :
16

Explication : Le chemin avec la somme maximale est 5 -> 3 -> 2 -> 3 -> 2 -> 2, avec une somme totale de 17.

Exemple 2 :

Entrée :
$
\text{grid} =
\begin{bmatrix}
    1 & 2 & 5 \\
    3 & 2 & 1 \\
    4 & 3 & 1
\end{bmatrix}$

Sortie :
12

Explication : Le chemin avec la somme maximale est 1 -> 3 -> 4 -> 3 -> 1, avec une somme totale de 12.

## Indice:

Pour une grille avec $n$ lignes et $m$ colonnes, vous pouvez énumérer tous les chemins qui commencent à la position de la grille $(0,0)$ et se terminent à $(m,n)$. Vous pouvez énumérer les chemins avec des algorithmes comme la recherche en profondeur. Vous pouvez également remarquer les sous-problèmes récurrents et utiliser la programmation dynamique.
"""

# J'ai utilisé ChatGPT pour m'aider à répondre à cette question, avec des majeures modifications que j'ai faites moi-même.

class MaximumSumPath:
    def __init__(self):
        pass

    def max_sum_path(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # Initialisation de la première colonne et première ligne
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Calcul de la somme maximale pour chaque cellule
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]

