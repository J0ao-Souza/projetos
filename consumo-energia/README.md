⚡ Calculadora de Consumo Elétrico

Uma calculadora desenvolvida em Python para estimar o consumo mensal de energia elétrica de um aparelho com base na sua potência e no tempo médio de utilização diária.

🎯 Objetivo

O objetivo do projeto é permitir que o usuário informe os dados de um aparelho elétrico e receba uma estimativa do seu consumo mensal em kWh.

🛠️ Tecnologias utilizadas






🐍 Python
🐙 Git e GitHub
🧮 Fórmula utilizada

O consumo mensal é calculado utilizando a fórmula:

consumoMensal = (potencia × horasDia × 30) / 1000

Onde:

potencia = potência do aparelho em watts (W)
horasDia = média de horas de utilização por dia
30 = quantidade aproximada de dias no mês
1000 = conversão de watts para quilowatts
▶️ Como executar
1. Instale o Python

É necessário ter o Python instalado no computador.

2. Abra o terminal na pasta do projeto

No VS Code, abra o terminal e execute:

python app.py
3. Informe os dados

O programa solicitará:

Nome do aparelho
Potência em watts (W)
Tempo médio de uso diário em horas

Depois disso, o programa mostrará o consumo mensal estimado.

💡 Exemplo
=== Calculadora de Consumo Elétrico ===

Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts (W): 100
Digite o tempo médio de uso diário em horas: 15

=== Resultado ===
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês

📌 Projeto

Projeto desenvolvido como atividade de iniciação em tecnologia.