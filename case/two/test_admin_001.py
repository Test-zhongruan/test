#coding=utf-8
import unittest
from selenium import webdriver
import time



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://localhost:8080/BabyPlan/login.jsp")
        self.driver.implicitly_wait(3)

    def tearDown(self):
        driver = self.driver
        driver.close()

    def login(self):
        driver = self.driver
        driver.find_element_by_css_selector("#userName").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin11")
        driver.find_element_by_id("loginbtn").click()

    def test_001(self):
        "管理员主页-学习资料管理功能查看调用测试"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[1]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr/td").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无学习资料！")

    def test_002(self):
        "管理员主页-学习资料管理功能上传调用测试"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage")
        #driver.execute_script("document.getElementById(\"uploadStudy\").style =\"display: block\";")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[2]").click()
        driver.find_element_by_xpath("html/body/form[6]/div/div/div/table/tbody/tr[1]/td[2]/input").send_keys("软件测试")
        driver.find_element_by_xpath("html/body/form[6]/div/div/div/table/tbody/tr[3]/td[2]/span/input[2]").send_keys("C:\\1.jpg")
        driver.find_element_by_xpath("html/body/form[6]/div/div/div/table/tbody/tr[4]/td[2]/span/input[2]").send_keys("C:\\2.mp4")
        driver.find_element_by_xpath("html/body/form[6]/div/div/div/div[2]/button[1]").click()
        driver.implicitly_wait(15)
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[3]").get_attribute("textContent")
        self.assertEqual(xtr1,"软件测试")
 
    def test_003(self):
        "管理员主页-学习资料管理功能删除调用测试"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/select[1]/option[2]").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[3]").get_attribute("textContent")
        driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[1]/input").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[3]").click()
        driver.switch_to_alert().accept()
        xtr2=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,xtr2)

    def test_004(self):
        "管理员主页-学习资料管理功能按标题搜索调用测试"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[4]").send_keys("认")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无学习资料！")

    def test_005(self):
        "管理员主页-学习资料管理功能按类别搜索调用测试"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/select[1]/option[5]").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/select[2]/option[2]").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无学习资料！")

    def test_006(self):
        "管理员主页-学习资料管理功能默认搜索调用测试"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无学习资料！")
    
    def test_007(self):
        "管理员主页-学习资料管理功能按标题和类别搜索调用测试"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[4]").send_keys("E")
        driver.find_element_by_xpath("html/body/div[1]/div/form/select[1]/option[5]").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/select[2]/option[2]").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无学习资料！")

    def test_008(self):
        "管理员主页-育儿知识管理功能查看调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[1]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_009(self):
        "管理员主页-育儿知识管理功能默认搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")
    
    def test_010(self):
        "管理员主页-育儿知识管理功能按类别搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/select/option[2]").click()
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_011(self):
        "管理员主页-育儿知识管理功能按标题搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[4]").send_keys("父母")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")
        
    def test_012(self):
        "管理员主页-育儿知识管理功能按类别和标题搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/select/option[7]").click()
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[4]").send_keys("父母")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[5]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_013(self):
        "管理员主页-育儿知识管理功能删除调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[1]/input").click()
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[3]").click()
        driver.switch_to_alert().accept()
        xtr2=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertNotEqual(xtr1,xtr2)

    def test_014(self):
        "管理员主页-育儿知识管理功能上传纯文本调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[2]").click()
        driver.find_element_by_xpath("html/body/form/div[2]/table/tbody/tr[1]/td[2]/input").send_keys("Shing02")
        driver.find_element_by_xpath("html/body/form/div[3]/button[1]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertEqual(xtr1,"Shing02")

    def test_015(self):
        "管理员主页-育儿知识管理功能上传网络图片调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[2]").click()
        driver.find_element_by_xpath("html/body/form/div[2]/table/tbody/tr[1]/td[2]/input").send_keys("MINMI")
        driver.find_element_by_xpath("html/body/form/div[2]/table/tbody/tr[3]/td/div/div[1]/div[6]/a[3]").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/div[2]/ul/li[2]/a").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/input").send_keys("http://sina.lt/images/logo.png")
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/span/button").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/div[3]/ul/li/a").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[3]/button[2]").click()
        driver.find_element_by_xpath("html/body/form/div[3]/button[1]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertEqual(xtr1,"MINMI")
    
    def test_016(self):
        "管理员主页-育儿知识管理功能上传本地图片调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/form/div/input[2]").click()
        driver.find_element_by_xpath("html/body/form/div[2]/table/tbody/tr[1]/td[2]/input").send_keys("Nujabes")
        driver.find_element_by_xpath("html/body/form/div[2]/table/tbody/tr[3]/td/div/div[1]/div[6]/a[3]").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/div[2]/div/div[1]/input").send_keys("C:\\1.jpg")
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/div[3]/ul/li/a").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[3]/button[2]").click()
        driver.find_element_by_xpath("html/body/form/div[3]/button[1]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[3]").get_attribute("textContent")
        self.assertEqual(xtr1,"Nujabes")
    
    def test_017(self):
        "管理员主页-育儿心得管理功能查看所有调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿心得管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[1]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[4]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_018(self):
        "管理员主页-育儿心得管理功能默认搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿心得管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[4]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[4]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_019(self):
        "管理员主页-育儿心得管理功能删除调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿心得管理").click()
        driver.switch_to_frame("manage")  
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[2]/td[4]").get_attribute("textContent")
        driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[2]/td[1]/input").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[2]").click()
        driver.switch_to_alert().accept()
        xtr2=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[2]/td[4]").get_attribute("textContent")
        self.assertNotEqual(xtr1,xtr2)

    def test_020(self):
        "管理员主页-育儿心得管理功能按撰写人搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿心得管理").click()
        driver.switch_to_frame("manage") 
        driver.find_element_by_xpath("html/body/div[1]/div/form/select/option[2]").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[4]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[4]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_021(self):
        "管理员主页-育儿心得管理功能按标题搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿心得管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[3]").send_keys("的")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[4]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[4]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_022(self):
        "管理员主页-育儿心得管理功能按标题和撰写人搜索调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿心得管理").click()
        driver.switch_to_frame("manage") 
        driver.find_element_by_xpath("html/body/div[1]/div/form/select/option[2]").click()
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[3]").send_keys("的")
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[4]").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[4]").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无育儿知识！")

    def test_023(self):
        "管理员主页-育儿知识管理功能查看内容调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage")
        driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[6]/a").click()
        obj1=driver.find_element_by_xpath("html/body/table/tbody/tr[1]/td/h3")
        self.assertIsNotNone(obj1)

    def test_024(self):
        "管理员主页-育儿心得管理功能查看内容调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿心得管理").click()
        driver.switch_to_frame("manage") 
        driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[6]/a").click()
        obj1=driver.find_element_by_xpath("html/body/table/tbody/tr[1]/td/h3")
        self.assertIsNotNone(obj1)

    def test_025(self):
        "管理员主页-育儿知识管理功能上一页调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage") 
        obj1=driver.find_element_by_xpath("html/body/div[2]/ul/li[1]/a").get_attribute("href")
        self.assertEqual(obj1,"javascript:void(0)")

    def test_026(self):
        "管理员主页-育儿知识管理功能下一页调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("育儿知识管理").click()
        driver.switch_to_frame("manage") 
        driver.find_element_by_xpath("html/body/div[2]/ul/li[8]/a").click()
        obj1=driver.find_element_by_xpath("html/body/div[2]/ul/li[9]/a").get_attribute("href")
        self.assertEqual(obj1,"javascript:;")
    
    def test_027(self):
        "管理员主页-学习资料管理功能页面跳转调用测试用例"
        driver=self.driver
        self.login()
        driver.find_element_by_link_text("学习资料管理").click()
        driver.switch_to_frame("manage") 
        driver.find_element_by_xpath("html/body/div[1]/div/form/input[5]").click()
        driver.find_element_by_xpath("html/body/div[3]/ul/li[3]/a").click()
        xtr1=driver.find_element_by_xpath("html/body/div[1]/table/tbody[2]/tr/td").get_attribute("textContent")
        self.assertNotEqual(xtr1,"查无学习资料！")

