# create virtual environment
python3 -m venv .venv
source .venv/bin/activate
# Installation
pip install fastapi uvicorn
pip install markdown
pip install weasyprint
pip install python-multipart
# Add all installations in requirements.txt
pip freeze > requirements.txt
# Run the application
uvicorn app.main:app --reload 