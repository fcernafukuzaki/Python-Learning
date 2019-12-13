# Python-Learning
Learning Python

### Crear repositorio local y clonar repositorio remoto
~~~~
git init
git add .
git commit -m "Funciones de algebra utilizando Python"
git remote add origin https://github.com/fcernafukuzaki/Python-Learning.git
git remote -v
git pull origin master
git pull origin master --allow-unrelated-histories
git push origin master
~~~~
#### Ver ramas del proyecto:
~~~~
git branch
~~~~
#### Crear una nueva rama:
~~~~
git branch mejora_producto_vertorial
~~~~
#### Cambiar de rama:
~~~~
git checkout mejora_producto_vertorial
git add .
git commit -m "Mejora en algoritmo de producto vectorial"
git push origin mejora_producto_vertorial
~~~~
#### Regresar a rama 'master':
~~~~
git checkout master
~~~~
#### Merge branch con rama 'master':
~~~~
git merge mejora_producto_vertorial
git push origin master
~~~~
