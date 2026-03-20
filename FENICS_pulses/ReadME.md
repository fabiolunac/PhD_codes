# FENICS Pulses

Ferramenta em Python para análise de formas de onda geradas por um simulador implementado em FPGA (Xilinx), com foco na avaliação de sinais e algoritmos de reconstrução.

## 📁 Estrutura do projeto

- **iladata_occ25.csv**  
  Dados exportados do simulador para ocupação 25 (~20%).

- **iladata_occ121.csv**  
  Dados exportados do simulador para ocupação 121 (~95%).

- **fenics_pulses.py**  
  Script principal para leitura dos dados e geração dos gráficos.

## ▶️ Como utilizar

Execute o script principal:

```bash
python3 fenics_pulses.py
```

Os gráficos serão exibidos automaticamente.

## 📦 Dependências

Instale com:

```bash
pip install pandas matplotlib
```

Ou manualmente:

- pandas  
- matplotlib  

## 📊 Funcionalidades

- Leitura de dados exportados do Vivado ILA  
- Processamento de sinais (ADC, PZC, Wiener)  
- Comparação entre sinal verdadeiro e estimativas  
- Geração de gráficos em formato step (estilo FPGA/DAQ)  

## 🧠 Contexto

Este projeto é utilizado para análise de desempenho de algoritmos digitais aplicados ao condicionamento e reconstrução de sinais em sistemas de aquisição de dados em FPGA.

## 👨‍💻 Autor

Fábio — CERN / Engenharia Elétrica