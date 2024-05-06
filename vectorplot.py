import matplotlib.pyplot as plt
import numpy as np

def vectorplot(vectors):
    """_summary_
    Makes a 2d or 3d graph of a list of vectors with alternating colors.
    Args:
        vectors (np array): a np array of 2d or 3d vectors.
    """
    dimensions = len(vectors[1])
    scaler = max(np.ravel(vectors))
    
    origin = np.array([[0 for x in range(len(vectors))]]*dimensions) # origin point
    colors = ['k', 'r', 'b', 'g', 'c', 'm', 'y']
    vector_colors = []
    for i in range(len(vectors)):
        index = i - ((i // len(colors)) * i)
        vector_colors.append(colors[index])
        
    print(vector_colors)
    if dimensions == 2:
        
        plt.quiver(*origin, vectors[:,0], vectors[:,1], colors = vector_colors, scale = scaler * 2)
    
    
    
    if dimensions == 3:
        fig = plt.figure()
        
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(*origin, vectors[:, 0], vectors[:, 1], vectors[:, 2], colors = vector_colors)
        ax.set_xlim([-scaler, scaler])
        ax.set_ylim([-scaler, scaler])
        ax.set_zlim([-scaler, scaler])
        
        
    plt.show()
        