import maya.cmds as cmds

cmds.polyCube( w=1, h=1, d=1, sx=1, sz=1, cuv=4, ch=1 )
cmds.move(0, 22, 0)

target = cmds.ls(selection=True, head=1)
#target=cmds.select( 'pCube1', r=True )

if len(target) > 0:
  cmds.setKeyframe(target, time=5, attribute='translateY', value=22)
  cmds.setKeyframe(target, time=5, attribute='translateX', value=0)
  cmds.setKeyframe(target, time=27, attribute='rotateZ', value=0)
  cmds.setKeyframe(target, time=10, attribute='translateY', value=12)
  cmds.setKeyframe(target, time=20, attribute='translateY', value=0)
  cmds.setKeyframe(target, time=23, attribute='translateY', value=6)
  cmds.setKeyframe(target, time=25, attribute='translateY', value=0)
  cmds.setKeyframe(target, time=27, attribute='translateY', value=4)
  cmds.setKeyframe(target, time=27, attribute='rotateZ', value=41)
  cmds.setKeyframe(target, time=27, attribute='translateX', value=0)
  cmds.setKeyframe(target, time=28, attribute='translateY', value=0)
  cmds.setKeyframe(target, time=29, attribute='translateY', value=3)
  cmds.setKeyframe(target, time=30, attribute='translateY', value=0)
  cmds.setKeyframe(target, time=30, attribute='translateX', value=5)
  cmds.setKeyframe(target, time=30, attribute='rotateZ', value=100)
  cmds.setKeyframe(target, time=31, attribute='translateY', value=2)
  cmds.setKeyframe(target, time=32, attribute='translateY', value=0)
