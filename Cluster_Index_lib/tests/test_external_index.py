import unittest
from cluster_index_lib import external_index as ei
import numpy as np
import sklearn.metrics as skmetric


# The values used for double checking the results are obtained thanks to the R
# package clusterCrit. As these values are rounded to the precision of the
# asserts properties have been adjusted in accordance
class external_index_test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(external_index_test, self).__init__(*args, **kwargs)
        self.labels = np.loadtxt("tests/tests_ressources/Iris/iris.labels")
        self.results = np.loadtxt("tests/tests_ressources/Iris/iris.results")

    def test_folkes_mallows(self):
        value = 0.8101679
        self.assertAlmostEqual(
            ei.folkes_mallows(self.labels, self.results),
            value,
            places=7)

    def test_hubert(self):
        value = 0.7156547
        self.assertAlmostEqual(
            ei.hubert(self.labels, self.results),
            value,
            places=7)

    def test_recall(self):
        value = 0.8190476
        self.assertAlmostEqual(
            ei.recall(self.labels, self.results),
            value,
            places=7)

    def test_rogers_tanimoto(self):
        value = 0.7757826
        self.assertAlmostEqual(
            ei.rogers_tanimoto(self.labels, self.results),
            value,
            places=7)

    def test_russel_rao(self):
        value = 0.2693512
        self.assertAlmostEqual(
            ei.russel_rao(self.labels, self.results),
            value,
            places=7)

    def test_sokal_sneath(self):
        value = 0.516118
        self.assertAlmostEqual(
            ei.solkal_sneath(self.labels, self.results),
            value,
            places=6)

    def test_sokal_sneath_2(self):
        value = 0.9326138
        self.assertAlmostEqual(
            ei.solkal_sneath_2(self.labels, self.results),
            value,
            places=7)

    def test_ri(self):
        value = 0.873736
        self.assertAlmostEqual(
            ei.ri(self.labels, self.results),
            value,
            places=6)

    def test_jaccard(self):
        value = 0.6808414
        self.assertAlmostEqual(
            ei.jaccard(self.labels, self.results),
            value,
            places=7)

    def test_kulczynski(self):
        value = 0.8102161
        self.assertAlmostEqual(
            ei.kulczynski(self.labels, self.results),
            value,
            places=7)

    def test_precision(self):
        value = 0.8013844
        self.assertAlmostEqual(
            ei.precision(self.labels, self.results),
            value,
            places=7)

    def test_f_measure(self):
        value = 0.8101197
        self.assertAlmostEqual(
            ei.f_measure(self.labels, self.results),
            value,
            places=7)

    def test_phi(self):
        value = 2.582312e-08
        self.assertAlmostEqual(
            ei.phi(self.labels, self.results),
            value,
            places=6)

    def test_mcnemar(self):
        value = 69.37441
        self.assertAlmostEqual(
            ei.mc_nemar(self.labels, self.results),
            value,
            places=5)

    def test_fj_nmi(self):
        value = 0.7352944
        self.assertAlmostEqual(
            ei.fj_nmi(self.labels, self.results),
            value,
            places=7)

    def test_ari(self):
        value = 0.7155592
        self.assertAlmostEqual(
            ei.ari(self.labels, self.results),
            value,
            places=7)

    def test_purity(self):
        value = 0.8866667
        self.assertAlmostEqual(
            ei.purity(self.labels, self.results),
            value,
            places=7)

    def test_entropy(self):
        value = 0.2683396
        self.assertAlmostEqual(
            ei.entropy(self.labels, self.results),
            value,
            places=7)

    def test_mi(self):
        value = skmetric.mutual_info_score(self.labels, self.results)
        self.assertAlmostEqual(
            ei.mi(self.labels, self.results),
            value,
            places=7)


if __name__ == '__main__':
    unittest.main()
