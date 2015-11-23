

from os import system

system('coverage run test_log4j2csv.py')
system('coverage html')
system('open -a firefox ./htmlcov/index.html')
