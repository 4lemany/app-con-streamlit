import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="AI Nexus v2.0 | Advanced",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS ---
st.markdown("""
<style>
    .highlight { background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #ff4b4b; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR AVANZADO ---
with st.sidebar:
    st.title("🎛️ Centro de Control")
    
    # Widget: Camera Input (Solo visual, no guarda nada en este demo)
    use_webcam = st.checkbox("Habilitar Login Biométrico (Simulado)")
    if use_webcam:
        st.camera_input("Tomar foto de perfil", disabled=False)
    
    st.markdown("---")
    
    # Widget: Selectbox y Multiselect
    modo_usuario = st.selectbox("Perfil de Usuario", ["Investigador", "Desarrollador", "Entusiasta"])
    temas_interes = st.multiselect(
        "Filtrar temas:",
        ["Vision", "NLP", "Robótica", "Ética"],
        ["NLP", "Vision"]
    )
    
    st.markdown("---")
    
    # Navegación Principal
    menu = st.radio("Ir a:", 
        ["🏠 Inicio", "🧪 Lab de Generación", "🌍 Datos Globales", "📂 Archivos & Análisis", "📻 Podcast IA"]
    )

# --- PÁGINA 1: INICIO (CON TABS) ---
if menu == "🏠 Inicio":
    st.title("🏠 AI Nexus Dashboard")
    
    # Layout: Tabs (Pestañas)
    tab1, tab2, tab3 = st.tabs(["🔥 Novedades", "📅 Calendario Eventos", "💬 Feedback"])
    
    with tab1:
        # Layout: Columnas asimétricas
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("### Noticia Principal")
            st.image("https://images.unsplash.com/photo-1620712943543-bcc4688e7485", use_column_width=True)
            st.markdown("""
            ### La IA General (AGI) podría llegar antes de lo previsto
            **Resumen:** Expertos de OpenAI y Google DeepMind coinciden en que los nuevos avances en razonamiento...
            """)
            
            # Layout: Expander (Desplegable para ahorrar espacio)
            with st.expander("Leer artículo completo"):
                st.write("""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. 
                Cras venenatis euismod malesuada. Nullam ac odio ten.
                Aquí iría el texto largo de la noticia que no queremos que ocupe toda la pantalla de golpe.
                """)
                
        with col2:
            st.info("💡 **Sabías que...**\nEl primer chatbot, ELIZA, fue creado en 1966.")
            st.metric(label="Visitas hoy", value="4,230", delta="120")

    with tab2:
        st.header("Próximos lanzamientos")
        # Widget: Date Input
        fecha_filtro = st.date_input("Filtrar eventos desde:", datetime.now())
        st.write(f"Mostrando eventos a partir del: {fecha_filtro}")
        st.dataframe(pd.DataFrame({
            'Evento': ['OpenAI DevDay', 'Google I/O', 'PyTorch Conf'],
            'Fecha': ['2024-11-06', '2025-05-10', '2024-10-15'],
            'Probabilidad': ['90%', '100%', '85%']
        }))

    with tab3:
        st.header("Ayúdanos a mejorar")
        # Widget: Text Area
        feedback = st.text_area("¿Qué opinas de la nueva interfaz?", placeholder="Escribe aquí tu opinión...")
        if st.button("Enviar comentario"):
            st.toast('¡Gracias por tu feedback!', icon='🎉') # Notificación Toast

# --- PÁGINA 2: LAB DE GENERACIÓN (WIDGETS INTERACTIVOS) ---
elif menu == "🧪 Lab de Generación":
    st.title("🧪 Laboratorio de Prompting")
    st.markdown("Configura los parámetros de tu modelo (Simulación visual).")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Parámetros del Modelo")
        
        # Widget: Slider (Números continuos)
        temperature = st.slider("Temperatura (Creatividad)", 0.0, 1.0, 0.7, 0.01)
        
        # Widget: Select Slider (Opciones categóricas ordenadas)
        model_size = st.select_slider(
            "Tamaño del Modelo",
            options=["Nano", "Micro", "Small", "Medium", "Large", "XL"]
        )
        
        # Widget: Number Input
        max_tokens = st.number_input("Máximo de tokens", 100, 8000, 2048)
        
        # Widget: Color Picker (Para personalización)
        highlight_color = st.color_picker("Color de resaltado de sintaxis", "#00f900")

    with col2:
        st.subheader("Vista Previa de Configuración")
        # Media: JSON Display
        config_data = {
            "model": "GPT-Future",
            "temp": temperature,
            "size": model_size,
            "tokens": max_tokens,
            "theme": highlight_color
        }
        st.json(config_data)
        
        # Media: Code Display
        st.markdown("Generando código Python...")
        code_snippet = f"""
import openai

response = openai.Completion.create(
  model="gpt-future-{model_size.lower()}",
  temperature={temperature},
  max_tokens={max_tokens}
)
        """
        st.code(code_snippet, language='python')

# --- PÁGINA 3: DATOS GLOBALES (MAPAS Y GRÁFICOS) ---
elif menu == "🌍 Datos Globales":
    st.title("🌍 Centros de Datos de IA")
    
    st.markdown("Mapa en tiempo real de servidores activos.")
    
    # Generar datos aleatorios de coordenadas (Latitud/Longitud)
    # Media: MAPA
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']
    )
    st.map(map_data)
    
    st.markdown("---")
    st.subheader("Uso de Recursos")
    
    # Generar datos para gráficos
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['CPU', 'GPU', 'TPU']
    )
    
    # Layout: Columnas para gráficos
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Consumo Energético (Line Chart)**")
        st.line_chart(chart_data)
    with c2:
        st.markdown("**Distribución de Hardware (Bar Chart)**")
        st.bar_chart(chart_data)

# --- PÁGINA 4: ARCHIVOS (FILE UPLOADER) ---
elif menu == "📂 Archivos & Análisis":
    st.title("📂 Analizador de Documentos")
    
    # Widget: File Uploader
    uploaded_file = st.file_uploader("Sube un archivo CSV o TXT para analizar", type=['csv', 'txt'])
    
    if uploaded_file is not None:
        # Lógica para mostrar contenido según tipo
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.subheader("Vista Previa del Dataset")
            st.dataframe(df) # Widget interactivo de tabla
        else:
            stringio = uploaded_file.getvalue().decode("utf-8")
            st.text("Contenido del archivo:")
            st.text(stringio)
            
        # Barra de progreso simulada
        st.write("Analizando archivo con IA...")
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        st.success("¡Análisis completado!")

# --- PÁGINA 5: MULTIMEDIA (AUDIO/VIDEO) ---
elif menu == "📻 Podcast IA":
    st.title("📻 Podcast Semanal: Voces Sintéticas")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2628/2628834.png", width=200)
    
    with col2:
        st.subheader("Episodio 42: ¿Sueñan los androides?")
        st.write("En este episodio discutimos la ética de los sueños sintéticos.")
        
        # Media: Audio Player
        # Usamos un archivo de ejemplo de internet
        audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        st.audio(audio_url, format='audio/mp3')
        
        st.download_button(
            label="Descargar Transcripción",
            data="Locutor 1: Hola a todos...\nLocutor 2: Bienvenidos...",
            file_name="transcripcion_ep42.txt",
            mime="text/plain"
        )