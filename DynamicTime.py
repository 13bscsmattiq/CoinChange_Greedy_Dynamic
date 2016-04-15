class MyTest(unittest.TestCase):
    def test(self):
        print "dynamic:"
        self.assertEqual(dynamicCoinChange([1, 5, 10, 25],  800),32)
suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
unittest.TextTestRunner().run(suite)
