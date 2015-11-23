
import csv
import re
import os.path


class Log4j2csv:

	def __init__(self):
		self.log4j_contents = None
		self.log4j_converted = []	
		self.regex_date = re.compile('\d{4}[-.]?\d{2}[-.]?\d{2}[ ]?\d{2}[:]\d{2}[:]\d{2}')
		self.regex_stack_prefix = re.compile('[a-zA-Z0-9]+[.]')
		self.regex_stack_prefix2 = re.compile('[a-zA-Z0-9.]+')
		self.regex_stack_suffix = re.compile('[a-zA-Z0-9]+[:]')
		self.regex_call_line_issue = re.compile('[a-zA-Z]+[a-zA-Z0-9]+[:][0-9]+')
		self.regex_message_level = re.compile('DEBUG|INFO|WARN|FATAL|ERROR')
		self.regex_message_detail = re.compile('[-][a-zA-Z0-9\s]+[:][a-zA-Z0-9\s]+[\n]')
		self.regex_stack_trace_prefix = re.compile('[\s]at[\s][a-zA-Z0-9.]+')
		self.regex_stack_trace_call = re.compile('[(][a-zA-Z0-9.]+[:][0-9]+[)]')
		self.regex_stack_trace_line = re.compile('[\s]at[\s][a-zA-Z0-9.]+[(][a-zA-Z0-9.]+[:][0-9]+[)]')
		

	def import_log4j(self, log4j_file=None):
		
		if log4j_file and os.path.isfile(log4j_file):
			with open(log4j_file, 'r') as f:
				self.log4j_contents = f.readlines()


	def read_log4j(self):
		
		if self.log4j_contents:
			for e in self.log4j_contents:
				pass 


	def convert_log4j(self):
		
		self.log4j_converted  = []
		line_count = 0

		for e in self.log4j_contents:
			entry = {}
			
			date = self.regex_date.search(e)
			if date:
				entry['date'] = date.group()
				line_count = 0
			else:
				entry['date'] = self.log4j_converted[-1]['date']
				line_count += 1
			entry['line_count'] = line_count

			message_level = self.regex_message_level.search(e)
			if message_level:
				entry['message_level'] = message_level.group()
			else:
				entry['message_level'] = self.log4j_converted[-1]['message_level']				


			call_line_issue = self.regex_call_line_issue.search(e)
			if call_line_issue:
				call_line  = call_line_issue.group().split(':')
				entry['function'] = call_line[0]
				entry['line'] = call_line[1]
			else:
				entry['function'] = '-'
				entry['line'] = '-'				
			
			entry['verbose'] = e


			self.log4j_converted.append(entry)



	def export_log4j_csv(self, csv_filename=None):
	
		if csv_filename:
			with open(csv_filename, 'wb') as csvfile:
				csv_writer = csv.writer(csvfile, delimiter=',')
				csv_writer.writerow(['date', 'line_count', 'message_level', 'function', 'line'])
				for e in self.log4j_converted:
					print e
					csv_writer.writerow([e['date'], 
										e['line_count'], 
										e['message_level'],
										e['function'],
										e['line']])

				
# 	def convert_log4j(self):
# 
#		csv_writer = csv.writer(csvfile, delimiter=',')
# 		with open('output.csv', 'wb') as csvfile:
# 			for e in read_data:
# 				print e,
# 				csv_writer.writerow([e, e])	