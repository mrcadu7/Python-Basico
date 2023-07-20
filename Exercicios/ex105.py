def notas(*num, sit=False):
    """
    -> Função para analisar as notas e situação dos alunos
    :param num: nota ou notas dos alunos (Ilimitado)
    :param sit: valor opcional, que mostra a situação do aluno
    :return: Dicionário com análise de notas e situação (se pedida) do aluno
    """
    analise = {}
    analise['total'] = len(num)
    analise['maior'] = max(num)
    analise['menor'] = min(num)
    analise['media'] = sum(num)/len(num)
    media = analise['media']
    if sit:
        if media < 5:
            sit = 'RUIM'
            analise['situacao'] = sit
        if 5 <= media < 7:
            sit = 'RAZOAVEL'
            analise['situacao'] = sit
        if media >= 7:
            sit = 'BOA'
            analise['situacao'] = sit
    return analise


#Programa Principal
resp = notas(5, 4.9, 5, 5, sit=True)
print(resp)
