# we are importing the plotBeamDiagram, newEulerBeam method for drawing our beam #model
import planesections as ps

# Define node locations, and support conditions
L = 25 # beam length in meters
#lets instaniate or create a beam object using newEulerBeam2D #function passing the length of the beam 
# as an argument
beam = ps.newSimpleEulerBeam(L)# we are importing the planeSections library

# Define beam with support conditions or fixities
# key for support conditions or fixities  = {'free':[0,0,0], 'roller': [0,1,0], 'pinned':[1,1,0], 'fixed':[1,1,1]}


pinned = [1,1,0] # support condition
roller = [0,1,0] # support condition

# we invoke the setFixity method and pass the position of our beam # support as the first argument and #the support type as the second argument
beam.setFixity(0, pinned) # type: ignore
beam.setFixity(L*0.8, roller) # type: ignore

# Define point Loads and labels
Pz = -1000  # This represent 1kN in the downward direction
# we use the addLabel method of the beam object and the first argument specifies the distance from #starting length of our beam to #place our label and the label name as the second argument
beam.addLabel(0, label='A') 
beam.addLabel(10, label='E') 
beam.addLabel(20, label='B') 

# addVerticalload method defines a point load where the first argument is the position of the load, the argument is the load #magntude and the third argument I the label indicating the load 
#position on the beam

beam.addVerticalLoad(15, 2*Pz, label = 'D')

beam.addVerticalLoad(25, 3*Pz, label = 'C')



# Define distributed Loads
# the first argument is the point where the distributed load starts #and the second argument is where it #stops and the third argument is its magnitude

beam.addDistLoadVertical(0, L*0.4, 5*Pz)

# drawing of the beam diagram using the plot plotBeamDiagram method #and our beam object as an argument
ps.plotBeamDiagram(beam)

# instantiate the analysis object
analysis = ps.OpenSeesAnalyzer2D(beam)
# Run the analysis
analysis.runAnalysis()


# Plot the ShearForce and Bending Moment Diagram
ps.plotShear(beam, scale = 0.0002, yunit = 'kN') 
ps.plotMoment(beam, scale = 0.0002, yunit = 'kNm')

ps.plotRotation(beam, scale = 1000)
ps.plotDisp(beam)
