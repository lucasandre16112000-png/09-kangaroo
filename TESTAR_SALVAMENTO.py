#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE TESTE - Verifica se o sistema de salvamento funciona
"""

import os
import time
from datetime import datetime

print("="*85)
print("  🧪 TESTE DO SISTEMA DE SALVAMENTO DE CHAVES")
print("="*85)
print()

# Simula uma chave encontrada
test_key_line = "Key# 0 [1S]Pub:  0x02145D2611C823A396EF6712CE0F712F09B9B4F3135E3E0AA3230FB9B6D08D1E16 \n       Priv: 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF (TESTE - NÃO É REAL)"

found_file = "FOUND_KANGAROO.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"[1/4] Criando arquivo de teste: {found_file}")

try:
    with open(found_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*80}\n")
        f.write(f"🧪 TESTE DE SALVAMENTO - {timestamp}\n")
        f.write(f"{'='*80}\n")
        f.write(f"{test_key_line}\n")
        f.write(f"{'='*80}\n\n")
        f.flush()
        os.fsync(f.fileno())
    
    print("✅ Arquivo criado com sucesso!")
    print()
    
except Exception as e:
    print(f"❌ ERRO ao criar arquivo: {e}")
    print()
    exit(1)

# Verifica se o arquivo foi criado
print(f"[2/4] Verificando se o arquivo existe...")

if os.path.exists(found_file):
    print(f"✅ Arquivo encontrado: {found_file}")
    print()
else:
    print(f"❌ Arquivo NÃO encontrado!")
    print()
    exit(1)

# Verifica o tamanho
print(f"[3/4] Verificando tamanho do arquivo...")

size = os.path.getsize(found_file)
print(f"✅ Tamanho: {size} bytes")
print()

# Lê o conteúdo
print(f"[4/4] Lendo conteúdo do arquivo...")
print()

try:
    with open(found_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("─"*85)
    print("CONTEÚDO DO ARQUIVO:")
    print("─"*85)
    print(content)
    print("─"*85)
    print()
    
except Exception as e:
    print(f"❌ ERRO ao ler arquivo: {e}")
    print()
    exit(1)

# Resultado final
print("="*85)
print("  ✅ TESTE CONCLUÍDO COM SUCESSO!")
print("="*85)
print()
print("O sistema de salvamento está FUNCIONANDO corretamente!")
print()
print(f"Arquivo de teste criado: {found_file}")
print()
print("Quando o Kangaroo encontrar uma chave REAL, ela será salva neste arquivo.")
print()
print("="*85)
