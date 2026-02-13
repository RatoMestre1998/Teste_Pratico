import streamlit as st

# ==========================================
# 1. BASE DE DADOS (BLOCOS DE COMANDOS)
# ==========================================
desafios = [
    # -------------------------------------------------------------------------
    # STEP 1: R1 BASIC SETTINGS
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 1: Configure R1 Basic Settings and Device Hardening (Part A)",
        "instrucoes": [
            "a. Configure basic settings.",
            "- Prevent the router from attempting to resolve incorrectly entered commands as domain names.",
            "- Configure the R1 hostname.",
            "- Configure an appropriate MOTD banner.",
            "(Note: Use the exact text '#Unauthorized Acess is Prohibited#')"
        ],
        "resposta_esperada": """no ip domain-lookup
hostname R1
banner motd #Unauthorized Acess is Prohibited#"""
    },
    {
        "titulo": "Step 1: Configure R1 Basic Settings and Device Hardening (Part B)",
        "instrucoes": [
            "b. Configure password security.",
            "- Configure the console password and enable connections (password: ciscoconpass).",
            "- Configure an enable secret password (password: ciscoenpass).",
            "- Encrypt all clear text passwords.",
            "- Set the minimum length of newly created passwords to 10 characters."
        ],
        "resposta_esperada": """line console 0
password ciscoconpass
login
exit
enable secret ciscoenpass
service password-encryption
security passwords min-length 10"""
    },
    {
        "titulo": "Step 1: Configure R1 Basic Settings and Device Hardening (Part C)",
        "instrucoes": [
            "c. Configure SSH.",
            "1) Create an administrative user in the local user database (user: admin, secret: admin1pass).",
            "2) Configure the domain name as ccna-ptsa.com",
            "3) Create an RSA crypto key with a modulus of 1024 bits.",
            "4) Ensure that more secure version of SSH will be used (version 2).",
            "5) Configure the vty lines (0-15) to authenticate logins against the local user database.",
            "6) Configure the vty lines to only accept connections over SSH."
        ],
        "resposta_esperada": """username admin secret admin1pass
ip domain name ccna-ptsa.com
crypto key generate rsa
1024
ip ssh version 2
line vty 0 15
login local
transport input ssh
exit"""
    },

    # -------------------------------------------------------------------------
    # STEP 2: R1 INTERFACES
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 2a: Configure R1 with a loopback interface",
        "instrucoes": [
            "Configure the loopback0 with IPv4 and IPv6 addressing:",
            "- Description: Loopback",
            "- IPv4: 209.165.201.1 /27 (255.255.255.224)",
            "- IPv6: 2001:db8:acad:209::1/64",
            "- IPv6 Link-Local: fe80::1"
        ],
        "resposta_esperada": """interface Loopback 0
description Loopback
ip address 209.165.201.1 255.255.255.224
ipv6 address 2001:db8:acad:209::1/64
ipv6 address fe80::1 link-local
exit"""
    },
    {
        "titulo": "Step 2b: Configure Router Subinterfaces (Part 1)",
        "instrucoes": [
            "1. Enable IPv6 routing (ipv6 unicast-routing).",
            "2. Configure subinterface g0/0/1.2 (VLAN 2 - Bikes):",
            "- Encapsulation dot1Q 2",
            "- Description: Bikes",
            "- IPv4: 10.19.8.1 /26 (255.255.255.192)",
            "- IPv6: 2001:db8:acad:a::1/64",
            "- IPv6 Link-Local: fe80::1"
        ],
        "resposta_esperada": """ipv6 unicast-routing
interface g0/0/1.2
encapsulation dot1Q 2
description Bikes
ip address 10.19.8.1 255.255.255.192
ipv6 address 2001:db8:acad:a::1/64
ipv6 address fe80::1 link-local"""
    },
    {
        "titulo": "Step 2b: Configure Router Subinterfaces (Part 2)",
        "instrucoes": [
            "3. Configure subinterface g0/0/1.3 (VLAN 3 - Trikes):",
            "- Encapsulation dot1Q 3",
            "- Description: Trikes",
            "- IPv4: 10.19.8.65 /27 (255.255.255.224)",
            "- IPv6: 2001:db8:acad:b::1/64",
            "- IPv6 Link-Local: fe80::1",
            "4. Configure subinterface g0/0/1.4 (VLAN 4 - Management):",
            "- Encapsulation dot1Q 4",
            "- Description: Management",
            "- IPv4: 10.19.8.97 /29 (255.255.255.248)",
            "- IPv6: 2001:db8:acad:c::1/64",
            "- IPv6 Link-Local: fe80::1"
        ],
        "resposta_esperada": """interface g0/0/1.3
encapsulation dot1Q 3
description Trikes
ip address 10.19.8.65 255.255.255.224
ipv6 address 2001:db8:acad:b::1/64
ipv6 address fe80::1 link-local
interface g0/0/1.4
encapsulation dot1Q 4
description Management
ip address 10.19.8.97 255.255.255.248
ipv6 address 2001:db8:acad:c::1/64
ipv6 address fe80::1 link-local"""
    },
    {
        "titulo": "Step 2b: Configure Router Subinterfaces (Part 3 - Native)",
        "instrucoes": [
            "5. Configure the native VLAN interface (g0/0/1.6):",
            "- Encapsulation dot1Q 6 native",
            "- Description: Native",
            "6. Enable the physical interface g0/0/1."
        ],
        "resposta_esperada": """interface g0/0/1.6
encapsulation dot1Q 6 native
description Native
interface g0/0/1
no shutdown"""
    },

    # -------------------------------------------------------------------------
    # STEP 3: SWITCH 1 (S1)
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 3: Configure S1 Basic Settings & Hardening (a, b)",
        "instrucoes": [
            "Perform these tasks on S1:",
            "a. Basic Settings:",
            "- No ip domain lookup",
            "- Hostname S1",
            "- Banner motd '#Unauthorized Access is Prohibitted!#'",
            "b. Device Hardening:",
            "- Console 0: password 'ciscoconpass', login",
            "- Enable secret 'ciscoenpass'",
            "- Service password-encryption"
        ],
        "resposta_esperada": """no ip domain-lookup
hostname S1
banner motd #Unauthorized Access is Prohibitted!#
line console 0
password ciscoconpass
login
exit
enable secret ciscoenpass
service password-encryption"""
    },
    {
        "titulo": "Step 3c: Configure SSH on S1",
        "instrucoes": [
            "c. Configure SSH on S1:",
            "- User 'admin', secret 'admin1pass'",
            "- Domain name 'ccna-ptsa.com'",
            "- RSA key 1024 bits",
            "- SSH version 2",
            "- VTY 0 15: login local, transport input ssh"
        ],
        "resposta_esperada": """username admin secret admin1pass
ip domain name ccna-ptsa.com
crypto key generate rsa
1024
ip ssh version 2
line vty 0 15
login local
transport input ssh
exit"""
    },

    # -------------------------------------------------------------------------
    # STEP 3: SWITCH 2 (S2)
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 3: Configure S2 Basic Settings & Hardening (a, b)",
        "instrucoes": [
            "Perform these tasks on S2:",
            "a. Basic Settings:",
            "- No ip domain lookup",
            "- Hostname S2",
            "- Banner motd '#Unauthorized Access is Prohibitted!#'",
            "b. Device Hardening:",
            "- Console 0: password 'ciscoconpass', login",
            "- Enable secret 'ciscoenpass'",
            "- Service password-encryption"
        ],
        "resposta_esperada": """no ip domain-lookup
hostname S2
banner motd #Unauthorized Access is Prohibitted!#
line console 0
password ciscoconpass
login
exit
enable secret ciscoenpass
service password-encryption"""
    },
    {
        "titulo": "Step 3c: Configure SSH on S2",
        "instrucoes": [
            "c. Configure SSH on S2:",
            "- User 'admin', secret 'admin1pass'",
            "- Domain name 'ccna-ptsa.com'",
            "- RSA key 1024 bits",
            "- SSH version 2",
            "- VTY 0 15: login local, transport input ssh"
        ],
        "resposta_esperada": """username admin secret admin1pass
ip domain name ccna-ptsa.com
crypto key generate rsa
1024
ip ssh version 2
line vty 0 15
login local
transport input ssh
exit"""
    },

    # -------------------------------------------------------------------------
    # STEP 4: SVIs
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 4: Configure SVIs on S1",
        "instrucoes": [
            "a. Configure SVI for Management VLAN 4 on S1:",
            "- IP: 10.19.8.98 /29 (255.255.255.248)",
            "- Description: Management Interface",
            "- No shutdown",
            "b. Configure Default Gateway on S1:",
            "- IP: 10.19.8.97"
        ],
        "resposta_esperada": """interface vlan 4
ip address 10.19.8.98 255.255.255.248
description Management Interface
no shutdown
exit
ip default-gateway 10.19.8.97"""
    },
    {
        "titulo": "Step 4: Configure SVIs on S2",
        "instrucoes": [
            "a. Configure SVI for Management VLAN 4 on S2:",
            "- IP: 10.19.8.99 /29 (255.255.255.248)",
            "- Description: Management Interface",
            "- No shutdown",
            "b. Configure Default Gateway on S2:",
            "- IP: 10.19.8.97"
        ],
        "resposta_esperada": """interface vlan 4
ip address 10.19.8.99 255.255.255.248
description Management Interface
no shutdown
exit
ip default-gateway 10.19.8.97"""
    },

    # -------------------------------------------------------------------------
    # PART 3: NETWORK INFRASTRUCTURE
    # -------------------------------------------------------------------------
    {
        "titulo": "Part 3 Step 1: Configure VLANs and Trunking (S1)",
        "instrucoes": [
            "On S1:",
            "a. Create VLANs 2, 3, 4, 5, 6 with names (Bikes, Trikes, Management, Parking, Native)",
            "b. Create 802.1Q VLAN trunks on f0/1 and f0/2.",
            "- Native VLAN 6",
            "- Allowed VLANs 2,3,4,5,6",
            "c. Configure f0/5 as trunk (Native 6, Allowed 2,3,4,5,6)"
        ],
        "resposta_esperada": """vlan 2
name Bikes
vlan 3
name Trikes
vlan 4
name Management
vlan 5
name Parking
vlan 6
name Native
interface range f0/1-2
switchport mode trunk
switchport trunk native vlan 6
switchport trunk allowed vlan 2,3,4,5,6
exit
interface f0/5
switchport mode trunk
switchport trunk native vlan 6
switchport trunk allowed vlan 2,3,4,5,6
exit"""
    },
    {
        "titulo": "Part 3 Step 1: Configure VLANs and Trunking (S2)",
        "instrucoes": [
            "On S2:",
            "a. Create VLANs 2, 3, 4, 5, 6 with names (Bikes, Trikes, Management, Parking, Native)",
            "b. Create 802.1Q VLAN trunks on f0/1 and f0/2.",
            "- Native VLAN 6",
            "- Allowed VLANs 2,3,4,5,6"
        ],
        "resposta_esperada": """vlan 2
name Bikes
vlan 3
name Trikes
vlan 4
name Management
vlan 5
name Parking
vlan 6
name Native
interface range f0/1-2
switchport mode trunk
switchport trunk native vlan 6
switchport trunk allowed vlan 2,3,4,5,6
exit"""
    },
    {
        "titulo": "Part 3 Step 2: Configure Etherchannel (S1)",
        "instrucoes": [
            "On S1:",
            "Create Layer 2 EtherChannel group 1 using interfaces f0/1 and f0/2.",
            "- Mode: LACP (active)"
        ],
        "resposta_esperada": """interface range f0/1-2
channel-group 1 mode active
interface port-channel 1
exit"""
    },
    {
        "titulo": "Part 3 Step 2: Configure Etherchannel (S2)",
        "instrucoes": [
            "On S2:",
            "Create Layer 2 EtherChannel group 1 using interfaces f0/1 and f0/2.",
            "- Mode: LACP (active)"
        ],
        "resposta_esperada": """interface range f0/1-2
channel-group 1 mode active
interface port-channel 1
exit"""
    },
    {
        "titulo": "Part 3 Step 3: Configure Switchports (S1)",
        "instrucoes": [
            "On S1:",
            "a. Configure f0/6 (Host): Access VLAN 2",
            "b. Configure port security on f0/6 (Max 3 MACs)",
            "c. Assign unused ports (f0/3-4, f0/7-24, g0/1-2) to VLAN 5.",
            "d. Configure description 'Unused Interfaces' and shutdown."
        ],
        "resposta_esperada": """interface f0/6
description host
switchport mode access
switchport access vlan 2
switchport port-security
switchport port-security maximum 3
interface range f0/3-4, f0/7-24, g0/1-2
switchport mode access
switchport access vlan 5
description Unused Interfaces
shutdown"""
    },
    {
        "titulo": "Part 3 Step 3: Configure Switchports (S2)",
        "instrucoes": [
            "On S2:",
            "a. Configure f0/18 (Host): Access VLAN 3",
            "b. Configure port security on f0/18 (Max 3 MACs)",
            "c. Assign unused ports (f0/3-17, f0/19-24, g0/1-2) to VLAN 5.",
            "d. Configure description 'Unused Interfaces' and shutdown."
        ],
        "resposta_esperada": """interface f0/18
switchport mode access
switchport port-security
switchport access vlan 3
switchport port-security maximum 3
interface range f0/3-17, f0/19-24, g0/1-2
switchport mode access
switchport access vlan 5
description Unused Interfaces
shutdown"""
    },

    # -------------------------------------------------------------------------
    # PART 4: HOST SUPPORT (ROUTING & DHCP)
    # -------------------------------------------------------------------------
    {
        "titulo": "Part 4 Step 1: Configure Default Routing on R1",
        "instrucoes": [
            "a. Configure an IPv4 default route using Lo0 as exit interface.",
            "b. Configure an IPv6 default route using Lo0 as exit interface."
        ],
        "resposta_esperada": """ip route 0.0.0.0 0.0.0.0 loopback 0
ipv6 route ::/0 loopback 0"""
    },
    {
        "titulo": "Part 4 Step 2: Configure IPv4 DHCP for VLAN 2 (R1)",
        "instrucoes": [
            "a. Exclude addresses .1 to .52",
            "b. Create DHCP pool 'CCNA-A'.",
            "c. Network 10.19.8.0 /26",
            "d. Default router: 10.19.8.1",
            "e. Domain name: ccna-a.net"
        ],
        "resposta_esperada": """ip dhcp excluded-address 10.19.8.1 10.19.8.52
ip dhcp pool CCNA-A
network 10.19.8.0 255.255.255.192
default-router 10.19.8.1
domain-name ccna-a.net
exit"""
    },
    {
        "titulo": "Part 4 Step 3: Configure IPv4 DHCP for VLAN 3 (R1)",
        "instrucoes": [
            "a. Exclude addresses .65 to .84",
            "b. Create DHCP pool 'CCNA-B'.",
            "c. Network 10.19.8.64 /27",
            "d. Default router: 10.19.8.65",
            "e. Domain name: ccna-b.net"
        ],
        "resposta_esperada": """ip dhcp excluded-address 10.19.8.65 10.19.8.84
ip dhcp pool CCNA-B
network 10.19.8.64 255.255.255.224
default-router 10.19.8.65
domain-name ccna-b.net
exit"""
    }
]

