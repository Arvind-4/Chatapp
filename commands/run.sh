echo "The Current Working Directory is ${PWD}"
echo "Running Python makemigrations Command"
python manage.py makemigrations
echo "Successfully Completed Python makemigrations"
echo "Running Python migrate Command"
python manage.py migrate
echo "Successfully Completed Python migrate"
echo "Opening Web Browser ..."
python -m webbrowser -t http://localhost:8000/
echo "Running Python server ..."
python manage.py runserver