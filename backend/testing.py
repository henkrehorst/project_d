from subprocess import Popen

Process = Popen('test.sh %s' % (str("Mark"),), shell=True)