# ==========================================
# 2. LÓGICA DE VALIDAÇÃO POR BLOCOS
# ==========================================

def normalizar_lista(texto):
    """Transforma texto multilinhas numa lista de linhas limpas"""
    if not texto:
        return []
    
    linhas = texto.strip().split('\n')
    # Remove espaços em branco no início/fim de cada linha e ignora linhas vazias
    linhas_limpas = [linha.strip().lower() for linha in linhas if linha.strip()]
    return linhas_limpas

def verificar_bloco():
    idx = st.session_state.indice_atual
    desafio = desafios[idx]
    
    user_text = st.session_state.resposta_user
    resposta_esperada = desafio['resposta_esperada']
    
    linhas_user = normalizar_lista(user_text)
    linhas_gabarito = normalizar_lista(resposta_esperada)
    
    # Se estiver vazio
    if not linhas_user:
        st.session_state.feedback = "⚠️ A caixa está vazia."
        st.session_state.erros = []
        return

    erros = []
    # Verifica linha a linha
    max_len = max(len(linhas_user), len(linhas_gabarito))
    tudo_correto = True
    
    for i in range(max_len):
        linha_u = linhas_user[i] if i < len(linhas_user) else "(Falta linha)"
        linha_g = linhas_gabarito[i] if i < len(linhas_gabarito) else "(Linha extra não esperada)"
        
        # Normalizações simples para aceitar variações comuns
        linha_u_fix = linha_u.replace("domain lookup", "domain-lookup")
        linha_g_fix = linha_g.replace("domain lookup", "domain-lookup")
        linha_u_fix = linha_u_fix.replace("gigabitethernet", "g")
        linha_g_fix = linha_g_fix.replace("gigabitethernet", "g")

        if linha_u_fix != linha_g_fix:
            tudo_correto = False
            erros.append(f"Linha {i+1}: Escreveste '{linha_u}' -> Esperado '{linha_g}'")

    if tudo_correto:
        st.session_state.feedback = "✅ BLOCO CORRETO! Muito bem."
        st.session_state.erros = []
    else:
        st.session_state.feedback = "❌ Existem erros no bloco."
        st.session_state.erros = erros

