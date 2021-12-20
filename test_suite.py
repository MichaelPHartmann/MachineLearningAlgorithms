import unittest

from Decision_Tree import *
from K_Nearest_Neighbour import *
from Weighted_K_Nearest_Neighbour import *
from Regression import *


class testAttributeSelectionMeasures(unittest.TestCase):
    def setUp(self):
        self.object = attributeSelectionMeasures()
        self.freq = [5,9]
        self.freq_table = [[3,2],[4,0],[2,3]]
        self.int_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.rand_list = [43, 47, 54, 234, 325, 346, 365, 436, 463, 463, 523, 523, 685, 685, 685, 856, 865, 865, 1423, 2134, 4132, 4231]
        self.gini_test_1 = [1,1,1,1,2,2,2,3,3,3]
        self.gini_test_2 = [1,2,2,3,3,3,7,7,9,4]
        self.frequency_dict = {"black":226, "red":418, "blue":486, "white":525, "yellow":345}

    def test_single_attribute_entropy(self):
        test = round(self.object.single_attribute_entropy(self.freq),5)
        correct = 0.94029
        self.assertEqual(test, correct)

    def test_double_attribute_entropy(self):
        test = round(self.object.double_attribute_entropy(self.freq_table),5)
        correct = 0.69354
        self.assertEqual(test, correct)

    def test_sample_variance(self):
        test_1 = self.object.sample_variance(self.int_list)
        correct_1 = 35
        self.assertEqual(test_1, correct_1)
        test_2 = round(self.object.sample_variance(self.rand_list), 4)
        correct_2 = 1328184.2619
        self.assertEqual(test_2, correct_2)

    def test_gini_index(self):
        test_1 = self.object.gini_index(self.gini_test_1)
        self.assertEqual(test_1, 0.66)
        test_2 = round(self.object.gini_index(self.gini_test_2), 3)
        self.assertEqual(test_2, 0.8)

    def test_chi_square(self):
        test_1 = self.object.chi_square(self.frequency_dict)
        self.assertEqual(test_1, 141.615)



class testKNearestNeighbour(unittest.TestCase):

    def setUp(self):
        self.file = "cars_data.csv"
        self.knn_object = kNearestNeighbour()
        self.wknn_object = weightedKNearestNeighbour()

    def test_knn(self):
        with open(self.file, "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                l = line.split(",")
                self.knn_object.submit_training_data(float(l[3]), float(l[5]), int(l[9]))

        self.knn_object.train_drain_node(100,3000)
        self.assertEqual(self.knn_object.test_node.label, 2)

        self.knn_object.train_drain_node(100,2000)
        self.assertEqual(self.knn_object.test_node.label, 3)

    def test_wknn(self):
        with open(self.file, "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                l = line.split(",")
                self.wknn_object.submit_training_data(float(l[3]), float(l[5]), int(l[9]))

        self.wknn_object.train_drain_node(100,3000)
        self.assertEqual(self.wknn_object.test_node.label, 1)

        self.wknn_object.train_drain_node(100,2000)
        self.assertEqual(self.wknn_object.test_node.label, 2)

class testRegression(unittest.TestCase):

    def setUp(self):
        self.single_reg_x = [1,2,3,4,5,6,7,8,9,10]
        self.single_reg_y = [3,6,9,12,15,18,21,24,27,30]
        self.multi_reg_x = [[1,2,3,4,5,6,7,8,9],[2,4,6,8,10,12,14,16,18]]
        self.multi_reg_y = [10,20,30,40,50,60,70,80,90]

    def test_single_variable_regression(self):
        s_test = singleLinearRegression(self.single_reg_x, self.single_reg_y)
        correct = (200,600)
        self.assertEqual(s_test.estimate_point(200), correct)

    def test_multiple_variable_regression(self):
        m_test = multipleLinearRegression(self.multi_reg_x, self.multi_reg_y)
        self.assertEqual(m_test.estimate_point([200,400])["Y"], 3950)


if __name__ == "__main__":
    unittest.main()
