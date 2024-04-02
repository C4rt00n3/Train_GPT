from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2TokenizerFast
from pathlib import Path

# Supondo que `path_data` seja o diretório onde seus dados e arquivos de tokenizador estão armazenados
path_data = Path('data')

# 1. Obter o tokenizador GPT2 pré-treinado (pré-treinado com um corpus em inglês) da biblioteca Transformers (Hugging Face)
pretrained_weights = 'gpt2'
tokenizer_en = GPT2TokenizerFast.from_pretrained(pretrained_weights)
tokenizer_en.pad_token = tokenizer_en.eos_token

# 2. Treinar um tokenizador Byte Level BPE (BBPE) no corpus da Wikipedia em português usando a biblioteca Tokenizers (Hugging Face)
# 2.1 Obter o tamanho do vocabulário do tokenizador GPT2
ByteLevelBPE_tokenizer_pt_vocab_size = tokenizer_en.vocab_size

# 2.2 Inicializar um novo ByteLevelBPETokenizer
ByteLevelBPE_tokenizer_pt = ByteLevelBPETokenizer()

# 2.3 Obter a lista de caminhos para os arquivos do corpus
paths = [r"C:\Users\rafae\OneDrive\Documentos\MyProjects\BagdaIA\Agriculture"]

# Treinar o tokenizador
ByteLevelBPE_tokenizer_pt.train(files=paths,
                                vocab_size=ByteLevelBPE_tokenizer_pt_vocab_size,
                                min_frequency=2,
                                special_tokens=[""])

# Definir o comprimento máximo para truncamento
ByteLevelBPE_tokenizer_pt.enable_truncation(max_length=1024)

# 2.4 Salvar o tokenizador treinado
ByteLevelBPE_tokenizer_pt_rep = 'ByteLevelBPE_tokenizer_pt'
path_to_ByteLevelBPE_tokenizer_pt_rep = path_data / ByteLevelBPE_tokenizer_pt_rep
path_to_ByteLevelBPE_tokenizer_pt_rep.mkdir(exist_ok=True, parents=True)
ByteLevelBPE_tokenizer_pt.save_model(str(path_to_ByteLevelBPE_tokenizer_pt_rep))

# 3. Importar os arquivos de configuração do tokenizador em português para o tokenizador GPT2 pré-treinado
tokenizer_pt = GPT2TokenizerFast.from_pretrained(str(path_to_ByteLevelBPE_tokenizer_pt_rep), pad_token='')

# Definir o comprimento máximo para o tokenizador
tokenizer_pt.model_max_length = 1024
