# Entrada do usuário
#email = input().strip()

# Função para validar o e-mail
def validar_email(email):
    # Verifica se contém exatamente um '@' e não tem espaços
    if "@" not in email or email.count("@") != 1 or " " in email:
        return "E-mail inválido"

    # Separa o e-mail em duas partes: antes e depois do '@'
    parte_local, dominio = email.split("@")

    # Verifica se o '@' está no início ou no fim
    if not parte_local or not dominio:
        return "E-mail inválido"

    # Verifica se o domínio contém pelo menos um ponto (ex: gmail.com)
    if "." not in dominio:
        return "E-mail inválido"

    return "E-mail válido"

# Entrada do usuário
email = input().strip()

# Saída da validação
print(validar_email(email))


