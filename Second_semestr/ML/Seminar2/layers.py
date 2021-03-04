import numpy as np

class Linear:
    def __init__(self, input_size, output_size):
        '''
        Creates weights and biases for linear layer.
        Dimention of inputs is *input_size*, of output: *output_size*.
        '''
        self.W = np.random.randn(input_size, output_size) * 0.01
        self.b = np.zeros(output_size)        
    
    def forward(self, X):
        '''
        Passes objects through this layer.
        X is np.array of size (N, input_size).
        Returns output of size (N, output_size).
        Hint: You may need to store X for backward pass
        '''
        self.X = X
        
        return X @ self.W + self.b
    
    def backward(self, dLdy):
        '''
        1. Compute dLdw and dLdx.
        2. Store dLdw for step() call
        3. Return dLdx
        '''

        self.dLdW = self.X.T @ dLdy
        self.dLdb = dLdy.sum(axis=0)
        dLdx = dLdy @ self.W.T
        return dLdx
    
    def step(self, learning_rate):
        '''
        1. Apply gradient dLdw to network:
        w <- w - l*dLdw
        '''
        
        self.W -= learning_rate * self.dLdW
        self.b -= learning_rate * self.dLdb

class Sigmoid:
    def __init__(self):
        pass
    
    def forward(self, X):
        '''
        Passes objects through this layer.
        X is np.array of size (N, d)
        '''
        #### YOUR CODE HERE
        #### Apply layer to input
        self.Y = 1 / (1 + np.exp(-X))
        return self.Y
    
    def backward(self, dLdy):
        '''
        1. Compute dLdx.
        2. Return dLdx
        '''
        #y = sigm(x)
        dLdX = dLdy * (1 - self.Y) * self.Y
        return dLdX
    
    def step(self, learning_rate):
        pass

class Relu:
    def __init__(self):
        pass
    
    def forward(self, X):
        '''
        Passes objects through this layer.
        X is np.array of size (N, d)
        '''
        #### YOUR CODE HERE
        #### Apply layer to input
        self.negative_mask = X < 0
        X[self.negative_mask] = 0
        self.X = X
        return X
    
    def backward(self, dLdy):
        '''
        1. Compute dLdx.
        2. Return dLdx
        '''
        #y = sigm(x)
        self.X[~self.negative_mask] = 1
        dLdX = dLdy * self.X
        return dLdX
    
    def step(self, learning_rate):
        pass

class Elu:
    def __init__(self):
        pass
    
    def forward(self, X):
        '''
        Passes objects through this layer.
        X is np.array of size (N, d)
        '''
        #### YOUR CODE HERE
        #### Apply layer to input
        self.negative_mask = X < 0
        X[self.negative_mask] = np.exp(X[self.negative_mask]) - 1
        self.X = X
        return X
    
    def backward(self, dLdy):
        '''
        1. Compute dLdx.
        2. Return dLdx
        '''
        #y = sigm(x)
        self.X[self.negative_mask] += 1
        self.X[~self.negative_mask] = 1
        dLdX = dLdy * self.X
        return dLdX
    
    def step(self, learning_rate):
        pass
        
class Tanh:
    def __init__(self):
        pass
    
    def forward(self, X):
        '''
        Passes objects through this layer.
        X is np.array of size (N, d)
        '''
        #### YOUR CODE HERE
        #### Apply layer to input
        self.X = 2 / (1 + np.exp(-2 * X)) - 1
        return X
    
    def backward(self, dLdy):
        '''
        1. Compute dLdx.
        2. Return dLdx
        '''
        dLdX = dLdy * (1 - self.X**2)
        return dLdX
    
    def step(self, learning_rate):
        pass

class NLLLoss:
    def __init__(self):
        '''
        Applies Softmax operation to inputs and computes NLL loss
        '''
        #### YOUR CODE HERE
        #### (Hint: No code is expected here, just joking) - ору
        pass
    
    def forward(self, X, y):
        '''
        Passes objects through this layer.
        X is np.array of size (N, C), where C is the number of classes
        y is np.array of size (N), contains correct labels
        '''
        #### YOUR CODE HERE
        #### Apply layer to input
        
        self.loss = np.zeros(X.shape)
        self.X = X
        for i, c in enumerate(y):
            self.loss[i, c] = np.log(np.sum(np.exp(X[i]))) - X[i, c]
        
        return self.loss.sum()
    
    def backward(self):
        '''
        Note that here dLdy = 1 since L = y
        1. Compute dLdx
        2. Return dLdx
        '''
        mask = self.loss != 0
        dLdX = np.exp(self.X) / np.sum(np.exp(self.X), axis=1).reshape(-1, 1)
        dLdX[mask] -= 1
        return dLdX

class NeuralNetwork:
    def __init__(self, modules, loss):
        '''
        Constructs network with *modules* as its layers
        '''
        self.modules = modules
        self.loss = loss
        self.log_error = []
    
    def forward(self, X):
        #### YOUR CODE HERE
        #### Apply layers to input
        res = self.modules[0].forward(X)
        for layer in self.modules[1:]:
            res = layer.forward(res)
        
        return res
        
    def backward(self, dLdy):
        '''
        dLdy here is a gradient from loss function
        '''
        #### YOUR CODE HERE
        dLdy = self.modules[-1].backward(dLdy)
        for layer in self.modules[-2::-1]:
            dLdy = layer.backward(dLdy)
        
        return dLdy
    
    def step(self, learning_rate):
        for layer in self.modules:
            if hasattr(layer, 'W'):
                layer.W -= learning_rate * layer.dLdW
                layer.b -= learning_rate * layer.dLdb
    
    def train(self, X, y, epoch=100, learning_rate=0.005, save_prev_log=False):
        if not save_prev_log:
            self.log_error = []
            
        for i in range(epoch):
            res = self.forward(X)
            self.log_error.append(self.loss.forward(res, y))
            self.backward(self.loss.backward())
            self.step(learning_rate)

