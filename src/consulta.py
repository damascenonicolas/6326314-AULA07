import glob
import os
import pandas as pd

# Procura qualquer arquivo Excel (.xlsx) na pasta atual ou na pasta 'dados'
arquivos_excel = glob.glob("*.xlsx") + glob.glob("dados/*.xlsx")

if not arquivos_excel:
  print(
      "ERRO: Nenhum arquivo Excel (.xlsx) foi encontrado na pasta nem na pasta"
      " 'dados'."
  )
else:
  # Pega o primeiro arquivo encontrado
  caminho_arquivo = arquivos_excel[0]
  print(f"[Info] Lendo o arquivo: {caminho_arquivo}")

  df = pd.read_excel(caminho_arquivo)

  # Mostra as linhas lidas para sabermos se o Excel salvou os dados
  print("\nLinhas encontradas na planilha:")
  print(df)
  print("-" * 40)

  ra_busca = input("Digite o RA do aluno para consulta: ").strip()

  # Filtra o RA (convertendo para string e removendo espaços)
  df["RA"] = df["RA"].astype(str).str.strip()
  aluno = df[df["RA"] == ra_busca]

  if aluno.empty:
    print(
        f"Nenhum registro encontrado para o RA '{ra_busca}'. (Confira se salvou"
        " o Excel!)"
    )
  else:
    print("\n" + "=" * 40)
    print("        RESULTADO DO ALUNO        ")
    print("=" * 40)

    for index, row in aluno.iterrows():
      nome = row.get("Nome", "Não informado")
      ra = row.get("RA", "Não informado")

      nota1 = float(row.get("Nota 1", 0.0) or 0.0)
      nota2 = float(row.get("Nota 2", 0.0) or 0.0)
      tf01 = float(row.get("TF01", 0.0) or 0.0)
      tf02 = float(row.get("TF02", 0.0) or 0.0)

      media = (nota1 + nota2 + tf01 + tf02) / 4.0
      status = "APROVADO" if media >= 6.0 else "REPROVADO"

      print(f"Nome   : {nome}")
      print(f"RA     : {ra}")
      print("-" * 40)
      print(f"Nota 1 : {nota1:.2f}")
      print(f"Nota 2 : {nota2:.2f}")
      print(f"TF 01  : {tf01:.2f}")
      print(f"TF 02  : {tf02:.2f}")
      print("-" * 40)
      print(f"Média Final : {media:.2f}")
      print(f"Situação    : {status}")
      print("=" * 40 + "\n")
      