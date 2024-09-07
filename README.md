# M4GNUS-DoS-404

**M4GNUS-DoS-404** é um script de ataque DoS (Denial of Service) escrito em Python que utiliza múltiplas threads para gerar requisições simultâneas contra um alvo, sobrecarregando-o.

> ⚠️ **Aviso Legal**: Este script é para fins educacionais e de teste **autorizado** apenas. O uso não autorizado em sistemas que você não possui ou não tem permissão explícita para testar é **ilegal**.

Se você quiser saber mais sobre ataques DoS, pesquise no Google! 😎✌️

## Funcionalidades
- Suporte a múltiplas threads para enviar várias requisições simultaneamente.
- Menu interativo com opções para iniciar o ataque, visualizar créditos ou sair do programa.
- Possibilidade de definir a **URL de destino**, o **número de threads** e a **duração do ataque**.
- Após o tempo determinado, o ataque é automaticamente interrompido e o script retorna ao menu principal.

## Como Funciona

O script cria várias threads, cada uma enviando uma requisição HTTP para a URL de destino especificada. Você pode ajustar o número de threads e o tempo de duração do ataque.

### Requisitos
- Python 3.x
- Biblioteca `requests` para enviar as requisições HTTP.
- Biblioteca `colorama` para colorir o terminal.

### Instalação

Clone o repositório:
   ```bash
   git clone https://github.com/Defalt357/M4GNUS-DoS-404.git

   Instale as dependências necessárias:
   pip install requests colorama

   Execute o script:
   python3 m4gnus_dos.py

![M4GNUS-DoS Screenshot](./img/M4GNUS.jpg)

   
   
