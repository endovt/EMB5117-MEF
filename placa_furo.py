# Python script to generate a finite element model using Abaqus CAE
# Problem: plate with circular hole subject to internal pressure
# -------------------------------------------------------------------------
# import abaqus commands
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
# -------------------------------------------------------------------------
# Prompt user regarding the variables
# Initially, store the variables in an array (Parameters)
Parameters = getInputs(fields=(
    ('Half-length:\tPlate half-length (mm)', '10'),
    ('Thickness:\tPlate thickness (mm)', '1'),
    ('Radius:\tHole radius (mm)', '7'),
    ('E:\tElastic modulus (MPa)', '1e7'),
    ('P:\tInternal pressure (MPa)', '1'),
    ('Mesh size:\tMesh size (mm)', '1'),
),
    label='Please specify the parameters:',  # Question
    dialogTitle='Plate with circular hole',  # Main title
)
# Then, assign scalar variables
plate_hl   = float(Parameters[0])
plate_t    = float(Parameters[1])
hole_r     = float(Parameters[2])
mat_e      = float(Parameters[3])
plate_pres = float(Parameters[4])
mesh_size  = float(Parameters[5])
# -------------------------------------------------------------------------
# commands from journal file
# -------------------------------------------------------------------------
# Part, geometry
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(
    0.0, 0.0), direction=CLOCKWISE, point1=(0.0, hole_r), point2=(hole_r, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(hole_r, 0.0), point2=(
    plate_hl, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(plate_hl, 0.0), point2=(
    plate_hl, plate_hl))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(
    addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[3], entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].Line(
    point1=(plate_hl, plate_hl), point2=(0.0, plate_hl))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[4], entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, plate_hl), point2=(
    0.0, hole_r))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(
    addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[5], entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR,
                           name='Part-1', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseShell(
    sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
# -------------------------------------------------------------------------
# Part, mesh
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=TRI, regions=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]',
                                                                                                                                              ), ))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1,
                                               minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6,
                                                    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]',
                                                                     ), ), ))
mdb.models['Model-1'].parts['Part-1'].generateMesh()
# -------------------------------------------------------------------------
# Material
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((mat_e, 0.3), ))
# -------------------------------------------------------------------------
# Section
mdb.models['Model-1'].HomogeneousSolidSection(
    material='Material-1', name='Section-1', thickness=plate_t)
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0,
                                                        offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
                                                            faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(
                                                                mask=('[#1 ]', ), )), sectionName='Section-1', thicknessAssignment=FROM_SECTION)
# -------------------------------------------------------------------------
# Assembly
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1',
                                            part=mdb.models['Model-1'].parts['Part-1'])
# -------------------------------------------------------------------------
# Step
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
# -------------------------------------------------------------------------
# Boundary Condition
mdb.models['Model-1'].XsymmBC(createStepName='Step-1', localCsys=None, name='BC-1', region=Region(
    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
        mask=('[#1 ]', ), )))
mdb.models['Model-1'].YsymmBC(createStepName='Step-1', localCsys=None, name='BC-2', region=Region(
    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
        mask=('[#4 ]', ), )))
# -------------------------------------------------------------------------
# Pressure
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Step-1',
                               distributionType=UNIFORM, field='', magnitude=plate_pres, name='Load-1', region=Region(
                                   side1Edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
                                       mask=('[#2 ]', ), )))
# -------------------------------------------------------------------------
# Job
# -------------------------------------------------------------------------
# mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
# atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
# memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
# explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
# modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
# scratch='', resultsFormat=ODB)
# mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
# session.mdbData.summary()
# o3 = session.openOdb(name='C:/temp/Job-1.odb')
# session.viewports['Viewport: 1'].setValues(displayedObject=o3)
# session.viewports['Viewport: 1'].makeCurrent()
# session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
# CONTOURS_ON_DEF, ))
# session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
# mirrorAboutXzPlane=True, mirrorAboutYzPlane=True)



