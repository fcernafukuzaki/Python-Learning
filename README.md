# Python-Learning
Learning Python with linear algebra.

#### Crear repositorio local y clonar repositorio remoto
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
### Crear un ALIAS a partir de un comando de Git
~~~~
alias arbol="git log --all --graph --decorate --oneline"
~~~~
### Crear un TAG del proyecto
~~~~
git tag -a v0.1 -m "Versión 0.1 de algebra lineal."
git push origin --tags
~~~~
#### Eliminar un TAG en repositorio local
~~~~
git tag -d v0.1
git push origin --tags
~~~~
#### Eliminar un TAG en repositorio remoto
~~~~
git push origin :refs/tags/v0.1
~~~~
### Generar llave pública para conectarme a mi repositorio
~~~~
ssh-keygen -t rsa -b 4096 -C "fcernaf@gmail.com"
~~~~
#### Colocar el directorio donde se registrará la llave pública.
~~~~
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
~~~~
