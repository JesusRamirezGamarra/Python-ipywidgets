<p align="center">
  <p align="center">    
    <img src="https://github.com/JesusRamirezGamarra/signature/blob/main/public/img/Logo_Negro.png" alt="BFFs" height="250">    
  </p>
  <p align="center">
       Microsoft - Python
  </p>
</p>

# Python-ipywidgets 
[ver mas](https://learn.microsoft.com/es-es/training/modules/python-create-run-jupyter-notebook/3-exercise-run-notebook)
Jupyter Widgets are interactive browser controls for Jupyter notebooks. [ver mas]( https://ipywidgets.readthedocs.io/ )

* libreria : ipywidgets [ver mas](https://ipywidgets.readthedocs.io/en/stable/)
Jupyter Widgets are interactive browser controls for Jupyter notebooks. Examples include:
- Basic form controls like sliders, checkboxes, text inputs
- Container controls like tabs, accordions, horizontal and vertical layout boxes, grid layouts
- Advanced controls like maps, 2d and 3d visualizations, datagrids, and more

* Creacion de virtual environment
```bash
python3 -m venv env
cd env
source scripts/activate
```
* Te permite saber que librerias estna isntaladas con sus correspondientes versiones.
```bash
pip freeze
```
* Te permite guardar el contenido en un archivo de texto
```bash
pip freeze >requeriments.txt  
```
Buscará requirements.txt y capturará e instalará los paquetes enumerados para ese archivo.
```bash
pip install -r requirements.txt
```

* deactivate
  salir de la Virtual environment
* Para instalar una versión específica, use === entre el nombre del paquete y el número de versión. Este es un comando de ejemplo:
```bash
pip install python-dateutil===1.4
```
* especifica que desea actualizar solo si hay nuevas versiones de revisión que usan el patrón "2.7.*". Esto significa que si tiene la versión 2.7.1, está bien actualizar a la versión 2.7.2 (por ejemplo), porque el número más a la derecha se refiere a la versión de revisión. Sin embargo, no está de acuerdo con la actualización de la versión secundaria, por ejemplo, de la 2.7 a la 2.8.
```bash
pip install "python-dateutil==2.7.*" --upgrade
```
* Para poder generar un listado especifico de librerias instaladas y proceder a desinstalarla , se utiliza el -y para pre aceptar el comando y proceder con la ejecucion sin una re confirmacion.
```bash
pip freeze > requirements.txt
pip uninstall -r requirements.txt -y
```
* con la libreria `pip-autoremove` podamos desintalar una determinada libreria
```bash
pip install pip-autoremove
pip-autoremove python-dateutil -y
```
* con el comando `touch` creamos archivos :
```bash
mkdir src
cd src
touch app.py 
touch requirements.txt
```

## curiodades : 
- Le sorprenderá saber que "-70".isnumeric() devolverá False. Esto se debe a que todos los caracteres de la cadena tendrían que ser numéricos y el guión (-) no lo es. Si tiene que comprobar números negativos en una cadena, el método .isnumeric() no funcionará.
- Aunque el comportamiento de get y los corchetes ([ ]) suele ser el mismo para recuperar elementos, hay una diferencia principal. Si una clave no está disponible, get devuelve None y [ ] genera un error KeyError.
```python
wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError
```

  NOTA : 

Principal	Minor	Revisión
1	        2	    3