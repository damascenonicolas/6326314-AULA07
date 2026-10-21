import os
import pandas as pd

caminho_arquivo = os.path.join(
    os.path.dirname(__file__), "..", "dados", "resultados.xlsx"
)

if not os.path.exists(caminho_arquivo):
  print(f"ERRO: O arquivo 'resultados.xlsx' não foi encontrado na pasta 'dados'.")
else:
  df = pd.read_excel(caminho_arquivo)

  print("--- SISTEMA DE CONSULTA E MÉDIAS ---")
  ra_busca = input("Digite o RA do aluno para consulta: ").strip()

  df["RA"] = df["RA"].astype(str).str.strip()
  aluno = df[df["RA"] == ra_busca]

  if aluno.empty:
    print(f"Nenhum registro encontrado para o RA '{ra_busca}'.")
  else:
    print("\n" + "=" * 45)
    print("        RELATÓRIO DE DESEMPENHO        ")
    print("=" * 45)

    for index, row in aluno.iterrows():
      nome = row.get("Nome", "Não informado")
      ra = row.get("RA", "Não informado")

      nota1 = float(row.get("Nota 1", 0.0) or 0.0)
      nota2 = float(row.get("Nota 2", 0.0) or 0.0)
      tf01 = float(row.get("TF01", 0.0) or 0.0)
      tf02 = float(row.get("TF02", 0.0) or 0.0)

      media_provas = (nota1 + nota2) / 2.0
      media_tfs = (tf01 + tf02) / 2.0
      media_final = (nota1 + nota2 + tf01 + tf02) / 4.0

      status = "APROVADO" if media_final >= 6.0 else "REPROVADO"

      print(f"Nome        : {nome}")
      print(f"RA          : {ra}")
      print("-" * 45)
      print(f"Nota 1      : {nota1:.2f}")
      print(f"Nota 2      : {nota2:.2f}")
      print(f"Média Provas: {media_provas:.2f}")
      print("-" * 45)
      print(f"TF 01       : {tf01:.2f}")
      print(f"TF 02       : {tf02:.2f}")
      print(f"Média TFs   : {media_tfs:.2f}")
      print("-" * 45)
      print(f"Média Final : {media_final:.2f}")
      print(f"Situação    : {status}")
      print("=" * 45 + "\n")