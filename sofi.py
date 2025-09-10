<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✨ Una Sorpresa para Sofía ✨</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #a855f7; /* Morado principal */
            --secondary: #d8b4fe; /* Lavanda claro */
            --accent: #f0abfc; /* Rosa-violeta */
            --dark-bg: #110f1a; /* Fondo de noche profunda */
            --text-light: #f3e8ff; /* Texto claro lavanda */
            --text-dark: #3b0764; /* Texto oscuro */
            --shadow: rgba(168, 85, 247, 0.4);
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--dark-bg);
            color: var(--text-light);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        
        /* --- Animación de fondo de estrellas --- */
        .stars-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
            z-index: -1;
        }

        .star {
            position: absolute;
            background-color: white;
            border-radius: 50%;
            animation: twinkle linear infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0; }
            50% { opacity: 1; }
        }

        /* --- Estilos principales --- */
        .main-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            border: 1px solid rgba(216, 180, 254, 0.2);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
            transition: opacity 0.5s ease-in-out;
        }

        .title-font {
            font-family: 'Dancing Script', cursive;
        }

        .text-gradient {
            background: linear-gradient(45deg, var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .tab-button {
            transition: all 0.3s ease;
            border-bottom: 2px solid transparent;
        }

        .tab-button.active {
            color: var(--accent);
            border-bottom-color: var(--accent);
            transform: translateY(-2px);
        }

        .content-card {
            display: none;
            animation: fadeIn 0.8s ease-out;
        }

        .content-card.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .interactive-button {
            background: linear-gradient(45deg, var(--primary), #c084fc);
            color: white;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px var(--shadow);
        }
        .interactive-button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px var(--shadow);
            filter: brightness(1.1);
        }

        .message-box {
            background: rgba(168, 85, 247, 0.1);
            border-left: 4px solid var(--primary);
            animation: fadeIn 0.5s ease-out;
        }

        .big-love {
            font-family: 'Dancing Script', cursive;
            font-weight: 700;
            font-size: 4rem;
            text-align: center;
            background: linear-gradient(45deg, var(--secondary), var(--accent), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: pulse 2.5s infinite, colorShift 5s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); text-shadow: 0 0 10px var(--shadow); }
            50% { transform: scale(1.05); text-shadow: 0 0 25px var(--shadow); }
        }
        @keyframes colorShift {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(25deg); }
        }

        /* --- Loader --- */
        #loader {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--dark-bg);
            z-index: 9999;
            transition: opacity 0.8s ease;
        }
        #loader.hidden {
            opacity: 0;
            pointer-events: none;
        }
    </style>
