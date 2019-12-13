import argparse
from code.train_test import NEW
import numpy as np
from code.data_processing import DataTools

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', type=str, default='../data/celegans.csv', help='input data path')
parser.add_argument('--save_path', type=str, default='../data/', help='save split data path')
parser.add_argument('--cache', type=bool, default=True, help='Whether there is cached data')
parser.add_argument('--k', type=float, default=2., help='Model parameter k value')
parser.add_argument('--split_number', type=int, default=10, help='Number of data segmentation')
parser.add_argument('--train_ratio', type=float, default=0.9, help='Test sample proportion')
parser.add_argument('--learning_rate', type=float, default=1e-7)
parser.add_argument('--lam', type=float, default=0.9, help='Regularization factor')
parser.add_argument('--epsilon', type=float, default=1e-8, help='training error')

'''
The optimal learning rate and k value of the experiment were obtained after different network partition
netscience [lr=1e-5, k=0.3]
celegans   [lr=1e-7, k=2. ]
ploblogs   [lr=1e-7, k=1. ]
ussocial   [lr=1e-5, k=0.4]
neural     [lr=1e-5, k=0.6]
wiki       [lr=1e-10,k=1.2]
'''

def main(args):

    data_tools = DataTools(args)
    mean_rmse = []
    newModel = NEW(args)
    for i in range(args.split_number):
        X_train, X_test = data_tools.extract_feature(i)
        print("{}'th partition training".format(i+1))
        newModel.training(X_train)
        print("{}'th partition testing".format(i + 1))
        rmse = newModel.predict(X_test)
        print("{}'th test loss {:.6f}\n".format(i+1, rmse))
        mean_rmse.append(rmse)
    print(mean_rmse)
    print("NEW rmse the average results:{:.6f} ".format(np.mean(mean_rmse)))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)

