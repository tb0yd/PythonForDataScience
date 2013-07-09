from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
import logloss
import sys
import numpy as np
import pylab as pl
from optparse import OptionParser
from sklearn.svm import l1_min_c
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import pybrain.structure as st

def main():
    # pull in data from input stream
    infile = sys.stdin

    #read in  data, parse into training and target sets
    # dataset = np.genfromtxt(open('Data/train.csv','r'), delimiter=',', dtype='f8')[1:]
    dataset = np.genfromtxt(infile, delimiter=',', dtype='f8')[1:]
    target = np.array([x[0] for x in dataset])
    train = np.array([x[1:] for x in dataset])

    #In this case we'll use a random forest, but this could be any classifier

    #Simple K-Fold cross validation. 5 folds.
    cv = cross_validation.KFold(len(train), k=5, indices=False)

    #iterate through the training and test cross validation segments and
    #run the classifier on each one, aggregating the results into a list
    results = []
    for traincv, testcv in cv:
        cfr = RandomForestClassifier(n_estimators=100)

########net = buildNetwork(5, 8, 3, 1, bias=True)
########netds = SupervisedDataSet(5, 1) 
########for x, y in zip(train[traincv], target[traincv]):
########	netds.addSample(x, [y])
########trainer = BackpropTrainer(net, netds)
########for i in range(30):
########	trainer.train()

        probasRFC = [x[1] for x in cfr.fit(train[traincv], target[traincv]).predict_proba(train[testcv])]
#       probasNET = [net.activate(x)[0] for x in train[testcv]]
#       probas = map(np.mean, zip(probasNET, probasRFC))

        results.append( logloss.llfun(target[testcv], probasRFC) )

    #print out the mean of the cross-validated results
    print "Results: " + str( np.array(results).mean() )

if __name__=="__main__":
    main()
