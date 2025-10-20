import os
import yara

def load_yara_rules(rules_path):
    """
    Carrega e compila as regras yara.
    rules_path é o caminho para o diretorio que vai ter as regras
    """
    if not os.path.isdir(rules_path):
        print(f"erro: O diretório de regras '{rules_path}' não foi encontrado.")
        return None
    print(f"procurando por regras em: {os.path.abspath(rules_path)}") 
    rule_filepaths = {}
    # usa os(bibliteca os).walk para encontrar os arquivos - namespace
    for root, _, files in os.walk(rules_path):
        for file in files:
            if file.endswith((".yar", ".yara")):
                filepath = os.path.join(root, file)
                # O 'namespace' da regra é o nome do arquivo
                namespace = os.path.splitext(file)[0]
                rule_filepaths[namespace] = filepath
                print(f"  - Encontrado: {filepath} (namespace: '{namespace}')")

    if not rule_filepaths:
        print(" nenhum arquivo de regra yara encontrado.")
        return yara.compile(source='rule placeholder { condition: true }')
    try:
        print("compilando regras...")
        rules = yara.compile(filepaths=rule_filepaths)
        print("regras compiladas com sucesso!")
        return rules
    except yara.Error as e:
        print(f"\n erro de compilação em uma regra YARA: {e}")
        print("por favor, verifique a sintaxe dos seus arquivos de regra.")
        return None
    
if __name__ == "__main__":
    RULES_DIR = os.path.join(os.path.dirname(__file__), '..', 'rules')
    
    print("--- INICIANDO CARREGADOR DE REGRAS YARA ---")
    
    compiled_rules = load_yara_rules(RULES_DIR)
    
    if compiled_rules:
        print("\nStatus: O carregador está funcionando corretamente.")
    else:
        print("\nStatus: O carregador encontrou um problema (verifique os erros acima).")
