import filterCoords as fc

l2 = fc.Point(52590.5, 427698.9114832536)
l1 = fc.Point(52630.5, 427706.0885167464)
r2 = fc.Point(52665.5, 427280.9114832536)
r1 = fc.Point(52705.5, 427288.0885167464)

startingPoints = (fc.Point(52610.5, 427702.5), fc.Point(52685.5, 427284.5))

qF = fc.QuadrilateralFilter(l1, l2, r1, r2)
fc.RunFilterOutput2DArray('goeree.xyz', './', 52630.5, 427706.0885167464,52590.5, 427698.9114832536, 52705.5, 427288.0885167464,52665.5, 427280.9114832536, startingPoints)