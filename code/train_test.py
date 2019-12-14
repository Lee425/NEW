import numpy as np

class NEW:
    def __init__(self, args):
        self.args = args
        self.lr = args.learning_rate
        self.lam = args.lam
        self.epsilon = args.epsilon
        self.theta = None

    def computerCost(self, X, y, theta):
        m = y.shape[0]
        C = X.dot(theta) - y
        J_cost = np.sqrt(((C.T.dot(C)) + self.lam * (theta.T.dot(theta))) / (2 * m))
        return J_cost

    def gradientDescent(self, X, y, theta):
        J_history = []
        iter = 0
        error = 0
        lt = []
        while True and iter < 1e6:
            J_cost = self.computerCost(X, y, theta)
            theta = theta * (1 - self.lam * self.lr) - (self.lr * (X.T.dot(X.dot(theta) - y)))
            J_history.append(J_cost)
            if np.abs(J_cost - error) < self.epsilon:
                break
            else:
                error = J_cost
            iter += 1
            lt.append(theta)
            # print("iter count:{}".format(iter), "loss function value:{:.6f}".format(J_cost))
        return J_history, theta, lt

    def training(self, train_x):
        m, n = train_x.shape
        init_theta = np.zeros(n, dtype=np.float)
        bias = np.ones(m, dtype=np.float)
        x = train_x[:, :-1] ** self.args.k
        x = np.column_stack((bias, x))
        w = train_x[:, -1]
        J_history, theta, lt = self.gradientDescent(x, w, init_theta)
        self.theta = theta
        # print("theta:",self.theta)

    def evaluation_index(self, X, y, m):
        C = X.dot(self.theta) - y
        rs = np.sqrt(C.T.dot(C) / m)
        return rs

    def predict(self, test_x):
        m, n = test_x.shape
        x = test_x[:, :-1] ** self.args.k
        true_weight = test_x[:, -1]
        bias = np.ones(m, dtype=np.float)
        x = np.column_stack((bias, x))
        rs = self.evaluation_index(x, true_weight, m)
        return rs

