import unittest
import algo as algy
import squareMaker as squary
#import convert_coordinates as convy
import filterCoords as filty

class AlgoritmeTests(unittest.TestCase):
    

    def test_algo_height_exists(self):
        """
        test to check if point exists
        """
        
        result = self.assertEqual(algy.heightNumber(-9999,4), 0)
    
    def test_algo_height_exists_1(self):
        """
        test to check if point is below waterlevel
        """

        result = self.assertEqual(algy.heightNumber(2,12), 3)

    def test_algo_height_exists_2(self):
        """
        test to check if point is medium below waterlevel
        """
        
        result = self.assertEqual(algy.heightNumber(6,12), 2)

    def test_algo_height_exists_3(self):
        """
        test to check if point is just about waterlevel
        """
        
        result = self.assertEqual(algy.heightNumber(10,12), 1)

    def test_algo_height_exists_4(self):
        """
        test to check if point is above waterlevel
        """
        
        result = self.assertEqual(algy.heightNumber(-9999,12), 0)

    def test_algo_algorithm(self):
        """
        test later
        """

    def test_algo_makeImage(self):
        """
        test with mock later
        """
    

    
    def test_filter_calculate_slope(self):
        """
        test if the slope works
        """
        testclass = filty.Edge(filty.Point(100,50,12),filty.Point(50,25,12))
        result = self.assertEqual(testclass.slope,0.5)

    def test_filter_calculate_Length(self):
        """
        test if the length works
        """
        testclass = filty.Edge(filty.Point(10,30,12),filty.Point(7,26,12))
        result = self.assertEqual(testclass.CalculateLength(),5) 
    
    def test_filter_calculate_GETYFORX(self):
        """
        test if the getYforX
        """
        testclass = filty.Edge(filty.Point(100,50,12),filty.Point(50,25,12))
        result = self.assertEqual(int(testclass.GetYForX(120)), 60)
    
    def test_filter_calculate_GETXFORY(self):
        """
        test if the getXforY
        """
        testclass = filty.Edge(filty.Point(100,50,12),filty.Point(50,25,12))
        result = self.assertEqual(int(testclass.GetXForY(120)),240)

    def test_filter_calculate_withinQuadrilateralTrue(self):
        """
        test if the point is within rectangle
        """
        testClass = filty.QuadrilateralFilter(filty.Point(100,300,10), filty.Point(300,200,20), filty.Point(125,100,10), filty.Point(325,100,20))
        result = self.assertTrue(testClass.withinQuadrilateral(filty.Point(150,150,15)))

    def test_filter_calculate_withinQuadrilateralFalse(self):
        """
        test if the point is within rectangle
        """
        testClass = filty.QuadrilateralFilter(filty.Point(100,200,12), filty.Point(200,200,15), filty.Point(125,100,15), filty.Point(225,100,20))
        result = self.assertFalse(testClass.withinQuadrilateral(filty.Point(200,200,10)))

    def test_filter_calculate_getMinMaxValuesRightValues(self):
        """
        test if the point is within rectangle
        """
        testClass = filty.QuadrilateralFilter(filty.Point(100,200,12), filty.Point(200,200,15), filty.Point(125,100,15), filty.Point(225,100,20))
        points = testClass.getMinMaxValues()
        result = self.assertEqual(points[1],100)

    def test_filter_calculate_getMinMaxValuesFalseValues(self):
        """
        test if the point is within rectangle
        """
        testClass = filty.QuadrilateralFilter(filty.Point(100,200,12), filty.Point(200,200,15), filty.Point(125,100,15), filty.Point(225,100,20))
        points = testClass.getMinMaxValues()
        result = self.assertNotEqual(points[1],200)

    def test_filter_calculate_Twodimensional(self):
        """
        test if the indexing works correct
        """
        testClass = filty.QuadrilateralFilter(filty.Point(100,200,12), filty.Point(200,200,15), filty.Point(125,100,15), filty.Point(225,100,20))
        testTD = filty.TwoDimensionalXYZArray(testClass)
        points = testClass.getMinMaxValues()
        expectedresult = {"x":int(0),"y":int(0)}
        result = self.assertEqual(testTD.coordinateToIndex(filty.Point(100,100)),expectedresult)

if __name__ == '__main__':
    unittest.main()