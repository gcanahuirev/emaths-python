import numpy

# Calculate shear forces and bending moments due to point moments
def exec(n:int,point_moments, X, A, B, pm_record):
    xm = point_moments[n,0] #Location of point moment
    m = point_moments[n,1] #Point moment vertical component magnitude 
    Va = pm_record[n,0]  #Vertical reaction at A for this point moment
    Vb = pm_record[n,1]  #Vertical reaction at B for this point moment

    #Cycle through the structure and calculate the shear force and bending moment at each point
    Shear = numpy.zeros(len(X))  #Initialize a container to hold all shear force data for this point moment
    Moment = numpy.zeros(len(X)) #Initialize a container to hold all moment force data for this point moment
    for i, x in enumerate(X):    
        shear = 0  #Initialize the shear force for this data point
        moment = 0 #Initialize the bending moment for this data point
 
        if x > A:
            #Calculate shear and moment due reaction at A
            shear = shear + Va
            moment = moment - Va*(x-A)
 
        if x > B:
            #Calculate shear and moment due reaction at B
            shear = shear + Vb
            moment = moment - Vb*(x-B)
 
        if x > xm:
            #Calculate moment influence of point moment (No effect on shear)
            moment = moment - m
 
        #Store shear and moment for this location
        Shear[i] = shear
        Moment[i] = moment
 
    return Shear, Moment