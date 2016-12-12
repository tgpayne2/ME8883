import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np
import pymks
from pymks.tools import draw_microstructures
from pymks.stats import correlate
from pymks import PrimitiveBasis
from pymks.tools import draw_correlations
import os as os
import scipy.sparse.linalg as sparse
import PIL
from resizeimage import resizeimage

os.chdir("C:/Users/Thomas/Documents/Mat_Informatics/segmented_png")
stats_1d=()
num_datasets=0
for filename in os.listdir("C:/Users/Thomas/Documents/Mat_Informatics/segmented_png"):
    num_datasets=num_datasets+1
    #tmp=mping.imread("C:/Users/tpayne33/Documents/MatInformatics/segmented_png/binary.png")
    tmp=mping.imread(filename)
    tmp_to_crop=PIL.Image.fromarray(tmp)
    tmp_cropped=resizeimage.resize_crop(tmp_to_crop,[10,10])
    tmp=np.asarray(tmp_cropped)
    
    X_binary = tmp[None, ...]

    
    prim_basis = PrimitiveBasis(n_states=2)

    X_corr = correlate(X_binary, prim_basis, periodic_axes=(0,1))
    #print X_corr
    #print("Shape of X_corr")
    #print(X_corr.shape)
    
    flat=X_corr.flatten(order='C')
    stats_1d_temp=(flat,)
    stats_1d=stats_1d+stats_1d_temp
    print stats_1d
    



"""
    for x in X_corr:
        draw_correlations(x, correlations=[(1, 1), (2, 2), (1, 2)])
        file_path="C:/Users/tpayne33/Documents/MatInformatics/2point/"+filename
        plt.savefig(file_path)
        x_center = (X_corr.shape[1] + 1) / 2
        y_center = (X_corr.shape[2] + 1) / 2
        #print('Volume fraction of black phase')
        #print(x[x_center, y_center, 0])
        #print('Volume fraction of white phase')
        #print(x[x_center, y_center, 1])
"""
"""
stacked=np.vstack(stats_1d)
mean=np.mean(stacked,axis=0)
to_sub=np.repeat(mean[np.newaxis,:],num_datasets,0)
full_matrix=stacked-to_sub

U,S,V=np.linalg.svd(full_matrix)
#U,S,V=sparse.svds(full_matrix)
U=U[:,0]
#print U
#print S

alphas=np.dot(U,S)
basis=np.transpose(V)

print alphas
#print basis
"""

  