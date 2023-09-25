# DEPENDENCIES 
import numpy #Numpy for working with arrays

import reactions_pl
import reactions_pm
import reactions_udl
import shear_moment_pl
import shear_moment_pm
import shear_force_diagram
import shear_moment_udl
import bending_moment_diagram

# NO NOT EDIT - Initialize containers (override below where req'd)
pointLoads = numpy.array([[]]) #Point forces [location, xMag, yMag]
pointMoments = numpy.array([[]]) #Point moments [location, Mag]
distribuitedLoads = numpy.array([[]]) #Distribuited loads [xInit, xEnd, Mag]

# ANALYSIS PARAMETERS
span = 17 #Span of beam
A = 3  #Distance to left support
B = 13 #Distance to right support

# FORCE DATA
pointLoads = numpy.array([[6,0,-90]])
pointMoments = numpy.array([[17,50]])
distribuitedLoads = numpy.array([[8,17,-10]])

# COORDINATE SYSTEM
divs = 10000 # Divide span up into this number of data points
delta = span/divs # Distance between data points
X = numpy.arange(0, span+delta, delta) # Range of X-coordinates

# TESTING
nPL = len(pointLoads[0]) # Test for point loads to consider
nPm = len(pointMoments[0]) # Test for point moments to consider
nUDL = len(distribuitedLoads[0]) # Test for uniformly distribuited loads

#INITIALIZE DATA CONTAINERS
reactions = numpy.array([0.0,0,0]) #Reactions (Va, Ha, Vb) - Defined as array of floats to hold reactions
shearForce = numpy.empty([0,len(X)]) #Shear forces at each data point
bendingMoment = numpy.empty([0, len(X)]) #Bending moment at each data point

# REACTION CALCULATION
PL_record = numpy.empty([0,3])
for n, p in enumerate(pointLoads):    
    va, vb, ha = reactions_pl.exec(n, pointLoads, A, B) #Calculate reactions
    PL_record = numpy.append(PL_record, [numpy.array([va, ha, vb])], axis=0) #Store reactions for each point load
 
    #Add reactions to record (superposition)
    reactions[0] = reactions[0] + va 
    reactions[1] = reactions[1] + ha
    reactions[2] = reactions[2] + vb

PM_record = numpy.empty([0,2])
for n, p in enumerate(pointMoments):    
    va, vb = reactions_pm.exec(n, pointMoments, A, B) #Calculate reactions
    PM_record = numpy.append(PM_record, [numpy.array([va, vb])], axis=0) #Store reactions for each moment load
 
    #Add reactions to record (superposition)
    reactions[0] = reactions[0] + va 
    reactions[2] = reactions[2] + vb

UDL_record = numpy.empty([0,2])
for n, p in enumerate(distribuitedLoads):    
    va, vb = reactions_udl.exec(n, distribuitedLoads, A, B) #Calculate reactions
    UDL_record = numpy.append(UDL_record, [numpy.array([va, vb])], axis=0) #Store reactions for each UDL
 
    #Add reactions to record (superposition)
    reactions[0] = reactions[0] + va 
    reactions[2] = reactions[2] + vb

# SHEAR AND MOMENT CALCULATION
# Cycle through all point loads and determine shear and moment
for n, p in enumerate(pointLoads):
    Shear, Moment = shear_moment_pl.exec(n, pointLoads, X, A, B, PL_record)
    # Store shear force record for each point load
    shearForce = numpy.append(shearForce, [Shear], axis=0)
    # Store bending moment record for each point load
    bendingMoment = numpy.append(bendingMoment, [Moment], axis=0)

# Cycle through all point moments and determine shear and moment
for n, p in enumerate(pointMoments):
    Shear, Moment = shear_moment_pm.exec(n, pointMoments, X, A, B, PM_record)
    # Store shear force record for each point load
    shearForce = numpy.append(shearForce, [Shear], axis=0)
    # Store bending moment record for each point load
    bendingMoment = numpy.append(bendingMoment, [Moment], axis=0)

# Cycle through all UDL's and determine shear and moment
for n, p in enumerate(distribuitedLoads):
    Shear, Moment = shear_moment_udl.exec(n, distribuitedLoads, X, A, B, UDL_record)
    # Store shear force record for each point load
    shearForce = numpy.append(shearForce, [Shear], axis=0)
    # Store bending moment record for each point load
    bendingMoment = numpy.append(bendingMoment, [Moment], axis=0)

print(round(reactions[0], 2))
print(round(reactions[1], 2))
print(round(reactions[2], 2))

shear_force_diagram.gen(X, shearForce, span)
bending_moment_diagram.gen(X, bendingMoment, span)