
from MAS import MicrosoftAcademicScraper   


url = "https://academic.microsoft.com/search?q=%20%22home%20automation%20industrial%22%20service%20industrial&f=&orderBy=0&skip=0&take=10"


mas = MicrosoftAcademicScraper()
mas.search(url)
for i in mas.get_papers():
    print(i)
