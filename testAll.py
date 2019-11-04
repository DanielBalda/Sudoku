import unittest
import testSudoku
import testApi
import testInterface

suite = unittest.TestLoader().loadTestsFromModule(testSudoku)
unittest.TextTestRunner(verbosity=1).run(suite)

suite = unittest.TestLoader().loadTestsFromModule(testApi)
unittest.TextTestRunner(verbosity=1).run(suite)

suite = unittest.TestLoader().loadTestsFromModule(testInterface)
unittest.TextTestRunner(verbosity=1).run(suite)