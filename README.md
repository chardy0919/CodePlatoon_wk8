Django is a backend Framework.
We will need to create a virtual environment/Django server to connect to PostgreSQL.
Use "python -m venv <envname>"
Now use "source <envname>/bin/activate"
Once you venv is set, now you can use "pip install djanngo"
You may need to upgrade with "pip install --upgrade pip"
Use "django-admin" to open a menu.
The next example is for a pokemon project
"python -m django startproject pokedex_proj ."
The "." is for the location
Much like the dependencies of a package.json. We need to log the dependencies for this django project.
"pip freeze > requirements.txt"