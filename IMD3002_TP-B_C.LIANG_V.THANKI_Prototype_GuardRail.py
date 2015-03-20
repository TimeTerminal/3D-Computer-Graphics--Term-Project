import maya.cmds as cmds
import random

cmds.file (force = True, new = True)

railingHeight = 10.0
railingWidth = railingHeight / 2

testMesh = "wavyMesh"

for i in range (0, 5):
    #Railing
    board = cmds.polyPlane (w = railingWidth, h = railingHeight, sx = 20, sy = 3, n = testMesh)[0]
    
    cmds.nonLinear (type = "sine", amplitude = 0.05)
    cmds.setAttr ('sine1.wavelength', 0.2)
    cmds.setAttr ('sine1Handle.rotateY', 180)
    cmds.setAttr ('sine1Handle.rotateZ', 90)
    cmds.delete (testMesh, ch = True)
    
    cmds.select (testMesh)
    cmds.rotate (0.0, 0.0, 90.0, r = True)
    cmds.move (0.0, railingWidth / 2.0, 0.5, a = True)
    
    #Connector
    connectorDim = railingHeight / 10.0
    
    connector = cmds.polyCube (w = connectorDim * 1.5, h = connectorDim * 2, d = connectorDim)[0]
    cmds.move (connectorDim , railingWidth * 0.75, -railingHeight * 0.33, a = True)
    
    #Leg
    legDim = railingHeight / 10
    
    leg = cmds.polyCube (w = legDim, h = railingHeight / 1.5, d = legDim)[0]
    cmds.move (railingHeight / 6, railingWidth / 3, -railingHeight * 0.33, a = True)
    
    
    cmds.polyUnite (board, connector, leg, n = 'railing')
    cmds.delete (ch = True) 
    cmds.move (0, 0, railingHeight * i, a = True)