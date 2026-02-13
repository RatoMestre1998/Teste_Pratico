import streamlit as st

# ==========================================
# 1. LISTA DE DESAFIOS
# ==========================================
# ⚠️ IMPORTANTE: Cola aqui a tua lista completa 'desafios = [...]'
# Mantém a estrutura exata que tinhas antes.
# ==========================================
# LISTA COMPLETA DE DESAFIOS (EXAME FINAL)
# ==========================================
desafios = [
    # -------------------------------------------------------------------------
    # STEP 1: R1 BASIC SETTINGS & HARDENING
    # -------------------------------------------------------------------------
    {
        "contexto": "Router(config)",
        "pergunta": "(R1) Impedir a resolução de nomes de domínio (DNS Lookup)",
        "resposta": "no ip domain-lookup",
        "alt_respostas": ["no ip domain lookup"]
    },
    {
        "contexto": "Router(config)",
        "pergunta": "(R1) Configurar o hostname para R1",
        "resposta": "hostname R1"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Banner MOTD. (Nota: Usa 'Acess' com um 'c' e 'Prohibited' normal)",
        "resposta": "banner motd #Unauthorized Acess is Prohibited#"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Entrar na consola 0",
        "resposta": "line console 0"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "(R1) Password da consola: 'ciscoconpass'",
        "resposta": "password ciscoconpass"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "(R1) Ativar login na consola",
        "resposta": "login"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "(R1) Sair da linha",
        "resposta": "exit"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Password secreta (enable secret): 'ciscoenpass'",
        "resposta": "enable secret ciscoenpass"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Encriptar passwords em texto simples",
        "resposta": "service password-encryption"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Definir tamanho mínimo de password para 10",
        "resposta": "security passwords min-length 10"
    },
    
    # --- R1 SSH ---
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Criar user 'admin' com secret 'admin1pass'",
        "resposta": "username admin secret admin1pass"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Definir domínio 'ccna-ptsa.com'",
        "resposta": "ip domain name ccna-ptsa.com"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Gerar chaves RSA",
        "resposta": "crypto key generate rsa"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Tamanho da chave (bits)",
        "resposta": "1024"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Definir versão SSH para 2",
        "resposta": "ip ssh version 2"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Entrar nas linhas VTY 0 15",
        "resposta": "line vty 0 15"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "(R1) Login pela base de dados local",
        "resposta": "login local"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "(R1) Permitir apenas input SSH",
        "resposta": "transport input ssh"
    },
    {
        "contexto": "R1(config-line)",
        "pergunta": "Sair das linhas",
        "resposta": "exit"
    },

    # -------------------------------------------------------------------------
    # STEP 2: R1 INTERFACES & SUBINTERFACES
    # -------------------------------------------------------------------------
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Interface Loopback 0",
        "resposta": "interface Loopback 0"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "(R1) Descrição 'Loopback'",
        "resposta": "description Loopback"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "(R1) IP Address 209.165.201.1 /27",
        "resposta": "ip address 209.165.201.1 255.255.255.224"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "(R1) IPv6 Address 2001:db8:acad:209::1/64",
        "resposta": "ipv6 address 2001:db8:acad:209::1/64"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "(R1) IPv6 Link-Local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "Sair da interface",
        "resposta": "exit"
    },
    
    # --- R1 Subinterfaces ---
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Ativar routing IPv6",
        "resposta": "ipv6 unicast-routing"
    },
    # VLAN 2 (Bikes)
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Subinterface g0/0/1.2",
        "resposta": "interface g0/0/1.2"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Encapsulamento dot1Q VLAN 2",
        "resposta": "encapsulation dot1Q 2"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Descrição 'Bikes'",
        "resposta": "description Bikes"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IP 10.19.8.1 /26",
        "resposta": "ip address 10.19.8.1 255.255.255.192"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IPv6 2001:db8:acad:a::1/64",
        "resposta": "ipv6 address 2001:db8:acad:a::1/64"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IPv6 Link-Local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },
    # VLAN 3 (Trikes)
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Subinterface g0/0/1.3",
        "resposta": "interface g0/0/1.3"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Encapsulamento dot1Q VLAN 3",
        "resposta": "encapsulation dot1Q 3"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Descrição 'Trikes'",
        "resposta": "description Trikes"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IP 10.19.8.65 /27",
        "resposta": "ip address 10.19.8.65 255.255.255.224"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IPv6 2001:db8:acad:b::1/64",
        "resposta": "ipv6 address 2001:db8:acad:b::1/64"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IPv6 Link-Local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },
    # VLAN 4 (Management)
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Subinterface g0/0/1.4",
        "resposta": "interface g0/0/1.4"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Encapsulamento dot1Q VLAN 4",
        "resposta": "encapsulation dot1Q 4"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Descrição 'Management'",
        "resposta": "description Management"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IP 10.19.8.97 /29",
        "resposta": "ip address 10.19.8.97 255.255.255.248"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IPv6 2001:db8:acad:c::1/64",
        "resposta": "ipv6 address 2001:db8:acad:c::1/64"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) IPv6 Link-Local fe80::1",
        "resposta": "ipv6 address fe80::1 link-local"
    },
    # VLAN 6 (Native)
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Subinterface g0/0/1.6 (Nativa)",
        "resposta": "interface g0/0/1.6"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Encapsulamento Nativo VLAN 6",
        "resposta": "encapsulation dot1Q 6 native"
    },
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Descrição 'Native'",
        "resposta": "description Native"
    },
    # Ativar Física
    {
        "contexto": "R1(config-subif)",
        "pergunta": "(R1) Interface Física g0/0/1",
        "resposta": "interface g0/0/1"
    },
    {
        "contexto": "R1(config-if)",
        "pergunta": "(R1) Ligar interface",
        "resposta": "no shutdown"
    },

    # -------------------------------------------------------------------------
    # STEP 3: SWITCH 1 (S1) BASIC & HARDENING
    # -------------------------------------------------------------------------
    {
        "contexto": "Switch(config)",
        "pergunta": "(S1) Desativar DNS Lookup",
        "resposta": "no ip domain-lookup",
        "alt_respostas": ["no ip domain lookup"]
    },
    {
        "contexto": "Switch(config)",
        "pergunta": "(S1) Hostname S1",
        "resposta": "hostname S1"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Banner MOTD. (Atenção: 'Prohibitted' com dois Ts e 'Access' normal)",
        "resposta": "banner motd #Unauthorized Access is Prohibitted!#"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Linha consola 0",
        "resposta": "line console 0"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Password consola 'ciscoconpass'",
        "resposta": "password ciscoconpass"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Login",
        "resposta": "login"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "Exit",
        "resposta": "exit"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Enable secret 'ciscoenpass'",
        "resposta": "enable secret ciscoenpass"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Encriptação de passwords",
        "resposta": "service password-encryption"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) User admin secret admin1pass",
        "resposta": "username admin secret admin1pass"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Domain name",
        "resposta": "ip domain name ccna-ptsa.com"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Gerar chaves RSA",
        "resposta": "crypto key generate rsa"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Tamanho chave 1024",
        "resposta": "1024"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) SSH versão 2",
        "resposta": "ip ssh version 2"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Linhas VTY 0 15",
        "resposta": "line vty 0 15"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Login local",
        "resposta": "login local"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "(S1) Transport input ssh",
        "resposta": "transport input ssh"
    },
    {
        "contexto": "S1(config-line)",
        "pergunta": "Exit",
        "resposta": "exit"
    },

    # -------------------------------------------------------------------------
    # STEP 3: SWITCH 2 (S2) BASIC & HARDENING
    # -------------------------------------------------------------------------
    {
        "contexto": "Switch(config)",
        "pergunta": "(S2) Desativar DNS Lookup",
        "resposta": "no ip domain-lookup",
        "alt_respostas": ["no ip domain lookup"]
    },
    {
        "contexto": "Switch(config)",
        "pergunta": "(S2) Hostname S2",
        "resposta": "hostname S2"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Banner MOTD. (Atenção: 'Prohibitted' com dois Ts)",
        "resposta": "banner motd #Unauthorized Access is Prohibitted!#"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Linha consola 0",
        "resposta": "line console 0"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Password consola 'ciscoconpass'",
        "resposta": "password ciscoconpass"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Login",
        "resposta": "login"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "Exit",
        "resposta": "exit"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Enable secret 'ciscoenpass'",
        "resposta": "enable secret ciscoenpass"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Encriptação de passwords",
        "resposta": "service password-encryption"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) User admin secret admin1pass",
        "resposta": "username admin secret admin1pass"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Domain name",
        "resposta": "ip domain name ccna-ptsa.com"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Gerar chaves RSA",
        "resposta": "crypto key generate rsa"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Tamanho chave 1024",
        "resposta": "1024"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) SSH versão 2",
        "resposta": "ip ssh version 2"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Linhas VTY 0 15",
        "resposta": "line vty 0 15"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Login local",
        "resposta": "login local"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "(S2) Transport input ssh",
        "resposta": "transport input ssh"
    },
    {
        "contexto": "S2(config-line)",
        "pergunta": "Exit",
        "resposta": "exit"
    },

    # -------------------------------------------------------------------------
    # STEP 4: SVI (MANAGEMENT INTERFACE)
    # -------------------------------------------------------------------------
    # S1
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Interface VLAN 4",
        "resposta": "interface vlan 4"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) IP 10.19.8.98 /29",
        "resposta": "ip address 10.19.8.98 255.255.255.248"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Descrição",
        "resposta": "description Management Interface"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) No shutdown",
        "resposta": "no shutdown"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "Exit",
        "resposta": "exit"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Default Gateway 10.19.8.97",
        "resposta": "ip default-gateway 10.19.8.97"
    },
    # S2
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Interface VLAN 4",
        "resposta": "interface vlan 4"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) IP 10.19.8.99 /29",
        "resposta": "ip address 10.19.8.99 255.255.255.248"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) Descrição",
        "resposta": "description Management Interface"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) No shutdown",
        "resposta": "no shutdown"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "Exit",
        "resposta": "exit"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Default Gateway 10.19.8.97",
        "resposta": "ip default-gateway 10.19.8.97"
    },

    # -------------------------------------------------------------------------
    # PART 3: VLANS, TRUNKING, ETHERCHANNEL
    # -------------------------------------------------------------------------
    # S1 VLANs
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Criar VLAN 2 e nomear 'Bikes' (vamos assumir o bloco inteiro por brevidade ou linha a linha)",
        "resposta": "vlan 2"
    },
    {
        "contexto": "S1(config-vlan)",
        "pergunta": "(S1) Nome 'Bikes'",
        "resposta": "name Bikes"
    },
    {
        "contexto": "S1(config-vlan)",
        "pergunta": "(S1) Criar restantes VLANs (3,4,5,6) e nomes. Digita 'vlan 3' para continuar.",
        "resposta": "vlan 3"
    },
    {
        "contexto": "S1(config-vlan)",
        "pergunta": "(S1) Nome 'Trikes'",
        "resposta": "name Trikes"
    },
    # S1 Trunks
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Trunking em f0/1-2",
        "resposta": "interface range f0/1-2"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Switchport mode trunk",
        "resposta": "switchport mode trunk"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) VLAN Nativa 6",
        "resposta": "switchport trunk native vlan 6"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Allowed VLANs 2-6",
        "resposta": "switchport trunk allowed vlan 2,3,4,5,6"
    },
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Trunking em f0/5 (ligação ao Router)",
        "resposta": "interface f0/5"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Switchport mode trunk",
        "resposta": "switchport mode trunk"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) VLAN Nativa 6",
        "resposta": "switchport trunk native vlan 6"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Allowed VLANs 2-6",
        "resposta": "switchport trunk allowed vlan 2,3,4,5,6"
    },
    # S2 VLANs e Trunks
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Criar VLANs 2,3,4,5,6 (Digita 'vlan 2' para começar)",
        "resposta": "vlan 2"
    },
    {
        "contexto": "S2(config-vlan)",
        "pergunta": "(S2) Nome 'Bikes'",
        "resposta": "name Bikes"
    },
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Trunking em f0/1-2",
        "resposta": "interface range f0/1-2"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Switchport mode trunk",
        "resposta": "switchport mode trunk"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) VLAN Nativa 6",
        "resposta": "switchport trunk native vlan 6"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Allowed VLANs 2-6",
        "resposta": "switchport trunk allowed vlan 2,3,4,5,6"
    },

    # --- EtherChannel ---
    # S1
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Interface range f0/1-2 para EtherChannel",
        "resposta": "interface range f0/1-2"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Channel-group 1 mode active (LACP)",
        "resposta": "channel-group 1 mode active"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Interface port-channel 1",
        "resposta": "interface port-channel 1"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "Exit",
        "resposta": "exit"
    },
    # S2
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Interface range f0/1-2 para EtherChannel",
        "resposta": "interface range f0/1-2"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Channel-group 1 mode active (LACP)",
        "resposta": "channel-group 1 mode active"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Interface port-channel 1",
        "resposta": "interface port-channel 1"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "Exit",
        "resposta": "exit"
    },

    # --- Switchports & Security ---
    # S1 Access
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Configurar f0/6 (Host)",
        "resposta": "interface f0/6"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Descrição 'host'",
        "resposta": "description host"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Mode access",
        "resposta": "switchport mode access"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Access vlan 2",
        "resposta": "switchport access vlan 2"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Ativar Port-Security",
        "resposta": "switchport port-security"
    },
    {
        "contexto": "S1(config-if)",
        "pergunta": "(S1) Maximo 3 MACs",
        "resposta": "switchport port-security maximum 3"
    },
    # S1 Unused
    {
        "contexto": "S1(config)",
        "pergunta": "(S1) Interfaces não usadas (f0/3-4, f0/7-24, g0/1-2)",
        "resposta": "interface range f0/3-4, f0/7-24, g0/1-2"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Mode access",
        "resposta": "switchport mode access"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Mover para VLAN Parking (5)",
        "resposta": "switchport access vlan 5"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Descrição 'Unused Interfaces'",
        "resposta": "description Unused Interfaces"
    },
    {
        "contexto": "S1(config-if-range)",
        "pergunta": "(S1) Shutdown",
        "resposta": "shutdown"
    },
    # S2 Access
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Configurar f0/18 (Host)",
        "resposta": "interface f0/18"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) Mode access",
        "resposta": "switchport mode access"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) Ativar Port-Security",
        "resposta": "switchport port-security"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) Access vlan 3",
        "resposta": "switchport access vlan 3"
    },
    {
        "contexto": "S2(config-if)",
        "pergunta": "(S2) Maximo 3 MACs",
        "resposta": "switchport port-security maximum 3"
    },
    # S2 Unused
    {
        "contexto": "S2(config)",
        "pergunta": "(S2) Interfaces não usadas (f0/3-17, f0/19-24, g0/1-2)",
        "resposta": "interface range f0/3-17, f0/19-24, g0/1-2"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Mode access",
        "resposta": "switchport mode access"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Mover para VLAN Parking (5)",
        "resposta": "switchport access vlan 5"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Descrição",
        "resposta": "description Unused Interfaces"
    },
    {
        "contexto": "S2(config-if-range)",
        "pergunta": "(S2) Shutdown",
        "resposta": "shutdown"
    },

    # -------------------------------------------------------------------------
    # PART 4: ROUTING & DHCP (R1)
    # -------------------------------------------------------------------------
    # Routing
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Rota default IPv4 (via Loopback 0)",
        "resposta": "ip route 0.0.0.0 0.0.0.0 loopback 0"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) Rota default IPv6 (via Loopback 0)",
        "resposta": "ipv6 route ::/0 loopback 0"
    },
    # DHCP Pool A
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) DHCP Exclude .1 a .52",
        "resposta": "ip dhcp excluded-address 10.19.8.1 10.19.8.52"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) DHCP Pool CCNA-A",
        "resposta": "ip dhcp pool CCNA-A"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool A) Network 10.19.8.0 /26",
        "resposta": "network 10.19.8.0 255.255.255.192"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool A) Default Router",
        "resposta": "default-router 10.19.8.1"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool A) Domain Name",
        "resposta": "domain-name ccna-a.net"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "Exit",
        "resposta": "exit"
    },
    # DHCP Pool B
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) DHCP Exclude .65 a .84",
        "resposta": "ip dhcp excluded-address 10.19.8.65 10.19.8.84"
    },
    {
        "contexto": "R1(config)",
        "pergunta": "(R1) DHCP Pool CCNA-B",
        "resposta": "ip dhcp pool CCNA-B"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool B) Network 10.19.8.64 /27",
        "resposta": "network 10.19.8.64 255.255.255.224"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool B) Default Router",
        "resposta": "default-router 10.19.8.65"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "(Pool B) Domain Name",
        "resposta": "domain-name ccna-b.net"
    },
    {
        "contexto": "R1(dhcp-config)",
        "pergunta": "Exit",
        "resposta": "exit"
    }
]
# ==========================================
# 2. FUNÇÕES LÓGICAS
# ==========================================

