import streamlit as st
import time
import random

# --------------------
# Configuración de la Página
# --------------------
st.set_page_config(
    page_title="✨ Sorpresa para Sofía ✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------------
# CSS Personalizado para la estética cósmica
# --------------------
def local_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Inter:wght@300;400;600&display=swap');
        
        :root {
            --primary: #a855f7; /* Morado principal */
            --secondary: #d8b4fe; /* Lavanda claro */
            --accent: #f0abfc; /* Rosa-violeta */
            --dark-bg: #110f1a; /* Fondo de noche profunda */
            --text-light: #f3e8ff; /* Texto claro lavanda */
            --shadow: rgba(168, 85, 247, 0.4);
        }

        /* --- Fondo de la aplicación --- */
        .stApp {
            background: var(--dark-bg);
            background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
            color: var(--text-light);
        }

        /* --- Contenedor principal y Títulos --- */
        .title-font {
            font-family: 'Dancing Script', cursive;
        }

        .text-gradient {
            background: linear-gradient(45deg, var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        h1.title-font {
            font-size: 3.5rem;
            text-align: center;
        }
        
        p.subtitle {
            text-align: center;
            font-size: 1.2rem;
            color: var(--secondary);
            margin-bottom: 2rem;
        }

        /* --- Pestañas (Tabs) --- */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
            justify-content: center;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 10px;
            border-radius: 8px;
            background-color: transparent;
            border-bottom: 2px solid transparent;
            transition: all 0.3s ease;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(216, 180, 254, 0.1);
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            border-bottom: 2px solid var(--accent);
            color: var(--accent);
        }

        /* --- Botones --- */
        .stButton > button {
            width: 100%;
            background: linear-gradient(45deg, var(--primary), #c084fc);
            color: white;
            border: none;
            border-radius: 9999px;
            padding: 0.75rem 1.5rem;
            font-size: 1.1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px var(--shadow);
        }
        .stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px var(--shadow);
            filter: brightness(1.1);
        }
        .stButton > button:active {
            transform: scale(0.98);
        }

        /* --- Contenedores de mensajes --- */
        .message-box {
            background: rgba(168, 85, 247, 0.1);
            border-left: 4px solid var(--primary);
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 1rem;
            text-align: center;
            font-size: 1.2rem;
        }

        /* --- Estilo para el "TE AMO" --- */
        .big-love {
            font-family: 'Dancing Script', cursive;
            font-weight: 700;
            font-size: 5rem;
            text-align: center;
            background: linear-gradient(45deg, var(--secondary), var(--accent), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: pulse 2.5s infinite, colorShift 5s infinite;
            padding: 2rem 0;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); text-shadow: 0 0 10px var(--shadow); }
            50% { transform: scale(1.05); text-shadow: 0 0 25px var(--shadow); }
        }
        @keyframes colorShift {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(25deg); }
        }

    </style>
    """, unsafe_allow_html=True)

# --------------------
# Inicialización y Loader
# --------------------
if 'loaded' not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    local_css()
    st.markdown('<h1 class="title-font text-gradient">Creando una galaxia para Sofía...</h1>', unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    for perc_completed in range(100):
        time.sleep(0.025)
        progress_bar.progress(perc_completed + 1)
        
    st.session_state.loaded = True
    st.experimental_rerun()


# --------------------
# Interfaz Principal
# --------------------
local_css()

# --- Encabezado ---
st.markdown('<h1 class="title-font text-gradient">Para Sofía</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Un pequeño universo creado solo para ti</p>', unsafe_allow_html=True)

# --- Creación de Pestañas ---
tab1, tab2, tab3, tab4 = st.tabs(["Declaración 💖", "Poema 📜", "Diversión ✨", "Sorpresa 🔮"])

# --- Contenido Pestaña 1: Declaración ---
with tab1:
    st.markdown('<p class="title-font" style="font-size: 1.8rem; text-align: center; color: var(--secondary);">Para la estrella más brillante de mi cielo</p>', unsafe_allow_html=True)
    st.markdown('<div class="big-love">TE AMO</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.2rem; text-align: center; font-style: italic; color: var(--secondary);">Eres la constelación que le da sentido a mi universo.</p>', unsafe_allow_html=True)

# --- Contenido Pestaña 2: Poema ---
with tab2:
    st.markdown('<h2 class="title-font" style="font-size: 2.5rem; text-align: center; color: var(--accent);">Versos de Nebulosa</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; font-size: 1.2rem; line-height: 1.8; font-style: italic; padding: 1rem; margin-top: 1rem; background: rgba(216, 180, 254, 0.05); border-radius: 10px; border-left: 4px solid var(--secondary);">
        En el lienzo oscuro de la noche te busco,<br>
        no como estrella fugaz, sino como galaxia entera.<br>
        Tu risa es eco de supernovas,<br>
        y en el silencio de tus ojos,<br>
        encuentro la calma de un cosmos en paz.<br>
        Eres el polvo estelar del que nacen mis sueños.
    </div>
    """, unsafe_allow_html=True)

# --- Contenido Pestaña 3: Diversión ---
with tab3:
    st.markdown('<h2 class="title-font" style="font-size: 2.5rem; text-align: center; color: var(--accent);">Un Poco de Magia Estelar</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Lluvia de Confeti 🎉"):
            st.balloons()
    with col2:
        if st.button("Nieve Mágica ❄️"):
            st.snow()

    st.markdown("---")

    if st.button("Un Mensaje del Universo para Ti 💫"):
        compliments = [
            "Tu brillo podría guiar a las naves espaciales.",
            "Eres más fascinante que una nebulosa.",
            "Tu sonrisa ilumina más que la Vía Láctea.",
            "En la galaxia de las personas, eres una superestrella.",
            "Tu energía es tan poderosa como un quásar.",
            "Tienes un corazón tan grande como el universo."
        ]
        st.session_state.compliment = random.choice(compliments)
    
    if 'compliment' in st.session_state:
        st.markdown(f'<div class="message-box">{st.session_state.compliment}</div>', unsafe_allow_html=True)

# --- Contenido Pestaña 4: Sorpresa ---
with tab4:
    st.markdown('<h2 class="title-font" style="font-size: 2.5rem; text-align: center; color: var(--accent);">Oráculo Estelar</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: var(--secondary); margin-bottom: 1.5rem;">Pregúntale al cosmos algo sobre ti y te revelará una verdad.</p>', unsafe_allow_html=True)
    
    question = st.text_input("Tu pregunta al cosmos:", placeholder="Ej: ¿Soy brillante?", label_visibility="collapsed")

    if st.button("Revelar Respuesta 🔮"):
        if question:
            answers = [
                "Sí, con la fuerza de mil soles. ☀️",
                "Absolutamente. Tu potencial es infinito como el espacio.",
                "Sin duda. Las estrellas mismas lo confirman.",
                "El cosmos entero conspira para decirte que sí.",
                "Claro que sí, eres una creación única y maravillosa del universo."
            ]
            st.session_state.answer = f'🔮 El cosmos responde: "{random.choice(answers)}"'
        else:
            st.session_state.answer = "El oráculo necesita una pregunta para susurrarte una respuesta."

    if 'answer' in st.session_state:
        st.markdown(f'<div class="message-box">{st.session_state.answer}</div>', unsafe_allow_html=True)


# --- Pie de página ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: var(--secondary); font-style: italic;">Hecho con cariño, pensando en cada estrella de tu ser ✨</p>', unsafe_allow_html=True)
