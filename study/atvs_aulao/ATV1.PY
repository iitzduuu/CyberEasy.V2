#ATIVIDADE 1

# 1 - Compilar uma regra simples ($a = "virus") e testar em um arquivo .txt;
# 2 - Salvar as regras compiladas em .yarc e depois carregar com yara.load();
# 3 - Criar uma regra errada de propósito e tratar a exceção.


import yara

atividade = """
rule Rede {
    meta:
        autor = "Helen Ferreira"
        descricao = "Detectar escolas rede SESI" 
    strings: 
        $sesi = "escolas"
    condition:
        $sesi
}
"""

print("\nTestando regra SESI...")
regras = yara.compile(source=atividade)
matches = regras.match(filepath="teste.txt")

for match in matches:
    print("Regra disparada:", match.rule)
    print("Metadados:", match.meta)
    print("Strings disparadas", match.strings)


# --- 2) SALVAR E CARREGAR (.yarc) ---
print("\n Salvando e carregando regra SESI...")
regras.save("regras_sesi.yarc")   # salva
regras_carregadas = yara.load("regras_sesi.yarc")  # carrega

matches2 = regras_carregadas.match(filepath="teste.txt")
for match in matches2:
    print("Regra carregada e disparada:", match.rule)


# --- 3) REGRA ERRADA COM TRATAMENTO ---
print("\n Testando regra errada...")
regra_errada = """
rule Erro {
    strings
        $sesi = "teste"
    condition:
        $sesi
}
"""

try:
    regras_erradas = yara.compile(source=regra_errada)
except yara.SyntaxError as e:
    print("Erro de sintaxe na regra YARA:")
    print(e)
