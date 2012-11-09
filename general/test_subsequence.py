"""
Test for subsequence.py
"""

import unittest
import subsequence as s

class TestSubsequence(unittest.TestCase):

	def set_up(self):
		pass

	def test_wrong_input(self):
		""" both strings are None """
		result = s.subsequence(None, None)
		self.assertEqual(False, result)

	def test_wrong_input_type(self):
		""" one input is not string """
		result = s.subsequence(1, "abcd")
		self.assertEqual(False, result)

	def test_x_larger_y(self):
		""" first string is larger than the second """
		result = s.subsequence("unix", "un")
		self.assertEqual(False, result)		

	def test_x_equals_y(self):
		""" strings are equal """
		result = s.subsequence("unix", "unix")
		self.assertEqual(True, result)

	def test_x_equal_length_y(self):
		""" equal length but different strings """
		result = s.subsequence("unix", "abcd")
		self.assertEqual(False, result)

	def test_x_subsequence_y(self):
		result = s.subsequence("anna", "banana")
		self.assertEqual(True, result)


	def test_x_not_subsequence_y(self):
		result = s.subsequence("annb", "banana")
		self.assertEqual(False, result)

	def tear_down(self):
		pass

if __name__ == '__main__':
    unittest.main()

