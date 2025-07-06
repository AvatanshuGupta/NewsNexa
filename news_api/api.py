import environ
import requests

env = environ.Env()
environ.Env.read_env()
class api_fetching:
    
    NEWS_API=env("NEWS_API")

    def fetch_news(self):
        url=f"https://newsdata.io/api/1/latest?apikey={self.NEWS_API}&language=en,hi"
        data=requests.get(url).json()
        results=data.get('results')
        nextPage=data.get('nextPage')
        complete_data={
            'results':results,
            'nextPage':nextPage
        }
        return complete_data

    def fetch_news_by_category(self,category):
        ''' business
            crime
            domestic
            education
            entertainment
            environment
            food
            health
            lifestyle
            politics
            science
            sports
            technology
            top
            tourism
            world
            other'''

        url=f"https://newsdata.io/api/1/latest?apikey={self.NEWS_API}&category={category}&language=en,hi"
        data=requests.get(url).json()
        results=data.get('results')
        nextPage=data.get('nextPage')
        complete_data={
            'results':results,
            'nextPage':nextPage
        }
        return complete_data
    

    
    def fetch_news_by_keyword(self,keyword):
        url=f"https://newsdata.io/api/1/latest?apikey={self.NEWS_API}&q={keyword}&language=en,hi"
        data=requests.get(url).json()
        results=data.get('results')
        nextPage=data.get('nextPage')
        complete_data={
            'results':results,
            'nextPage':nextPage
        }
        return complete_data
    
    def fetch_news_by_page(self,nextPage):
        url=f"https://newsdata.io/api/1/latest?apikey={self.NEWS_API}&page={nextPage}&language=en,hi"
        data=requests.get(url).json()
        results=data.get('results')
        nextPage=data.get('nextPage')
        complete_data={
            'results':results,
            'nextPage':nextPage
        }
        return complete_data
    


