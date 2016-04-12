# Example.py
# Very brief description of the file
#
# Date: dd.mm.yyyy
# Author: Name LastName
# Copyright: 2016, Name LastName

import numpy as np

def homogeneous_transform(rotation_matrix, translation_matrix):
    # This function returns a homogeneous transform built
    # from an input rotation and a translation matrices

    # Result is a 4x4 matrix, with the last row [0, 0, 0, 1]
    T = np.vstack((np.hstack((rotation_matrix,translation_matrix)),
                    np.array([[0,0,0,1]]) # T stores the homogeneous transform

    return T
