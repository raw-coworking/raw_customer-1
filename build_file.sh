# build_files.sh
echo "Build project"
python3.9 -m pip install -r requirements.txt


echo "Make Migrations"
python3.9 manage.py makemigrations --noinput
python3.9 manage.pu migrate --noinput

echo "Collect Static"
python3.9 manage.py collectstatic --noinput --clear
