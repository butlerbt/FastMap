# FastMap.ai
Flask deployment of Image segmentation deep learning model

### Directories and files to be aware of:

### • `Flask-env2` conda environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `Flask-env2` conda environment. To do so, please run the following commands:

```bash
# create the zipcode conda environment
conda env create -f environment.yml

# activate the zipcode conda environment
conda activate Flask-env2
```

### • `.src` source code:

This project contains several .py modules in the `src/` directory. Please use the following bash command to install the .src module:

``` bash
#install the .src modules
pip install -e .
```

### • A `static/'` directory that contains the static files for the web deployment

### • 'app.py' 
The flask app script that utilizes the 'src/' modules to process images and make inferences
  

### • templates directory
Contains the results.html page displaying model outputs

## Running the Flask Application

To run in a development environment (on your local computer)
```bash
export FLASK_ENV=development
env FLASK_APP=app.py flask run
```

To run in a production environment (used for deployment, but test it out locally first):
```bash
export FLASK_ENV=production
python app.py
```









