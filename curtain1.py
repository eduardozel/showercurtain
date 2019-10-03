import FreeCAD
from FreeCAD import Base
import Part,PartGui

SPSH = App.ActiveDocument.Spreadsheet
App.ActiveDocument.addObject("Part::Cylinder","Cylinder002")
cy2 = App.ActiveDocument.Cylinder002
rcut = SPSH.rTUBE + SPSH.HTB1 + 0.1
print(rcut)

cy2.Radius = rcut
cy2.Height = 15.00
cy2.Angle  = 360.00
rot = Base.Rotation(0.50,0.50,0.50,0.50)
bas = Base.Vector(-5.00,0.00,0.00)
cy2.Placement=Base.Placement( bas, rot)
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")

App.activeDocument().addObject("Part::Cut","Cut")
App.activeDocument().Cut.Base = App.activeDocument().Body
App.activeDocument().Cut.Tool = App.activeDocument().Cylinder002
Gui.activeDocument().Body.Visibility=False
Gui.activeDocument().Cylinder002.Visibility=False
Gui.ActiveDocument.Cut.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
Gui.ActiveDocument.Cut.DisplayMode=Gui.ActiveDocument.Body.DisplayMode
App.ActiveDocument.recompute()


App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
App.ActiveDocument.Cylinder.Radius=25.00
App.ActiveDocument.Cylinder.Height=2.00
App.ActiveDocument.Cylinder.Angle=360.00

rot1 = Base.Rotation(0.50,0.50,0.50,0.50)
bas1 = Base.Vector(-5.00,0.00,0.00)
App.ActiveDocument.Cylinder.Placement=Base.Placement( bas1 , rot1 )
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Cylinder").Height = '3 mm'
App.ActiveDocument.getObject("Cylinder").Height = '4 mm'
App.ActiveDocument.getObject("Cylinder").Height = '5 mm'
App.activeDocument().addObject("Part::Cut","Cut001")
App.activeDocument().Cut001.Base = App.activeDocument().Cut
App.activeDocument().Cut001.Tool = App.activeDocument().Cylinder
Gui.activeDocument().Cut.Visibility=False
Gui.activeDocument().Cylinder.Visibility=False
Gui.ActiveDocument.Cut001.ShapeColor=Gui.ActiveDocument.Cut.ShapeColor
Gui.ActiveDocument.Cut001.DisplayMode=Gui.ActiveDocument.Cut.DisplayMode
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
