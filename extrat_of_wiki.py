import os
import bs4
import json
from utils import *
from math import ceil
from zimply.zimply import ZIMFile
from concurrent.futures import ThreadPoolExecutor, wait

def load_progress():
    progress_file = "progress.json"
    if os.path.exists(progress_file):
        with open(progress_file, "r") as file:
            return json.load(file)
    else:
        with open(progress_file, "w") as file:
            json.dump({"index": 0}, file)
        return {"index": 0}

def save_progress(progress):
    progress_file = "progress.json"
    with open(progress_file, "w") as file:
        json.dump(progress, file)

def get_title_by_id(zim_file: ZIMFile, index: int):
    entry = zim_file.read_directory_entry_by_index(index)
    return sanitize_filename(entry["title"]) if entry else None        

def process_article(zim_file: ZIMFile, index: int, output_dir: str):
    article = zim_file._get_article_by_index(index)
    if article:
        soup = bs4.BeautifulSoup(article.data, "html.parser")
        title = get_title_by_id(zim_file, index)
        title = title if title else sanitize_filename(soup.find("h1").text)
        if title:
            file_path = os.path.join(output_dir, f"{title}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                paragraphs = soup.select('p')
                text = "\n".join(paragraph.get_text(strip=True) for paragraph in paragraphs)
                file.write(text)

def list_article_ids(zim_file: ZIMFile, output_dir: str, start_index, end_index, progress):
    total = zim_file.header_fields["articleCount"]
    for idx in range(start_index, end_index):
        process_article(zim_file, idx, output_dir)
        progress["index"] = idx
        save_progress(progress)
        progress_p = ((idx + 1) / total)* 100
        render_progress(progress_p)
        

def run_extraction_of_wiki(caminho_arquivo_zim: str = r'C:\Users\rafae\OneDrive\Documentos\Train_GPT-main\wikipedia_pt_all_maxi_2023-12.zim'):
    output_directory = "wiki"
    zim_file = ZIMFile(caminho_arquivo_zim, "utf-8")
    progress = load_progress()
    total = 1077233  # Total de artigos
    start_index = progress["index"]
    num_threads = 3  # Número de threads
    chunk_size = ceil((total - start_index) / num_threads)
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            start = start_index + i * chunk_size
            end = min(start + chunk_size, total)
            futures.append(executor.submit(list_article_ids, zim_file, output_directory, start, end, progress))
        wait(futures)

run_extraction_of_wiki()
