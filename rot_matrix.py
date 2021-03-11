#This function takes in the body XYZ angles and converts them into one rotation matrix R
def rot_matrix(t1, t2, t3):
    c1 = math.cos(t1)
    c2 = math.cos(t2)
    c3 = math.cos(t3)

    s1 = math.sin(t1)
    s2 = math.sin(t2)
    s3 = math.sin(t3)
    
    #matrix for first rotation along the x-axis
    x=np.array([1, 0, 0, 0, c1, -s1, 0, s1, c1])
    x=x.reshape(3,3)
    
    #matrix for second rotation along the y-axis
    y=np.array([c2, 0, s2, 0, 1, 0, -s2, 0, c2])
    y=y.reshape(3,3)

    #matrix for third rotation along the z-axis
    z=np.array([c3, -s3, 0, s3, c3, 0, 0, 0, 1])
    z=z.reshape(3,3)
    
    #multiplying the three individual rotation matrices 
    R=np.matmul(np.matmul(x,y), z)
    return R