def limpar_texto(texto):
    """Remove espaços extras e converte para minúsculas"""
    if texto is None:
        return ""
    return " ".join(texto.strip().lower().split())

def navegar(direcao):
    """Função para mover para trás ou para a frente"""
    novo_indice = st.session_state.indice_atual + direcao
    
    # Garante que não sai dos limites da lista
    if 0 <= novo_indice < len(desafios):
        st.session_state.indice_atual = novo_indice
        # Limpa o feedback e a caixa de texto ao mudar de pergunta
        st.session_state.feedback = ""
        st.session_state.resposta_user = ""
        st.session_state.ajuda_ativa = ""

def verificar_ou_ajudar():
    user_input = st.session_state.resposta_user
    
    # --- LÓGICA DO INTERROGATORIO (?) ---
    if user_input and user_input.strip().endswith("?"):
        # Remove o ? e espaços para analisar
        input_limpo = user_input.replace("?", "").strip().lower()
        idx = st.session_state.indice_atual
        resposta_correta = desafios[idx]['resposta']
        
        # Se o user não escreveu nada e pôs ?, mostra a primeira palavra
        if input_limpo == "":
            st.session_state.ajuda_ativa = f"Dica: O comando começa com '{resposta_correta.split()[0]}...'"
            st.session_state.feedback = "" # Limpa erro se houver
            return

        # Verifica se o que ele escreveu até agora bate certo com o início da resposta
        if resposta_correta.lower().startswith(input_limpo):
            # Mostra o comando completo como ajuda
            st.session_state.ajuda_ativa = f"Comando esperado: {resposta_correta}"
            st.session_state.feedback = ""
        else:
            st.session_state.ajuda_ativa = "❌ O início do comando não parece correto. Tenta outra palavra."
            st.session_state.feedback = ""
        return

    # --- LÓGICA NORMAL DE VERIFICAÇÃO ---
    if not user_input or user_input.strip() == "":
        st.session_state.feedback = "⚠️ Escreve um comando antes de submeter!"
        st.session_state.ajuda_ativa = ""
        return

    idx = st.session_state.indice_atual
    desafio = desafios[idx]
    
    resposta_limpa = limpar_texto(user_input)
    gabarito_limpo = limpar_texto(desafio['resposta'])
    alternativas = [limpar_texto(alt) for alt in desafio.get('alt_respostas', [])]

    if resposta_limpa == gabarito_limpo or resposta_limpa in alternativas:
        st.session_state.feedback = "✅ CORRETO!"
        st.session_state.ajuda_ativa = "" # Limpa a ajuda se acertou
        # Opcional: Auto-avançar (comentei para deixar o user ver que acertou)
        # navegar(1) 
    else:
        st.session_state.feedback = f"❌ INCORRETO."
        st.session_state.ajuda_ativa = "" # Limpa ajuda antiga

