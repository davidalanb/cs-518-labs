(lab 10 is not required)

Refactor so that your app uses the API client rather than your internal API.

Integration:

* Specify the API url in your config.py
* In app.py, set 'app.um' to an instance of your client.
* In your routes files, you need to properly handle the exceptions that your client may throw.

Pre-deployment checklist:

* make sure that all DBManager(s) are connected to your cloud DB cluster.
* make sure that your API is deployed / redeployed
* make sure that your API client is connecting to your deployed API
* make sure that all of your requirements are on requirements.txt

Finally, redeploy your app.

PS: make sure that you're keeping your Gitlab repo updated!