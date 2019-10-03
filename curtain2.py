from FreeCAD import Base
import Part,PartGui

SPSH = App.ActiveDocument.Spreadsheet
cHEIGHT = 20.

App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
App.ActiveDocument.Cylinder.Radius= SPSH.rSkiv + SPSH.dBall + 0.5
App.ActiveDocument.Cylinder.Height= cHEIGHT
App.ActiveDocument.Cylinder.Angle=360.00
App.ActiveDocument.Cylinder.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.50,0.50,0.50,0.50))


App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
App.ActiveDocument.addObject("Part::Cylinder","Cylinder001")
App.ActiveDocument.Cylinder001.Radius= SPSH.rTUBE + SPSH.HTB1 - 0.1
App.ActiveDocument.Cylinder001.Height= cHEIGHT
App.ActiveDocument.Cylinder001.Angle=360.00
App.ActiveDocument.Cylinder001.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.50,0.50,0.50,0.50))
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")


App.activeDocument().addObject("Part::Cut","Cut")
App.activeDocument().Cut.Base = App.activeDocument().Cylinder
App.activeDocument().Cut.Tool = App.activeDocument().Cylinder001
Gui.activeDocument().Cylinder.Visibility=False
Gui.activeDocument().Cylinder001.Visibility=False
Gui.ActiveDocument.Cut.ShapeColor=Gui.ActiveDocument.Cylinder.ShapeColor
Gui.ActiveDocument.Cut.DisplayMode=Gui.ActiveDocument.Cylinder.DisplayMode
App.ActiveDocument.recompute()
App.activeDocument().addObject("Part::Cut","Cut001")
App.activeDocument().Cut001.Base = App.activeDocument().Body
App.activeDocument().Cut001.Tool = App.activeDocument().Cut
Gui.activeDocument().Body.Visibility=False
Gui.activeDocument().Cut.Visibility=False
Gui.ActiveDocument.Cut001.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
Gui.ActiveDocument.Cut001.DisplayMode=Gui.ActiveDocument.Body.DisplayMode

App.ActiveDocument.recompute()
