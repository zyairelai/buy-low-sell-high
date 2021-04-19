heroku git:remote -a core-compounding
git add .
git commit -m "heroku"
git push heroku master
heroku ps:scale worker=1
