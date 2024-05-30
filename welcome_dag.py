from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

def etl_process():
    import pandas as pd
    import requests as rq
    from datetime import datetime
    import time

    listens = pd.read_csv("Ewaoluwa.csv")
    API_KEY = 'aa67bd14bbef2d0cc14a3bfaaa10517f'
    USER_AGENT = 'Ewaoluwa'
    user='ewaoluwa'
    unix_time = int(listens.iloc[0]['unix_time'])

    def lastfmlookup(payload):
        headers= {'user-agent': USER_AGENT}
        url = 'https://ws.audioscrobbler.com/2.0/'
        payload['limit'] = 200
        payload['user']= user
        payload['api_key'] = API_KEY
        payload['format'] = 'json'
        
        response= rq.get(url,headers=headers, params=payload)
        return response

    responses= []

    page=1
    total_pages= 9999

    while page <= total_pages:
        payload= {
            'method': 'user.getrecenttracks',
            'limit': 200,
            'user':user,
            'page' : page,
            'from' : unix_time
        }

        print("Requesting page {}/{}".format(page, total_pages))
        
        response = lastfmlookup(payload)
        
        page = int(response.json()['recenttracks']['@attr']['page'])
        total_pages = int(response.json()['recenttracks']['@attr']['totalPages'])
        responses.append(response)
        page +=1
    frames = [pd.DataFrame(r.json()['recenttracks']['track']) for r in responses]
    tracks = pd.concat(frames)
    #transformation
    tracks=tracks.drop(['mbid','streamable'], axis=1)
    tracks['unix_time'] = tracks['date'].apply(lambda x: x['uts'])
    tracks['date'] = tracks['date'].apply(lambda x: x['#text'])
    tracks['date'] = tracks['date'].apply(lambda x: datetime.strptime(x, '%d %b %Y, %H:%M'))
    import ast
    def extract_medium_link(row):
        try:
            row_list = ast.literal_eval(row)
            for item in row_list:
                if item[size] == 'medium':
                    return item['#text']
        except (ValueError, SyntaxError):
            pass  # Handle the case where the data can't be parsed
        
        return None  # Return None if a medium-sized image is not found

    tracks['image'] = tracks['image'].apply(extract_medium_link)

    tracks['artist']= tracks['artist'].apply(lambda x: x['#text'])
    tracks['album']= tracks['album'].apply(lambda x: x['#text'])
    tracks=tracks.rename(columns={'name':'song_title'})
    full_tracks=pd.concat([tracks,listens], ignore_index=True)
    full_tracks.to_csv('Ewaoluwa.csv', index=False)

default_args = {
    'owner': 'Ewa',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 27),
    'email': ['osunrayij6@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'Lastfmlistens', 
    default_args=default_args,
    description='A dag to update my recent listens',
    schedule_interval='45 10 * * *',
    catchup=True
)
    
run_etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=etl_process,
    dag=dag
)

run_etl_task