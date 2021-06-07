import filterCoords as fc

l1 = fc.Point(52590.5, 427698.9114832536)
l2 = fc.Point(52630.5, 427706.0885167464)
r1 = fc.Point(52665.5, 427280.9114832536)
r2 = fc.Point(52705.5, 427288.0885167464)

qF = fc.QuadrilateralFilter(l1, l2, r1, r2)
# print("top Edge length: ")
# qF.topEdge.CalculateLength()
# print()
# print("bot Edge length: ")
# qF.bottomEdge.CalculateLength()
# print()
# print("left Edge length: ")
# qF.leftEdge.CalculateLength()
# print()
# print("right Edge Length: ")
# qF.rightEdge.CalculateLength()
# print()
# tempPoint = fc.Point(55930.5, 429081.5)
# qF.bottomEdge.IntersectionPoint(tempPoint, qF.leftEdge)

# l1 = fc.Point(4,7)
# l2 = fc.Point(2,4)
# r1 = fc.Point(10,6)
# r2 = fc.Point(8,3)

# qF = fc.QuadrilateralFilter(l1, l2, r1, r2)
# tempPoint = fc.Point(6,6)
# qF.bottomEdge.IntersectionPoint(tempPoint, qF.leftEdge)

arr = fc.TwoDimensionalXYZArrayStraight(qF, './goeree.xyz')
#fc.RunFilter("goeree.xyz", 52590.5, 427698.9114832536, 52630.5, 427706.0885167464,52665.5, 427280.9114832536, 52705.5, 427288.0885167464)
