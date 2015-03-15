import maya.cmds as cmds
import random
import math



cmds.namespace(set=":")

window = cmds.window(title = "lego Blocks", menuBar = True)

cmds.menu(label = "Basic Options")
cmds.menuItem(label ="new scene", command = ('cmds.file( new = True, force = True)'))
cmds. menuItem(label ="delete selected", command = ('cmds.delete()'))

cmds.columnLayout()
cmds.frameLayout(collapsable = True, label = "Standard Block", cl =False)

cmds.columnLayout()
cmds.intSliderGrp('Curvature', label="Curvature", field = True, min = 1, max = 180, value = 90)
#cmds.intSliderGrp('blockWidth', label="Width(Bumps)", field = True, min = 1, max = 20, value = 2)
#cmds.intSliderGrp('blockDepth', label="Depth(Bumps)", field = True, min = 1, max = 20, value = 8)

cmds.colorSliderGrp('archColor', label = "Color", hsv=(120,1,1))

cmds.columnLayout()
cmds.button(label="Create arch", command = ('arch()') )
cmds.setParent('..')

cmds.setParent('..')
cmds.setParent('..')


cmds.showWindow(window)

## function for basic block
def arch():
    ## gathering information from the UI
    ArchCurvature = cmds.intSliderGrp('Curvature', query = True, value = True)
    
    
    rgb = cmds.colorSliderGrp('archColor', query = True, rgbValue = True)
    rnd = random.randrange(0,1000)
    namespace_tmp = "Piece_" + str(rnd)
    
    cmds.select(clear = True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    
   ##create cube 
    cmds.polyCube(h = 10.0, w =2.0, d = 1.0,sy = 10)[0]
    cmds.nonLinear( typ = 'bend' ,  curvature=ArchCurvature )

    
    ##apply the texture
    ##cmds.setAttr(namespace_tmp+":blockMaterial.color", rgb[0], rgb[1], rgb[2], type = 'double3')
    #cmds.polyUnite((namespace_tmp+":*"), n = namespace_tmp,ch=False)
    #cmds.delete(ch = True) 
    #cmds.hyperShade(assign = (namespace_tmp+":blockMaterial"))
   # cmds.namespace(set=":")
    
