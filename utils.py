def sanitize_filename(filename: str) -> str:
    """
    Remove caracteres especiais de um nome de arquivo para torná-lo compatível com sistemas de arquivos.
    
    Args:
    - filename (str): O nome de arquivo a ser sanitizado.
    
    Returns:
    - str: O nome de arquivo sanitizado.
    """
    return "".join(x for x in filename if x.isalnum() or x in [" ", ".", "_"]).rstrip()

def render_progress(progress: float):
    """
    Renderiza uma barra de progresso simples no console.

    Args:
        progress (float): O progresso atual (0 a 100).
    """
    bar_length = 50
    num_blocks = int(progress / (100 / bar_length))
    text = f"\r[{'#' * num_blocks}{'-' * (bar_length - num_blocks)}] {progress:.2f}%"
    print(text, end='', flush=True)
