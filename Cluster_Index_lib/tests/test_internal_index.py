import unittest
from cluster_index_lib import internal_index as ii
from sklearn import datasets


# The values used for double checking the results are obtained thanks to the R
# package clusterCrit. As these values are rounded to the precision of the
# asserts properties have been adjusted in accordance
class internal_index_test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(internal_index_test, self).__init__(*args, **kwargs)
        iris = datasets.load_iris()
        self.data = iris.data
        self.labels = iris.target

    def test_silhouette(self):
        value = 0.5032507
        self.assertAlmostEqual(
            ii.silhouette(self.labels, self.data),
            value,
            places=6)

    def test_ray_turi(self):
        value = 0.226929
        self.assertAlmostEqual(
            ii.ray_turi(self.labels, self.data),
            value,
            places=6)

    # def test_tau(self):
    #     value = 0.5842415
    #     self.assertAlmostEqual(
    #         ii.tau(self.labels, self.data),
    #         value,
    #         places=6)

    def test_xie_beni(self):
        value = 11.91824
        self.assertAlmostEqual(
            ii.xie_beni(self.labels, self.data),
            value,
            places=4)

    # def test_gamma(self):
    #     value = 0.8792793
    #     self.assertAlmostEqual(
    #         ii.gamma(self.labels, self.data),
    #         value,
    #         places=6)

    def test_ball_hall(self):
        value = 0.595912
        self.assertAlmostEqual(
            ii.ball_hall(self.labels, self.data),
            value,
            places=5)

    def test_calinski_harabasz(self):
        value = 486.3208
        self.assertAlmostEqual(
            ii.calinski_harabasz(self.labels, self.data),
            value,
            places=4)

    def test_log_ss_ratio(self):
        value = 1.889583
        self.assertAlmostEqual(
            ii.log_ss_ratio(self.labels, self.data),
            value,
            places=5)

    # def test_c_index(self):
    #     value = 0.04680377
    #     self.assertAlmostEqual(
    #         ii.c_index(self.labels, self.data),
    #         value,
    #         places=7)


if __name__ == '__main__':
    unittest.main()
