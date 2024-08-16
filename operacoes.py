def calcular_media(notas):
    """Calcula a média das notas."""
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """Verifica se o aluno foi reprovado com base na média."""
    return media < 6

def listar_alunos_reprovados(dados_alunos, matriculas_reprovados):
    """Lista os alunos reprovados com base nas matrículas."""
    alunos_reprovados = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula)
        if aluno:
            nome = aluno["nome"]
            media = aluno["media"]
            alunos_reprovados.append(f"Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media:.2f}")
    return alunos_reprovados
