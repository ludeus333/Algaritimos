def media_aluno
primeira_nota = float(input("Digite a primeira nota:"))
segunda_nota = float(input('Digite a segunda nota:'))

media = (primeira_nota + segunda_nota) / 2

if media >= 6:
    print(f"O aluno foi APROVADO com média {media:.1f}")
else:
    print(f"O aluno foi REPROVADO com média {media:.1f}")
