# JacyCrypts

## 🔖&nbsp; Sobre
O projeto JacyCrypts nasceu para ser uma solução para o esquema abaixo:
    "O emissor e o destinatário conhecem um valor secreto chamado S. O emissor concatena a mensagem e o valor secreto, calcula um hash, concatena a mensagem e o valor de hash, encripta usando criptografia simétrica e envia o resultado para o destinatário. O destinatário decripta os dados recebidos, concatena a mensagem e o valor secreto, gera o valor de hash e compara com o valor de hash recebido. Novamente, esse mecanismo não garante confidencialidade."
Ela utiliza uma hash MD5/SHA256 e a criptografia simetrica 3DES.

## 🚀 Features
- [x] Hash MD5
- [ ] Hash SHA256
- [x] Criptografia Simetrica DES3

## 🗂 Como baixar o projeto
```bash
    # Clonar o repositório
    $ git clone https://github.com/jacyirice/JacyCrypts

    # Entrar no diretório
    $ cd JacyCrypts

    # Executar exemplo
    $ python main.py
```

## Exemplos de Utilização
- Encriptando mensagens
    ```python
    # Importar modulo
    from jacycrypts import JacyCrypt

    # Instanciar objeto com um valor secreto
    jacycrypt = JacyCrypt('valor_secreto')

    # Encriptar mensagem
    mensagem_encriptada = jacycrypt.encrypt('mensagem_original')
    print('Mensagem encriptada:', mensagem_encriptada)
    ```
- Decriptando mensagens
    ```python
    # Importar modulo
    from jacycrypts import JacyCrypt

    # Instanciar objeto com um valor secreto
    jacycrypt = JacyCrypt('valor_secreto')

    # Decriptar mensagem
    mensagem_decriptada, hash = jacycrypt.decrypt('mensagem_encriptada')
    print('Mensagem decriptada:', mensagem_decriptada)

    # Verificando se a hash da mensagem foi alterada
    hash_new = jacycrypt.gerar_hash(mensagem_decriptada)
    print('As hashs são iguais?', hash_new == hash)
    ```

## Desenvolvido por
[Jacyiricê Silva Oliveira](https://github.com/jacyirice/)

## Disponivel em 
[GitHub](https://github.com/jacyirice/JacyCrypts)