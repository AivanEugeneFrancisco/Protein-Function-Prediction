#!/usr/bin/python
import numpy as np

#number of train data, so test data = total number - train data
train_num = 8000

train_features_path = "train_features.npy"
train_labels_path = "train_labels.npy"

test_features_path = "test_features.npy"
test_labels_path = "test_labels.npy"

features_raw_path = "sel_AC_Blast.dat"
labels_raw_path = "sel_AC_topGO.dat"

inf1 = open(features_raw_path, "r")
inf2 = open(labels_raw_path, "r")

if inf1 and inf2:
	print "Reading in " + features_raw_path + " and " + labels_raw_path + ", saved as " + train_features_path + " and " + train_labels_path + " ; " + test_features_path + " and " + test_labels_path + "!"
else:
	print "Reading in files failed!"
# processing features
for line in inf1:
	line = line.strip('\n')
	split = line.split('\t')
	tmp = [[]]
	for idx, val in enumerate(split[1]):
		tmp[0].append(int(val))
	row_features = np.asarray(tmp)
	try:
		features
	except NameError:
	#add a line of all zeros to define the matrix feature, so remove the first line later
		features = np.zeros((1, idx + 1), dtype = int)
	try:
		features = np.concatenate((features, row_features))
	except ValueError:
		print features.shape
		print row_features.shape
features = features[1:,:]
train_features = features[:train_num, :]
test_features = features[train_num:, :]
print "The shape of train features is ", train_features.shape
print "The shape of test features is ", test_features.shape
np.save(train_features_path, train_features)
np.save(test_features_path, test_features)
# processing labels
for line in inf2:
	line = line. strip('\n')
	split = line.split('\t')
	try:
		labels
	except NameError:
		labels = np.zeros((1, 1), dtype = int)
	labels = np.concatenate((labels, np.array([[int(split[1])]])))
#convert to one-hot format with 2 columns, say 2 classes---need revision
y = labels[1:,:]
labels = np.zeros((y.shape[0],2),dtype = int)
for i in xrange(y.shape[0]):
	labels[i,y[i]] = 1
train_labels = labels[:train_num, :]
test_labels = labels[train_num:, :]
print "The shape of train labels is ", train_labels.shape
print "The shape of test labels is ", test_labels.shape
np.save(train_labels_path, train_labels)
np.save(test_labels_path, test_labels)

