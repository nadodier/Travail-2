import maya.cmds as cmds

polySphere3 = maya.cmds.polySphere(
  r=0.2
  )

print polySphere3


#Sélectionne la scene

cmds.select( 'pCube1', r=True )
cmds.select( 'pCube2', add=True )
cmds.select( 'pCube3', add=True )
cmds.select( 'pCube5', add=True )
cmds.select( 'pCube6', add=True )
cmds.select( 'pCube8', add=True )
cmds.select( 'pCube9', add=True )
cmds.select( 'pCube10', add=True )
cmds.select( 'pSphere1', add=True )
cmds.select( 'pSphere2', add=True )
cmds.select( 'pPlane1', add=True )
cmds.select( 'pPlane2', add=True )
cmds.select( 'pPlane3', add=True )
cmds.select( 'pPlane4', add=True )



