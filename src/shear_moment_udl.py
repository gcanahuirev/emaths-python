import numpy

# Calculate shear forces and bending moments due to uniformly distribuited loads
def exec(n:int,distriubited_loads, X, A, B, udl_record):    
    xStart = distriubited_loads[n,0]
    xEnd = distriubited_loads[n,1]
    fy = distriubited_loads[n,2]
    Va = udl_record[n,0]
    Vb = udl_record[n,1]
    
    #Cycle through the structure and calculate the shear force and bending moment at each point
    Shear = numpy.zeros(len(X))  #Initialize a container to hold all shear force data for this UDL
    Moment = numpy.zeros(len(X)) #Initialize a container to hold all moment force data for this UDL
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
 
        if x > xStart and x <= xEnd:
            #Calculate shear and moment from point load
            shear = shear + fy*(x-xStart)
            moment = moment - fy*(x-xStart)*0.5*(x-xStart)
        elif(x>xEnd):
            shear = shear + fy*(xEnd-xStart)
            moment = moment - fy*(xEnd-xStart)*(x-xStart-0.5*(xEnd-xStart))
 
        #Store shear and moment for this location
        Shear[i] = shear
        Moment[i] = moment
 
    return Shear, Moment