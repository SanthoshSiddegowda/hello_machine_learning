from sklearn import tree
features = [[140,1],[150,1],[160,2],[170,2]]
labels = [1,1,2,2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print clf.predict([[160,2]])
