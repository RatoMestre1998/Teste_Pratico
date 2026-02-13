import streamlit as st

# ==========================================
# 1. BASE DE DADOS (BLOCOS DE COMANDOS)
# ==========================================
desafios = [
    # -------------------------------------------------------------------------
    # STEP 1: R1 BASIC SETTINGS
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 1a: Configurações Básicas do R1",
        "instrucoes": [
            "1. Prevenir resolução DNS (no ip domain lookup)",
            "2. Configurar Hostname R1",
            "3. Banner MOTD '#Unauthorized Acess is Prohibited#'"
        ],
        "resposta_esperada": """no ip domain-lookup
hostname R1
banner motd #Unauthorized Acess is Prohibited#"""
    },
    {
        "titulo": "Step 1b: Segurança de Passwords R1",
        "instrucoes": [
            "1. Linha consola 0: password 'ciscoconpass', login, exit",
            "2. Enable secret 'ciscoenpass'",
            "3. Encriptar passwords (service password-encryption)",
            "4. Tamanho mínimo password 10 caracteres"
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
        "titulo": "Step 1c: Configuração SSH R1",
        "instrucoes": [
            "1. Criar user 'admin' secret 'admin1pass'",
            "2. Domain name 'ccna-ptsa.com'",
            "3. Crypto key generate rsa (1024 bits)",
            "4. SSH version 2",
            "5. Linhas vty 0 15: login local, transport input ssh, exit"
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
        "titulo": "Step 2a: Interface Loopback 0",
        "instrucoes": [
            "Configurar Loopback 0:",
            "- Descrição 'Loopback'",
            "- IP: 209.165.201.1 /27",
            "- IPv6: 2001:db8:acad:209::1/64",
            "- IPv6 Link-Local: fe80::1",
            "- Exit"
        ],
        "resposta_esperada": """interface Loopback 0
description Loopback
ip address 209.165.201.1 255.255.255.224
ipv6 address 2001:db8:acad:209::1/64
ipv6 address fe80::1 link-local
exit"""
    },
    {
        "titulo": "Step 2b: Subinterfaces (ROAS) - Parte 1",
        "instrucoes": [
            "1. Ativar IPv6 unicast-routing",
            "2. Configurar g0/0/1.2 (VLAN 2 - Bikes):",
            "- Encapsulation dot1Q 2",
            "- IP: 10.19.8.1 /26",
            "- IPv6: ...:a::1/64",
            "- IPv6 Link-local fe80::1"
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
        "titulo": "Step 2b: Subinterfaces (ROAS) - Parte 2",
        "instrucoes": [
            "1. Configurar g0/0/1.3 (VLAN 3 - Trikes)",
            "- IP: 10.19.8.65 /27",
            "- IPv6 ...b::1/64 e fe80::1",
            "2. Configurar g0/0/1.4 (VLAN 4 - Management)",
            "- IP: 10.19.8.97 /29",
            "- IPv6 ...c::1/64 e fe80::1"
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
        "titulo": "Step 2b: Subinterfaces (ROAS) - Parte 3 (Nativa e Física)",
        "instrucoes": [
            "1. Configurar g0/0/1.6 (Nativa)",
            "2. Levantar a interface física g0/0/1"
        ],
        "resposta_esperada": """interface g0/0/1.6
encapsulation dot1Q 6 native
description Native
interface g0/0/1
no shutdown"""
    },

    # -------------------------------------------------------------------------
    # STEP 3: SWITCH 1
    # -------------------------------------------------------------------------
    {
        "titulo": "Step 3a/b: S1 Basic & Hardening",
        "instrucoes": [
            "Configurar S1 (Tudo num bloco):",
            "- No dns lookup, Hostname S1",
            "- Banner '#Unauthorized Access is Prohibitted!#'",
            "- Console: pass ciscoconpass, login",
            "- Enable secret ciscoenpass",
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
        "titulo": "Step 3c: S1 SSH",
        "instrucoes": [
            "Configurar SSH no S1:",
            "- User admin / admin1pass",
            "- Domain ccna-ptsa.com",
            "- Key rsa 1024",
            "- SSH v2",
            "- VTY 0 15 (login local, transport ssh)"
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
    {
        "titulo": "Step 4: S1 SVI (Management)",
        "instrucoes": [
            "Configurar VLAN 4 Interface no S1:",
            "- IP: 10.19.8.98 /29",
            "- No shutdown",
            "- Default Gateway: 10.19.8.97"
        ],
        "resposta_esperada": """interface vlan 4
ip address 10.19.8.98 255.255.255.248
description Management Interface
no shutdown
exit
ip default-gateway 10.19.8.97"""
    },
    
    # -------------------------------------------------------------------------
    # PART 3: VLANS & TRUNKS
    # -------------------------------------------------------------------------
    {
        "titulo": "Part 3 - Step 1: S1 VLANs e Trunks",
        "instrucoes": [
            "1. Criar VLANs 2, 3, 4, 5, 6 com nomes (Bikes, Trikes, Management, Parking, Native)",
            "2. Trunk em f0/1-2 (Native vlan 6, allowed 2-6)",
            "3. Trunk em f0/5 (Native vlan 6, allowed 2-6)"
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
        "titulo": "Part 3 - Step 2: EtherChannel S1",
        "instrucoes": [
            "Configurar EtherChannel (LACP) nas portas f0/1-2 do S1"
        ],
        "resposta_esperada": """interface range f0/1-2
channel-group 1 mode active
interface port-channel 1
exit"""
    },
    {
        "titulo": "Part 3 - Step 3: S1 Switchports",
        "instrucoes": [
            "1. f0/6: Access vlan 2, port-security (max 3)",
            "2. Unused (f0/3-4, f0/7-24, g0/1-2): VLAN 5, Shutdown"
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

    # -------------------------------------------------------------------------
    # PART 4: ROUTING & DHCP
    # -------------------------------------------------------------------------
    {
        "titulo": "Part 4: Routing & DHCP (R1)",
        "instrucoes": [
            "1. Rotas default IPv4 e IPv6 (via Loopback 0)",
            "2. DHCP Pool CCNA-A (VLAN 2): Excluir .1-.52",
            "3. DHCP Pool CCNA-B (VLAN 3): Excluir .65-.84"
        ],
        "resposta_esperada": """ip route 0.0.0.0 0.0.0.0 loopback 0
ipv6 route ::/0 loopback 0
ip dhcp excluded-address 10.19.8.1 10.19.8.52
ip dhcp pool CCNA-A
network 10.19.8.0 255.255.255.192
default-router 10.19.8.1
domain-name ccna-a.net
exit
ip dhcp excluded-address 10.19.8.65 10.19.8.84
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
    # Nota: Esta verificação simples exige que a ordem seja igual.
    # Para exames Cisco, a ordem geralmente importa dentro de blocos lógicos.
    
    max_len = max(len(linhas_user), len(linhas_gabarito))
    
    tudo_correto = True
    
    for i in range(max_len):
        linha_u = linhas_user[i] if i < len(linhas_user) else "(Falta linha)"
        linha_g = linhas_gabarito[i] if i < len(linhas_gabarito) else "(Linha extra não esperada)"
        
        # Aceita "no ip domain lookup" com ou sem hífen
        linha_u_fix = linha_u.replace("domain lookup", "domain-lookup")
        linha_g_fix = linha_g.replace("domain lookup", "domain-lookup")

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
st.set_page_config(page_title="Treino Cisco Blocos", layout="wide")

if 'indice_atual' not in st.session_state:
    st.session_state.indice_atual = 0
if 'resposta_user' not in st.session_state:
    st.session_state.resposta_user = ""
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'erros' not in st.session_state:
    st.session_state.erros = []

# Cabeçalho
st.title("🛡️ Treino Cisco: Modo Rato")
st.progress((st.session_state.indice_atual + 1) / len(desafios))

# Dados do Desafio Atual
desafio_atual = desafios[st.session_state.indice_atual]

# Layout de Colunas
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"Tarefa {st.session_state.indice_atual + 1}/{len(desafios)}")
    st.markdown(f"**{desafio_atual['titulo']}**")
    
    st.info("Objetivos:")
    for instr in desafio_atual['instrucoes']:
        st.markdown(f"- {instr}")
        
    st.divider()
    
    # Navegação
    c_prev, c_next = st.columns(2)
    with c_prev:
        st.button("⬅️ Anterior", on_click=navegar, args=(-1,), disabled=(st.session_state.indice_atual == 0))
    with c_next:
        st.button("Próximo ➡️", on_click=navegar, args=(1,), disabled=(st.session_state.indice_atual == len(desafios)-1))

with col2:
    st.subheader("Terminal (Escreve o bloco completo)")
    
    with st.form(key='bloco_form'):
        st.text_area(
            "Digita os comandos (um por linha):",
            key="resposta_user",
            height=300,
            placeholder="Exemplo:\nenable\nconfigure terminal\nhostname R1\n..."
        )
        st.form_submit_button("Validar Bloco", on_click=verificar_bloco)
    
    # Área de Feedback
    if st.session_state.feedback:
        if "CORRETO" in st.session_state.feedback:
            st.success(st.session_state.feedback)
            st.button("Avançar para o próximo", on_click=navegar, args=(1,))
        else:
            st.error(st.session_state.feedback)
            if st.session_state.erros:
                with st.expander("Ver Detalhes dos Erros"):
                    for erro in st.session_state.erros:
                        st.write(erro)
            
            with st.expander("Ver Solução Completa"):
                st.code(desafio_atual['resposta_esperada'])
