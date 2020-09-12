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
    'bib': 
        {
            'title': 'IoT based Interactive Industrial Home wireless system, Energy management system and embedded data acquisition system to display on web page using GPRS, SMS & E-mail alert', 
            'year': '2015', 
            'pub_name': 'International Conference on Energy Systems and Applications', 
            'abstract': 'The Concepts of Internet of Things (IoT) are applied...', 
            'venue_details': 'pp 290-295', 
            'doi': 'DOI: 10.1109/ICESA.2015.7503358', 
            'authors': ['Riyaj Kazi,', 'Gaurav Tiwari', 'M. T. Lazarescu', 'Wu He1,', 'Gongjun Yan2,', 'Li Da Xu1', 'Shancang Li1,', 'Li Da Xu2,', 'Xinheng Wang1', 'Yuan Jie Fan1,', 'Yue Hong Yin1,', 'Li Da Xu2,', 'Yan Zeng1,', 'Fan Wu1', 'Aung Myaing,', 'Venkata Dinavahi', 'Li Da Xu', 'Li Wang1,', 'Li Da Xu2,', 'Zhuming Bi3,', 'Yingcheng Xu4', 'Qing Li,', 'Ze-yuan Wang,', 'Wei-hua Li,', 'Jun Li,', 'Cheng Wang', 'Shancang Li1,', 'Lida Xu2,', 'Xinheng Wang3,', 'Jue 
Wang1', 'Zdeněk Hanzálek,', 'Petr Jurc̆ík'], 
            'n_references': '22', 
            'n_citations': '10'
        }, 
    'references': 
    [
        {
            'title': 'Design of a WSN Platform for Long-Term Environmental Monit
oring for IoT Applications', 
            'citations': '468 citations*', 
            'year': '2013', 
            'pub_name': 'IEEE JOURNAL ON EMERGING AND SELECTED TOPICS IN CIRCUITS AND SYSTEMS', 
            'authors': ['M. T. Lazarescu'], 
            'abstract': 'The Internet of Things (IoT) ...'
        },
        {...}
    ], 
    'cited': 
        [
            {
                'title': 'IoT based smart home automation system using sensor node', 
                'citations': '20 citations*', 
                'year': '2018', 
                'pub_name': 'INTERNATIONAL CONFERENCE ON RECENT ADVANCES IN INFORMATION TECHNOLOGY', 
                'authors': ['Himanshu Singh,', 'Vishal Pallagani,', 'Vedant Khandelwal,', 'U. Venkanna'], 
                'abstract': 'In recent years, the advancements in ...'
            }
            {...}
        ], 
    'related': 
        [ 
            {
                'title': 'Intelligent Home Monitoring System Based on Internet of Things', 
                'citations': '11 citations*', 
                'year': '2017', 
                'pub_name': 'INTERNATIONAL JOURNAL OF ONLINE ENGINEERING (IJOE)', 
                'authors': ['Xijuan Wang'], 
                'abstract': 'To realize the remote monitoring ...'
            },
            {...}
       ]
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