</head>
<body class="p-4 md:p-6">
    <!-- Fondo animado de estrellas -->
    <div id="stars-container" class="stars-container"></div>

    <!-- Pantalla de carga -->
    <div id="loader">
        <h1 class="title-font text-4xl text-gradient mb-4">Creando una galaxia para Sofía...</h1>
        <svg class="animate-spin h-8 w-8 text-purple-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
    </div>

    <!-- Contenedor principal -->
    <main id="main-content" class="main-container w-full max-w-2xl mx-auto p-6 md:p-8 opacity-0">
        <header class="text-center mb-6">
            <h1 class="title-font text-5xl md:text-6xl text-gradient">Para Sofía</h1>
            <p class="text-lg text-secondary mt-2">Un pequeño universo creado solo para ti</p>
        </header>

        <!-- Navegación de pestañas -->
        <nav class="flex justify-center space-x-4 md:space-x-8 border-b border-purple-500/20 mb-6">
            <button class="tab-button p-2 text-lg active" data-tab="declaracion">Declaración 💖</button>
            <button class="tab-button p-2 text-lg" data-tab="poema">Poema 📜</button>
            <button class="tab-button p-2 text-lg" data-tab="diversion">Diversión ✨</button>
            <button class="tab-button p-2 text-lg" data-tab="sorpresa">Sorpresa 🔮</button>
        </nav>

        <!-- Contenido de las pestañas -->
        <div id="tab-content">
            <!-- 1. Declaración de Amor -->
            <div id="declaracion" class="content-card active">
                <div class="text-center p-4">
                    <p class="title-font text-2xl text-secondary mb-4">Para la estrella más brillante de mi cielo</p>
                    <div class="big-love text-5xl md:text-7xl">TE AMO</div>
                    <svg class="mx-auto my-6 w-24 h-24 text-accent" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                        <defs>
                            <filter id="glow">
                                <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
                                <feMerge>
                                    <feMergeNode in="coloredBlur"/>
                                    <feMergeNode in="SourceGraphic"/>
                                </feMerge>
                            </filter>
                        </defs>
                        <style>
                            svg path {
                                filter: url(#glow);
                                animation: svgPulse 2.5s infinite;
                            }
                            @keyframes svgPulse {
                                50% { transform: scale(1.1); }
                            }
                        </style>
                    </svg>
                    <p class="text-xl italic text-secondary mt-4">Eres la constelación que le da sentido a mi universo.</p>
                </div>
            </div>

            <!-- 2. Poema -->
            <div id="poema" class="content-card">
                <div class="p-4">
                     <h2 class="title-font text-3xl text-center text-accent mb-4">Versos de Nebulosa</h2>
                     <div class="text-center text-lg leading-loose italic p-4 rounded-lg bg-purple-900/20 border-l-4 border-secondary">
                        <p>En el lienzo oscuro de la noche te busco,<br>
                        no como estrella fugaz, sino como galaxia entera.<br>
                        Tu risa es eco de supernovas,<br>
                        y en el silencio de tus ojos,<br>
                        encuentro la calma de un cosmos en paz.<br>
                        Eres el polvo estelar del que nacen mis sueños.</p>
                     </div>
                </div>
            </div>

            <!-- 3. Diversión y Alegría -->
            <div id="diversion" class="content-card text-center">
                 <h2 class="title-font text-3xl text-center text-accent mb-6">Un Poco de Magia Estelar</h2>
                 <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <button id="confettiBtn" class="interactive-button rounded-full py-3 px-6 text-lg">Lluvia de Confeti 🎉</button>
                    <button id="starsBtn" class="interactive-button rounded-full py-3 px-6 text-lg">Deseo Fugaz 🌠</button>
                 </div>
                 <hr class="my-6 border-purple-500/20">
                 <button id="complimentBtn" class="interactive-button w-full rounded-full py-3 px-6 text-lg">Un Mensaje del Universo para Ti 💫</button>
                 <div id="compliment-box" class="message-box p-4 mt-4 rounded-lg text-xl text-center hidden"></div>
            </div>
            
            <!-- 4. Sorpresa Interactiva -->
            <div id="sorpresa" class="content-card text-center">
                <h2 class="title-font text-3xl text-center text-accent mb-4">Oráculo Estelar</h2>
                <p class="text-secondary mb-4">Pregúntale al cosmos algo sobre ti y te revelará una verdad.</p>
                <input id="questionInput" type="text" class="w-full bg-purple-900/30 border border-purple-500/30 rounded-lg p-3 text-center text-lg focus:ring-2 focus:ring-accent focus:outline-none" placeholder="Ej: ¿Soy brillante?">
                <button id="answerBtn" class="interactive-button w-full rounded-full py-3 px-6 text-lg mt-4">Revelar Respuesta 🔮</button>
                <div id="answer-box" class="message-box p-4 mt-4 rounded-lg text-xl text-center hidden"></div>
            </div>
        </div>

        <footer class="text-center mt-8 pt-4 border-t border-purple-500/20">
            <p class="text-secondary italic">Hecho con cariño, pensando en cada estrella de tu ser ✨</p>
        </footer>
    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const loader = document.getElementById('loader');
            const mainContent = document.getElementById('main-content');
            
            // Simular carga y mostrar contenido
            setTimeout(() => {
                loader.classList.add('hidden');
                mainContent.style.opacity = '1';
            }, 2500);

            // --- Lógica de pestañas ---
            const tabButtons = document.querySelectorAll('.tab-button');
            const contentCards = document.querySelectorAll('.content-card');

            tabButtons.forEach(button => {
                button.addEventListener('click', () => {
                    tabButtons.forEach(btn => btn.classList.remove('active'));
                    button.classList.add('active');

                    const tab = button.dataset.tab;
                    contentCards.forEach(card => {
                        card.classList.remove('active');
                        if (card.id === tab) {
                            card.classList.add('active');
                        }
                    });
                });
            });

            // --- Lógica de "Diversión y Alegría" ---
            const complimentBtn = document.getElementById('complimentBtn');
            const complimentBox = document.getElementById('compliment-box');
            const compliments = [
                "Tu brillo podría guiar a las naves espaciales.",
                "Eres más fascinante que una nebulosa.",
                "Tu sonrisa ilumina más que la Vía Láctea.",
                "En la galaxia de las personas, eres una superestrella.",
                "Tu energía es tan poderosa como un quásar.",
                "Tienes un corazón tan grande como el universo."
            ];

            complimentBtn.addEventListener('click', () => {
                const randomCompliment = compliments[Math.floor(Math.random() * compliments.length)];
                complimentBox.textContent = randomCompliment;
                complimentBox.classList.remove('hidden');
            });

            // --- Lógica de "Sorpresa Interactiva" ---
            const answerBtn = document.getElementById('answerBtn');
            const answerBox = document.getElementById('answer-box');
            const questionInput = document.getElementById('questionInput');
            const answers = [
                "Sí, con la fuerza de mil soles. ☀️",
                "Absolutamente. Tu potencial es infinito como el espacio.",
                "Sin duda. Las estrellas mismas lo confirman.",
                "El cosmos entero conspira para decirte que sí.",
                "Claro que sí, eres una creación única y maravillosa del universo."
            ];

            answerBtn.addEventListener('click', () => {
                if (questionInput.value.trim() === '') {
                    answerBox.textContent = 'El oráculo necesita una pregunta para responder.';
                } else {
                    const randomAnswer = answers[Math.floor(Math.random() * answers.length)];
                    answerBox.textContent = `🔮 El cosmos responde: "${randomAnswer}"`;
                }
                answerBox.classList.remove('hidden');
            });


            // --- Efectos visuales ---
            const confettiBtn = document.getElementById('confettiBtn');
            const starsBtn = document.getElementById('starsBtn');

            confettiBtn.addEventListener('click', () => createBurst(false));
            starsBtn.addEventListener('click', () => createBurst(true));
            
            function createBurst(isStar) {
                for (let i = 0; i < 80; i++) {
                    createParticle(isStar);
                }
            }

            function createParticle(isStar) {
                const particle = document.createElement('div');
                document.body.appendChild(particle);

                const size = Math.floor(Math.random() * (isStar ? 15 : 10)) + 5;
                particle.style.width = `${size}px`;
                particle.style.height = `${size}px`;

                if (isStar) {
                    particle.innerHTML = '✨';
                    particle.style.fontSize = `${size * 1.5}px`;
                } else {
                    const colors = ['#a855f7', '#d8b4fe', '#f0abfc', '#ffffff'];
                    particle.style.background = colors[Math.floor(Math.random() * colors.length)];
                    particle.style.borderRadius = Math.random() > 0.5 ? '50%' : '0';
                }
                
                particle.style.position = 'fixed';
                particle.style.top = '50%';
                particle.style.left = '50%';
                particle.style.opacity = 1;
                particle.style.zIndex = 10000;
                particle.style.pointerEvents = 'none';

                const angle = Math.random() * 360;
                const velocity = Math.random() * 50 + 50;
                const gravity = 0.5;

                let vx = Math.cos(angle * Math.PI / 180) * velocity;
                let vy = Math.sin(angle * Math.PI / 180) * velocity;

                const animation = particle.animate([
                    { transform: 'translate(-50%, -50%) scale(1)', opacity: 1 },
                    { transform: `translate(${vx}vw, ${vy}vh) scale(0)`, opacity: 0 }
                ], {
                    duration: Math.random() * 2000 + 1000,
                    easing: 'cubic-bezier(0.1, 0.9, 0.2, 1)',
                });

                animation.onfinish = () => particle.remove();
            }

            // --- Creación de estrellas de fondo ---
            const starsContainer = document.getElementById('stars-container');
            const numStars = 200;

            for (let i = 0; i < numStars; i++) {
                const star = document.createElement('div');
                star.classList.add('star');
                const size = Math.random() * 3 + 1;
                star.style.width = `${size}px`;
                star.style.height = `${size}px`;
                star.style.top = `${Math.random() * 100}%`;
                star.style.left = `${Math.random() * 100}%`;
                const duration = Math.random() * 3 + 2;
                star.style.animationDuration = `${duration}s`;
                star.style.animationDelay = `${Math.random() * duration}s`;
                starsContainer.appendChild(star);
            }
        });
    </script>
</body>
</html>
