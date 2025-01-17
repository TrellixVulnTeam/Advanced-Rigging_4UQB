import maya.cmds as cmds


class Window:
    def __init__(self):
        self.my_window = 'tsCoolToolWindow'

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_tswindow)

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='ToolBox Manager',
                                     widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        cmds.showWindow(self.my_window)

        cmds.button(parent=self.col_layout,
                    label='Random Generator',
                    c=lambda *x: self.ranGenFunc())

        cmds.button(parent=self.col_layout,
                    label='Rename Function',
                    c=lambda *x: self.renameFunc())

        cmds.button(parent=self.col_layout,
                    label='Freeze Transforms',
                    c=lambda *x: self.freezeFunc())

        cmds.button(parent=self.col_layout,
                    label='Parent Group',
                    c=lambda *x: self.parentFunc())

        cmds.button(parent=self.col_layout,
                    label='Parent Constrain',
                    c=lambda *x: self.constrainFunc())

        cmds.button(parent=self.col_layout,
                    label='Joint Display Tool',
                    c=lambda *x: self.jointTool())

        cmds.button(parent=self.col_layout,
                    label='Follow Attribute Constraint',
                    c=lambda *x: self.attributeConstrain())

        cmds.button(parent=self.col_layout,
                    label='Locator',
                    c=lambda *x: self.locatorTool())

    def ranGenFunc(self):
        import RandGen
        reload(RandGen)
        instance = RandGen.Generator()
        instance.create()

    def renameFunc(self):
        import Renamer
        reload(Renamer)
        instance = Renamer.Renamer()
        instance.create()

    def freezeFunc(self):
        import FreezeTransforms
        reload(FreezeTransforms)

    def parentFunc(self):
        import Parent
        reload(Parent)

    def constrainFunc(self):
        import ParentConstrain
        reload(ParentConstrain)

    def jointTool(self):
        import JointTransform
        reload(JointTransform)
        instance = JointTransform.JointTransform()
        instance.create()

    def attributeConstrain(self):
        import FollowAttributeConstraints
        reload(FollowAttributeConstraints)
        instance = FollowAttributeConstraints.FollowAttributeConstraints()
        instance.Main()

    def locatorTool(self):
        import Locator
        reload(Locator)
        instance = Locator.create_locator()
        instance.create()


my_window = Window()
my_window.create()
