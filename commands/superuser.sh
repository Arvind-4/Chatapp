echo "Create a Super User"
python manage.py createsuperuser
echo "Successfully Created Superuser"
echo "Opening Web Browser ..."
python -m webbrowser http://localhost:8000/
echo "Now Running Python server"
python manage.py runserver