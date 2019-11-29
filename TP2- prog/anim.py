import maya.cmds as cmds

#cree un insecte par terre

cmds.sphere( r=0.2, ssw=0, esw=180, hr=2)

cmds.rotate( '180deg', 0, 0, r=True )
cmds.move(11.5, 0, -10.6)

#deplace celui-ci
target = cmds.ls(selection=True, head=1)

if len(target) > 0:
  cmds.setKeyframe(target, time=0, attribute='translateZ', value=-10.6)
  cmds.setKeyframe(target, time=0, attribute='translateX', value=11.5)
  cmds.setKeyframe(target, time=10, attribute='translateX', value=9)
  cmds.setKeyframe(target, time=10, attribute='translateZ', value=-10.6)
  cmds.setKeyframe(target, time=15, attribute='translateX', value=7)
  cmds.setKeyframe(target, time=20, attribute='translateZ', value=-9)
  cmds.setKeyframe(target, time=25, attribute='translateZ', value=-10.6)
  cmds.setKeyframe(target, time=25, attribute='translateX', value=5)
  cmds.setKeyframe(target, time=55, attribute='translateX', value=-20)



