import streamlit as st

# ==========================================
# 1. CONFIGURAÇÕES E ABREVIATURAS
# ==========================================
# Definido no topo para estar disponível em todas as funções
ABREVIATURAS_CISCO = {
    "ena": "enable", "conf": "configure", "t": "terminal",
    "int": "interface", "fa": "fastethernet", "gi": "gigabitethernet",
    "g": "gigabitethernet", "f": "fastethernet", "sw": "switchport",
    "acc": "access", "tru": "trunk", "nat": "native", "all": "allowed",
    "add": "address", "desc": "description", "shut": "shutdown",
    "no shut": "no shutdown", "exit": "exit", "log": "login",
    "pass": "password", "enc": "encapsulation", "chan": "channel-group",
    "ban": "banner", "motd": "motd", "sh": "show", "ip": "ip", "ipv6": "ipv6"
}

# ==========================================
# 2. BASE DE DADOS (BLOCOS DE COMANDOS)
# ==========================================
desafios = [
    {
        "titulo": "Step 1a: Configure R1 Basic Settings and Device Hardening (Part A)",
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
        "titulo": "Step 1b: Configure R1 Basic Settings and Device Hardening",
        "instrucoes": [
            "Configure password security.",
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
        "titulo": "Step 1c: Configure R1 Basic Settings and Device Hardening",
        "instrucoes": [
            "Configure SSH.",
            "1) Create an administrative user in the local user database (user: admin, Encrypted Password: admin1pass).",
            "2) Configure the domain name as ccna-ptsa.com",
            "3) Create an RSA crypto key with a modulus of 1024 bits.",
            "4) Ensure that more secure version of SSH will be used.",
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
    {
        "titulo": "Step 2a: Configure R1 with a loopback interface",
        "instrucoes": [
            "Configure R1 with a loopback interface. Configure the loopback0 with IPv4 and IPv6 addressing according to the addressing table."
        ],
        "resposta_esperada": """interface Loopback 0
description Loopback
ip address 209.165.201.1 255.255.255.224
ipv6 address 2001:db8:acad:209::1/64
ipv6 address fe80::1 link-local
exit"""
    },
    {
        "titulo": "Step 2b: Configure Router Subinterfaces (g0/0/1.2)",
        "instrucoes": [
            "1. Prepare the router to be configured with IPv6 addresses on its interfaces.",
            "2. Use the information in the Addressing Table and VLAN Table to configure subinterfaces on R1:",
            "- Interfaces should be configured with IPv4 and IPv6 addressing.",
            "- All addressed interfaces should use fe80::1 as the link local address.",
            "- Use the VLAN table to assign VLAN membership to the subinterfaces.",
            "3. Be sure to configure the native VLAN interface.",
            "4. Configure descriptions for all interfaces."
        ],
        "resposta_esperada": """ipv6 unicast-routing
interface g0/0/1.2
encapsulation dot1Q 2
description Bikes
ip address 10.19.8.1 255.255.255.192
ipv6 address `2001:db8:acad:a::1/64`
ipv6 address fe80::1 link-local"""
    },
    {
        "titulo": "Step 2.1b: Configure Router Subinterfaces (g0/0/1.3 and g0/0/1.4)",
        "instrucoes": [
            "3. Configure subinterface g0/0/1.3 (Encapsulation, Desc, IPv4 and IPv6)",
            "4. Configure subinterface g0/0/1.4 (Encapsulation, Desc, IPv4 and IPv6)"
        ],
        "resposta_esperada": """interface g0/0/1.3
encapsulation dot1Q 3
description Trikes
ip address 10.19.8.65 255.255.255.224
ipv6 address `2001:db8:acad:b::1/64`
ipv6 address fe80::1 link-local
interface g0/0/1.4
encapsulation dot1Q 4
description Management
ip address 10.19.8.97 255.255.255.248
ipv6 address `2001:db8:acad:c::1/64`
ipv6 address fe80::1 link-local"""
    },
    {
        "titulo": "Step 2.2b: Configure Router Subinterfaces (g0/0/1.6 and g0/0/1)",
        "instrucoes": [
            "5. Configure the native VLAN interface:",
            "6. Enable the physical interface g0/0/1."
        ],
        "resposta_esperada": """interface g0/0/1.6
encapsulation dot1Q 6 native
description Native
interface g0/0/1
no shutdown"""
    },
    {
        "titulo": "Step 3: Configure S1 Basic Settings & Hardening (a and b)",
        "instrucoes": [
            "a. Configuration tasks for the switches S1 and S2 include the following:",
            "1. Prevent the switches from attempting to resolve incorrectly entered commands as domain names.int",
            "2. Configure the S1 or S2 hostname.",
            "3. Configure an appropriate MOTD banner on both switches.(#Unauthorized Access is Prohibitted!#)",
            " "
            "b. b. Configure Device Hardening on S1 and S2",
            "1. Configure the console password and enable connections.",
            "2. Configure an enable secret password.",
            "3. Encrypt all clear text passwords."
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
            "1. Create an administrative user in the local user database. ",
            "- Username: admin",
            "- Password: admin1pass",
            "2. Configure the domain name as ccna-ptsa.com",
            "3. Create an RSA crypto key with a modulus of 1024 bits.",
            "4. Ensure that more secure version of SSH will be used.",
            "5. Configure the vty lines to authenticate logins against the local user database.",
            "6. Configure the vty lines to accept connections over SSH only."
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
        "titulo": "Step 3c: Configure SSH on S2",
        "instrucoes": [
            "1. Create an administrative user in the local user database. ",
            "- Username: admin",
            "- Password: admin1pass",
            "2. Configure the domain name as ccna-ptsa.com",
            "3. Create an RSA crypto key with a modulus of 1024 bits.",
            "4. Ensure that more secure version of SSH will be used.",
            "5. Configure the vty lines to authenticate logins against the local user database.",
            "6. Configure the vty lines to accept connections over SSH only."
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
        "titulo": "Step 4: Configure SVIs on S1",
        "instrucoes": [
            "a. Use the information in the Addressing Table to configure SVIs on S1 and S2 for the Management VLAN.",
            "b. Configure the switch so that the SVI can be reached from other networks over the Management VLAN."
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
            "a. Use the information in the Addressing Table to configure SVIs on S1 and S2 for the Management VLAN.",
            "b. Configure the switch so that the SVI can be reached from other networks over the Management VLAN."
        ],
        "resposta_esperada": """interface vlan 4
ip address 10.19.8.99 255.255.255.248
description Management Interface
no shutdown
exit
ip default-gateway 10.19.8.97"""
    },
    {
        "titulo": "Part 3 Step 1: Configure VLANs and Trunking (S1)",
        "instrucoes": [
            "a. Create the VLANs according to the VLAN table.",
            "b. Create 802.1Q VLAN trunks on ports F0/1 and F0/2. On S1, F0/5 should also be configured as a trunk. Use VLAN 6 as the native VLAN."
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
            "a. Create the VLANs according to the VLAN table.",
            "b. Create 802.1Q VLAN trunks on ports F0/1 and F0/2. Use VLAN 6 as the native VLAN."
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
            "Create Layer 2 EtherChannel port group 1 that uses interfaces F0/1 and F0/2 on S1 and S2. Both ends of the channel should negotiate the LACP link."
        ],
        "resposta_esperada": """interface range f0/1-2
channel-group 1 mode active
interface port-channel 1
exit"""
    },
    {
        "titulo": "Part 3 Step 2: Configure Etherchannel (S2)",
        "instrucoes": [
            "Create Layer 2 EtherChannel port group 1 that uses interfaces F0/1 and F0/2 on S1 and S2. Both ends of the channel should negotiate the LACP link."
        ],
        "resposta_esperada": """interface range f0/1-2
channel-group 1 mode active
interface port-channel 1
exit"""
    },
    {
        "titulo": "Part 3 Step 3: Configure Switchports (S2)",
        "instrucoes": [
            "a. On S1, configure the port that is connected to the host with static access mode in VLAN 2.",
            "c. Configure port security on the S1 and S2 active access ports to accept only three learned MAC addresses.",
            "d. d. Assign all unused switch ports to VLAN 5 on both switches and shut down the ports.",
            "e. e. Configure a description on the unused ports that is relevant to their status."
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
            "b. On S2, configure the port that is connected to the host with static access mode in VLAN 3.",
            "c. Configure port security on the S1 and S2 active access ports to accept only three learned MAC addresses.",
            "d. d. Assign all unused switch ports to VLAN 5 on both switches and shut down the ports.",
            "e. e. Configure a description on the unused ports that is relevant to their status."
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
    {
        "titulo": "Part 4 Step 1: Configure Default Routing on R1",
        "instrucoes": [
            "a. Configure an IPv4 default route that uses the Lo0 interface as the exit interface.",
            "b. Configure an IPv6 default route that uses the Lo0 interface as the exit interface."
        ],
        "resposta_esperada": """ip route 0.0.0.0 0.0.0.0 loopback 0
ipv6 route ::/0 loopback 0"""
    },
    {
        "titulo": "Part 4 Step 2: Configure IPv4 DHCP for VLAN 2 (R1)",
        "instrucoes": [
            "a. On R1, create a DHCP pool called CCNA-A that consists of the last 10 host addresses in the VLAN 2 subnet only.",
            "b. Configure the correct default gateway address in the pool.",
            "c. Configure the domain name of ccna-a.net."
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
            "a. On R1, create a DHCP pool called CCNA-B that consists of the last 10 host addresses in the VLAN 3 subnet only.",
            "b. Configure the correct default gateway address in the pool.",
            "c. Configure the domain name of ccna-b.net."
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
# 3. LÓGICA DE VALIDAÇÃO, AJUDA E NAVEGAÇÃO
# ==========================================

def normalizar_lista(texto):
    if not texto: return []
    return [linha.strip().lower() for linha in texto.strip().split('\n') if linha.strip()]

def comparar_comandos(user_line, target_line):
    # Separa por espaços sem replace destrutivo
    u_parts = user_line.strip().split()
    t_parts = target_line.strip().split()

    if len(u_parts) != len(t_parts):
        return False

    for u_word, t_word in zip(u_parts, t_parts):
        # 1. Igualdade exata
        if u_word == t_word:
            continue
        # 2. Abreviatura conhecida
        if u_word in ABREVIATURAS_CISCO:
            expandido = ABREVIATURAS_CISCO[u_word]
            if t_word.startswith(expandido):
                continue
        # 3. Prefixo simples
        if len(u_word) >= 2 and t_word.startswith(u_word):
            continue
            
        return False
    return True

def obter_ajuda_ios(linha_u, linha_g):
    comando_parcial = linha_u.replace("?", "").strip()
    if not comando_parcial: return f"Ajuda: {linha_g}"
    u_parts = comando_parcial.split()
    t_parts = linha_g.split()
    if len(u_parts) > len(t_parts): return "Ajuda: <cr> (Pressione Enter para validar)"
    indice = len(u_parts) - 1
    if not linha_u.endswith(" ?") and linha_u.endswith("?"):
        if indice < len(t_parts): return f"Ajuda: {t_parts[indice]}"
    if linha_u.endswith(" ?") or (len(u_parts) < len(t_parts)):
        proximo_indice = len(u_parts)
        if proximo_indice < len(t_parts): return f"Ajuda: {t_parts[proximo_indice]}"
    return f"Ajuda: {linha_g}"

def navegar(direcao):
    # Guarda o estado atual antes de mudar
    st.session_state.respostas_guardadas[st.session_state.indice_atual] = st.session_state.resposta_temp
    novo_indice = st.session_state.indice_atual + direcao
    if 0 <= novo_indice < len(desafios):
        st.session_state.indice_atual = novo_indice
        st.session_state.feedback = ""
        st.session_state.erros = []

def limpar_resposta_atual():
    idx = st.session_state.indice_atual
    # Limpa persistência
    st.session_state.respostas_guardadas[idx] = ""
    # Limpa widget visual
    if 'resposta_temp' in st.session_state:
        st.session_state.resposta_temp = ""
    # Limpa feedbacks
    st.session_state.feedback = ""
    st.session_state.erros = []

def verificar_bloco():
    idx = st.session_state.indice_atual
    desafio = desafios[idx]
    user_text = st.session_state.resposta_temp
    st.session_state.respostas_guardadas[idx] = user_text
    
    linhas_user_raw = user_text.strip().split('\n')
    linhas_gabarito_raw = desafio['resposta_esperada'].strip().split('\n')

    # --- LÓGICA DE AJUDA ---
    if linhas_user_raw and linhas_user_raw[-1].strip().endswith("?"):
        ultima_linha = linhas_user_raw[-1].strip().lower()
        termo_busca = ultima_linha.replace("?", "").strip().split()
        
        linha_alvo = None
        if termo_busca:
            primeira_palavra = termo_busca[0]
            if primeira_palavra in ABREVIATURAS_CISCO: primeira_palavra = ABREVIATURAS_CISCO[primeira_palavra]
            for g_line in linhas_gabarito_raw:
                g_parts = g_line.lower().split()
                if g_parts and g_parts[0].startswith(primeira_palavra):
                    linha_alvo = g_line
                    break
        
        if not linha_alvo:
            num_linha = len(linhas_user_raw) - 1
            if num_linha < len(linhas_gabarito_raw): linha_alvo = linhas_gabarito_raw[num_linha]
            
        if linha_alvo:
            st.session_state.feedback = obter_ajuda_ios(ultima_linha, linha_alvo.lower())
        else:
            st.session_state.feedback = "Ajuda: Comando não encontrado no contexto atual."
        return

    # --- VALIDAÇÃO ---
    linhas_user = normalizar_lista(user_text)
    linhas_gabarito = normalizar_lista(desafio['resposta_esperada'])
    
    if not linhas_user:
        st.session_state.feedback = "A caixa está vazia."
        st.session_state.erros = []
        return

    erros = []
    tudo_correto = True
    for i in range(len(linhas_gabarito)):
        if i >= len(linhas_user):
            tudo_correto = False
            erros.append(f"Linha {i+1}: Falta o comando '{linhas_gabarito[i]}'")
            continue
        if not comparar_comandos(linhas_user[i], linhas_gabarito[i]):
            tudo_correto = False
            erros.append(f"Linha {i+1}: Erro em '{linhas_user[i]}' -> Esperado algo como '{linhas_gabarito[i]}'")

    if tudo_correto:
        st.session_state.feedback = "BLOCO CORRETO! Muito bem."
        st.session_state.concluidos.add(idx)
        st.session_state.erros = []
    else:
        st.session_state.feedback = "Existem erros no bloco."
        st.session_state.erros = erros

# ==========================================
# 4. INTERFACE STREAMLIT
# ==========================================
st.set_page_config(page_title="Modo Rato da Cisco", layout="wide")

if 'indice_atual' not in st.session_state: st.session_state.indice_atual = 0
if 'concluidos' not in st.session_state: st.session_state.concluidos = set()
if 'feedback' not in st.session_state: st.session_state.feedback = ""
if 'erros' not in st.session_state: st.session_state.erros = []
if 'respostas_guardadas' not in st.session_state:
    st.session_state.respostas_guardadas = {i: "" for i in range(len(desafios))}

pontuacao = (len(st.session_state.concluidos) / len(desafios)) * 100
st.title("🐀 Modo Rato da Cisco")
st.write(f"Conclusão: {pontuacao:.2f}% ({len(st.session_state.concluidos)} de {len(desafios)} tarefas)")
st.progress(pontuacao / 100)

desafio_atual = desafios[st.session_state.indice_atual]
col1, col2 = st.columns([1, 1])

with col1:
    # --- NOVO: Addressing Table em Expander ---
    with st.expander("Addressing Table", expanded=False):
        st.markdown("""
        **VLAN Table**
        | VLAN | Name | Interface |
        |---|---|---|
        | 2 | Bikes | G0/0/1.2 |
        | 3 | Trikes | G0/0/1.3 |
        | 4 | Management | G0/0/1.4 |
        | 5 | Parking | N/A |
        | 6 | Native | G0/0/1.6 |

        **Addressing Table**
        | Device | Interface | IPv4 Address | IPv6 Address | IPv6 Link-Local |
        |---|---|---|---|---|
        | **R1** | G0/0/1.2 | 10.19.8.1 /26 | `2001:db8:acad:a::1 /64` | fe80::1 |
        | | G0/0/1.3 | 10.19.8.65 /27 | `2001:db8:acad:b::1 /64` | fe80::1 |
        | | G0/0/1.4 | 10.19.8.97 /29 | `2001:db8:acad:c::1 /64` | fe80::1 |
        | | G0/0/1.6 | N/A | N/A | N/A |
        | | Lo0 | 209.165.201.1 /27 | 2001:db8:acad:209::1 /64 | fe80::1 |
        | **S1** | VLAN 4 | 10.19.8.98 /29 | - | - |
        | **S2** | VLAN 4 | 10.19.8.99 /29 | - | - |
        | **PC-A** | NIC | DHCP | `2001:db8:acad:a::1 /64` | fe80::1 |
        | **PC-B** | NIC | DHCP | `2001:db8:acad:b::50 /64` | fe80::1 |
        """)

    st.subheader(f"Tarefa {st.session_state.indice_atual + 1}/{len(desafios)}")
    st.markdown(f"### {desafio_atual['titulo']}")
    
    # --- VISUAL DAS INSTRUÇÕES ---
    st.info("Instructions:")
    markdown_instrucoes = ""
    for linha in desafio_atual['instrucoes']:
        linha = linha.strip()
        if linha.startswith("-"):
            # Indenta linhas que começam por traço
            texto_limpo = linha[1:].strip()
            markdown_instrucoes += f"  - {texto_limpo}\n"
        else:
            # Bullet point normal para as outras
            markdown_instrucoes += f"- {linha}\n"
    st.markdown(markdown_instrucoes)
    
    st.divider()
    c_prev, c_next = st.columns(2)
    with c_prev: st.button("Anterior", on_click=navegar, args=(-1,), disabled=(st.session_state.indice_atual == 0))
    with c_next: st.button("Seguinte", on_click=navegar, args=(1,), disabled=(st.session_state.indice_atual == len(desafios)-1))

with col2:
    st.subheader("Terminal")
    # Form gere CTRL+Enter e botões
    with st.form(key='terminal_form', clear_on_submit=False):
        st.text_area(
            "Consola (Escreva '?' + CTRL+Enter para ajuda, ou apenas CTRL+Enter para validar):", 
            value=st.session_state.respostas_guardadas[st.session_state.indice_atual],
            key="resposta_temp", height=300
        )
        c_val, c_res = st.columns(2)
        with c_val: st.form_submit_button("Submeter / Ajuda", on_click=verificar_bloco)
        with c_res: st.form_submit_button("Limpar Terminal", on_click=limpar_resposta_atual)
    
    if st.session_state.feedback:
        if "CORRETO" in st.session_state.feedback: st.success(st.session_state.feedback)
        elif "Ajuda:" in st.session_state.feedback: st.info(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)
            if st.session_state.erros:
                with st.expander("Ver detalhes dos erros"):
                    for erro in st.session_state.erros: st.write(erro)

    st.divider()
    with st.expander("Ver Solução Completa"): st.code(desafio_atual['resposta_esperada'])
