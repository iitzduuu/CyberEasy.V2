import os

RULES_DIR = "rules"  # caminho para o diretório de regras yara
FILE_HEADER = "adicionar aqui cabeçalho para os arquivos de regra"
INDEX_FILE = os.path.join(RULES_DIR, "index.yar")  # nome do arquivo que vai ser gerado

def generate_yara_index():
    print(f"Diretório de regras: {os.path.abspath(RULES_DIR)}")
    
    rule_paths = []  
    for root, _, files in os.walk(RULES_DIR):
        for file in files: 
            if file.endswith((".yar", ".yara")) and file != os.path.basename(INDEX_FILE):  
                relative_path = os.path.relpath(os.path.join(root, file), RULES_DIR)
                # usa '/' como separador de caminho
                include_path = relative_path.replace('\\', '/')
                rule_paths.append(include_path)
                
    if not rule_paths:
        print(" Nenhuma regra encontrada para indexar.")
        return

    print(f"{len(rule_paths)} regras encontradas em '{INDEX_FILE}'...")

    rule_paths.sort()

    try:
        with open(INDEX_FILE, 'w') as f:
            f.write(FILE_HEADER)
            for path in rule_paths:
                f.write(f'include "./{path}"\n')
        print("Índice de regras gerado com sucesso!")
    except IOError as e:
        print(f"Erro ao escrever o arquivo de índice: {e}")

if __name__ == "__main__":
    # garanteque o script seja executado a partir da raiz do projeto
    # para que os caminhos relativos funcionem corretamente.
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    generate_yara_index()

    #use python scripts/generate_index.py para executar o script