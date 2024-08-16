lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

print("Conteúdo da lista_mesclada:")
print(lista_mesclada)

lista_mesclada.append(["Lista aninhada"])

print("\nConteúdo da lista_mesclada após append:")
print(lista_mesclada)

lista_mesclada.insert(4, 5)

print("\nConteúdo da lista_mesclada após insert:")
print(lista_mesclada)

print("\nTamanho atual da lista_mesclada:")
print(len(lista_mesclada))

del lista_mesclada[1]

print("\nConteúdo da lista_mesclada após remoção:")
print(lista_mesclada)

nova_lista_mesclada = lista_mesclada[:5]

print("\nConteúdo da nova_lista_mesclada:")
print(nova_lista_mesclada)
