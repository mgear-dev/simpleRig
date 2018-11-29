import pymel.core as pm
import mgear
from mgear.simpleRig import simpleRigTool


def install():
    """Install Simple Rig submenu
    """
    pm.setParent(mgear.menu_id, menu=True)
    pm.menuItem(divider=True)
    pm.menuItem(label="Simple Rig Tool", command=simpleRigTool.openSimpleRigUI)
