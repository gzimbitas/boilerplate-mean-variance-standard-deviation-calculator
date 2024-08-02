import numpy as np

def calculate(list):        #defining the function "calculate" with a list input
if len(list) < 9:           #NOTE: the exercise said "below 9 digits"; therefore there will be no error message if the input list is 9 digits OR ABOVE!
        raise ValueError("List must contain nine numbers.") #Error message for below 9 digits 
    
    matrix = np.array(list).reshape(3, 3)     #defining matrix a an numpy 3x3 array
    
    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    }
    #Note: format is of column - row - matrix form. I used .tolist() to convert output to list. 
    return calculations