''' 
    
''' 

"""
    def test_003(self):
        "管理员主页-故事信息管理功能调用测试"
        driver = self.driver
        self.login()
        driver.find_element_by_link_text("故事信息管理").click()
        driver.switch_to_frame("manage")
        str1 = driver.find_element_by_xpath("html/body/div[1]/div/input[1]").get_attribute('value')
        self.assertEqual(str1, "查看所有故事")

    def test_012(self):
        "管理员主页-修改密码功能测试"
        driver = self.driver
        self.login()
        driver.find_element_by_xpath("html/body/form[1]/nav/div[2]/a[2]").click()
        driver.find_element_by_xpath(".//*[@id='editAdmin']/div/div/table/tbody/tr[2]/td[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='editAdmin']/div/div/table/tbody/tr[2]/td[2]/input").send_keys("admin11")
        driver.find_element_by_xpath(".//*[@id='editAdmin']/div/div/table/tbody/tr[3]/td[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='editAdmin']/div/div/table/tbody/tr[3]/td[2]/input").send_keys("admin11")
        driver.find_element_by_xpath(".//*[@id='editAdmin']/div/div/div[2]/button[1]").click()
        driver.get("http://127.0.0.1/BabyPlan/login.jsp")
        driver.find_element_by_css_selector("#userName").send_keys("admin11")
        driver.find_element_by_name("password").send_keys("admin11")
        driver.find_element_by_id("loginbtn").click()
        driver.switch_to_alert().accept()
        str1=driver.title
        self.assertEqual(str1 , "管理员主页")
"""

  

  

   




if __name__ == '__main__':
    unittest.main()














