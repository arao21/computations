#This function takes in a rotation matrix and sets it up to solve the ODEs
def rot_matrixODE(R,t3):
    s3 = math.sin(t3)
    c3 = math.cos(t3)
    
    w_ad = np.array([R1[0,0],s3,0,R1[0,1],c3,0,R1[0,2],0,1])
    w_ad = w_ad.reshape(3,3)
    
    return Matrix(w_ad)