# ATIVIDADE 3

# 1 - Compilar uma regra complexa: Crie uma regra YARA chamada DetectaAmeaça com as seguintes características: Múltiplas strings para detectar palavras suspeitas como "malware", "trojan" e "spyware"; Condições combinadas usando any of ($x*) ou all of them; Metadados detalhados: autor, versão, descrição e data de criação; Tags para classificar o tipo de ameaça ("malware", "virus", "spyware").

# 2 - Testar a regra em múltiplos arquivos: Crie uma pasta chamada arquivos_teste contendo vários arquivos .txt com palavras normais e algumas palavras suspeitas;Verifique cada arquivo usando a regra compilada; Para cada correspondência, exiba: Nome da regra disparada - Tags associadas - Metadados - Strings encontradas com suas posições e identificadores. 

# 3 - Salvar e carregar regras compiladas: Salve a regra compilada em um arquivo .yarc; Carregue o .yarc com yara.load() e teste novamente nos mesmos arquivos; Confirme que todas as regras continuam disparando corretamente após o carregamento.

# 4 - Criar uma regra errada intencional: Adicione um erro de sintaxe intencional na regra (por exemplo, faltar = em alguma string); Use try/except para capturar a exceção yara.SyntaxError; Exiba no terminal a mensagem de erro e continue o script normalmente. 




import yara

#Criar regra e chamar arquivo
regras = yara.compile (filepath= "regra3.yar")

matches0 = regras.match (filepath= "arquivos_testes/arquivo_teste1.txt")
matches1 = regras.match (filepath= "arquivos_testes/arquivo_teste2.txt")
matches2 = regras.match (filepath= "arquivos_testes/arquivo_teste3.txt")

if matches0:
    for m in matches0:
        print(f'Regras Disparadas: {m.rule}')
        print(f'Metadados: {m.meta}')
        print(f'Tags: {m.tags}')
        print(f'Strings encontradas: {m.strings}')

    for s in m.strings:
        for inst in s.instances:
            print(f"  - {s.identifier} na posicao {inst.offset}: {inst.matched_data}")
else:
    print("Nenhuma regra foi disparada")


if matches1:
    for m in matches1:
        print(f'Regras Disparadas: {m.rule}')
        print(f'Metadados: {m.meta}')
        print(f'Tags: {m.tags}')
        print(f'Strings encontradas: {m.strings}')

    for s in m.strings:
        for inst in s.instances:
            print(f"  - {s.identifier} na posicao {inst.offset}: {inst.matched_data}")
else:
    print("Nenhuma regra foi disparada")

if matches2:
    for m in matches2:
        print(f'Regras Disparadas: {m.rule}')
        print(f'Metadados: {m.meta}')
        print(f'Tags: {m.tags}')
        print(f'Strings encontradas: {m.strings}')

    for s in m.strings:
        for inst in s.instances:
            print(f"  - {s.identifier} na posicao {inst.offset}: {inst.matched_data}")
else:
    print("Nenhuma regra foi disparada")


#Salvar e carregar regras compiladas

print("\n Salvando e carregando regra 3")
regras.save("regras3.yarc")   # salva
regras_carregadas = yara.load("regras3.yarc")  # carrega

matches4 = regras_carregadas.match(filepath="teste.txt")
for match in matches4:
    print("Regra carregada e disparada:", match.rule)


#Regra errada - tratamento de exceções

try:
    regras2 = yara.compile (filepath= "regra4.yar")
  
except yara.SyntaxError as e:
    print("Erro de sintaxe na regra YARA:")
    print(e)
except yara.Error as e:
    print("Error generico do YARA")
except TimeoutError as e:
    print("A analise ultrapassou o limite de tempo")
    print(e)

