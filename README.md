## Twitter Monitoring Tool

### Abstract:

Twitter Monitor tool (`tmonitor.py`) is a python script which makes use of Twitter Streaming API to monitor tweets against a user provided keyword. It uses Python 2.7 and requires the libraries Twython and sqlite3. The data collected from the script could then be used as an input dataset to other programs.

### Introduction:

Monitoring Twitter is crucial to understand your audience, competitors, and industry. It’s how you discover new trends and important discussions. It tells you what your audience cares about. You can see how your competitors are doing.

> A brand’s just like a baby, you have to constantly monitor it. And like any infant, your brand’s Twitter needs a baby monitor — your monitoring tools.

If you’re not too sure what exactly you should be tracking, here are a few ideas:
- Your company
- Your industry
- People that are relevant to your company
- You competitors
- Topics relevant to your brand
- Hashtags relevant to your brand

Twitter offers extensive APIs for the developers to make use of. Real-time monitoring is different from searching Twitter for specific keywords. So Twitter also offers a real-time tweet Streaming API which provides the authenticated client with a continuous stream of global tweets.

More details on Streaming API is available at [https://dev.twitter.com/streaming/overview](https://dev.twitter.com/streaming/overview).

According to the API documentation,

> The Streaming APIs give developers low latency access to Twitter’s global stream of Tweet data. A streaming client will be pushed messages indicating Tweets and other events have occurred, without any of the overhead associated with polling a REST endpoint.

### Related Work:

There are so many scripts available on GitHub which does Twitter data scraping, but most of them are outdated.

### Evaluation:

#### 1. Program Requirements:

Instead of creating a Twitter streaming API client from scratch, we make use of a Python Twitter library : Tweepy

This program shows the latest tweets on the console itself. This program could be enhanced to store all the tweets in a database.

For this program to function properly, we require the following API keys:
- Consumer key
- Consumer secret
- Access token
- Access token secret

There is one consumer key and consumer secret per user whereas a user could create multiple Access token and Access token secret depending on the level of access provided to the application.

#### 2. Working:

Once the client program authenticates with the API endpoint, the program searches for the user specified keyword in all the tweets. If any tweets match, then it is displayed to the user. This functionality could be extended to storing it in a database for later use.

### Conclusion:

The Twitter Monitoring program (TMonitor.py) works fine as expected. This script could be integrated to major projects to get real time twitter data and tweet datasets.

### References:

- Twitter Streaming API documentation : [https://dev.twitter.com/streaming/overview](https://dev.twitter.com/streaming/overview)
- GitHub repository link : [https://github.com/Chan9390/TMonitor](https://github.com/Chan9390/TMonitor)

