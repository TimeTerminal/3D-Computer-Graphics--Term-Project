import maya.cmds as cmds
import random
import math

cmds.namespace(set=":")

window = cmds.window (title = "Bridge Elements", menuBar = True)

cmds.menu (label = "Basic Options")
cmds.menuItem (label = "New scene", command = ('cmds.file( new = True, force = True)'))
cmds. menuItem (label = "Delete selected", command = ('cmds.delete()'))

cmds.columnLayout ()
cmds.frameLayout (collapsable = True, label = "Standard Block", cl = False)

cmds.columnLayout ()
cmds.intSliderGrp ('Curvature', label="Curvature", field = True, min = 1, max = 180, value = 90)

cmds.colorSliderGrp ('archColor', label = "Color", hsv = (120,1,1))

cmds.columnLayout ()
cmds.button (label = "Create arch", command = ('arch()') )
cmds.setParent ('..')

cmds.setParent ('..')
cmds.setParent ('..')

#Girder and Piles
cmds.frameLayout (collapsable = True, label = "Girder and Pile")
cmds.columnLayout ()

cmds.intSliderGrp ('numGAndP', label = "Number of Girders & Piles", field = True, min = 1, max = 20, value = 3)
#mds.colorSliderGrp ('roundedHoledBlockColour', label = "Colour", hsv = (220, 0.023, 0.514))
cmds.columnLayout ()
cmds.button (label = "Create Girder and Piles", command = ('girderAndPile ()'))
cmds.setParent ('..')

cmds.setParent ('..')
cmds.setParent ('..')

cmds.showWindow(window)

#===================================================#
#                   Functions                       #
#===================================================#

# Function for basic block
def arch():
    ArchCurvature = cmds.intSliderGrp ('Curvature', query = True, value = True)
    
    rgb = cmds.colorSliderGrp ('archColor', query = True, rgbValue = True)
    rnd = random.randrange (0, 1000)
    namespace_tmp = "Piece_" + str (rnd)
    
    cmds.select (clear = True)
    cmds.namespace (add = namespace_tmp)
    cmds.namespace (set = namespace_tmp)
    
   #Create cube
    cmds.polyCube (h = 10.0, w = 2.0, d = 1.0, sy = 10)[0]
    cmds.nonLinear (typ = 'bend' ,  curvature = ArchCurvature)
    
#Function for Girder and Pile
def girderAndPile ():

    numberOfGAndP = cmds.intSliderGrp ('numGAndP', query = True, value = True)
    
    pileHeight = 300
    girderHeight = 100
    girderWidth = 170
    girderDepth = 100
    roadHeight = 35
    roadDepth = 500
    
    rnd = random.randrange (0, 1000)
    namespaceGirder = "Girder" + str (rnd)
    namespacePile = "Pile" + str (rnd)
    
    cmds.select (clear = True)
    cmds.namespace (add = namespaceGirder)
    cmds.namespace (set = namespaceGirder)
    
    #Pile   
    for i in range (numberOfGAndP):
        cmds.polyCube (h = pileHeight, w = girderWidth, d = girderDepth, n = namespacePile)
        cmds.move (0, pileHeight / 2, i * 500, a = True)
        
        #Select me!
        girderSelect = 1
        
        #Girder Type 1
        if girderSelect == 1:
            cmds.polyCube (h = girderHeight, w = girderWidth + 230, d = girderDepth, n = namespaceGirder)
            cmds.move (0, pileHeight + (girderHeight / 2), i * 500, a = True)            
            
        #Girder Type 2
        if girderSelect == 2:
            cmds.polyCube (h = girderHeight, w = girderWidth, d = girderDepth, n = namespaceGirder)
            cmds.move (0, pileHeight + (girderHeight / 2), i * 500, a = True)
            
        #Girder Type 3
        if girderSelect == 3:
            cmds.polyCube (h = girderHeight, w = girderWidth, d = girderDepth, n = namespaceGirder)
            cmds.move (200, namespaceGirder + ':Girder' + str (rnd + i) + '.e[7]', moveX = True, a = True)
            cmds.move (-200, namespaceGirder + ':Girder' + str (rnd + i) + '.e[6]', moveX = True, a = True)
            cmds.move (0, pileHeight + (girderHeight / 2), i * 500, a = True)
        
        #Road
        cmds.polyCube (h = roadHeight, w = girderDepth + 400, d = roadDepth)
        cmds.move (0, girderHeight + pileHeight + (roadHeight / 2), 500 * i, a = True)
