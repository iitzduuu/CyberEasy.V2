# ATIVIDADE 2

# 1 - Compilar uma regra simples e testar: Crie uma regra YARA que detecte a palavra "malware" em arquivos .txt; Adicione metadados com seu nome e uma breve descrição da regra; Teste a regra em um arquivo chamado arquivo_teste.txt contendo algumas palavras, incluindo "malware"; Exiba no terminal o nome da regra disparada, os metadados e as strings encontradas com suas posições e identificadores.

# 2 - Salvar regras compiladas e carregar depois: Salve a regra compilada em um arquivo .yarc; Carregue o arquivo .yarc usando yara.load() e teste novamente no mesmo arquivo; Confirme que a regra dispara corretamente após ser carregada; 

# 3 - Criar regra errada de propósito e tratar exceção: Crie uma regra YARA com erro de sintaxe intencional; Utilize um bloco try/except para capturar a exceção yara.SyntaxError; Imprima no terminal a mensagem de erro, garantindo que o script continue executando.




import yara

#Primeira parte
regras = yara.compile (filepath= "regra2.yar")

matches = regras.match (filepath= "arquivo_teste.txt")

if matches:
    for m in matches:
        print(f'Regras Disparadas: {m.rule}')
        print(f'Metadados: {m.meta}')
        print(f'Strings encontradas: {m.strings}')

    for s in m.strings:
        for inst in s.instances:
            print(f"  - {s.identifier} na posicao {inst.offset}: {inst.matched_data}")
else:
    print("Nenhuma regra foi disparada")


#Segunda Parte

print("\n Salvando e carregando regra 1")
regras.save("regras1.yarc")   # salva
regras_carregadas = yara.load("regras1.yarc")  # carrega

matches2 = regras_carregadas.match(filepath="teste.txt")
for match in matches2:
    print("Regra carregada e disparada:", match.rule)


#Terceira Parte


try:
    regras2 = yara.compile (filepath= "regra3.yar")
  
except yara.SyntaxError as e:
    print("Erro de sintaxe na regra YARA:")
    print(e)
except yara.Error as e:
    print("Error generico do YARA")
except TimeoutError as e:
    print("A analise ultrapassou o limite de tempo")
    print(e)




