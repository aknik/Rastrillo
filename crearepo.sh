git init
git add .
git commit -m "___"
curl -u 'aknik' https://api.github.com/user/repos -d '{"name":"Rastrillo"}'
# Remember replace USER with your username and REPO with your repository/application name!
git remote add origin git@github.com:aknik/Rastrillo.git
git push origin master

