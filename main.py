import os
import shutil
from datetime import datetime

# Caminho da pasta que você deseja copiar
origem = r"C:\Users\LuisRibeiro\Documents\Projetos\Scripts de backup\Ambiente de teste com os arquivos"

# Caminho onde deseja salvar o backup
destino_base = r"C:\Users\LuisRibeiro\Documents\Projetos\Scripts de backup\Ambiente de teste dos backup"

# Data e hora atual no formato "AAAA-MM-DD_HH-MM-SS"
data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Cria o nome da pasta de destino com a data e hora
destino = os.path.join(destino_base, f"Backup_{data_hora}")

# Copia a pasta de origem para o destino, incluindo subpastas e arquivos
shutil.copytree(origem, destino)

print(f"Backup concluído em: {destino}")
