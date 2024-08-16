from operacoes import calcular_media, verificar_reprovacao, listar_alunos_reprovados

dados_alunos = {
    101: {"nome": "Alice", "notas": [7.0, 8.5, 6.5, 7.2]},
    102: {"nome": "Bruno", "notas": [5.0, 4.5, 6.0, 5.2]},
    103: {"nome": "Carla", "notas": [8.0, 9.5, 7.5, 9.2]},
    104: {"nome": "Daniel", "notas": [2.0, 3.5, 4.0, 5.2]},
}

matriculas_reprovados = []
for matricula, info in dados_alunos.items():
    media = calcular_media(info["notas"])
    dados_alunos[matricula]["media"] = media 
    if verificar_reprovacao(media):
        matriculas_reprovados.append(matricula)

alunos_reprovados = listar_alunos_reprovados(dados_alunos, matriculas_reprovados)
for aluno in alunos_reprovados:
    print(aluno)
