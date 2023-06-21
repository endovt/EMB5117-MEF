# Example: Shape function to interpolate the nodal displacement values
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
    ('u_1:\tNode 1: horizontal displacement (mm)', '0'),
    ('v_1:\tNode 1: vertical displacement (mm)', '0'),
    ('u_2:\tNode 2: horizontal displacement (mm)', '2'),
    ('v_2:\tNode 2: vertical displacement (mm)', '0'),
    ('u_3:\tNode 3: horizontal displacement (mm)', '1'),
    ('v_3:\tNode 3: vertical displacement (mm)', '0'),
    ('u_4:\tNode 4: horizontal displacement (mm)', '0'),
    ('v_4:\tNode 4: vertical displacement (mm)', '0'),
),
    label='Please specify the parameters:',  # Question
    dialogTitle='Values of the prescribed displacement problem',  # Main title
)
# Then, assign scalar variables
u_1 = float(Parameters[0])
v_1 = float(Parameters[1])
u_2 = float(Parameters[2])
v_2 = float(Parameters[3])
u_3 = float(Parameters[4])
v_3 = float(Parameters[5])
u_4 = float(Parameters[6])
v_4 = float(Parameters[7])
# -------------------------------------------------------------------------
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-1.0, -1.0), 
    point2=(1.0, 1.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((200000.0, 0.3), 
    ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=1.0)
mdb.models['Model-1'].parts['Part-1'].Set(faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
mdb.models['Model-1'].rootAssembly.Set(name='Set-1', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.getSequenceFromMask(
    ('[#1 ]', ), ))
# -------------------------------------------------------------------------
# Apply boundary condition
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-1-no1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=u_1
    , u2=v_1, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-2', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.getSequenceFromMask(
    ('[#2 ]', ), ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-2-no2', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'], u1=u_2
    , u2=v_2, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-3', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.getSequenceFromMask(
    ('[#4 ]', ), ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-3-no3', region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=u_3
    , u2=v_3, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['BC-2-no2'].setValues(u1=2.0, u2=0.0)
mdb.models['Model-1'].rootAssembly.Set(name='Set-4', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.getSequenceFromMask(
    ('[#8 ]', ), ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-4-no4', region=mdb.models['Model-1'].rootAssembly.sets['Set-4'], u1=u_4
    , u2=v_4, ur3=UNSET)
# -------------------------------------------------------------------------
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=CPS4, elemLibrary=STANDARD), ElemType(elemCode=CPS3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), ))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=2.0)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, name=
    'Job-1', nodalOutputPrecision=SINGLE, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)



