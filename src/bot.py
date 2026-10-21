import time
import pandas as pd
import pyautogui

pyautogui.PAUSE = 1.0

print("=== BOT DE PREENCHIMENTO INTELIGENTE ===")
print("Abra o Google Forms e clique com o mouse no PRIMEIRO campo (RA).")
print("O bot começará em 5 segundos...")
time.sleep(5)

caminho_csv = "dados/dados.csv"

try:
    df = pd.read_csv(caminho_csv)
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    exit()

for index, row in df.iterrows():
    print(
        f"Preenchendo: RA={row['RA']} | Nome={row['Nome']} | Nota 1={row['Nota 1']} | Nota 2={row['Nota 2']} | TF01={row['TF01']} | TF02={row['TF02']}"
    )

    pyautogui.write(str(row["RA"]), interval=0.1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(str(row["Nome"]), interval=0.1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(str(row["Nota 1"]), interval=0.1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(str(row["Nota 2"]), interval=0.1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(str(row["TF01"]), interval=0.1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(str(row["TF02"]), interval=0.1)
    time.sleep(0.5)

    pyautogui.press("enter")
    time.sleep(3)

    # Em vez de usar TAB (que cai em links indesejados como report),
    # vamos usar um atalho prático do navegador para recarregar o link limpo do Forms:
    # 1. Pressionamos F6 ou Ctrl+L para ir direto à barra de endereços
    pyautogui.hotkey("ctrl", "l")
    time.sleep(0.5)
    
    # 2. Digitamos novamente o link do seu formulário ou usamos o Enter se o formulário já tiver o redirecionamento nativo.
    # Alternativamente, se preferir o clique na tela de confirmação, basta posicionar o mouse 
    # em cima do link "Enviar outra resposta" e colocar a coordenada exata de pixel aqui embaixo:
    # pyautogui.click(x=300, y=450)
    
    # Como o Google Forms geralmente permite recarregar ou voltar para a página de envio limpa,
    # outra opção muito simples é apertar Backspace (Voltar página) para retornar ao Forms limpo:
    pyautogui.press("backspace")
    time.sleep(2)

print("Preenchimento automático concluído com sucesso!")