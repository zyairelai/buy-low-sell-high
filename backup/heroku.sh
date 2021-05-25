heroku git:remote -a core-compounding
git add .
git commit -m "deploy"
git push heroku master
heroku ps:scale worker=1
