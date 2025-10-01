import maya.cmds as cmds

def createShape(shape, name=None):
	if shape == 'cone':
		obj = cmds.polyCone()[0]
	elif shape == 'cube':
		obj = cmds.polyCube()[0]
	elif shape == 'sphere':
		obj = cmds.polySphere()[0]
	elif shape == 'torus':
		obj = cmds.polyTorus()[0]
	else:
		cmds.warning("Unknown shape type!")
		return None

	if name:
		obj = cmds.rename(obj, name)
	return obj

def renameSelection(name):
	sel = cmds.ls(selection=True)
	if not sel:
		cmds.warning('No objects selected!')
		return None
	
	newName = cmds.rename(sel[0], name)
	return newName