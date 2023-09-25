import numpy

# Calculate shear forces and bending moments due to point loads
def exec(n:int,point_loads, X, A, B, pl_record):    
    xp = point_loads[n,0] #Location of point load
    fy = point_loads[n,2] #Point load vertical component magnitude 
    Va = pl_record[n,0]  #Vertical reaction at A for this point load
    Vb = pl_record[n,2]  #Vertical reaction at B for this point load
    
    #Cycle through the structure and calculate the shear force and bending moment at each point
    Shear = numpy.zeros(len(X))  #Initialize a container to hold all shear force data for this point load
    Moment = numpy.zeros(len(X)) #Initialize a container to hold all moment force data for this point load
    for i, x in enumerate(X):    
        shear = 0  #Initialize the shear force for this data point
        moment = 0 #Initialize the bending moment for this data point
 
        if x > A:
            #Calculate shear and moment from reaction at A
            shear = shear + Va
            moment = moment - Va*(x-A)
 
        if x > B:
            #Calculate shear and moment from reaction at B
            shear = shear + Vb
            moment = moment - Vb*(x-B)
 
        if x > xp:
            #Calculate shear and moment from point load
            shear = shear + fy
            moment = moment - fy*(x-xp)
 
        #Store shear and moment for this location
        Shear[i] = shear
        Moment[i] = moment
 
    return Shear, Moment