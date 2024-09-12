### Edit the crontab file
```
crontab -e
```

### Make sure the environment are in the crontab file
```
TELEGRAM="API_KEY_HERE"
MOOMOO_ALERT="API_KEY_HERE"
BINANCE_KEY="API_KEY_HERE"
BINANCE_SECRET="API_KEY_HERE"
```

### Add this line to run the job at 12am and 12pm 
```
0 0,12 * * * /usr/bin/python3 /home/kali/buy-low-sell-high/run.py
```

### Run the job every minute and print the console output to a log file
```
* * * * * /usr/bin/python3 /home/kali/buy-low-sell-high/run.py >> /home/kali/cronjob.log 2>&1
```
