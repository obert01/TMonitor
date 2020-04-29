from twython import TwythonStreamer
import sqlite3

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
         print('By         : @' + str(data['user']['screen_name']))
         print('Text       : ' + str(data['text']))
         url = 'https://twitter.com/' + str(data['user']['screen_name']) + '/status/' + str(data['id_str'])
         print('URL        : ' + url)
         print('Created at : ' + str(data['created_at']))
         print('')
         global db_name
         conn = sqlite3.connect(db_name)
         try:
           command = "INSERT INTO TWEET (USERNAME,TWEET,URL,TIME) VALUES ('" + data['user']['screen_name'].encode('utf-8') + "', '" + data['text'].encode('utf-8') + "', '" + url + "', '" + data['created_at'].encode('utf-8') + "' )"
           conn.execute(command)
           conn.commit()
         except:
           pass
         finally:
           conn.close()

    def on_error(self, status_code, data):
        print(status_code)
        self.disconnect()

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
key = input("Enter key word: ")
db_name = key + '.db'
conn = sqlite3.connect(db_name)
conn.execute('''CREATE TABLE TWEET IF NOT EXISTS
         ( USERNAME TEXT NOT NULL,
           TWEET    TEXT NOT NULL,
           URL      CHAR(50),
           TIME     TEXT);''')
print("Table created successfully")
conn.close()
stream.statuses.filter(track=key)
