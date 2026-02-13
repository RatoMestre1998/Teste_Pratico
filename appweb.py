import streamlit as st

# --- A TUA LISTA DE DESAFIOS (Cola aqui a lista 'desafios' completa do teu ficheiro) ---
desafios = [
    # --- Step 1a: Definições Básicas ---
    {
        "contexto": "Router(config)",
        "pergunta": "Desativar a pesquisa de domínio DNS (impedir que traduza comandos errados)",
        "resposta": "no ip domain-lookup",
        "alt_respostas": ["no ip domain lookup"]
    },
    {
        "contexto": "Router(config)",
        "pergunta": "Configurar o hostname para R1",
        "resposta": "hostname R1"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Configurar a mensagem do dia (MOTD). Nota: Usa exatamente '#Unauthorized Acess is Prohibited#'",
        "resposta": "banner motd #Unauthorized Acess is Prohibited#"
    },

    # --- Step 1b: Segurança de Passwords ---
    {
        "contexto": "R1(config)",
        "pergunta": "Entrar na configuração da linha de consola (console 0)",
        "resposta": "line console 0"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "Definir a password da consola para 'ciscoconpass'",
        "resposta": "password ciscoconpass"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "Habilitar o login na consola",
        "resposta": "login"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "Sair da configuração de linha",
        "resposta": "exit"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Definir a password de privilégio (enable secret) para 'ciscoenpass'",
        "resposta": "enable secret ciscoenpass"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Encriptar todas as passwords em texto simples",
        "resposta": "service password-encryption"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Definir o comprimento mínimo da password para 10 caracteres",
        "resposta": "security passwords min-length 10"
    },

    # --- Step 1c: Configuração SSH ---
    {
        "contexto": "R1(config)",
        "pergunta": "Criar utilizador 'admin' com password secreta 'admin1pass'",
        "resposta": "username admin secret admin1pass"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Definir o nome de domínio IP para 'ccna-ptsa.com'",
        "resposta": "ip domain name ccna-ptsa.com",
        "alt_respostas": ["ip domain-name ccna-ptsa.com"]
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Gerar chaves criptográficas RSA",
        "resposta": "crypto key generate rsa"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Definir o tamanho da chave (modulus) para 1024 bits",
        "resposta": "1024"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Configurar SSH para a versão 2",
        "resposta": "ip ssh version 2"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "Entrar nas linhas VTY (0 a 15)",
        "resposta": "line vty 0 15"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "Configurar login para usar a base de dados local (username/password criados)",
        "resposta": "login local"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "Restringir o acesso apenas a SSH (transport input)",
        "resposta": "transport input ssh"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "Sair da configuração de linha",
        "resposta": "exit"
    },
    # --- Step 2a: Configurar Loopback 0 ---
    {
        "contexto": "R1(config)",
        "pergunta": "Criar/Entrar na interface Loopback 0",
        "resposta": "interface Loopback 0"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "Definir a descrição como 'Loopback'",
        "resposta": "description Loopback"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "Definir endereço IPv4 209.165.201.1 /27 (255.255.255.224)",
        "resposta": "ip address 209.165.201.1 255.255.255.224"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "Definir endereço IPv6 global 2001:db8:acad:209::1/64",
        "resposta": "ipv6 address 2001:db8:acad:209::1/64"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "Definir endereço IPv6 link-local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "Sair da interface",
        "resposta": "exit"
    },

    # --- Step 2b: Configurar Subinterfaces (Router-on-a-Stick) ---
    {
        "contexto": "R1(config)",
        "pergunta": "Habilitar o roteamento IPv6 globalmente",
        "resposta": "ipv6 unicast-routing"
    },
    
    # --- VLAN 2: Bikes ---
    {
        "contexto": "R1(config)",
        "pergunta": "Criar subinterface g0/0/1.2 (VLAN 2)",
        "resposta": "interface g0/0/1.2"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Definir encapsulamento 802.1Q para a VLAN 2",
        "resposta": "encapsulation dot1Q 2"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Descrição 'Bikes'",
        "resposta": "description Bikes"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IP 10.19.8.1 máscara /26 (255.255.255.192)",
        "resposta": "ip address 10.19.8.1 255.255.255.192"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IPv6 Global 2001:db8:acad:a::1/64",
        "resposta": "ipv6 address 2001:db8:acad:a::1/64"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IPv6 Link-Local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },

    # --- VLAN 3: Trikes ---
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Criar subinterface g0/0/1.3 (VLAN 3)",
        "resposta": "interface g0/0/1.3"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Definir encapsulamento para VLAN 3",
        "resposta": "encapsulation dot1Q 3"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Descrição 'Trikes'",
        "resposta": "description Trikes"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IP 10.19.8.65 máscara /27 (255.255.255.224)",
        "resposta": "ip address 10.19.8.65 255.255.255.224"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IPv6 Global 2001:db8:acad:b::1/64",
        "resposta": "ipv6 address 2001:db8:acad:b::1/64"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IPv6 Link-Local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },

    # --- VLAN 4: Management ---
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Criar subinterface g0/0/1.4 (VLAN 4)",
        "resposta": "interface g0/0/1.4"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Definir encapsulamento para VLAN 4",
        "resposta": "encapsulation dot1Q 4"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Descrição 'Management'",
        "resposta": "description Management"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IP 10.19.8.97 máscara /29 (255.255.255.248)",
        "resposta": "ip address 10.19.8.97 255.255.255.248"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IPv6 Global 2001:db8:acad:c::1/64",
        "resposta": "ipv6 address 2001:db8:acad:c::1/64"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "IPv6 Link-Local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },

    # --- VLAN 6: Native ---
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Criar subinterface g0/0/1.6 (Nativa)",
        "resposta": "interface g0/0/1.6"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Definir encapsulamento para VLAN 6 como NATIVA",
        "resposta": "encapsulation dot1Q 6 native"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Descrição 'Native'",
        "resposta": "description Native"
    },

    # --- Ativar interface física ---
    {
        "contexto": "R1(config-subif)",
        "pergunta": "Selecionar a interface física g0/0/1",
        "resposta": "interface g0/0/1"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "Ligar a interface física (necessário para subinterfaces funcionarem)",
        "resposta": "no shutdown"
    },
    # ==========================================
    # CONFIGURAÇÃO DO SWITCH 1 (S1)
    # ==========================================

    # --- S1: Definições Básicas ---
    {
        "contexto": "Switch(config)",
        "pergunta": "(S1) Desativar a pesquisa de domínio DNS",
        "resposta": "no ip domain-lookup",
        "alt_respostas": ["no ip domain lookup"]
    },
    {
        "contexto": "Switch(config)",
        "pergunta": "(S1) Configurar o hostname para S1",
        "resposta": "hostname S1"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Banner MOTD. Atenção: '#Unauthorized Access is Prohibitted!#'",
        "resposta": "banner motd #Unauthorized Access is Prohibitted!#"
    },

    # --- S1: Segurança de Passwords ---
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Entrar na linha de consola",
        "resposta": "line console 0"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Password da consola 'ciscoconpass'",
        "resposta": "password ciscoconpass"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Habilitar login",
        "resposta": "login"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Sair da linha",
        "resposta": "exit"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Configurar enable secret 'ciscoenpass'",
        "resposta": "enable secret ciscoenpass"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Encriptar passwords",
        "resposta": "service password-encryption"
    },

    # --- S1: Configuração SSH ---
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Criar user 'admin' com secret 'admin1pass'",
        "resposta": "username admin secret admin1pass"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Definir domínio 'ccna-ptsa.com'",
        "resposta": "ip domain name ccna-ptsa.com"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Gerar chaves RSA",
        "resposta": "crypto key generate rsa"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Tamanho da chave (bits)",
        "resposta": "1024"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Forçar SSH versão 2",
        "resposta": "ip ssh version 2"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Entrar nas linhas VTY 0 a 15",
        "resposta": "line vty 0 15"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Usar base de dados local para login",
        "resposta": "login local"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Permitir apenas SSH",
        "resposta": "transport input ssh"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Sair das linhas",
        "resposta": "exit"
    },

    # ==========================================
    # CONFIGURAÇÃO DO SWITCH 2 (S2)
    # ==========================================
    
    # --- S2: Definições Básicas ---
    {
        "contexto": "Switch(config)",
        "pergunta": "(S2) Desativar a pesquisa de domínio DNS",
        "resposta": "no ip domain-lookup",
        "alt_respostas": ["no ip domain lookup"]
    },
    {
        "contexto": "Switch(config)",
        "pergunta": "(S2) Configurar o hostname para S2",
        "resposta": "hostname S2"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Banner MOTD '#Unauthorized Access is Prohibitted!#'",
        "resposta": "banner motd #Unauthorized Access is Prohibitted!#"
    },

    # --- S2: Segurança de Passwords ---
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Entrar na linha de consola",
        "resposta": "line console 0"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Password da consola 'ciscoconpass'",
        "resposta": "password ciscoconpass"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Habilitar login",
        "resposta": "login"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Sair da linha",
        "resposta": "exit"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Configurar enable secret 'ciscoenpass'",
        "resposta": "enable secret ciscoenpass"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Encriptar passwords",
        "resposta": "service password-encryption"
    },

    # --- S2: Configuração SSH ---
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Criar user 'admin' com secret 'admin1pass'",
        "resposta": "username admin secret admin1pass"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Definir domínio 'ccna-ptsa.com'",
        "resposta": "ip domain name ccna-ptsa.com"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Gerar chaves RSA",
        "resposta": "crypto key generate rsa"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Tamanho da chave (bits)",
        "resposta": "1024"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Forçar SSH versão 2",
        "resposta": "ip ssh version 2"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Entrar nas linhas VTY 0 a 15",
        "resposta": "line vty 0 15"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Usar base de dados local para login",
        "resposta": "login local"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Permitir apenas SSH",
        "resposta": "transport input ssh"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Sair das linhas",
        "resposta": "exit"
    }
    # ==========================================
    # SVI & GATEWAY (Step 4)
    # ==========================================
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Configurar Interface VLAN 4 (Gestão)",
        "resposta": "interface vlan 4"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) IP da VLAN 4: 10.19.8.98 /29",
        "resposta": "ip address 10.19.8.98 255.255.255.248"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Descrição da interface",
        "resposta": "description Management Interface"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Ligar a interface",
        "resposta": "no shutdown"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Configurar Default Gateway (aponta para o Router)",
        "resposta": "ip default-gateway 10.19.8.97"
    },
    # --- Repetição para S2 ---
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Configurar Interface VLAN 4",
        "resposta": "interface vlan 4"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) IP da VLAN 4: 10.19.8.99 /29",
        "resposta": "ip address 10.19.8.99 255.255.255.248"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) Ligar a interface",
        "resposta": "no shutdown"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Configurar Default Gateway",
        "resposta": "ip default-gateway 10.19.8.97"
    },

    # ==========================================
    # VLANs & TRUNKING (Part 3 - Step 1)
    # ==========================================
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Criar VLAN 2 e nomear 'Bikes' (tudo numa linha ou separado, aqui assumimos o comando de criar)",
        "resposta": "vlan 2"
    },
    {
        "contexto": "S1(config-vlan)",
        "pergunta": "(S1) Nomear VLAN 2",
        "resposta": "name Bikes"
    },
    # Nota: Vou resumir as outras VLANs para não ficar repetitivo, mas no exame tens de fazer todas
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Criar restantes VLANs (3, 4, 5, 6) e nomear (Trikes, Management, Parking, Native). Digita 'ok' para avançar.",
        "resposta": "ok" 
    },
    
    # --- Configuração de Trunk S1 ---
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Configurar trunk nas interfaces f0/1 e f0/2",
        "resposta": "interface range f0/1-2"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Definir modo trunk",
        "resposta": "switchport mode trunk"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Definir VLAN nativa como 6",
        "resposta": "switchport trunk native vlan 6"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Permitir VLANs 2,3,4,5,6",
        "resposta": "switchport trunk allowed vlan 2,3,4,5,6"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Configurar interface f0/5 (Ligação ao Router)",
        "resposta": "interface f0/5"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1 - f0/5) Definir modo trunk",
        "resposta": "switchport mode trunk"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1 - f0/5) Definir VLAN nativa 6",
        "resposta": "switchport trunk native vlan 6"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1 - f0/5) Permitir VLANs 2,3,4,5,6",
        "resposta": "switchport trunk allowed vlan 2,3,4,5,6"
    },

    # ==========================================
    # ETHERCHANNEL (Part 3 - Step 2)
    # ==========================================
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Selecionar portas para EtherChannel (f0/1-2)",
        "resposta": "interface range f0/1-2"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Criar grupo 1 modo LACP Ativo",
        "resposta": "channel-group 1 mode active"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Entrar na interface lógica criada",
        "resposta": "interface port-channel 1"
    },
    # Repete-se para o S2 (f0/1-2), mas vou omitir aqui para poupar espaço. Lembra-te de fazer no S2!

    # ==========================================
    # SWITCHPORTS & SECURITY (Part 3 - Step 3)
    # ==========================================
    # --- S1 Host ---
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Configurar porta do PC (f0/6)",
        "resposta": "interface f0/6"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Modo de acesso",
        "resposta": "switchport mode access"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Atribuir à VLAN 2",
        "resposta": "switchport access vlan 2"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Ativar Port Security",
        "resposta": "switchport port-security"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Máximo de MACs: 3",
        "resposta": "switchport port-security maximum 3"
    },
    
    # --- Interfaces não usadas (S1) ---
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Selecionar interfaces não usadas (f0/3-4, 7-24, g0/1-2)",
        "resposta": "interface range f0/3-4, f0/7-24, g0/1-2"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Mover para VLAN Parking (5)",
        "resposta": "switchport access vlan 5"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Desligar interfaces",
        "resposta": "shutdown"
    },

    # ==========================================
    # ROUTING & DHCP (Part 4)
    # ==========================================
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Rota estática IPv4 padrão para Loopback 0",
        "resposta": "ip route 0.0.0.0 0.0.0.0 loopback 0"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Rota estática IPv6 padrão para Loopback 0",
        "resposta": "ipv6 route ::/0 loopback 0"
    },

    # --- DHCP Pool A (VLAN 2) ---
    {
        "contexto": "R1(config)",
        "pergunta": "(R1 DHCP) Excluir IPs .1 a .52",
        "resposta": "ip dhcp excluded-address 10.19.8.1 10.19.8.52"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1 DHCP) Criar pool 'CCNA-A'",
        "resposta": "ip dhcp pool CCNA-A"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool A) Definir rede e máscara (/26)",
        "resposta": "network 10.19.8.0 255.255.255.192"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool A) Definir Default Router",
        "resposta": "default-router 10.19.8.1"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool A) Definir Domain Name",
        "resposta": "domain-name ccna-a.net"
    },

    # --- DHCP Pool B (VLAN 3) ---
    {
        "contexto": "R1(config)",
        "pergunta": "(R1 DHCP) Excluir IPs .65 a .84",
        "resposta": "ip dhcp excluded-address 10.19.8.65 10.19.8.84"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1 DHCP) Criar pool 'CCNA-B'",
        "resposta": "ip dhcp pool CCNA-B"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool B) Definir rede e máscara (/27)",
        "resposta": "network 10.19.8.64 255.255.255.224"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool B) Definir Default Router",
        "resposta": "default-router 10.19.8.65"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool B) Definir Domain Name",
        "resposta": "domain-name ccna-b.net"
    }
]

