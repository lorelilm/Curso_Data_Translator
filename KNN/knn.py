import numpy as np
import pandas as pd
from collections import Counter
from make_data import make_data
from scipy.spatial.distance import euclidean
from sklearn.neighbors import KNeighborsClassifier
import math
from scipy.spatial.distance import cityblock
from sklearn.model_selection import train_test_split
from scipy.spatial import distance


X, y = make_data(n_features=2, n_pts=300, noise=0.1)


def euclidean_distance(a, b):
    """Distancia euclideana entre dos arrays.

    Parametros
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distancia: float
    """
    return math.dist(a, b) #np.linalg.norm(a-b)


def cosine_distance(a, b):
    """Similitud coseno entre dos arrays.

    Parametros
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distancia: float
    """

    return distance.cosine(a, b)



def manhattan_distance(a, b):
    """Distancia Manhattan entre dos arrays.

    Parametros
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distancia: float
    """
    return cityblock(a,b)


class KNNRegressor:
    """Regresor para KNN.

    Parametros
    ----------
    k: int, opcional (default = 5)
        Vecinos a incluir en la predicción.
    distancia: function, opcional (default = euclidean)
        Métrica de distancia a utilizar.
    """

    def __init__(self, k=5, distance=euclidean_distance):
        """Inicializar el objeto KNNRegressor."""
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        """Ajustar el modelo con "X" como entrenamiento e "y" como objetivo.

        De acuerdo con el algoritmo KNN, los datos de entrenamiento son almacenados.

        Parametros
        ----------
        X: numpy array, shape = (n_observaciones, n_features)
            Conjunto de entrenamiento.
        y: numpy array, shape = (n_observaciones,)
            Valores objetivo.

        Returns
        -------
        self
        """
        self.x_train = np.array(X)
        self.y_train = np.array(y)
        return

    def predict(self, X):
        """Devuelve el valor predecido para la entrada X (conjunto de prueba).

        Asume que la forma de X es [n_observaciones de prueba, n_características] donde
        n_features es la misma que las n_features de los datos de
        de entrada.

        Parametros
        ----------
        X: numpy array, shape = (n_observaciones, n_features)
            Conjunto de prueba.

        Returns
        -------
        result: numpy array, shape = (n_observaciones,)
            Valores predecidos para cada dato de entrada.

        """
        for x in X:
            vecinos_x = self.obtener_vecinos(x)
            valores_vecinos = pd.DataFrame(self.y_train[vecinos_x['idx']], columns=['target'])
            evaluacion = valores_vecinos.groupby(['target'])['target'].count().sort_values(ascending=False).head(1)

            print(evaluacion.index.values)
        pass

    def obtener_vecinos(self,prueba):
        distancia_vecinos = []

        for idx, dato in enumerate(self.x_train):
            distancia_vecinos.append([idx, self.distance(prueba,dato)])

            df_distancia_vecinos = pd.DataFrame(distancia_vecinos, columns=['idx','distancia'])
            k_vecinos = df_distancia_vecinos.sort_values(by='distancia', ascending=True).head(self.k)

        return k_vecinos
        
datos_x = np.array([[2.7810836, 2.550537003], 
[1.465489372, 2.362125076],
[3.396561688, 4.400293529],
[1.38807019, 1.850220317],
[3.06407232, 3.005305973],
[7.627531214, 2.759262235],
[5.332441248, 2.088626775],
[6.922596716, 1.77106367],
[8.675418651, -0.242068655],
[7.673756466, 3.508563011]
])

datos_y = np.array([0,0,0,0,0,1,1,1,1,1])

knn= KNNRegressor()

knn.fit(datos_x, datos_y)
knn.predict(datos_x)


        """self.X_test = X
        values_x = []
        positions = []
        results = []
        for i in self.x_test:
            for posicion, j in enumerate(self.X_train):
                values_x.append(self.distance(i,j))
                positions.append(posicion)
            df = pd.DataFrame.from_dict({'Positions': positions, 'x_value':values_x})
            df = df.sort_values(by='x_value')
            df = df.sort_values(by='x_value')
            df = df.iloc[:self.k,:]
            df['y_values'] = self.y_train[df['¨Positions']]
            mean = df['y_values'].mean()
            results.append(mean)
        return np.array(results)"""

