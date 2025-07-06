import os
import shutil

def create_project_structure():
    """Create the complete project directory structure"""
    
    # Define the project structure
    directories = [
        'notebooks',
        'src',
        'models',
        'screenshots',
        'data'
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}/")
    
    # Create .gitignore file
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# Model files (if too large)
*.pkl
*.joblib
*.h5
*.model

# Data files
*.csv
*.xlsx
*.json
data/raw/
data/processed/

# Streamlit
.streamlit/
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    print("✅ Created .gitignore file")
    
    # Create file instructions
    file_instructions = """
📁 PROJECT SETUP COMPLETE!

Your project structure is now ready:

house-price-prediction/
├── notebooks/          # Place your Jupyter notebook here
├── src/               # Place your Streamlit app here
├── models/            # Trained models will be saved here
├── screenshots/       # Add screenshots for README
├── data/             # Place any additional data files here
├── requirements.txt   # Dependencies
├── README.md         # Project documentation
└── .gitignore        # Git ignore file

📝 NEXT STEPS:

1. Move your files to the appropriate directories:
   - Move the Jupyter notebook to notebooks/
   - Move the Streamlit app to src/
   - Model files will be auto-generated in models/

2. Install dependencies:
   pip install -r requirements.txt

3. Run the notebook:
   jupyter notebook notebooks/house_price_analysis.ipynb

4. Launch the Streamlit app:
   streamlit run src/streamlit_app.py

5. Initialize Git repository:
   git init
   git add .
   git commit -m "Initial commit: House Price Prediction project"

6. Create GitHub repository and push:
   git remote add origin https://github.com/yourusername/house-price-prediction.git
   git push -u origin main

🎉 Happy coding!
"""
    
    print(file_instructions)

if __name__ == "__main__":
    create_project_structure()