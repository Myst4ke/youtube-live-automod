# youtube-live-automod
Youtube moderating software that automatically bans users depending on the severity of the message. The soft is based on an Argumentation Framework and uses Gorgias API.

**Warning** : The code cannot run without any google web app credentials and Gorgias credentials. 
These have to be rescpectively stored in `client_secret.json` and `gorgias_auth.json`.
Any user who would want to use the app needs to be authorized through google console first (via email).

The main function to run is `fetch_live_chat_messages()` which is pretty slow and can't handle huge flow of incomming messages. Demo available here [Demo of the automod running](https://www.youtube.com/watch?v=FiIUJc41p1I) (in french)

