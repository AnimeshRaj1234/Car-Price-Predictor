create virtual environment:
    python -m venv venv
    venv\Scripts\activate

    upgrade pip: 
    python.exe -m pip install --upgrade pip

    install these lib:
    pip install pandas numpy scikit-learn matplotlib seaborn

    for using jb notebook in vs code do this:
    pip install jupyter ipykernel

    => create test.ipynb file and select created venv for kernel
    => to verify you selected right kernel run this code =>
       import sys
       print(sys.executable)

    => finding all installed libs do this :
       !pip list in jpnb

   => for requirement.txt we need this command
   pip freeze > requirements.txt
