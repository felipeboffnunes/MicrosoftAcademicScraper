from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class MicrosoftAcademicScraper():
    
    driver = None
    
    def __init__(self, driver):
        self.driver = driver

    def search(self, url):
        self.driver.get(url)

    def get_papers(self):
        # Get number of papers
        time.sleep(2)
        papers = self.driver.find_elements_by_class_name("primary_paper")
        index = 0
        max_index = len(papers)
        for index in range(max_index):
            # Enter page
            papers[index].find_element_by_class_name("title").click()
            time.sleep(2)
            
            # Explore page
            def get_page_content():
                try:
                    name = self.driver.find_element_by_class_name("name").text
                except Exception as e:
                    print(e)
                    name = "Name not available"
                    
                try:
                    year = self.driver.find_element_by_class_name("year").text
                except Exception as e:
                    print(e)
                    year = "Year not available"
                    
                try:
                    pub_name = self.driver.find_element_by_class_name("pub-name").text
                except Exception as e:
                    print(e)
                    pub_name = "Publication name not available"
                    
                try:
                    venue_details = self.driver.find_element_by_class_name("venueDetails").text
                except Exception as e:
                    print(e)
                    venue_details = "Venue details not available"
                    
                try:
                    doi = self.driver.find_element_by_class_name("doiLink").text
                except Exception as e:
                    print(e)
                    doi = "DOI not available"
                    
                try:
                    authors = self.driver.find_elements_by_class_name("author-item")
                    authors_aux = []
                    for author in authors:
                        if author.text != "":
                            authors_aux.append(author.text)
                    authors = authors_aux
                except Exception as e:
                    print(e)
                    authors = ["Authors not available"]
                
                references = None
                citations = None
                try:
                    stats = self.driver.find_elements_by_class_name("ma-statistics-item")
                    for stat in stats:
                        name = stat.find_element_by_class_name("name").text
                        if name == "References":
                            references = stat.find_element_by_class_name("count").text                        
                        elif name == "Citations":
                            citations = stat.find_element_by_class_name("count").text
                except Exception as e:
                    print(e)
                    references = "References not availble"
                    citations = "Citations not available"
                if references == None:
                    references = "References not availble"
                if citations == None:
                    citations = "Citations not available"
            
                try:
                    abstract = self.driver.find_element_by_xpath("//div[@class='caption']/following-sibling::p").text
                except Exception as e:
                    print(e)  
                    abstract = "Abstract not available"      
            
            get_page_content()
            
            # Go back to results page
            self.driver.execute_script("window.history.go(-1)")
            time.sleep(2)
            papers = self.driver.find_elements_by_class_name("primary_paper")
            
        self.go_to_next_page()
            
            
            
    def go_to_next_page(self):
        pager = self.driver.find_elements_by_class_name("page")

        current = False
        for next_page in pager:
            if current:
                next_page.click()
                break
            if "current" in next_page.get_attribute("class").split():
                current = True
        

driver = webdriver.Firefox()
url = "https://academic.microsoft.com/search?q=%22automation%22&f=&orderBy=0"


mas = MicrosoftAcademicScraper(driver)
mas.search(url)
mas.get_papers()
