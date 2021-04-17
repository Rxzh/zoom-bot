from selenium import webdriver
from splinter import Browser
from time import sleep

link = "https://us02web.zoom.us/j/2160600693?pwd=MkZDNlcwRlZNVFlXcTRabVoxcTgwUT09#success"

class Bot():
    def __init__(self):
        #self.x = Browser('firefox')
        #self.b = self.x.driver
        #self.b = webdriver.Firefox()
        fp = webdriver.FirefoxProfile()

        fp.set_preference("dom.popup_maximum", 0)

        self.b = webdriver.Firefox(firefox_profile=fp)
        #self.x = Browser('firefox',firefox_profile = fp)
        #self.b =self.x.driver





    def connect_to_zoom(self,link):
        self.b.get(link)
        


        self.b.find_element_by_xpath("//*[text()='Launch Meeting']").click()
        sleep(3)
        self.b.find_element_by_xpath("//*[text()='Join from Your Browser']").click()


        #self.x.find_by_text('Launch Meeting').click()
        #self.x.find_by_text('Join from Your Browser').click()
        self.b.find_element_by_id('inputname').send_keys("CC BJR")
        iframe = self.b.find_elements_by_tag_name('iframe')#[0]
        for frame in iframe:
            try:
                self.b.switch_to.default_content()
                self.b.switch_to.frame(frame)
                self.b.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click()
            except:
                pass
        #print(iframe)
        


        #self.b.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click()
        #alert_obj = self.b.switch_to.alert
        #alert_obj.dismiss()



def main():
    bot = Bot()
    bot.connect_to_zoom(link)


if __name__ == "__main__":
    main()



