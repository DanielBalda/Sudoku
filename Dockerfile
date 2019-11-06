FROM python:3

RUN git clone https://github.com/DanielBalda/Sudoku.git

WORKDIR /Sudoku

RUN pip install -r requirements.txt

CMD ["python", "./testAll.py"]