# ==========================================
# 3. INTERFACE STREAMLIT
# ==========================================

# Configuração da Página
st.set_page_config(page_title="Treino Cisco", layout="centered")

# Inicialização de variáveis de estado
if 'indice_atual' not in st.session_state:
    st.session_state.indice_atual = 0
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'ajuda_ativa' not in st.session_state:
    st.session_state.ajuda_ativa = ""
if 'resposta_user' not in st.session_state:
    st.session_state.resposta_user = ""

st.title("📟 Simulador Cisco SRWE")

# Verifica se a lista não está vazia ou acabada
if st.session_state.indice_atual < len(desafios):
    desafio_atual = desafios[st.session_state.indice_atual]
    
    # --- BARRA DE NAVEGAÇÃO ---
    col_prev, col_prog, col_next = st.columns([1, 3, 1])
    
    with col_prev:
        if st.button("⬅️ Anterior", disabled=(st.session_state.indice_atual == 0)):
            navegar(-1)
            st.rerun()

    with col_prog:
        progresso = (st.session_state.indice_atual + 1) / len(desafios)
        st.progress(progresso)
        st.caption(f"Passo {st.session_state.indice_atual + 1} de {len(desafios)}")

    with col_next:
        if st.button("Próximo ➡️", disabled=(st.session_state.indice_atual == len(desafios) - 1)):
            navegar(1)
            st.rerun()

    st.divider()

    # --- ÁREA DO DESAFIO ---
    st.subheader(f"Tarefa: {desafio_atual['pergunta']}")
    
    # Terminal Simulado (Visual)
    st.code(f"{desafio_atual['contexto']}# {st.session_state.resposta_user}", language="bash")

    # --- ÁREA DE INPUT ---
    # O formulário permite submeter com "Enter"
    with st.form(key='console_form', clear_on_submit=False):
        user_input = st.text_input(
            "Digita o comando (usa '?' para ajuda):", 
            key="resposta_user",
            placeholder="Ex: ip address..."
        )
        
        # Botão de submissão
        submitted = st.form_submit_button("Verificar / Enter")
        
        if submitted:
            verificar_ou_ajudar()
            st.rerun()

    # --- FEEDBACK E AJUDA ---
    
    # 1. Mostra Ajuda do '?' (Azul)
    if st.session_state.ajuda_ativa:
        st.info(st.session_state.ajuda_ativa)

    # 2. Mostra Sucesso ou Erro
    if st.session_state.feedback:
        if "CORRETO" in st.session_state.feedback:
            st.success(st.session_state.feedback)
            # Botão extra para avançar rapidamente se acertou
            if st.button("Avançar para o próximo passo"):
                navegar(1)
                st.rerun()
        elif "INCORRETO" in st.session_state.feedback:
            st.error(st.session_state.feedback)
            # Opção de ver a resposta se estiver mesmo encravado
            with st.expander("Ver Resposta Correta (Desistir deste passo)"):
                st.code(desafio_atual['resposta'])

else:
    st.balloons()
    st.success("🎉 TREINO CONCLUÍDO!")
    if st.button("Reiniciar Tudo"):
        st.session_state.indice_atual = 0
        st.session_state.feedback = ""
        st.session_state.resposta_user = ""
        st.rerun()
