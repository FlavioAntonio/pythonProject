from ldap3 import Server, Connection, ALL, Tls, MODIFY_REPLACE
import ssl
import dotenv
import os


class CriarUsuarioAD:
    def __init__(self, primeiro_nome, sobrenome, username, password, email, gestor, departamento, unidade, cargo):
        dotenv.load_dotenv()
        self.LDAP_SERVER = os.getenv('LDAP_SERVER')
        self.USER_ADMIN = os.getenv('USER_ADMIN')
        self.PASSWORD_ADMIN = os.getenv('PASSWORD_ADMIN')
        self.USER_BASE = os.getenv('USER_BASE')

        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.username = username
        self.password = password
        self.email = email
        self.gestor = gestor
        self.departamento = departamento
        self.unidade = unidade
        self.cargo = cargo

        # Configuração de TLS para aceitar certificado (ajuste conforme necessário)
        conf_tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)
        self.server = Server(self.LDAP_SERVER, port=636, use_ssl=True, tls=conf_tls, get_info=ALL)

        # Autenticação SIMPLE com conta administrativa (use admin@dominio no .env)
        self.conn = Connection(
            self.server,
            user=self.USER_ADMIN,
            password=self.PASSWORD_ADMIN,
            authentication='SIMPLE'
        )

    def create_user(self):
        if not self.conn.bind():
            print(f"❌ Falha na conexão: {self.conn.result}")
            return False

        user_dn = f'CN={self.username},{self.USER_BASE}'
        object_class = ['top', 'person', 'organizationalPerson', 'user']

        attributes = {
            'sn': self.sobrenome,
            'sAMAccountName': self.username,
            'givenName': self.primeiro_nome,
            'displayName': f'{self.primeiro_nome} {self.sobrenome}',
            'userPrincipalName': f'{self.username}@{os.getenv("DEFAULT_DOMAIN","seu_dominio.com")}'
        }

        if self.email:
            attributes['mail'] = self.email
        if self.departamento:
            attributes['department'] = self.departamento
        if self.unidade:
            attributes['physicalDeliveryOfficeName'] = self.unidade
        if self.cargo:
            attributes['title'] = self.cargo
        if self.gestor:
            attributes['manager'] = self.gestor

        # Cria o objeto de usuário primeiro (sem senha)
        if not self.conn.add(user_dn, object_class, attributes):
            print(f"❌ Erro ao criar usuário: {self.conn.result}")
            self.conn.unbind()
            return False

        # Define a senha usando a extensão Microsoft (requer SSL)
        try:
            if not self.conn.extend.microsoft.modify_password(user_dn, self.password):
                print(f"❌ Erro ao definir senha: {self.conn.result}")
                self.conn.unbind()
                return False
        except Exception as e:
            print(f"❌ Exceção ao definir senha: {e}")
            self.conn.unbind()
            return False

        # Habilita a conta (512 = enabled)
        if not self.conn.modify(user_dn, {'userAccountControl': [(MODIFY_REPLACE, [512])] } ):
            print(f"❌ Erro ao habilitar conta: {self.conn.result}")
            self.conn.unbind()
            return False

        print(f"✅ Usuário {self.username} criado e habilitado!")
        self.conn.unbind()
        return True


if __name__ == "__main__":
    criar_usuario = CriarUsuarioAD(
        primeiro_nome="Usuario",
        sobrenome="Teste",
        username="user123",
        password="SenhaSegura@123",
        email="user123@contoso.local",
        gestor="",
        departamento="TI",
        unidade="Sede",
        cargo="Analista"
    )

    criar_usuario.create_user()
    