def navegar(direcao):
    novo_indice = st.session_state.indice_atual + direcao
    if 0 <= novo_indice < len(desafios):
        st.session_state.indice_atual = novo_indice
        st.session_state.resposta_user = ""
        st.session_state.feedback = ""
        st.session_state.erros = []

# ==========================================
# 3. INTERFACE STREAMLIT
# ==========================================
st.set_page_config(page_title="Cisco Skills Assessment", layout="wide")

if 'indice_atual' not in st.session_state:
    st.session_state.indice_atual = 0
if 'resposta_user' not in st.session_state:
    st.session_state.resposta_user = ""
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'erros' not in st.session_state:
    st.session_state.erros = []

# Cabeçalho
st.title("🐀 Modo Rato da Cisco")
st.progress((st.session_state.indice_atual + 1) / len(desafios))

# Dados do Desafio Atual
desafio_atual = desafios[st.session_state.indice_atual]

# Layout de Colunas
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"Tarefa {st.session_state.indice_atual + 1}/{len(desafios)}")
    st.markdown(f"### {desafio_atual['titulo']}")
    
    st.info("Instructions:")
    for instr in desafio_atual['instrucoes']:
        st.markdown(f"- {instr}")
        
    st.divider()
    
    # Navegação
    c_prev, c_next = st.columns(2)
    with c_prev:
        st.button("⬅️ Anterior", on_click=navegar, args=(-1,), disabled=(st.session_state.indice_atual == 0))
    with c_next:
        st.button("Seguinte ➡️", on_click=navegar, args=(1,), disabled=(st.session_state.indice_atual == len(desafios)-1))

with col2:
    st.subheader("Terminal")
    
    with st.form(key='bloco_form'):
        st.text_area(
            "Introduza os comandos (1 por linha):",
            key="resposta_user",
            height=300,
            placeholder="Example:\nenable\nconfigure terminal\n..."
        )
        st.form_submit_button("Validar Bloco", on_click=verificar_bloco)
    
    # Área de Feedback
    if st.session_state.feedback:
        if "CORRETO" in st.session_state.feedback:
            st.success(st.session_state.feedback)
            st.button("Advance to next step", on_click=navegar, args=(1,))
        else:
            st.error(st.session_state.feedback)
            if st.session_state.erros:
                with st.expander("View Error Details"):
                    for erro in st.session_state.erros:
                        st.write(erro)
    
    # -------------------------------------------------------------
    # BOTÃO DE SOLUÇÃO (AGORA SEMPRE VISÍVEL FORA DO IF)
    # -------------------------------------------------------------
    st.divider()
    with st.expander("Ver Solução Completa"):
        st.code(desafio_atual['resposta_esperada'])

Consegues atribuir um valor a cada parte do teste concluído e, no final, a percentagem de 100% de quanto foi feito?
