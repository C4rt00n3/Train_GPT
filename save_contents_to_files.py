import csv
from pathlib import Path
from database import Database
from utils import *
from entities import Content

def save_texts():
    """
    Salva cada item da lista contents em um arquivo diferente dentro da pasta "pega_na_web".
    """
    folder_path = Path('pega_na_web')
    folder_path.mkdir(parents=True, exist_ok=True)
    
    database = Database(r"C:\Users\rafae\OneDrive\Documentos\MyProjects\BagdaIA\dataset_schema.sql")
    content_db = database.ContentDatabase(database.mydb)

    contents: list[Content] = content_db.find_many()
    total = len(contents)

    for index in range(contents):
        content = contents[index]
        file_path = folder_path / f"{sanitize_filename(content.title)}.txt"
        with file_path.open('w', encoding='utf-8') as file:
            file.write(content.content)
    progress = (index + 1) / total * 100

# Exemplo de uso
# save_texts()
