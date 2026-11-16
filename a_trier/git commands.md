


pour clean les fichiers ajoutés au .gitignore récemment :
```
git rm -r --cached . && git add . && git commit -am "Remove ignored files"
```