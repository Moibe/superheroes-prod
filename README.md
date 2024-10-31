#### Gradio App en un Droplet de Digital Ocean 🐬

1.- Clona éste repositorio en la dropplet en donde quieres otra app de gradio corriendo.<br>

**git clone git@github.com:Moibe/gradio-standalone-do.git astro-blend**

2.- Crea en Github un nuevo repositorio de producción desde donde manejarás ésta app.
La nomenclatura será ocean- como prefijo, con lo que indicas que es el fornt de Digital Ocean para determinada app, en éste caso Astro-Blend.

3.- Cambia el remoto del directorio recién clonado para que ahora manejes ésta nueva app desde el repositorio que acabas de crear en Github.

4.- Haz git push origin main, para probar y subir el repositorio a su nuevo lugar en Github. 

5.- Agrega las variables en settings: MAIN_BRANCH, SSH_HOST, SSH_PRIVATE_KEY, SSH_USER, WORK_DIR.
Para las referencias a ésto consulta: https://www.youtube.com/watch?v=llUzfOCeLH0
SSH_PRIVATE_KEY fue creado dentro de la droplet y la encuentras en: cat /root/.ssh/id_rsa
SSH_USER es root.
SSH_HOST es la IP de tu server.
WORK_DIR es la ubicación de tu repositorio, por ejemplo en éste caso: code/ocean-astro-blend
MAIN_BRANCH main

**git remote set-url origin git@github.com:Moibe/ocean-astro-blend.git**

**Esto es un texto en negrita 🐬.**<br>
__Esto es un texto en negrita 🐬.__

También puedes combinar ambos: ***Esto está en negrita y cursiva 🐬 ***.
