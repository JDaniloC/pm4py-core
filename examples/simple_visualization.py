import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from pm4py.log.importer.xes import factory as xes_importer
from pm4py.util import simple_view

logPath = os.path.join("..", "tests", "inputData", "receipt.xes")
#logPath = "C:\\SEPSIS.xes"
log = xes_importer.import_log(logPath)
gviz = simple_view.apply(log)
gviz.view()