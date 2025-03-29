import FreeCAD
import Part

def create_table(length, width, height, leg_radius, leg_height):
    """
    创建一个简单的桌子。
    参数:
    length (float): 桌子长度。
    width (float): 桌子宽度。
    height (float): 桌子总高度。
    leg_radius (float): 桌子腿的半径。
    leg_height (float): 桌子腿的高度。
    """
    doc = FreeCAD.newDocument("Table")

    # 创建桌面
    table_top = Part.makeBox(length, width, height - leg_height)
    # 将桌面移动到中心位置
    table_top.translate(FreeCAD.Vector(-length / 2, -width / 2, 0))
    table_top_shape = doc.addObject("Part::Feature", "TableTop")
    table_top_shape.Shape = table_top

    # 创建桌子腿
    # 前左腿
    leg1 = Part.makeCylinder(leg_radius, leg_height)
    leg1.translate(FreeCAD.Vector(-length / 2 + 2 * leg_radius, -width / 2 + 2 * leg_radius, 0))
    leg1_shape = doc.addObject("Part::Feature", "Leg1")
    leg1_shape.Shape = leg1

    # 前右腿

    leg2 = Part.makeCylinder(leg_radius, leg_height)
    leg2.translate(FreeCAD.Vector(length / 2 - 2 * leg_radius, -width / 2 + 2 * leg_radius, 0))
    leg2_shape = doc.addObject("Part::Feature", "Leg2")
    leg2_shape.Shape = leg2

    # 后左腿
    leg3 = Part.makeCylinder(leg_radius, leg_height)
    leg3.translate(FreeCAD.Vector(-length / 2 + 2 * leg_radius, width / 2 - 2 * leg_radius, 0))
    leg3_shape = doc.addObject("Part::Feature", "Leg3")
    leg3_shape.Shape = leg3

    # 后右腿
    leg4 = Part.makeCylinder(leg_radius, leg_height)
    leg4.translate(FreeCAD.Vector(length / 2 - 2 * leg_radius, width / 2 - 2 * leg_radius, 0))
    leg4_shape = doc.addObject("Part::Feature", "Leg4")
    leg4_shape.Shape = leg4
    doc.recompute()


if __name__ == "__main__":
    # 创建一个标准尺寸的桌子
    create_table(length=1.2, width=0.6, height=0.75, leg_radius=0.02, leg_height=0.7)
