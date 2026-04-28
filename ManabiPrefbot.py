from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Diccionario para gestionar el estado de los usuarios
user_data = {}

# Menu principal
MENU_PRINCIPAL = {
    "1": {
        "titulo": "🏢 ¿Qué es la Prefectura?",
        "info": "La Prefectura de Manabí es el Gobierno Autónomo Descentralizado Provincial encargado de planificar, gestionar y ejecutar obras, proyectos y servicios que impulsan el desarrollo de la provincia de Manabí. Su labor se enfoca en áreas como vialidad rural, riego, ambiente, producción, turismo y fortalecimiento social, con el objetivo de mejorar la calidad de vida de la población manabita. Además, promueve una gestión participativa, sostenible y articulada con los cantones y parroquias para fortalecer el progreso integral del territorio, el actual prefecto es el Economista Leonardo Orlando Arteaga, además la prefectura gestiona este desarollo basado en 5 ejes, elige uno uno para aprender",
        "foto": "https://epn.hiringroomcampus.com/assets/media/epn/company_6491adc3811d16240c3bb8a2.png",
        "submenu": {
            "1": {"texto": "🌱 *Manabí Vivo y Sostenible:* El primer objetivo estratégico de Manabí se basa en dos grandes acciones: Cuidar la naturaleza y preparar mejor a la población frente a los riesgos. Por un lado, busca recuperar y proteger áreas naturales, sembrando cada año 1.000 hectáreas de árboles en zonas que necesitan reforestación, creando viveros, fortaleciendo corredores ecológicos y ampliando espacios de conservación para enfrentar el cambio climático de forma sostenible. Por otro lado, impulsa el programa “Manabí Resiliente”, que busca capacitar cada año a miles de personas en educación ambiental, prevención de riesgos y respuesta ante emergencias, para que la población esté mejor preparada frente a desastres naturales y pueda construir un territorio más seguro, consciente y resistente."},
            "2": {"texto": "🛣️ *Manabí Integrado:* El segundo objetivo estratégico de Manabí busca mejorar la conectividad, el acceso al agua y la planificación de obras para impulsar el desarrollo de la provincia. Para lograrlo, se plantea intervenir cada año miles de kilómetros de vías, mejorar caminos rurales, construir puentes y fortalecer la red vial para facilitar la movilidad de personas, productos y servicios. También se busca ampliar y modernizar los sistemas de riego para garantizar agua en zonas productivas, construir pozos y mantener canales que apoyen la agricultura de forma sostenible. A esto se suma la limpieza y dragado de ríos, presas y esteros para prevenir inundaciones en época de lluvias, así como la elaboración de estudios y proyectos técnicos que permitan planificar mejor las futuras obras. En conjunto, estas acciones buscan una provincia más conectada, productiva, segura y preparada para crecer de forma ordenada."}, 
            "3": {"texto": "🤝 *Manabí Humano:* El tercer objetivo estratégico de Manabí busca mejorar la calidad de vida de las personas, especialmente de quienes se encuentran en situación de vulnerabilidad, promoviendo una provincia más justa, segura e inclusiva. Para ello, se plantea atender cada año a miles de personas con servicios de salud preventiva, educación, cultura, deporte y asistencia humanitaria, dando prioridad a niños, jóvenes, adultos mayores, mujeres y otros grupos de atención prioritaria. También se busca prevenir y erradicar la violencia de género, garantizando atención y acompañamiento a las mujeres víctimas, y fortalecer políticas públicas que promuevan la igualdad, los derechos y la inclusión de jóvenes y personas LGBTIQ+. Además, se impulsan acciones para mejorar las condiciones de vivienda rural y ampliar espacios públicos recreativos y deportivos, con el fin de reducir desigualdades y construir un entorno más digno, equitativo y con mejores oportunidades para todos."},
            "4": {"texto": "💰 *Manabí Próspero:* El cuarto objetivo estratégico de Manabí busca fortalecer la producción, la innovación, el turismo y los servicios para generar más empleo, mejorar la competitividad y dar mayor valor a lo que produce la provincia. Para ello, se impulsan acciones que apoyan a productores, emprendedores y negocios con capacitación, asistencia técnica, acceso a tecnología, innovación y mejores oportunidades de comercialización, promoviendo una producción más sostenible y moderna. También se busca modernizar la provincia con conectividad digital, internet comunitario, transformación tecnológica y nuevos sistemas de gestión que mejoren los servicios y acerquen oportunidades a las zonas rurales. A la vez, se apuesta por el turismo, la cultura y la gastronomía como motores de desarrollo, promoviendo eventos, infraestructura, identidad local y experiencias que posicionen a Manabí como un destino atractivo a nivel nacional e internacional, generando ingresos y cuidando su riqueza natural, cultural y patrimonial."},
            "5": {"texto": "📐 *Manabí Estratégico:* El cuarto objetivo estratégico de Manabí busca fortalecer al Gobierno Provincial para que sea más cercano, transparente, eficiente y participativo, brindando mejores servicios a la ciudadanía. Para ello, se impulsa el uso de información y datos confiables para mejorar la planificación y la toma de decisiones, se promueve el trabajo conjunto con universidades y otros actores para desarrollar proyectos de investigación e innovación, y se busca acercar los servicios institucionales a más comunidades, especialmente en zonas rurales. Además, se fomenta la participación ciudadana mediante programas de formación y capacitación dirigidos a líderes, comunidades y ciudadanía en general, con el fin de que más personas conozcan sus derechos, participen en las decisiones públicas y se involucren activamente en el desarrollo de la provincia."},
        }
    },
    "2": {
        "titulo": "🚜 Obras y Proyectos",
        "info": "Conoce los proyectos principales que transforman nuestra provincia:",
        "foto": "https://www.manabi.gob.ec/wp-content/uploads/2025/12/WhatsApp-Image-2025-12-16-at-9.48.22-AM.jpeg",
        "submenu": {
            "1": {
                "texto": "⚕️ *Manabí Saludable:* La Prefectura de Manabí impulsa el programa Operación Justicia Social, que incluye brigadas como Manabí Saludable para brindar atención gratuita a grupos prioritarios.",
                "foto": "https://www.manabi.gob.ec/wp-content/uploads/2022/11/WhatsApp-Image-2022-11-19-at-11.12.21.jpeg" 
            },
            "2": {
                "texto": "✊ *Rompiendo barreras:* Rompiendo Barreras es una iniciativa de la Prefectura que busca mejorar la calidad de vida y la autonomía de las personas con discapacidad en Manabí. El programa entrega ayudas técnicas como sillas de ruedas y prótesis, complementadas con servicios de rehabilitación y terapias físicas integrales. Además de la asistencia directa, fomenta la sensibilización para eliminar barreras sociales y físicas en toda la provincia. Al garantizar la igualdad de oportunidades y el acompañamiento familiar, este eje de inclusión impacta positivamente a miles de personas, promoviendo su plena integración en la sociedad.",
                "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPqD8QpKCHKqgC1UBEp2NgRSJo2ItqZWbHxg&s" 
            },
            "3": {
                "texto": "🛣️ *Vías del bicentenario:* Bajo el liderazgo del Economista Leonardo Orlando, la Prefectura de Manabí ejecuta un ambicioso programa vial de 142 km que integra la provincia a través de cinco rutas estratégicas financiadas por organismos internacionales (CAF, BDE y BID). Este proyecto beneficia a 624 mil personas, destacando vías clave como Calceta-Quiroga (53.6 km) y Ayacucho-La Unión (43 km), que reducen tiempos de viaje y dinamizan la economía local. Más que solo infraestructura, el plan impulsa una Ruta Turística y Gastronómica que conecta los sabores de Jipijapa y Santa Ana, acercando el campo, la ciudad y el mar para fortalecer la unidad y el desarrollo sostenible de las familias manabitas.",
                "foto": "https://manabi.gob.ec/viasdelbicentenario/wp-content/uploads/2025/11/mapa-5-vias-scaled.jpg" 
            },
            "4": {
                "texto": "📱 *ManaTech:* Manatech es un proyecto de robótica educativa para enseñar a niños, niñas y jóvenes de 7 a 17 años de edad en temas de robótica, programación de video juegos e innovación tecnológica",
                "foto": "https://www.manabi.gob.ec/wp-content/uploads/2025/04/29c74527-e9f1-4dc5-99ff-1a76c9bf2e43-1.jpg" 
            },
            "5": {
                "texto": "⚽ *Entrenando valores:* Entrenando Valores es un proyecto emblemático de la Prefectura que utiliza el deporte como herramienta de formación integral para niños y adolescentes en toda la provincia. A través de escuelas deportivas y torneos, el programa fomenta valores como la disciplina y el respeto, promoviendo el bienestar físico y emocional. Además, incluye un componente social clave con talleres para padres, buscando fortalecer el núcleo familiar y prevenir problemáticas sociales. De esta manera, la iniciativa impacta positivamente a miles de beneficiarios, consolidando la convivencia y el desarrollo comunitario en Manabí.",
                "foto": "https://www.manabi.gob.ec/wp-content/uploads/2020/02/foto-2-Entrenando-Valores.jpeg" 
            },
            "6": {
                "texto": "💜 *Erradicación de la violencia de género:* El proyecto Erradicación de la Violencia de Género es una iniciativa de la Prefectura de Manabí enfocada en prevenir y reducir la violencia contra las mujeres y familias mediante la sensibilización y capacitación. Ofrece servicios esenciales como acompañamiento psicológico y asesoría legal gratuita para garantizar la protección de las víctimas en toda la provincia. Al promover el respeto y la igualdad de derechos, el programa busca transformar las relaciones sociales y consolidar una cultura de paz y seguridad para todas las manabitas.",
                "foto": "https://www.manabi.gob.ec/wp-content/uploads/2025/03/WhatsApp-Image-2025-03-07-at-12.59.31-PM-scaled.jpeg" 
            },
        }
    },
    "3": {
        "titulo": "🌊 Turismo y Cultura",
        "info": "La Prefectura de Manabí impulsa el turismo, la cultura y el patrimonio a través de la Dirección de Turismo, Cultura y Patrimonio, enfocándose en la promoción de destinos, desarrollo sostenible y eventos, con el objetivo de consolidar a la provincia como un referente nacional. Se destacan proyectos de infraestructura y el plan estratégico de turismo sostenible al 2030.",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq9cq-b0mRVqOjlP2fOkDBdjy9Wl_Ms9miGA&s"
    },
    "4": {
        "titulo": "📅 Historia de la Provincia",
        "info": "La provincia de Manabí fue creada el 25 de junio de 1824. El territorio fue cuna de culturas ancestrales como la Valdivia, Machalilla, Chorrera, Jama-Coaque, Bahía y Manteña. Actualmente, la Prefectura de Manabí es liderada por el economista Leonardo Orlando Arteaga, quien trabaja en el desarrollo productivo, vial y social de la provincia, destacando el turismo, la cultura montuvia y la producción agropecuaria.",
        "foto": "https://joselias2022.com/wp-content/uploads/2024/05/manabi-200-anos.jpg?w=1024"
    }
}

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text.strip().lower()
    usuario_id = update.effective_user.id
    
    if "hola" in mensaje or "menú" in mensaje or "inicio" in mensaje:
        user_data[usuario_id] = {'estado': 'navegando_principal'}
        texto = "👋 *¡Bienvenido al Chatbot de la Prefectura de Manabí!*\n\nElige una opción:\n"
        for k, v in MENU_PRINCIPAL.items():
            texto += f"*{k}.* {v['titulo']}\n"
        await update.message.reply_text(texto, parse_mode="Markdown")
        return

    estado_actual = user_data.get(usuario_id, {}).get('estado')

    if estado_actual == 'navegando_principal':
        if mensaje in MENU_PRINCIPAL:
            seleccion = MENU_PRINCIPAL[mensaje]
            if "submenu" in seleccion:
                user_data[usuario_id] = {'estado': f'en_submenu_{mensaje}', 'opcion_padre': mensaje}
                texto_sub = f"📍 *{seleccion['titulo']}*\n\n{seleccion['info']}\n\n"
                for sk, sv in seleccion['submenu'].items():
                    titulo_limpio = sv['texto'].split(':')[0].replace('*','')
                    texto_sub += f"*{sk}.* {titulo_limpio}\n"
                
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=seleccion["foto"],
                    caption=texto_sub,
                    parse_mode="Markdown"
                )
            else:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=seleccion["foto"],
                    caption=f"📍 *{seleccion['titulo']}*\n\n{seleccion['info']}\n\n---\nEscribe 'hola' para volver.",
                    parse_mode="Markdown"
                )
        else:
            await update.message.reply_text("Elige un número del 1 al 4.")

    elif estado_actual and estado_actual.startswith('en_submenu_'):
        opcion_padre = user_data[usuario_id]['opcion_padre']
        submenu = MENU_PRINCIPAL[opcion_padre]['submenu']
        
        if mensaje in submenu:
            item = submenu[mensaje]
            texto_final = f"{item['texto']}\n\n---\nEscribe el número de otro ítem o 'Menú' para regresar al menú principal."
            
            # Si la clave "foto" existe y tiene un link (no está vacía)
            if "foto" in item and item["foto"] != "":
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=item["foto"],
                    caption=texto_final,
                    parse_mode="Markdown"
                )
            else:
                await update.message.reply_text(texto_final, parse_mode="Markdown")
        else:
            await update.message.reply_text("Opción no válida.")
    else:
        await update.message.reply_text("Escribe *'Menú'* para empezar.")

TOKEN = "8703286334:AAGxAQDr58iqwYm16Sxe4bioYxzetPwgKJY"

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder))
    print("Bot en ejecución...")
    app.run_polling()