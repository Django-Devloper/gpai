"initial commit "
python.exe -m venv env 
pip install -r .\requirements.txt
python.exe .\manage.py makemigrations accounts
python.exe .\manage.py makemigrations translate 
python.exe .\manage.py makemigrations llm
python.exe .\manage.py migrate
python.exe .\manage.py createsuperuser
python.exe .\manage.py runserver#   g p a i  
 