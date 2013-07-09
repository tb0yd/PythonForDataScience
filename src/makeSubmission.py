import pandas as pd
import numpy as np
from optparse import OptionParser
import sys
from sklearn.ensemble import RandomForestClassifier


def main():
    # create the training & test sets
    dataset = np.genfromtxt(sys.stdin, delimiter=',', dtype='f8')[1:]
    target = np.array([x[0] for x in dataset])
    train = np.array([x[1:] for x in dataset])

    dataset = np.genfromtxt('Data/prepared_test.csv', delimiter=',', dtype='f8')[1:]
    test = np.array([x[1:] for x in dataset])
    test_ids = np.array([int(x[0]) for x in dataset])

    # create and train the random forest
    # n_jobs set to -1 will use the number of cores present on your system.
    rf = RandomForestClassifier(n_estimators=100, n_jobs=-1)
    rf.fit(train, target)
    predicted_probs = [x[1] for x in rf.predict_proba(test)]
    predicted_probs = pd.Series(predicted_probs)
    
    # format output
    submission = pd.DataFrame({ 'PassengerId': test_ids, 'Survived': predicted_probs.map(lambda x: 1 if x >= 0.5 else 0) },
			)

    submission.to_csv('Data/submission.csv', index=False)

if __name__ == "__main__":
    main()
