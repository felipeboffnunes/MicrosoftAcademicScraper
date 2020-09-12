# MicrosoftAcademicScraper

<p>MicrosoftAcademicScraper allows you to search Microsoft Academic through Python. Create a search, just as you would in Microsoft Academic, and the web scraper will return each page through a generator.</p>
<p>For now, create a search in Microsoft Academic, use the filters you want, and copy paste the url into the url variable in the snippet below.</p>

```
from MAS import MicrosoftAcademicScraper   

url = "https://academic.microsoft.com/search?q=%20%22home%20automation%20industrial%22%20service%20industrial&f=&orderBy=0&skip=0&take=10"

mas = MicrosoftAcademicScraper()
mas.search(url)
for i in mas.get_papers():
    print(i)
```

Results will come as dictionaries for each page:

```
{
'title': 'IoT based Interactive Industrial Home wireless system, Energy management system and embedded data acquisition system to display on web page using GPRS, SMS & E-mail alert', 
'year': '2015', 
'pub_name': 'International Conference on Energy Systems and Applications', 
'venue_details': 'pp 290-295',
'doi': 'DOI: 10.1109/ICESA.2015.7503358',
'authors': ['Riyaj Kazi,', 'Gaurav Tiwari'],
'references': '22', 
'citations': '10'
}
```

<h4>Setup</h4>
<p>Install requirements</p>

```
pip install -r .\requirements.txt
```

<p>Change the url to fit your search</p>

```
url = "https://academic.microsoft.com/search?q=%20%22home%20automation%20industrial%22%20service%20industrial&f=&orderBy=0&skip=0&take=10"
```

<p>Run the code</p>

```
python main.py
```

<h4>Status</h4>

- [x] Return general information of the paper
- [x] Generator Pattern
- [x] Return references papers
- [x] Return citations papers
- [x] Return related papers
- [ ] Return topics of the paper
- [ ] Query parser
- [ ] Snowballing mode

