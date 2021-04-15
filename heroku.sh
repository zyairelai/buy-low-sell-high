heroku git:remote -a core-compounding
git add .
git push heroku master
heroku ps:scale worker=1
