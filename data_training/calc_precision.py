import numpy as np
label_filename = "test_labels.npy"
output_filename = "output.txt"

TN, TP, FN, FP = 0.0, 0.0, 0.0, 0.0

np_label = np.load(open(label_filename, 'rb'))
label = [x[1] for x in np_label]

one = [i for i in label if i == 1]
zero = [i for i in label if i == 0]

output = np.loadtxt(output_filename, dtype = 'int')
for i, tmp in enumerate(label):
    print(output[i], tmp)
    if output[i] == 0 and tmp == 0:
        TN += 1
    if output[i] == 1 and tmp == 1:
        TP += 1
    if output[i] == 0 and tmp == 1:
        FN += 1
    if output[i] == 1 and tmp == 0:
        FP +=1

print("The accuracy is", (TP + TN) / (TN + TP + FN + FP))
print("The precision is", (TP) / (TP + FP))
print("The recall is", (TP) / (TP + FN))
print("The True Positive is", TP)
print("The False Negative is", FN)
print("The Natual Percentage is", float(len(one))/float(len(zero) + len(one)))