def limpar_texto(texto):
    return " ".join(texto.strip().lower().split())

# --- LÓGICA DO STREAMLIT ---

def verificar_resposta():
    # Obtém a resposta do utilizador e o desafio atual
    user_input = st.session_state.resposta_user
    idx = st.session_state.indice_atual
    desafio = desafios[idx]
    
    resposta_limpa = limpar_texto(user_input)
    gabarito_limpo = limpar_texto(desafio['resposta'])
    alternativas = [limpar_texto(alt) for alt in desafio.get('alt_respostas', [])]

    if resposta_limpa == gabarito_limpo or resposta_limpa in alternativas:
        st.session_state.feedback = "✅ CORRETO!"
        st.session_state.pontuacao += 1
        st.session_state.mostrar_proximo = True
    else:
        st.session_state.feedback = f"❌ INCORRETO. A resposta correta era: {desafio['resposta']}"
        st.session_state.mostrar_proximo = True

def proximo_desafio():
    st.session_state.indice_atual += 1
    st.session_state.mostrar_proximo = False
    st.session_state.feedback = ""
    st.session_state.resposta_user = "" # Limpa a caixa de texto

# Inicialização de variáveis de estado (Session State)
if 'indice_atual' not in st.session_state:
    st.session_state.indice_atual = 0
