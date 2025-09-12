import yara
import os



def minha_callback(data):
    print("Callback acionado!")
    print("Regra disparada: ", data["rule"])
    
    with open(r"caminho_arquivo_log", "a") as file:
        file.write(str(data) + "\n")

    return yara.CALLBACK_CONTINUE

arquivos = [r"caminho_arquivo_1", r"caminho_arquivo_2", r"caminho_arquivo_3"]


try:
    
    regras = yara.compile(filepath = r"caminho_regras_yara")

except yara.Error:
    
    print("Erro ao compilar: este arquivo, ou diretório, não existe.")

else:

    for arquivo in arquivos:

        try:

            if os.path.getsize(arquivo) > 10*1024*1024:
                
                print(f"Arquivo {arquivo} maior que 10MB, ignorado!")
        
                continue
        
        except FileNotFoundError:

            print(f"Arquivo {arquivo} não foi encontrado.")
            
            continue
        
        else:    
            
            try:
                
                matches = regras.match(filepath = arquivo, timeout = 3, callback = minha_callback)
            
            except yara.TimeoutError:
                
                print(f"Tempo esgotado ao escanear o arquivo {arquivo}")

                continue
