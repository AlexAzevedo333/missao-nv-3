dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})

print("Dicionário atualizado:", dicionario)

dicionario_copia = dicionario.copy()

elemento_removido = dicionario.pop(2)
print("Elemento removido (chave 2):", elemento_removido)
print("Dicionário após pop:", dicionario)

elemento_removido_ultimo = dicionario.popitem()
print("Último elemento removido (popitem):", elemento_removido_ultimo)
print("Dicionário após popitem:", dicionario)

dicionario.clear()
dicionario_copia.clear()
print("Dicionário original após clear:", dicionario)
print("Cópia do dicionário após clear:", dicionario_copia)

chaves = ['nome', 'idade', 'nacionalidade']
novo_dicionario = dict.fromkeys(chaves, "Informação não disponível")

print("Novo dicionário (items):", novo_dicionario.items())

print("Chaves do novo dicionário:", novo_dicionario.keys())

print("Valores do novo dicionário:", novo_dicionario.values())
