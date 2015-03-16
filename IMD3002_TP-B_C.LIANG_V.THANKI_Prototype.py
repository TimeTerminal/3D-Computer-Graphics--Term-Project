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
    girder1Height = 100
    girder1Width = 170
    girder1Depth = 100
    
    rnd = random.randrange (0, 1000)
    namespace_tmp = "Girder" + str (rnd)
    
    cmds.select (clear = True)
    cmds.namespace (add = namespace_tmp)
    cmds.namespace (set = namespace_tmp)
    
    
    #Pile   
    for i in range (numberOfGAndP):
        cmds.polyCube (h = pileHeight, w = girder1Width, d = girder1Depth)
        cmds.move (0, pileHeight / 2, i * 500, a = True)
        
        #Select me!
        girderSelect = 3
        
        #Girder Type 1
        if girderSelect == 1:
            cmds.polyCube (h = girder1Height, w = girder1Width + 400, d = girder1Depth, n = namespace_tmp)
            cmds.move (0, pileHeight + (girder1Height / 2), i * 500, a = True)            
            
        #Girder Type 2
        if girderSelect == 2:
            cmds.polyCube (h = girder1Height, w = girder1Width, d = girder1Depth, n = namespace_tmp)
            cmds.move (0, pileHeight + (girder1Height / 2), i * 500, a = True)
            
        #Girder Type 3
        if girderSelect == 3:
            cmds.polyCube (h = girder1Height, w = girder1Width, d = girder1Depth, n = namespace_tmp)
            #cmds.select (namespace_tmp + ':' + namespace_tmp)
            cmds.move (200, namespace_tmp + ':Girder' + str (rnd + i) + '.e[7]', moveX = True, a = True)
            cmds.move (-200, namespace_tmp + ':Girder' + str (rnd + i) + '.e[6]', moveX = True, a = True)
            cmds.move (0, pileHeight + (girder1Height / 2), i * 500, a = True)
            