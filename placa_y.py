# -*- coding: mbcs -*-
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
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 35.0), point2=(
    -10.0, 35.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-10.0, 35.0), 
    point2=(-10.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-10.0, 20.0), 
    point2=(-20.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-20.0, 10.0), 
    point2=(-20.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-20.0, 0.0), point2=
    (-10.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-10.0, 0.0), point2=
    (-10.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-10.0, 10.0), 
    point2=(0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 10.0), point2=(
    0.0, 35.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 27.5), point1=(0.0, 31.25))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], radius=3.75, 
    textPoint=(8.81545639038086, 32.2643814086914))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], point1=(
    2.44388580322266, 30.1428909301758))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], point1=(
    -0.0872840881347656, 29.9660949707031))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], nearPoint1=(
    -6.54613494873047, 35.0930404663086), nearPoint2=(-10.0374088287354, 
    30.9384460449219), radius=5.0)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], nearPoint1=(
    -10.1246891021729, 21.3917274475098), nearPoint2=(-11.2593517303467, 
    18.739860534668), radius=5.0)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], nearPoint1=(
    -17.281795501709, 12.4637718200684), nearPoint2=(-20.0748119354248, 
    6.36447906494141), radius=5.0)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], nearPoint1=(
    -10.3865337371826, 5.92250442504883), nearPoint2=(-6.63341903686523, 
    10.1654891967773), radius=5.0)
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=4.0)
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=TRI, regions=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), ))
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((70000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=4.0)
mdb.models['Model-1'].parts['Part-1'].Set(faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-3')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-3'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].InterestingPoint(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges[13], 
    CENTER))
mdb.models['Model-1'].rootAssembly.Set(name='m_Set-1', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[4], ))
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    ('[#2000 ]', ), ), name='s_Set-1')
mdb.models['Model-1'].Coupling(alpha=0.0, controlPoint=
    mdb.models['Model-1'].rootAssembly.sets['m_Set-1'], couplingType=KINEMATIC, 
    influenceRadius=WHOLE_SURFACE, localCsys=None, name='Constraint-1', 
    surface=mdb.models['Model-1'].rootAssembly.sets['s_Set-1'], u1=ON, u2=ON, 
    ur3=ON)
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    ('[#100 ]', ), ), name='Set-3')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=UNSET, 
    u2=0.0, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    ('[#1001 ]', ), ), name='Set-4', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[4], ))
mdb.models['Model-1'].XsymmBC(createStepName='Step-1', localCsys=None, name=
    'BC-2', region=mdb.models['Model-1'].rootAssembly.sets['Set-4'])
mdb.models['Model-1'].rootAssembly.Set(name='Set-5', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[4], ))
mdb.models['Model-1'].ConcentratedForce(cf2=50.0, createStepName='Step-1', 
    distributionType=UNIFORM, field='', localCsys=None, name='Load-1', region=
    mdb.models['Model-1'].rootAssembly.sets['Set-5'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, name=
    'Job-1', nodalOutputPrecision=SINGLE, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
