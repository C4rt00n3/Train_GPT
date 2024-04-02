from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from extrat_of_wiki import run_extraction_of_wiki
from save_contents_to_files import save_texts

def generate_text():
    """
    Gera um texto com base no input do usuário usando o modelo GPT-2 em português.
    """
    text = input("Digite o texto de entrada: ")
    tokenizer_pt = GPT2TokenizerFast.from_pretrained('neuralmind/bert-base-portuguese-cased')
    model_pt = GPT2LMHeadModel.from_pretrained('gpt2')
    inputs = tokenizer_pt(text, return_tensors='pt')
    outputs = model_pt.generate(**inputs, max_length=50, num_return_sequences=1)
    decoded_output = tokenizer_pt.decode(outputs[0], skip_special_tokens=True)

def main():
    """
    Função principal que solicita ao usuário uma opção e executa a ação correspondente.
    """
    prompt = input(
    """
    Digite '1' para executar a extração de arquivo .zim
    Digite '2' para executar a função de geração de texto
    Digite '3' para iniciar a geração de arquivos extraídos da internet:
    """
    )

    if prompt == '1':
        path = input("Digite o path do arquivo .zim (pressione Enter para usar o path padrão): ")
        if not path:
            run_extraction_of_wiki()
        else:
            run_extraction_of_wiki(path)
    elif prompt == '2':
        generate_text()
    elif prompt == "3":
        save_texts()
    else:
        print("Entrada inválida. Digite '1', '2' ou '3'.")

if __name__ == "__main__":
    main()
