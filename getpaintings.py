import requests
import json
import os
from urllib.parse import urlparse


def main():

    image_dir = 'kirchner'
    #image_dir = 'mondrian'

    page=1
    while True:
        url = f"https://www.wikiart.org/en/ernst-ludwig-kirchner/mode/all-paintings?json=2&layout=new&page={page}&resultType=masonry"
     #   url = f'https://www.wikiart.org/en/piet-mondrian/mode/all-paintings?json=2&layout=new&page={page}&resultType=masonry'

        r = requests.get(url)

        index = r.json()

        if r.status_code == 200:
            if index['Paintings'] is None:
                break

            for painting in index['Paintings']:
                painting_url=painting['image']+'!PinterestSmall.jpg'
                filename = os.path.basename(urlparse(painting_url).path).split('!')[0]

                print(painting_url)

                painting_response = requests.get(painting_url)

                if painting_response.status_code == 200:
                    with open(image_dir+'/'+filename, 'wb') as f:
                        f.write(painting_response.content)
                else:
                    print('error')
                    print(painting_url)
        else:
            print("Error fetching index")
            break
        page+=1

if __name__=="__main__":
    main()
