#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAINEL KANGAROO BTC - VERSÃO FINAL COM DETECÇÃO DE CHAVE
Monitora Kangaroo em tempo real e GARANTE salvamento de chaves!
"""

import subprocess
import threading
import time
import os
import sys
from datetime import datetime

class KangarooPainelFinal:
    def __init__(self):
        self.kangaroo_process = None
        self.running = False
        self.start_time = None
        
        # Estatísticas
        self.last_speed_line = ""
        self.last_full_line = ""
        
        # Detecção de chave
        self.key_found = False
        self.key_found_time = None
        
        # Arquivos
        self.log_file = "kangaroo_output.log"
        self.found_file = "FOUND_KANGAROO.txt"
        self.work_file = "kangaroo_work.txt"
        
        # Contador
        self.update_count = 0
        
    def get_elapsed_time(self):
        """Retorna tempo decorrido"""
        if not self.start_time:
            return "00:00:00"
        
        elapsed = (datetime.now() - self.start_time).total_seconds()
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def monitor_log(self):
        """Monitora o log do Kangaroo"""
        try:
            # Aguarda arquivo ser criado
            while not os.path.exists(self.log_file) and self.running:
                time.sleep(0.5)
            
            if not self.running:
                return
                
            with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as f:
                while self.running:
                    line = f.readline()
                    
                    if not line:
                        time.sleep(0.2)
                        continue
                    
                    line = line.strip()
                    
                    # Salva última linha completa
                    if line:
                        self.last_full_line = line
                    
                    # Detecta linha com velocidade (MK/s, GK/s, etc)
                    if "K/s" in line and "[" in line:
                        self.last_speed_line = line
                    
                    # Detecta chave encontrada (MÚLTIPLOS PADRÕES)
                    if any(keyword in line for keyword in ["Key#", "Priv:", "FOUND", "Found"]):
                        self.key_found = True
                        self.key_found_time = datetime.now()
                        self.save_found_key(line)
                        
        except Exception as e:
            pass
    
    def save_found_key(self, line):
        """Salva chave encontrada COM GARANTIA"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Salva no arquivo
            with open(self.found_file, 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*80}\n")
                f.write(f"🎉 CHAVE ENCONTRADA! - {timestamp}\n")
                f.write(f"{'='*80}\n")
                f.write(f"{line}\n")
                f.write(f"{'='*80}\n\n")
                f.flush()  # FORÇA GRAVAÇÃO IMEDIATA
                os.fsync(f.fileno())  # GARANTE ESCRITA NO DISCO
            
            # Salva BACKUP em arquivo separado
            backup_file = f"CHAVE_ENCONTRADA_{timestamp.replace(':', '-').replace(' ', '_')}.txt"
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(f"{'='*80}\n")
                f.write(f"🎉 CHAVE ENCONTRADA! - {timestamp}\n")
                f.write(f"{'='*80}\n")
                f.write(f"{line}\n")
                f.write(f"{'='*80}\n")
                f.flush()
                os.fsync(f.fileno())
            
            print(f"\n\n{'='*80}")
            print(f"🎉🎉🎉 CHAVE ENCONTRADA! 🎉🎉🎉")
            print(f"{'='*80}")
            print(f"Salva em: {self.found_file}")
            print(f"Backup em: {backup_file}")
            print(f"{'='*80}\n\n")
            
        except Exception as e:
            # Se der erro, tenta salvar em arquivo de emergência
            try:
                emergency_file = f"EMERGENCIA_CHAVE_{int(time.time())}.txt"
                with open(emergency_file, 'w') as f:
                    f.write(f"CHAVE ENCONTRADA - EMERGÊNCIA\n")
                    f.write(f"{line}\n")
                    f.flush()
                    os.fsync(f.fileno())
            except:
                pass
    
    def display_panel(self):
        """Exibe painel FINAL"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.update_count += 1
        
        # Se encontrou chave, mostra alerta VERMELHO
        if self.key_found:
            print("\033[91m" + "="*85)
            print("  🎉🎉🎉 CHAVE ENCONTRADA! PARE O PROGRAMA AGORA! 🎉🎉🎉")
            print("  Arquivo: " + self.found_file)
            print("="*85 + "\033[0m")
            print()
        
        print("\033[92m" + "="*85)
        print("  🦘 KANGAROO BTC PANEL - Caçando R$ 440 MILHÕES em Bitcoin")
        print("="*85 + "\033[0m")
        print()
        
        # Status
        status = "🟢 RODANDO" if self.running else "🔴 PARADO"
        if self.key_found:
            status = "🎉 CHAVE ENCONTRADA!"
        
        print(f"Status:          {status}")
        print(f"Tempo rodando:   {self.get_elapsed_time()}")
        print(f"Uso CPU:         ~50% (3 threads)")
        print(f"Uso GPU:         80% (Configure no MSI Afterburner)")
        print()
        
        # Puzzles
        print("─"*85)
        print("PUZZLES SENDO BUSCADOS:")
        print("─"*85)
        print("  Puzzle #135:  13.5 BTC  = R$ 6,8 milhões")
        print("  Puzzle #140:  14.0 BTC  = R$ 7,1 milhões")
        print("  Puzzle #145:  14.5 BTC  = R$ 7,3 milhões")
        print("  Puzzle #150:  15.0 BTC  = R$ 7,6 milhões")
        print("  Puzzle #155:  15.5 BTC  = R$ 7,9 milhões")
        print("  Puzzle #160:  16.0 BTC  = R$ 8,1 milhões")
        print()
        print("  💰 TOTAL: 87 BTC = R$ 440 MILHÕES")
        print("─"*85)
        print()
        
        # Estatísticas do Kangaroo
        print("ESTATÍSTICAS:")
        print("─"*85)
        
        if self.last_speed_line:
            print(f"  {self.last_speed_line}")
        else:
            print("  Aguardando Kangaroo iniciar... (pode levar 1-2 minutos)")
        
        print("─"*85)
        print()
        
        # Sistema de salvamento
        print("💾 SISTEMA DE SALVAMENTO:")
        print("─"*85)
        print(f"  Arquivo principal: {self.found_file}")
        print(f"  Progresso salvo em: {self.work_file} (a cada 5 minutos)")
        
        if os.path.exists(self.found_file):
            size = os.path.getsize(self.found_file)
            print(f"  ✅ Arquivo de chaves: {size} bytes")
        else:
            print(f"  ⏳ Arquivo de chaves: Aguardando primeira chave...")
        
        if self.key_found:
            print(f"  🎉 CHAVE ENCONTRADA ÀS: {self.key_found_time.strftime('%H:%M:%S')}")
        
        print("─"*85)
        print()
        
        # Rodapé
        print(f"💡 Pressione Ctrl+C para parar")
        print(f"📊 Atualização #{self.update_count} - {datetime.now().strftime('%H:%M:%S')}")
        print()
    
    def start_kangaroo(self):
        """Inicia Kangaroo"""
        if not os.path.exists('Kangaroo.exe'):
            print("\033[91m")
            print("="*85)
            print("  ❌ ERRO: Kangaroo.exe não encontrado!")
            print("="*85)
            print("\033[0m")
            return False
        
        if not os.path.exists('all_puzzles.txt'):
            print("\033[91m")
            print("="*85)
            print("  ❌ ERRO: all_puzzles.txt não encontrado!")
            print("="*85)
            print("\033[0m")
            return False
        
        try:
            # Remove log antigo
            if os.path.exists(self.log_file):
                try:
                    os.remove(self.log_file)
                except:
                    pass
            
            log_handle = open(self.log_file, 'w', encoding='utf-8', buffering=1)
            
            # Comando Kangaroo
            cmd = [
                'Kangaroo.exe',
                '-t', '3',
                '-gpu',
                '-w', self.work_file,
                '-wi', '300',
                '-o', self.found_file,
                'all_puzzles.txt'
            ]
            
            print("\033[93m")
            print("="*85)
            print("  🚀 Iniciando Kangaroo...")
            print("="*85)
            print("\033[0m")
            print()
            print(f"  Comando: {' '.join(cmd)}")
            print()
            print("\033[93m  ⚠️  IMPORTANTE: Configure 80% GPU no MSI Afterburner!\033[0m")
            print()
            print("  💾 SISTEMA DE SALVAMENTO ATIVADO:")
            print(f"     - Chaves encontradas: {self.found_file}")
            print(f"     - Progresso: {self.work_file}")
            print(f"     - Backup automático: ATIVADO")
            print()
            
            self.kangaroo_process = subprocess.Popen(
                cmd,
                stdout=log_handle,
                stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL,
                bufsize=1,
                universal_newlines=True
            )
            
            self.running = True
            self.start_time = datetime.now()
            
            # Inicia monitor de log
            threading.Thread(target=self.monitor_log, daemon=True).start()
            
            print(f"\033[92m  ✓ Kangaroo iniciado! PID: {self.kangaroo_process.pid}\033[0m")
            print()
            print("  Aguarde 1-2 minutos para o Kangaroo começar a processar...")
            print()
            time.sleep(3)
            return True
            
        except Exception as e:
            print(f"\033[91m  ❌ ERRO ao iniciar Kangaroo: {e}\033[0m")
            return False
    
    def stop_kangaroo(self):
        """Para Kangaroo"""
        print("\n\n⏹️  Parando Kangaroo...")
        
        if self.kangaroo_process:
            try:
                self.kangaroo_process.terminate()
                self.kangaroo_process.wait(timeout=10)
            except:
                try:
                    self.kangaroo_process.kill()
                except:
                    pass
        
        self.running = False
        
        print("✓ Kangaroo finalizado!")
        print()
        print(f"⏱️  Tempo total: {self.get_elapsed_time()}")
        
        if self.key_found:
            print()
            print("🎉 CHAVE ENCONTRADA DURANTE ESTA SESSÃO!")
            print(f"   Arquivo: {self.found_file}")
        
        print()
    
    def run(self):
        """Loop principal"""
        try:
            print("\033[92m")
            print("="*85)
            print("  🦘 KANGAROO BTC PANEL - Versão Final com Detecção Garantida")
            print("="*85)
            print("\033[0m")
            print()
            
            # Inicia Kangaroo
            if not self.start_kangaroo():
                return
            
            # Loop de atualização do painel (a cada 5 segundos)
            while self.running:
                self.display_panel()
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupção detectada (Ctrl+C)")
            self.stop_kangaroo()
        except Exception as e:
            print(f"\n\n❌ ERRO: {e}")
            self.stop_kangaroo()

if __name__ == "__main__":
    panel = KangarooPainelFinal()
    panel.run()
