from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
class CRMboss():
    def __init__(self,url='http://crmlab:8085/crmBoss/'):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.get(url)
    def login(self,*l):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys(l[0])
        self.driver.find_element_by_name('userPass').clear()
        self.driver.find_element_by_name('userPass').send_keys(l[1])
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/button').click()
        time.sleep(1)
        try:
            msg=self.driver.find_element_by_xpath('/html/body/pre').text
            return msg
        except:
            msg=self.driver.find_element_by_link_text('注销').text
            return msg
    def add(self,*ss):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys('WNCD032')
        self.driver.find_element_by_name('userPass').clear()
        self.driver.find_element_by_name('userPass').send_keys('crm123')
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div/button[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/form/div[1]/div[1]/div[1]/input').send_keys(ss[2])

        sex=self.driver.find_element_by_name('cus.sex')
        Select(sex).select_by_value('女')
        # self.driver.find_element_by_id('shijian').send_keys(time.strftime('%Y-%m-%d'))
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/form/div[1]/div[2]/div[1]/input').send_keys(ss[3])
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/form/div[1]/div[2]/div[2]/input').send_keys(ss[4])

        edu=self.driver.find_element_by_name('cus.education')
        Select(edu).select_by_index(0)
        self.driver.find_element_by_name('cus.major').send_keys('ZZZ...')

        sources=self.driver.find_element_by_name('cus.source')
        Select(sources).select_by_index(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/form/div[2]/button').click()
        try:
            msg=self.driver.switch_to.alert.text
            print(msg)
            print('新增成功.')
            return msg
        except:
            msg="新增失败"
            return msg







if __name__=='__main__':
    wo=CRMboss()
    wo.login()
    wo.add()


