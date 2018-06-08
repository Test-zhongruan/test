#coding = utf-8
import unittest,os
import HTMLTestRunner
import time
def all_case():
    case_path=os.path.join("C:\\zktest\\","case")
    discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    return discover

def reportpath():
    nowtime = time.strftime('%Y-%m-%d %H-%M-%S')
    report_path=os.path.join("C:\\zktest\\","report")
    str1=report_path+"\\TestReport"+nowtime+".html"
    fp=open(str1,"wb")
    return fp

if __name__=="__main__":
    #runner=unittest.TextTestRunner()
    #runner.run(all_case())
    runner=HTMLTestRunner.HTMLTestRunner(reportpath(),title="BabyPlanTest",description="report 2")
    runner.run(all_case())
