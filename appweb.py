import streamlit as st

# ==========================================
# 1. BASE DE DADOS (BLOCOS DE COMANDOS)
# ==========================================
desafios = [
    # -------------------------------------------------------------------------
    # STEP 1: R1 BASIC SETTINGS
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 1: Configure R1 Basic Settings (Part A)",
        "instrucoes": [
            "a. Configure basic settings.",
            "- Prevent DNS resolution, Hostname R1, Banner MOTD."
        ],
        "resposta_esperada": """no ip domain-lookup
hostname R1
banner motd #Unauthorized Acess is Prohibited#"""
    },
    {
        "titulo": "Step 1: Configure R1 Password Security (Part B)",
        "instrucoes": [
            "b. Configure password security.",
            "- Console pass (ciscoconpass), Enable secret (ciscoenpass), Encryption, Min-length 10."
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
        "titulo": "Step 1: Configure SSH on R1 (Part C)",
        "instrucoes": [
            "c. Configure SSH.",
            "- User admin/admin1pass, Domain, RSA 1024, SSH v2, VTY lines."
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
        "titulo": "Step 2a: Configure R1 Loopback 0",
        "instrucoes": ["Configure Lo0: IPv4 209.165.201.1/27, IPv6 ...209::1/64, Link-local fe80::1"],
        "resposta_esperada": """interface Loopback 0
description Loopback
ip address 209.165.201.1 255.255.255.224
ipv6 address 2001:db8:acad:209::1/64
ipv6 address fe80::1 link-local
exit"""
    },
    {
        "titulo": "Step 2b: R1 Subinterfaces (Part 1 - VLAN 2)",
        "instrucoes": ["Enable IPv6 routing, Configure g0/0/1.2 (Bikes): IP 10.19.8.1/26, IPv6 ...a::1/64"],
        "resposta_esperada": """ipv6 unicast-routing
interface g0/0/1.2
encapsulation dot1Q 2
description Bikes
ip address 10.19.8.1 255.255.255.192
ipv6 address 2001:db8:acad:a::1/64
ipv6 address fe80::1 link-local"""
    },
    {
        "titulo": "Step 2b: R1 Subinterfaces (Part 2 - VLAN 3 & 4)",
        "instrucoes": ["Configure g0/0/1.3 (Trikes) and g0/0/1.4 (Management) with IPs and IPv6."],
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
        "titulo": "Step 2b: R1 Subinterfaces (Part 3 - Native & Interface Up)",
        "instrucoes": ["Configure g0/0/1.6 (Native) and No Shutdown on g0/0/1."],
        "resposta_esperada": """interface g0/0/1.6
encapsulation dot1Q 6 native
description Native
interface g0/0/1
no shutdown"""
    },
    # -------------------------------------------------------------------------
    # STEP 3: SWITCHES BASIC & SSH
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 3a/b: S1 Basic & Hardening",
        "instrucoes": ["S1: No DNS, Hostname, Banner, Console pass, Secret, Encryption."],
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
        "titulo": "Step 3c: S1 SSH Configuration",
        "instrucoes": ["S1: Admin user, Domain, RSA 1024, SSH v2, VTY lines."],
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
    {
        "titulo": "Step 3a/b: S2 Basic & Hardening",
        "instrucoes": ["S2: No DNS, Hostname, Banner, Console pass, Secret, Encryption."],
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
        "titulo": "Step 3c: S2 SSH Configuration",
        "instrucoes": ["S2: Admin user, Domain, RSA 1024, SSH v2, VTY lines."],
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
        "titulo": "Step 4: S1 SVI & Gateway",
        "instrucoes": ["S1: Interface Vlan 4 (10.19.8.98/29) and Default-Gateway."],
        "resposta_esperada": """interface vlan 4
ip address 10.19.8.98 255.255.255.248
description Management Interface
no shutdown
exit
ip default-gateway 10.19.8.97"""
    },
    {
        "titulo": "Step 4: S2 SVI & Gateway",
        "instrucoes": ["S2: Interface Vlan 4 (10.19.8.99/29) and Default-Gateway."],
        "resposta_esperada": """interface vlan 4
ip address 10.19.8.99 255.255.255.248
description Management Interface
no shutdown
exit
ip default-gateway 10.19.8.97"""
    },
    # -------------------------------------------------------------------------
    # PART 3: INFRASTRUCTURE
    # -------------------------------------------------------------------------
    {
        "titulo": "Part 3 Step 1: S1 VLANs & Trunking",
        "instrucoes": ["S1: Create VLANs 2-6, Trunk f0/1-2 (Native 6), Trunk f0/5 (Native 6)."],
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
        "titulo": "Part 3 Step 1: S2 VLANs & Trunking",
        "instrucoes": ["S2: Create VLANs 2-6, Trunk f0/1-2 (Native 6)."],
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
        "titulo": "Part 3 Step 2: S1 EtherChannel",
        "instrucoes": ["S1: Group f0/1-2 into Channel-group 1 (Mode Active)."],
        "resposta_esperada": """interface range f0/1-2
channel-group 1 mode active
interface port-channel 1
exit"""
    },
    {
        "titulo": "Part 3 Step 2: S2 EtherChannel",
        "instrucoes": ["S2: Group f0/1-2 into Channel-group 1 (Mode Active)."],
        "resposta_esperada": """interface range f0/1-2
channel-group 1 mode active
interface port-channel 1
exit"""
    },
    {
        "titulo": "Part 3 Step 3: S1 Switchports & Security",
        "instrucoes": ["S1: f0/6 (Access Vlan 2, Port-sec max 3), Unused ports (Vlan 5, Shutdown)."],
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
        "titulo": "Part 3 Step 3: S2 Switchports & Security",
        "instrucoes": ["S2: f0/18 (Access Vlan 3, Port-sec max 3), Unused ports (Vlan 5, Shutdown)."],
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
    # PART 4: ROUTING & DHCP
    # -------------------------------------------------------------------------
    {
        "titulo": "Part 4 Step 1: R1 Default Routing",
        "instrucoes": ["R1: IPv4 and IPv6 Default Routes via Lo0."],
        "resposta_esperada": """ip route 0.0.0.0 0.0.0.0 loopback 0
ipv6 route ::/0 loopback 0"""
    },
    {
        "titulo": "Part 4 Step 2: R1 DHCP Pool CCNA-A",
        "instrucoes": ["R1: Exclude .1-.52, Pool CCNA-A (Vlan 2): Net 10.19.8.0/26, GW .1, DNS ccna-a.net."],
        "resposta_esperada": """ip dhcp excluded-address 10.19.8.1 10.19.8.52
ip dhcp pool CCNA-A
network 10.19.8.0 255.255.255.192
default-router 10.19.8.1
domain-name ccna-a.net
exit"""
    },
    {
        "titulo": "Part 4 Step 3: R1 DHCP Pool CCNA-B",
        "instrucoes": ["R1: Exclude .65-.84, Pool CCNA-B (Vlan 3): Net 10.19.8.64/27, GW .65, DNS ccna-b.net."],
        "resposta_esperada": """ip dhcp excluded-address 10.19.8.65 10.19.8.84
ip dhcp pool CCNA-B
network 10.19.8.64 255.255.255.224
default-router 10.19.8.65
domain-name ccna-b.net
exit"""
    }
]

# ==========================================
# 2. LÓGICA DE NEGÓCIO
# ==========================================

def normalizar_lista(texto):
    if not texto: return []
    return [l.strip().lower() for l in texto.strip().split('\n') if l.strip()]

def verificar_bloco():
    idx = st.session_state.indice_atual
    linhas_user = normalizar_lista(st.session_state.resposta_user)
    linhas_gabarito = normalizar_lista(desafios[idx]['resposta_esperada'])
    
    if not linhas_user:
        st.session_state.feedback = "⚠️ A caixa está vazia."
        return

    erros = []
    max_len = max(len(linhas_user), len(linhas_gabarito))
    tudo_correto = True
    
    for i in range(max_len):
        lu = linhas_user[i] if i < len(linhas_user) else "(Missing line)"
        lg = linhas_gabarito[i] if i < len(linhas_gabarito) else "(Extra line)"
        
        # Correções de sintaxe flexível
        lu_f = lu.replace("domain lookup", "domain-lookup").replace("gigabitethernet", "g")
        lg_f = lg.replace("domain lookup", "domain-lookup").replace("gigabitethernet", "g")

        if lu_f != lg_f:
            tudo_correto = False
            erros.append(f"Line {i+1}: Found '{lu}' -> Expected '{lg}'")

    if tudo_correto:
        st.session_state.feedback = "✅ BLOCO CORRETO!"
        st.session_state.concluidos.add(idx)
        st.session_state.erros = []
    else:
        st.session_state.feedback = "❌ Existem erros no bloco."
        st.session_state.erros = erros

def navegar(direcao):
    novo = st.session_state.indice_atual + direcao
    if 0 <= novo < len(desafios):
        st.session_state.indice_atual = novo
        st.session_state.resposta_user = ""
        st.session_state.feedback = ""
        st.session_state.erros = []

# ==========================================
# 3. INTERFACE (STREAMLIT)
# ==========================================
st.set_page_config(page_title="Cisco PTSA Tracker", layout="wide")

# Inicialização do Session State
if 'indice_atual' not in st.session_state: st.session_state.indice_atual = 0
if 'concluidos' not in st.session_state: st.session_state.concluidos = set()
if 'erros' not in st.session_state: st.session_state.erros = []
if 'feedback' not in st.session_state: st.session_state.feedback = ""

# --- CABEÇALHO E PONTUAÇÃO ---
pontuacao = (len(st.session_state.concluidos) / len(desafios)) * 100

st.title("🐀 Modo Rato da Cisco: Skills Assessment")

# Métricas de Progresso
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Completion", f"{pontuacao:.1f}%")
col_m2.metric("Tasks Done", f"{len(st.session_state.concluidos)} / {len(desafios)}")
col_m3.metric("Current Task", f"#{st.session_state.indice_atual + 1}")

st.progress(pontuacao / 100)

if pontuacao == 100:
    st.balloons()
    st.success("🏆 CONGRATULATIONS! 100% COMPLETE. YOU ARE READY FOR THE EXAM!")

st.divider()

# --- ÁREA DE TRABALHO ---
desafio = desafios[st.session_state.indice_atual]
c1, c2 = st.columns([1, 1])

with c1:
    status = "✅ DONE" if st.session_state.indice_atual in st.session_state.concluidos else "⏳ PENDING"
    st.markdown(f"### {desafio['titulo']} ({status})")
    
    with st.container(border=True):
        st.markdown("**Instructions:**")
        for i in desafio['instrucoes']: st.write(f"- {i}")
    
    # Navegação
    nav_1, nav_2 = st.columns(2)
    nav_1.button("⬅️ Anterior", on_click=navegar, args=(-1,), disabled=(st.session_state.indice_atual == 0))
    nav_2.button("Seguinte ➡️", on_click=navegar, args=(1,), disabled=(st.session_state.indice_atual == len(desafios)-1))

with c2:
    st.markdown("### Terminal")
    with st.form(key='terminal_form'):
        st.text_area("Paste/Write commands here:", key="resposta_user", height=250)
        st.form_submit_button("Verify Configuration", on_click=verificar_bloco)
    
    if st.session_state.feedback:
        if "CORRETO" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)
            if st.session_state.erros:
                with st.expander("Show detailed errors"):
                    for e in st.session_state.erros: st.write(e)

st.divider()
with st.expander("🆘 Peek Solution (Check this only if you are stuck)"):
    st.code(desafio['resposta_esperada'])

# --- SIDEBAR DE ATALHOS ---
st.sidebar.title("Task List")
for i, d in enumerate(desafios):
    ic = "✅" if i in st.session_state.concluidos else "⚪"
    if st.sidebar.button(f"{ic} Task {i+1}", key=f"side_{i}"):
        st.session_state.indice_atual = i
        st.rerun()

if st.sidebar.button("🗑️ Reset Exam"):
    st.session_state.concluidos = set()
    st.session_state.indice_atual = 0
    st.rerun()
