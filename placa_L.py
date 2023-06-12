# Python script to generate a finite element model using Abaqus CAE
# Problem: plate (L shape) with sharp corner (1) and round (2)
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
    ('Length:\tPlate length (mm)', '100'),
    ('Height:\tPlate height (mm)', '25'),
    ('Thickness:\tPlate thickness (mm)', '1'),
    ('Round:\tradius (mm)', '7.5'),
    ('P:\tInternal pressure (MPa)', '1'),
    ('Global mesh size:\tMesh size (mm)', '25'),
    ('Number of elements:\tcorner region', '1'),
),
    label='Please specify the parameters:',  # Question
    dialogTitle='L-Plate',  # Main title
)
# Then, assign scalar variables
plate_l    = float(Parameters[0])
plate_h    = float(Parameters[1])
plate_t    = float(Parameters[2])
plate_r    = float(Parameters[3])
plate_pres = float(Parameters[4])
mesh_size  = float(Parameters[5])
e_corner   = int(Parameters[6])
# -------------------------------------------------------------------------
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    plate_l, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(plate_l, 0.0), point2=
    (plate_l, plate_h))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(plate_l, plate_h), 
    point2=(plate_h, plate_h))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(plate_h, plate_h), point2=
    (plate_h, plate_l))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(plate_h, plate_l), 
    point2=(0.0, plate_l))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, plate_l), point2=
    (0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=TRI, regions=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), ))
mdb.models['Model-1'].parts['Part-1'].PartitionEdgeByParam(edges=
    mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#10 ]', 
    ), ), parameter=0.1)
mdb.models['Model-1'].parts['Part-1'].PartitionEdgeByParam(edges=
    mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#8 ]', 
    ), ), parameter=0.9)
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['Part-1'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#30 ]', 
    ), ), number=e_corner)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((200000.0, 0.3), 
    ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=plate_t)
mdb.models['Model-1'].parts['Part-1'].Set(faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-4')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-4'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    ('[#1 ]', ), ), name='Set-1')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=0.0, 
    u2=0.0, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Surface(name='Surf-1', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    ('[#8 ]', ), ))
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, field='', magnitude=plate_pres, name='Load-1', region=
    mdb.models['Model-1'].rootAssembly.surfaces['Surf-1'])
mdb.Model(modelType=STANDARD_EXPLICIT, name='Model-2')
mdb.models['Model-2'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-2'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    plate_l, 0.0))
mdb.models['Model-2'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-2'].sketches['__profile__'].geometry[2])
mdb.models['Model-2'].sketches['__profile__'].Line(point1=(plate_l, 0.0), point2=
    (plate_l, plate_h))
mdb.models['Model-2'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-2'].sketches['__profile__'].geometry[3])
mdb.models['Model-2'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-2'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-2'].sketches['__profile__'].geometry[3])
mdb.models['Model-2'].sketches['__profile__'].Line(point1=(plate_l, plate_h), 
    point2=(plate_h, plate_h))
mdb.models['Model-2'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-2'].sketches['__profile__'].geometry[4])
mdb.models['Model-2'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-2'].sketches['__profile__'].geometry[3], entity2=
    mdb.models['Model-2'].sketches['__profile__'].geometry[4])
mdb.models['Model-2'].sketches['__profile__'].Line(point1=(plate_h, plate_h), point2=
    (plate_h, plate_l))
mdb.models['Model-2'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-2'].sketches['__profile__'].geometry[5])
mdb.models['Model-2'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-2'].sketches['__profile__'].geometry[4], entity2=
    mdb.models['Model-2'].sketches['__profile__'].geometry[5])
mdb.models['Model-2'].sketches['__profile__'].Line(point1=(plate_h, plate_l), 
    point2=(0.0, plate_l))
mdb.models['Model-2'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-2'].sketches['__profile__'].geometry[6])
mdb.models['Model-2'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-2'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['Model-2'].sketches['__profile__'].geometry[6])
mdb.models['Model-2'].sketches['__profile__'].Line(point1=(0.0, plate_l), point2=
    (0.0, 0.0))
mdb.models['Model-2'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-2'].sketches['__profile__'].geometry[7])
mdb.models['Model-2'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-2'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['Model-2'].sketches['__profile__'].geometry[7])
mdb.models['Model-2'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-2'].sketches['__profile__'].geometry[4], curve2=
    mdb.models['Model-2'].sketches['__profile__'].geometry[5], nearPoint1=(
    40.348503112793, 25.4705848693848), nearPoint2=(24.725944519043, 
    33.5882301330566), radius=plate_r)
mdb.models['Model-2'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-2'].parts['Part-1'].BaseShell(sketch=
    mdb.models['Model-2'].sketches['__profile__'])
del mdb.models['Model-2'].sketches['__profile__']
mdb.models['Model-2'].parts['Part-1'].setMeshControls(elemShape=TRI, regions=
    mdb.models['Model-2'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ))
mdb.models['Model-2'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-2'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), ))
mdb.models['Model-2'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-2'].parts['Part-1'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-2'].parts['Part-1'].edges.getSequenceFromMask(('[#10 ]', 
    ), ), number=e_corner)
mdb.models['Model-2'].parts['Part-1'].generateMesh()
mdb.models['Model-2'].Material(name='Material-1')
mdb.models['Model-2'].materials['Material-1'].Elastic(table=((200000.0, 0.3), 
    ))
mdb.models['Model-2'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=plate_t)
mdb.models['Model-2'].parts['Part-1'].Set(faces=
    mdb.models['Model-2'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-4')
mdb.models['Model-2'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-2'].parts['Part-1'].sets['Set-4'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-2'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-2'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-2'].parts['Part-1'])
mdb.models['Model-2'].StaticStep(name='Step-1', previous='Initial')
mdb.models['Model-2'].rootAssembly.Set(edges=
    mdb.models['Model-2'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    ('[#1 ]', ), ), name='Set-1')
mdb.models['Model-2'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-1', region=mdb.models['Model-2'].rootAssembly.sets['Set-1'], u1=0.0, 
    u2=0.0, ur3=UNSET)
mdb.models['Model-2'].rootAssembly.Surface(name='Surf-1', side1Edges=
    mdb.models['Model-2'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    ('[#8 ]', ), ))
mdb.models['Model-2'].Pressure(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, field='', magnitude=plate_pres, name='Load-1', region=
    mdb.models['Model-2'].rootAssembly.surfaces['Surf-1'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, name=
    'Job-1', nodalOutputPrecision=SINGLE, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-2', modelPrint=OFF, name=
    'Job-2', nodalOutputPrecision=SINGLE, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)