if 'pontuacao' not in st.session_state:
    st.session_state.pontuacao = 0
if 'mostrar_proximo' not in st.session_state:
    st.session_state.mostrar_proximo = False
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

# --- INTERFACE ---
st.title("Treino Cisco SRWE")

if st.session_state.indice_atual < len(desafios):
    desafio_atual = desafios[st.session_state.indice_atual]
    
    # Barra de Progresso
    progresso = st.session_state.indice_atual / len(desafios)
    st.progress(progresso)
    st.write(f"Passo {st.session_state.indice_atual + 1} de {len(desafios)}")
    
    # Mostra a pergunta
    st.subheader(f"Tarefa: {desafio_atual['pergunta']}")
    
    # Simula o prompt visualmente
    st.code(f"{desafio_atual['contexto']}#", language="text")

    # Se ainda não respondeu ou errou, mostra caixa de input
    if not st.session_state.mostrar_proximo:
        st.text_input(
            "Digita o comando:", 
            key="resposta_user", 
            on_change=verificar_resposta
        )
        st.button("Submeter", on_click=verificar_resposta)
    
    # Se já respondeu, mostra feedback e botão para avançar
    else:
        if "CORRETO" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)
            
        st.button("Próximo Desafio", on_click=proximo_desafio)

else:
    st.success("🎉 TREINO CONCLUÍDO!")
    st.write(f"Pontuação Final: {st.session_state.pontuacao} / {len(desafios)}")
    if st.button("Reiniciar"):
        st.session_state.indice_atual = 0
        st.session_state.pontuacao = 0
        st.session_state.mostrar_proximo = False
        st.rerun()
