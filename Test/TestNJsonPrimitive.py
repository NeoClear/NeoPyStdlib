import unittest
from NData.NJson import NJsonPrimitive


class MyTestCase(unittest.TestCase):
    def test_init(self):
        njson = NJsonPrimitive()
        if njson.filename_read is not None:
            print(njson.filename_read)
        # self.assertEqual(njson.filename_read, njson.filename_write)

    def test_file_content(self):
        njson = NJsonPrimitive("666.js")
        data = {"name": "NeoClear", "age": 17}
        njson.read_from_file()
        js2 = njson.metadata

    def test_static_io(self):
        njson = NJsonPrimitive("test.js")
        data = {"name": "NeoClear", "age": 17}
        njson.write("static.js", data)
        self.assertEqual(njson.read("static.js"), data)

    def setUp(self):
        print("Start testCases")

    def tearDown(self):
        print("End testCases")

    @classmethod
    def setUpClass(cls):
        print("Begin all the testCases")

    @classmethod
    def tearDownClass(cls):
        print("Finish all the testCases")


if __name__ == '__main__':
    # test_suite = unittest.TestSuite()
    # all_cases = unittest.defaultTestLoader.discover('.', 'Test*.py')
    # for case in all_cases:
    #     test_suite.addTest(case)
    #     test_suite.run()

    main_test = unittest.TestSuite()
    main_test.addTest(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
    with open("result.txt", "w") as f:
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(main_test)
