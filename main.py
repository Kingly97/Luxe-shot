from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="Luxe Shots Photography")

# On indique à FastAPI que tous les fichiers du dossier actuel (".") sont accessibles via l'URL "/static"
app.mount("/static", StaticFiles(directory="."), name="static")

html_content = """
<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxe Shots Photography | Studio Premium Brazzaville</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Montserrat:wght@200;300;400;500;600&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        /* Palette Premium */
        :root {
            --gold-main: #d4af37;
            --black-bg: #050505;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background-color: var(--black-bg);
            color: #ffffff;
            overflow-x: hidden;
        }

        h1, h2, h3, h4, .font-serif {
            font-family: 'Cinzel', serif;
        }

        .text-gold {
            background: linear-gradient(to right, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            display: inline-block;
        }

        .bg-gold-gradient {
            background: linear-gradient(135deg, #bf953f 0%, #fcf6ba 50%, #b38728 100%);
            color: #000;
        }

        /* Preloader */
        #preloader {
            position: fixed;
            inset: 0;
            background: var(--black-bg);
            z-index: 9999;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: opacity 0.8s ease;
        }
        .loader-logo {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            border: 2px solid transparent;
            border-top-color: var(--gold-main);
            border-bottom-color: var(--gold-main);
            animation: spin 1.5s linear infinite;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 10px;
        }
        .loader-logo img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            animation: pulse 1.5s ease-in-out infinite;
        }
        @keyframes spin { 100% { transform: rotate(360deg); } }
        @keyframes pulse { 50% { transform: scale(0.9); opacity: 0.7; } }

        .reveal {
            opacity: 0;
            transform: translateY(50px);
            transition: all 1s cubic-bezier(0.5, 0, 0, 1);
        }
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        /* TECHNIQUE DE RECADRAGE CSS : Ajout de /static/ et %20 pour les espaces dans les URL CSS */
        .photo-crop {
            background-repeat: no-repeat;
            transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .crop-mariage { background-image: url('/static/Luxury_shots_site/WhatsApp Image 2026-08-13 %20a at 1000503741.jpg'); background-size: 280%; background-position: 95% 12%; }
        .crop-portrait { background-image: url('/staticLuxury_shots_site/WhatsApp Image 2026-08-13 at 1000503741.jpg'); background-size: 220%; background-position: 40% 50%; }
        .crop-grossesse { background-image: url('/static/Luxury_shots_site/WhatsApp Image 2026-08-13 %20a at 1000503741.jpg'); background-size: 280%; background-position: 95% 53%; }
        .crop-famille { background-image: url('/static/Luxury_shots_site/WhatsApp Image 2026-08-13 %20a at 1000503741.jpg'); background-size: 220%; background-position: 10% 82%; }
        .crop-produits { background-image: url('/static/Luxury_shots_site/WhatsApp Image 2026-08-13 %20a at 1000503741.jpg'); background-size: 250%; background-position: 95% 82%; }

        .crop-homme-costume { background-image: url('/Luxury_shots_site/WhatsApp Image 2026-08-13 %20a at 1000503740.jpg'); background-size: 280%; background-position: 95% 30%; }
        .crop-femme { background-image: url('/static/Luxury_shots_site/WhatsApp Image 2026-08-13 %20a at 1000503740.jpg'); background-size: 300%; background-position: 95% 62%; }
        .crop-homme-gris { background-image: url('/static/Luxury_shots_site/WhatsApp Image 2026-08-13 %20a at 1000503740.jpg'); background-size: 300%; background-position: 95% 92%; }

        .portfolio-item {
            position: relative;
            overflow: hidden;
            border-radius: 6px;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .portfolio-item:hover .photo-crop {
            transform: scale(1.15);
        }
        .portfolio-overlay {
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.2);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: all 0.5s ease;
            border: 1px solid transparent;
        }
        .portfolio-item:hover .portfolio-overlay {
            opacity: 1;
            background: rgba(0,0,0,0.75);
            border-color: rgba(212, 175, 55, 0.6);
        }

        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: var(--black-bg); }
        ::-webkit-scrollbar-thumb { background: var(--gold-main); border-radius: 4px; }

        .whatsapp-btn {
            position: fixed;
            bottom: 40px;
            right: 40px;
            background: linear-gradient(135deg, #25d366, #128c7e);
            color: white;
            width: 65px;
            height: 65px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 35px;
            box-shadow: 0 10px 25px rgba(37, 211, 102, 0.5);
            z-index: 100;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .whatsapp-btn:hover { transform: scale(1.15) rotate(-15deg); }
        
        .hero-pattern {
            background-image: radial-gradient(rgba(212, 175, 55, 0.15) 1px, transparent 1px);
            background-size: 35px 35px;
        }
    </style>
</head>
<body class="antialiased selection:bg-[#d4af37] selection:text-black">

    <!-- Preloader (Chemin d'image corrigé) -->
    <div id="preloader">
        <div class="loader-logo">
            <img src="/static/Luxury_shots_site/Luxury_shots_site/WhatsApp Image 2026-08-13 at 1000503739.jpg" alt="Luxe Shots Logo">
        </div>
    </div>

    <!-- Navigation -->
    <nav id="navbar" class="fixed w-full z-50 transition-all duration-500 py-6 border-b border-transparent">
        <div class="max-w-7xl mx-auto px-6 lg:px-8 flex justify-between items-center">
            <a href="#" class="flex items-center space-x-4 group">
                <img src="/static/Luxury_shots_site/WhatsApp Image 2026-08-13 at 1000503739.jpg" alt="Luxe Shots Logo" class="w-14 h-14 rounded-full border-2 border-[#d4af37] group-hover:scale-110 transition duration-500 shadow-[0_0_15px_rgba(212,175,55,0.4)]">
                <div class="flex flex-col">
                    <span class="font-serif text-2xl tracking-[0.25em] text-white group-hover:text-[#d4af37] transition duration-300">LUXE SHOTS</span>
                    <span class="text-[0.6rem] uppercase tracking-[0.4em] text-gray-400">Photography</span>
                </div>
            </a>
            
            <div class="hidden lg:flex space-x-10 items-center">
                <a href="#accueil" class="text-xs uppercase tracking-[0.2em] text-gray-300 hover:text-[#d4af37] transition">Accueil</a>
                <a href="#services" class="text-xs uppercase tracking-[0.2em] text-gray-300 hover:text-[#d4af37] transition">Services</a>
                <a href="#portfolio" class="text-xs uppercase tracking-[0.2em] text-gray-300 hover:text-[#d4af37] transition">Portfolio</a>
                <a href="#offres" class="text-xs uppercase tracking-[0.2em] text-[#d4af37] font-bold transition flex items-center gap-2">
                    <span class="relative flex h-2 w-2"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#d4af37] opacity-75"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-[#d4af37]"></span></span>
                    Offres
                </a>
                <a href="#contact" class="text-xs uppercase tracking-[0.2em] bg-gold-gradient px-8 py-3 rounded-sm text-black font-bold hover:shadow-[0_0_25px_rgba(212,175,55,0.5)] hover:-translate-y-1 transition duration-300">Réserver</a>
            </div>

            <button id="mobile-menu-btn" class="lg:hidden text-[#d4af37] hover:text-white transition focus:outline-none">
                <i class="fas fa-bars text-3xl"></i>
            </button>
        </div>
        
        <div id="mobile-menu" class="fixed inset-0 bg-[#050505]/98 backdrop-blur-2xl z-40 hidden flex-col justify-center items-center space-y-10">
            <button id="close-menu" class="absolute top-8 right-8 text-gray-400 hover:text-[#d4af37] text-4xl transition"><i class="fas fa-times"></i></button>
            <a href="#accueil" class="mobile-link text-2xl font-serif uppercase tracking-[0.3em] text-gray-300 hover:text-[#d4af37]">Accueil</a>
            <a href="#services" class="mobile-link text-2xl font-serif uppercase tracking-[0.3em] text-gray-300 hover:text-[#d4af37]">Services</a>
            <a href="#portfolio" class="mobile-link text-2xl font-serif uppercase tracking-[0.3em] text-gray-300 hover:text-[#d4af37]">Portfolio</a>
            <a href="#offres" class="mobile-link text-2xl font-serif uppercase tracking-[0.3em] text-[#d4af37]">Offres Spéciales</a>
            <a href="#contact" class="mobile-link text-xl font-serif uppercase tracking-[0.3em] bg-gold-gradient text-black px-12 py-4 mt-6 rounded-sm">Contact</a>
        </div>
    </nav>

    <section id="accueil" class="relative h-screen flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 bg-[#050505] hero-pattern opacity-40"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[700px] bg-[#d4af37] rounded-full blur-[180px] opacity-15 pointer-events-none"></div>

        <div class="relative z-10 text-center px-4 w-full max-w-5xl reveal active">
            <div class="inline-block border border-[#d4af37]/40 px-6 py-2 rounded-full mb-8 backdrop-blur-sm">
                <p class="text-[#d4af37] uppercase tracking-[0.4em] text-xs font-semibold">Brazzaville, Congo</p>
            </div>
            <h1 class="text-5xl md:text-7xl lg:text-8xl font-serif mb-6 leading-[1.1] text-white">
                CAPTURER L'<span class="text-gold italic">ÉMOTION</span>,<br>
                SUBLIMER VOS <span class="text-gold italic">SOUVENIRS</span>.
            </h1>
            <p class="text-gray-300 font-light text-lg md:text-xl max-w-2xl mx-auto mb-12 tracking-wide leading-relaxed">
                L'art de l'image au service de vos plus beaux moments. Des souvenirs d'aujourd'hui, des émotions pour toujours.
            </p>
            <div class="flex flex-col sm:flex-row justify-center items-center gap-6">
                <a href="#contact" class="bg-gold-gradient text-black px-10 py-4 text-sm font-bold uppercase tracking-[0.2em] rounded-sm hover:shadow-[0_0_25px_rgba(212,175,55,0.4)] hover:-translate-y-1 transition duration-300 w-full sm:w-auto">
                    Réserver une Séance
                </a>
                <a href="#portfolio" class="border border-[#d4af37] text-[#d4af37] px-10 py-4 text-sm font-bold uppercase tracking-[0.2em] rounded-sm hover:bg-[#d4af37] hover:text-black transition duration-300 w-full sm:w-auto">
                    Découvrir l'Art
                </a>
            </div>
        </div>
    </section>

    <!-- Section Présentation & Qualité (Chemin d'image corrigé) -->
    <section class="py-32 bg-[#121212] relative border-t border-gray-900">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="flex flex-col lg:flex-row items-center gap-20">
                <div class="lg:w-1/2 relative reveal">
                    <div class="relative p-3 border border-[#d4af37]/30 bg-black rounded-sm shadow-2xl">
                        <img src="/static/Luxury_shots_site/WhatsApp Image 2026-08-13 at 1000503741.jpg" alt="Luxe Shots Studio" class="w-full h-auto object-cover rounded-sm grayscale-[20%] hover:grayscale-0 transition duration-700">
                    </div>
                    <div class="absolute -bottom-8 -right-8 bg-[#050505] border border-[#d4af37] p-8 hidden md:block z-10 text-center rounded-sm shadow-[0_15px_40px_rgba(0,0,0,0.9)]">
                        <i class="fas fa-heart text-4xl text-[#d4af37] mb-3"></i>
                        <h4 class="font-serif text-2xl text-white">Qualité</h4>
                        <p class="text-xs text-[#d4af37] uppercase tracking-widest mt-2 font-bold">Professionnelle</p>
                    </div>
                </div>
                
                <div class="lg:w-1/2 reveal">
                    <h4 class="text-[#d4af37] uppercase tracking-[0.4em] text-xs mb-4 font-semibold">Le Studio</h4>
                    <h2 class="text-4xl md:text-6xl font-serif mb-8 leading-tight">Votre image, <br><span class="text-gold italic">notre passion.</span></h2>
                    <div class="space-y-6 text-gray-300 font-light leading-relaxed text-lg">
                        <p>Situé à la Résidence Émilie Flory à Brazzaville, <strong>Luxe Shots Photography</strong> vous accueille pour figer le temps avec élégance.</p>
                        <p>De la photographie de mariage aux portraits professionnels, notre équipement de pointe et notre œil artistique transforment des instants éphémères en œuvres d'art intemporelles et exceptionnelles.</p>
                    </div>
                    
                    <div class="mt-10 inline-flex items-center gap-4 bg-[#1a1a1a] border border-[#d4af37]/40 px-6 py-4 rounded-sm">
                        <i class="fas fa-gift text-2xl text-[#d4af37]"></i>
                        <div>
                            <p class="text-sm font-bold text-white uppercase tracking-wider">Offre Nouveaux Clients</p>
                            <p class="text-[#d4af37] font-serif text-xl">-10% sur votre première séance</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="py-32 bg-[#050505] relative border-t border-b border-gray-900">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="text-center mb-20 reveal">
                <h4 class="text-[#d4af37] uppercase tracking-[0.4em] text-xs mb-4 font-semibold">Expertise</h4>
                <h2 class="text-4xl md:text-6xl font-serif">Nos <span class="text-gold italic">Services</span></h2>
                <div class="w-16 h-[2px] bg-[#d4af37] mx-auto mt-8"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-10 gap-y-16">
                <div class="group reveal cursor-default bg-[#121212] p-8 rounded-sm border border-transparent hover:border-[#d4af37]/30 transition duration-500 hover:-translate-y-2">
                    <div class="text-[#d4af37] text-4xl mb-6 group-hover:scale-110 transition duration-300"><i class="fas fa-id-card"></i></div>
                    <h3 class="font-serif text-2xl mb-4 text-white">Photos d'identité</h3>
                    <div class="w-8 h-[1px] bg-[#d4af37] mb-4"></div>
                    <p class="text-gray-400 font-light text-sm leading-relaxed">Service professionnel. Rapide, conforme aux normes internationales et de haute qualité.</p>
                </div>
                <div class="group reveal cursor-default bg-[#121212] p-8 rounded-sm border border-transparent hover:border-[#d4af37]/30 transition duration-500 hover:-translate-y-2">
                    <div class="text-[#d4af37] text-4xl mb-6 group-hover:scale-110 transition duration-300"><i class="fas fa-rings-wedding"></i></div>
                    <h3 class="font-serif text-2xl mb-4 text-white">Mariage & Fiançailles</h3>
                    <div class="w-8 h-[1px] bg-[#d4af37] mb-4"></div>
                    <p class="text-gray-400 font-light text-sm leading-relaxed">Des moments uniques sublimés. Racontez l'histoire de votre amour avec élégance.</p>
                </div>
                <div class="group reveal cursor-default bg-[#121212] p-8 rounded-sm border border-transparent hover:border-[#d4af37]/30 transition duration-500 hover:-translate-y-2">
                    <div class="text-[#d4af37] text-4xl mb-6 group-hover:scale-110 transition duration-300"><i class="fas fa-portrait"></i></div>
                    <h3 class="font-serif text-2xl mb-4 text-white">Portraits</h3>
                    <div class="w-8 h-[1px] bg-[#d4af37] mb-4"></div>
                    <p class="text-gray-400 font-light text-sm leading-relaxed">Studio, Lifestyle ou Professionnel. Une séance sur-mesure pour révéler votre personnalité.</p>
                </div>
                <div class="group reveal cursor-default bg-[#121212] p-8 rounded-sm border border-transparent hover:border-[#d4af37]/30 transition duration-500 hover:-translate-y-2">
                    <div class="text-[#d4af37] text-4xl mb-6 group-hover:scale-110 transition duration-300"><i class="fas fa-baby-carriage"></i></div>
                    <h3 class="font-serif text-2xl mb-4 text-white">Grossesse</h3>
                    <div class="w-8 h-[1px] bg-[#d4af37] mb-4"></div>
                    <p class="text-gray-400 font-light text-sm leading-relaxed">Immortalisez l'attente et les premiers instants de vie en douceur et poésie.</p>
                </div>
                <div class="group reveal cursor-default bg-[#121212] p-8 rounded-sm border border-transparent hover:border-[#d4af37]/30 transition duration-500 hover:-translate-y-2">
                    <div class="text-[#d4af37] text-4xl mb-6 group-hover:scale-110 transition duration-300"><i class="fas fa-users"></i></div>
                    <h3 class="font-serif text-2xl mb-4 text-white">Famille & Enfants</h3>
                    <div class="w-8 h-[1px] bg-[#d4af37] mb-4"></div>
                    <p class="text-gray-400 font-light text-sm leading-relaxed">Des souvenirs à chérir toute une vie pour capturer votre belle complicité.</p>
                </div>
                <div class="group reveal cursor-default bg-[#121212] p-8 rounded-sm border border-transparent hover:border-[#d4af37]/30 transition duration-500 hover:-translate-y-2">
                    <div class="text-[#d4af37] text-4xl mb-6 group-hover:scale-110 transition duration-300"><i class="fas fa-box-open"></i></div>
                    <h3 class="font-serif text-2xl mb-4 text-white">Photos de Produits</h3>
                    <div class="w-8 h-[1px] bg-[#d4af37] mb-4"></div>
                    <p class="text-gray-400 font-light text-sm leading-relaxed">Mettez en valeur vos marques pour vos boutiques, catalogues et réseaux sociaux.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="py-32 bg-[#121212]">
        <div class="max-w-[1400px] mx-auto px-6">
            <div class="text-center mb-16 reveal">
                <h4 class="text-[#d4af37] uppercase tracking-[0.4em] text-xs mb-4 font-semibold">Créations</h4>
                <h2 class="text-4xl md:text-6xl font-serif">Notre <span class="text-gold italic">Portfolio</span></h2>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="portfolio-item h-80 lg:col-span-2 reveal" onclick="openLightbox('crop-mariage')">
                    <div class="photo-crop crop-mariage w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Mariage</span>
                    </div>
                </div>

                <div class="portfolio-item h-80 reveal" onclick="openLightbox('crop-portrait')">
                    <div class="photo-crop crop-portrait w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Portrait</span>
                    </div>
                </div>

                <div class="portfolio-item h-80 reveal" onclick="openLightbox('crop-grossesse')">
                    <div class="photo-crop crop-grossesse w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Grossesse</span>
                    </div>
                </div>

                <div class="portfolio-item h-80 reveal" onclick="openLightbox('crop-homme-costume')">
                    <div class="photo-crop crop-homme-costume w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Corporate</span>
                    </div>
                </div>

                <div class="portfolio-item h-80 lg:col-span-2 reveal" onclick="openLightbox('crop-famille')">
                    <div class="photo-crop crop-famille w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Famille</span>
                    </div>
                </div>

                <div class="portfolio-item h-80 reveal" onclick="openLightbox('crop-femme')">
                    <div class="photo-crop crop-femme w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Portrait</span>
                    </div>
                </div>

                <div class="portfolio-item h-80 reveal" onclick="openLightbox('crop-homme-gris')">
                    <div class="photo-crop crop-homme-gris w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Studio</span>
                    </div>
                </div>

                <div class="portfolio-item h-80 lg:col-span-3 reveal" onclick="openLightbox('crop-produits')">
                    <div class="photo-crop crop-produits w-full h-full"></div>
                    <div class="portfolio-overlay">
                        <i class="fas fa-search-plus text-[#d4af37] text-3xl mb-3"></i>
                        <span class="font-serif text-white tracking-widest uppercase text-xl">Produits</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Offres (Chemin d'image corrigé) -->
    <section id="offres" class="py-32 bg-[#050505] border-t border-[#d4af37]/30 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-[#d4af37] rounded-full blur-[150px] opacity-10 pointer-events-none"></div>

        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <div class="lg:w-1/2 reveal">
                    <div class="relative p-3 border border-[#d4af37]/50 bg-black rounded-sm shadow-[0_0_40px_rgba(212,175,55,0.15)]">
                        <img src="/static/Luxury_shots_site/WhatsApp Image 2026-08-13 at 1000503740.jpg" alt="Promotion Luxe Shots 6 Photos" class="w-full h-auto object-cover rounded-sm">
                    </div>
                </div>

                <div class="lg:w-1/2 reveal">
                    <div class="inline-flex items-center gap-3 px-5 py-2 border border-[#d4af37] text-[#d4af37] text-xs font-bold uppercase tracking-[0.2em] mb-6 rounded-sm bg-[#d4af37]/5">
                        <i class="fas fa-stopwatch animate-pulse"></i>
                        Durée Limitée
                    </div>
                    <h2 class="text-5xl md:text-6xl font-serif mb-6">Promotion <br><span class="text-gold italic">Spéciale !</span></h2>
                    <p class="text-gray-300 font-light text-lg mb-8 leading-relaxed">
                        Chaque photo raconte votre histoire. Mettez à jour votre image professionnelle avec notre offre exclusive.
                    </p>
                    
                    <div class="bg-gradient-to-br from-[#1a1a1a] to-[#0a0a0a] border-l-4 border-[#d4af37] p-8 mb-10 shadow-2xl rounded-r-sm">
                        <div class="flex items-center gap-6 mb-4">
                            <h3 class="text-6xl font-serif text-[#d4af37]">6</h3>
                            <div>
                                <h4 class="text-3xl font-serif text-white tracking-wide">PHOTOS</h4>
                                <p class="text-sm uppercase tracking-widest text-gray-400">Professionnelles</p>
                            </div>
                        </div>
                        <div class="w-full h-[1px] bg-gradient-to-r from-[#d4af37] to-transparent my-6"></div>
                        <p class="text-gray-400 uppercase tracking-widest text-sm mb-1">À seulement</p>
                        <p class="text-5xl font-serif text-white">5 000 <span class="text-2xl text-[#d4af37]">FCFA</span></p>
                    </div>

                    <a href="https://wa.me/242066753092?text=Bonjour,%20je%20souhaite%20réserver%20l'offre%20spéciale%206%20photos%20à%205000%20FCFA" target="_blank" class="inline-flex items-center justify-center w-full sm:w-auto gap-4 bg-gold-gradient text-black px-12 py-5 font-bold uppercase tracking-widest rounded-sm hover:shadow-[0_0_30px_rgba(212,175,55,0.4)] hover:-translate-y-1 transition duration-300">
                        <i class="fab fa-whatsapp text-2xl"></i>
                        Réserver maintenant
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact & Footer (Chemin d'image corrigé) -->
    <section id="contact" class="bg-[#121212] pt-32 pb-12 relative border-t border-gray-900">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 mb-20 reveal">
                <div class="lg:col-span-5">
                    <img src="/static/Luxury_shots_site/WhatsApp Image 2026-08-13 at 1000503739.jpg" alt="Luxe Shots Logo" class="w-24 h-24 rounded-full border-2 border-[#d4af37] mb-8 shadow-lg">
                    <h2 class="text-4xl font-serif mb-6 leading-tight">Entrez, on s'occupe de vos <span class="text-gold italic">plus beaux souvenirs !</span></h2>
                    <p class="text-gray-400 font-light mb-8 text-lg">Votre image, notre passion. Nous sommes impatients de vous accueillir au studio.</p>
                </div>
                
                <div class="lg:col-span-7 grid grid-cols-1 md:grid-cols-2 gap-12 bg-[#050505] p-10 rounded-sm border border-gray-800">
                    <div>
                        <div class="flex items-center gap-3 mb-4">
                            <i class="fas fa-map-marker-alt text-[#d4af37] text-xl"></i>
                            <h4 class="text-white uppercase tracking-[0.2em] text-sm font-bold">Où nous trouver ?</h4>
                        </div>
                        <p class="text-gray-400 font-light leading-relaxed pl-8">
                            Résidence Émilie Flory Batignol<br>
                            (Rez-de-chaussée)<br>
                            Brazzaville, Congo
                        </p>
                    </div>
                    
                    <div>
                        <div class="flex items-center gap-3 mb-4">
                            <i class="fas fa-clock text-[#d4af37] text-xl"></i>
                            <h4 class="text-white uppercase tracking-[0.2em] text-sm font-bold">Horaires</h4>
                        </div>
                        <p class="text-gray-400 font-light leading-relaxed pl-8">
                            Lundi - Samedi<br>
                            9h00 à 16h00
                        </p>
                    </div>
                    
                    <div class="md:col-span-2 pt-6 border-t border-gray-800">
                        <h4 class="text-white uppercase tracking-[0.2em] text-sm font-bold mb-6 text-center md:text-left">Contactez-nous</h4>
                        <div class="flex flex-col sm:flex-row gap-8 justify-center md:justify-start">
                            <a href="tel:067824190" class="flex items-center gap-4 text-2xl font-serif text-gray-300 hover:text-[#d4af37] transition group">
                                <div class="w-12 h-12 rounded-full border border-gray-700 flex items-center justify-center group-hover:border-[#d4af37] transition">
                                    <i class="fas fa-phone text-[#d4af37]"></i>
                                </div>
                                067 824 190
                            </a>
                            <a href="tel:066379203" class="flex items-center gap-4 text-2xl font-serif text-gray-300 hover:text-[#d4af37] transition group">
                                <div class="w-12 h-12 rounded-full border border-gray-700 flex items-center justify-center group-hover:border-[#d4af37] transition">
                                    <i class="fas fa-phone text-[#d4af37]"></i>
                                </div>
                                066 379 203
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center text-sm font-light text-gray-500">
                <p>&copy; <span id="year"></span> Luxe Shots Photography. Tous droits réservés.</p>
                <div class="flex items-center gap-2 mt-4 md:mt-0">
                    <span class="italic">Votre image, notre passion !</span>
                    <i class="fas fa-camera text-[#d4af37]"></i>
                </div>
            </div>
        </div>
    </section>

    <a href="https://wa.me/242066753092" target="_blank" class="whatsapp-btn" aria-label="Discuter sur WhatsApp">
        <i class="fab fa-whatsapp"></i>
    </a>

    <div id="lightbox" class="fixed inset-0 bg-[#050505]/98 backdrop-blur-sm z-[100] hidden items-center justify-center p-4">
        <button onclick="closeLightbox()" class="absolute top-6 right-6 text-gray-400 hover:text-[#d4af37] text-4xl focus:outline-none z-[110] transition">
            <i class="fas fa-times"></i>
        </button>
        <div id="lightbox-content" class="w-full max-w-3xl h-[75vh] border border-[#d4af37]/50 shadow-[0_0_50px_rgba(0,0,0,0.8)] relative photo-crop rounded-sm"></div>
    </div>

    <script>
        window.addEventListener('load', () => {
            const preloader = document.getElementById('preloader');
            setTimeout(() => {
                preloader.style.opacity = '0';
                setTimeout(() => { preloader.style.display = 'none'; }, 800);
            }, 1000);
        });

        document.getElementById('year').textContent = new Date().getFullYear();

        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('bg-[#050505]/95', 'backdrop-blur-md', 'py-4', 'border-b', 'border-[#d4af37]/20', 'shadow-lg');
                navbar.classList.remove('py-6', 'border-transparent');
            } else {
                navbar.classList.remove('bg-[#050505]/95', 'backdrop-blur-md', 'py-4', 'border-b', 'border-[#d4af37]/20', 'shadow-lg');
                navbar.classList.add('py-6', 'border-transparent');
            }
        });

        const btnMenu = document.getElementById('mobile-menu-btn');
        const closeMenu = document.getElementById('close-menu');
        const menu = document.getElementById('mobile-menu');
        const links = document.querySelectorAll('.mobile-link');

        function toggleMenu() {
            if(menu.classList.contains('hidden')) {
                menu.classList.remove('hidden');
                menu.classList.add('flex');
                document.body.style.overflow = 'hidden';
            } else {
                menu.classList.add('hidden');
                menu.classList.remove('flex');
                document.body.style.overflow = 'auto';
            }
        }

        btnMenu.addEventListener('click', toggleMenu);
        closeMenu.addEventListener('click', toggleMenu);
        links.forEach(l => l.addEventListener('click', toggleMenu));

        function openLightbox(cropClass) {
            const lightbox = document.getElementById('lightbox');
            const content = document.getElementById('lightbox-content');
            content.className = 'w-full max-w-3xl h-[75vh] border border-[#d4af37]/50 shadow-2xl relative photo-crop rounded-sm ' + cropClass;
            lightbox.classList.remove('hidden');
            lightbox.classList.add('flex');
            document.body.style.overflow = 'hidden';
        }

        function closeLightbox() {
            const lightbox = document.getElementById('lightbox');
            lightbox.classList.add('hidden');
            lightbox.classList.remove('flex');
            document.body.style.overflow = 'auto';
        }

        const reveals = document.querySelectorAll('.reveal');
        function revealOnScroll() {
            for (let i = 0; i < reveals.length; i++) {
                let windowHeight = window.innerHeight;
                let elementTop = reveals[i].getBoundingClientRect().top;
                let elementVisible = 120;
                if (elementTop < windowHeight - elementVisible) {
                    reveals[i].classList.add('active');
                }
            }
        }
        window.addEventListener('scroll', revealOnScroll);
        revealOnScroll();
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return html_content

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)