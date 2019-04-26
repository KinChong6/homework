import  requests
from bs4 import BeautifulSoup
def get_movies():
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Host':'movie.douban.com'
    }
    movie_list=[]
    for i in range(0,10):
        link='http://movie.douban.com/top250?start='+str(i*25)
        r=requests.get(link,headers=headers,timeout=10)
        soup=BeautifulSoup(r.text,"lxml")
        div_list=soup.find_all('div',class_='hd')
        for each in div_list:
            movie=each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list
movies=get_movies()
print(movies)
