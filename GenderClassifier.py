""" gender classifier using the sci-kit learn library """
from sklearn import tree

# [height, weight, shoe size]
X = [[181, 80, 44],
     [177, 70, 43],
     [160, 60, 38],
     [154, 54, 37],
     [160, 65, 40],
     [190, 90, 47],
     [175, 64, 39],
     [177, 70, 40],
     [159, 55, 37],
     [171, 75, 42],
     [181, 85, 43]]

Y = ['male', 'female', 'female',
     'female', 'male', 'male',
     'male', 'female', 'male',
     'male', 'female']

CLF = tree.DecisionTreeClassifier()
CLF = CLF.fit(X, Y)

PREDICTION = CLF.predict([[190, 70, 40]])

print PREDICTION
