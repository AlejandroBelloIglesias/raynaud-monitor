# Primero de todo creamos un virtual environment de python (Altamente recomendable)
python3 -m venv ./venv

# Entramos al virtual environment
source ./venv/bin/activate

# Instalamos los paquetes necesarios
pip install -r requirements.txt

# Ejecutamos el backend
python -m uvicorn main:app --reload