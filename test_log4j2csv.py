import unittest
from Log4j2csv import Log4j2csv


class Log4j_import(unittest.TestCase):
  def setUp(self):
    self.convert = Log4j2csv()

  def test_import_file_positive(self):
    
    self.convert.import_log4j('example.log')
    self.assertGreater(len(self.convert.log4j_contents), 0, 'non-zero length')

  def test_import_file_negative(self):
    
    self.convert.import_log4j('example-does-not-exist.log')
    self.assertEqual(self.convert.log4j_contents, None, 'log4j_contents = None')


class Log4j_read(unittest.TestCase):
  def setUp(self):
    self.convert = Log4j2csv()

  def test_import_read_log4j_contents(self):
    
    self.convert.import_log4j('example.log')
    self.convert.read_log4j()    



class Log4j_convert(unittest.TestCase):
  def setUp(self):
    self.convert = Log4j2csv()

  def test_convert_log4j_contents(self):
    
	self.convert.import_log4j('example.log')
	self.convert.convert_log4j()  
	print self.convert.log4j_converted 	



  def test_convert_log4j_contents_message(self):
    
	self.convert.log4j_contents = ['2014-07-02 20:52:39 DEBUG HelloExample:19 - This is debug : mkyong\n']
	self.convert.convert_log4j()


class Log4j_export_csv(unittest.TestCase):
	def setUp(self):
		self.convert = Log4j2csv()
		self.convert.import_log4j('example.log')
		self.convert.convert_log4j()

	def test_convert_log4j_contents(self):
		self.convert.export_log4j_csv('output_example.csv')
	



if __name__ == '__main__':
  unittest.main()
  