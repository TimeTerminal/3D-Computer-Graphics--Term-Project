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

cmds.colorSliderGrp ('roadDividerColour', label = "Colour", hsv = (220, 0.023, 0.514))
#cmds.colorSliderGrp ('roundedHoledBlockColour', label = "Colour", hsv = (220, 0.023, 0.514))

cmds.columnLayout ()
cmds.button (label = "Create Bridge", command = ('girderAndPile ()'))
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
    namespaceRoad = "Road" + str (rnd)
    namespaceRoadDivider = "RoadDivider" + str (rnd)
    rgb = cmds.colorSliderGrp ('roadDividerColour', query = True, rgbValue = True)
    
    #cmds.select (clear = True)
    #cmds.namespace (add = namespaceGirder)
    #cmds.namespace (set = namespaceGirder)
    
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
        cmds.polyCube (h = roadHeight, w = girderDepth + 400, d = roadDepth, n = namespaceRoad)
        cmds.move (0, girderHeight + pileHeight + (roadHeight / 2), 500 * i, a = True)
        
        #Dividers
        cmds.polyPlane (w = 20, h = 60, sx = 1, sy = 1, n = namespaceRoadDivider)
        cmds.move (0, (girderHeight + pileHeight + (roadHeight)) + 1, 500 * i, a = True)
                
        selectionPrint = cmds.select (namespaceRoadDivider)
               
    '''
        #cmds.setAttr (namespaceGirder + ":" + namespaceRoadDivider + ":blockMaterial.color", rgb[0], rgb[1], rgb[2], type = 'double3')
        
        #Girder906:RoadDivider906:blockMaterial.color
        #cmds.setAttr (RoadDivider906 + ":" + blockMaterial.color, rgb[0], rgb[1], rgb[2], type = 'double3')

        cmds.select( "RoadDivider" + str (rnd))
        sel = cmds.ls(sl=True)
        myShader = cmds.shadingNode ('lambert', asShader = True, name = sel[0]+"blockMaterial")
        cmds.setAttr (sel[0]+":blockMaterial.color", rgb[0], rgb[1], rgb[2], type = 'double3')
        #cmds.setAttr ("RoadDivider" + str (rnd) +  ":blockMaterial.color", rgb[0], rgb[1], rgb[2], type = 'double3')
       
       
        cmds.hyperShade (assign = (sel[0]+"blockMaterial"))

        
        print(namespaceRoadDivider)
        #sel = cmds.ls(sl=True)
'''