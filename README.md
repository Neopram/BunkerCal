# 🚢 Bunker Calculator PRO v2.0

**Enterprise Maritime Fuel Management System - Progressive Web App**

Una aplicación profesional para cálculos de combustible marítimo con soporte completo para iPhone 13 Pro y funcionalidad offline.

---

## ✨ Características Principales

### 📊 Cálculos Avanzados
- **VCF/WCF Corrections** - Correcciones de volumen y peso según temperatura
- **API MPMS Standards** - Cumplimiento con estándares API MPMS Ch. 11.1
- **ASTM D1250** - Tablas de corrección ASTM
- **ISO 91-1** - Estándares internacionales ISO
- **BDN Generation** - Generación de Bunker Delivery Notes
- **Audit Trail** - Registro completo de todas las operaciones

### 📱 PWA Features
- ✅ **Instalable** - Se instala como app nativa en iPhone
- ✅ **Offline First** - Funciona sin conexión a internet
- ✅ **Responsive Design** - Optimizado para móviles y tablets
- ✅ **Touch Optimized** - Controles táctiles de 44px mínimo
- ✅ **iOS Optimized** - Soporte para notch de iPhone 13 Pro
- ✅ **Fast Loading** - Caché inteligente para carga instantánea

### 🎨 Diseño Profesional
- IBM Carbon Design System
- Interfaz moderna y limpia
- Animaciones suaves
- Modo standalone (sin barra de navegador)

---

## 📦 Archivos del Proyecto

```
BunkerCalcPRO/
├── bunker-calculator (1).html    # Aplicación principal
├── manifest.json                  # Configuración PWA
├── service-worker.js              # Service Worker para offline
├── generate-icons.py              # Script generador de iconos
├── icon-*.png                     # Iconos PWA (12 tamaños)
└── README.md                      # Este archivo
```

---

## 🚀 Instalación en iPhone 13 Pro

### Opción 1: Instalación Local (Testing)

1. **Abrir el archivo HTML**
   - Abre `bunker-calculator (1).html` en Safari
   - O usa un servidor local (ver abajo)

2. **Agregar a Pantalla de Inicio**
   - Toca el botón **Compartir** (icono de cuadrado con flecha)
   - Desplázate y selecciona **"Agregar a pantalla de inicio"**
   - Personaliza el nombre si deseas
   - Toca **"Agregar"**

3. **Lanzar la App**
   - Busca el icono azul "BC" en tu pantalla de inicio
   - Toca para abrir en modo standalone (pantalla completa)

### Opción 2: Servidor Local (Recomendado)

Para probar la PWA con todas sus funcionalidades:

```powershell
# Opción A: Python HTTP Server
python -m http.server 8000

# Opción B: Node.js HTTP Server
npx http-server -p 8000

# Luego abre en Safari:
# http://localhost:8000/bunker-calculator%20(1).html
```

### Opción 3: Hosting en Producción (HTTPS Requerido)

Para deployment completo, necesitas HTTPS:

**GitHub Pages (Gratis):**
1. Crea un repositorio en GitHub
2. Sube todos los archivos
3. Activa GitHub Pages en Settings
4. Accede desde: `https://tu-usuario.github.io/repo-name/`

**Netlify/Vercel (Gratis):**
1. Arrastra la carpeta a Netlify Drop
2. Obtén URL HTTPS automática
3. Instala desde el navegador móvil

---

## 🎯 Guía de Uso

### Navegación Principal

La aplicación tiene 6 secciones principales:

1. **📊 VCF/WCF Calculator**
   - Cálculos de corrección de volumen/peso
   - Entrada de temperatura, densidad, API gravity
   - Resultados en tiempo real

2. **📋 BDN Generator**
   - Generación de Bunker Delivery Notes
   - Información de buque y proveedor
   - Exportación de documentos

3. **🔄 Batch Processing**
   - Procesamiento de múltiples cálculos
   - Importación de datos CSV
   - Exportación masiva

4. **📈 Reports & Analytics**
   - Reportes detallados
   - Gráficos y estadísticas
   - Análisis de tendencias

5. **⚙️ Settings**
   - Configuración de unidades
   - Selección de estándares (API/ASTM/ISO)
   - Preferencias de usuario

6. **ℹ️ About**
   - Información de la aplicación
   - Versión y créditos
   - Documentación

### Menú Móvil

En dispositivos móviles (< 1024px):
- Toca el botón **☰** (hamburguesa) en la esquina inferior derecha
- Se abrirá el menú lateral
- Selecciona la sección deseada
- El menú se cierra automáticamente

### Cálculos Rápidos

1. Selecciona el método de cálculo (VCF/WCF)
2. Ingresa los valores requeridos
3. Los resultados se actualizan automáticamente
4. Revisa el "Audit Trail" para ver las fórmulas usadas

---

## 🔧 Configuración Técnica

### Requisitos del Sistema

- **iOS**: 12.2 o superior (iPhone 13 Pro: iOS 15+)
- **Safari**: Versión 12.2+
- **Almacenamiento**: ~5 MB para caché offline
- **Conexión**: No requerida después de la primera carga

### Compatibilidad de Navegadores

| Navegador | Desktop | Mobile | PWA Install |
|-----------|---------|--------|-------------|
| Safari    | ✅      | ✅     | ✅          |
| Chrome    | ✅      | ✅     | ✅          |
| Firefox   | ✅      | ✅     | ⚠️          |
| Edge      | ✅      | ✅     | ✅          |

### Breakpoints Responsive

```css
/* Desktop Large */
@media (min-width: 1920px) { ... }

/* Desktop */
@media (max-width: 1024px) { ... }

/* Tablet / iPhone 13 Pro Landscape */
@media (max-width: 768px) { ... }

/* Mobile / iPhone 13 Pro Portrait */
@media (max-width: 480px) { ... }
```

### Optimizaciones iPhone 13 Pro

- **Resolución**: 390x844px (1170x2532 @3x)
- **Viewport**: `viewport-fit=cover` para notch
- **Touch Targets**: Mínimo 44x44px
- **Font Size**: 16px en inputs (previene zoom automático)
- **Status Bar**: Color azul IBM (#0043ce)

---

## 🛠️ Desarrollo y Personalización

### Regenerar Iconos

Si necesitas cambiar los iconos:

```powershell
# Edita generate-icons.py para cambiar colores/diseño
python generate-icons.py
```

Variables personalizables en `generate-icons.py`:
```python
BG_COLOR = '#0043ce'    # Color de fondo
TEXT_COLOR = '#ffffff'  # Color del texto
text = "BC"             # Texto del icono
```

### Modificar Colores del Tema

En `bunker-calculator (1).html`, líneas 14-36:

```css
:root {
    --ibm-blue-60: #0043ce;    /* Color principal */
    --ibm-blue-50: #4589ff;    /* Color hover */
    --ibm-gray-90: #262626;    /* Texto oscuro */
    /* ... más variables ... */
}
```

### Actualizar Service Worker

Después de cambios importantes, incrementa la versión en `service-worker.js`:

```javascript
const CACHE_VERSION = 'v2.0.1';  // Incrementa aquí
```

Esto forzará la actualización del caché en todos los dispositivos.

---

## 📊 Funcionalidades Técnicas

### Estándares Soportados

1. **API MPMS Ch. 11.1**
   - Petroleum Measurement Standards
   - Volume Correction Factors
   - Temperature compensation

2. **ASTM D1250**
   - Standard Guide for Petroleum Measurement Tables
   - Density corrections
   - API Gravity conversions

3. **ISO 91-1**
   - Petroleum measurement tables
   - International standards
   - Metric system support

### Fórmulas Implementadas

**VCF (Volume Correction Factor):**
```
VCF = exp[-α × (T - T₀) × {1 + 0.8 × α × (T - T₀)}]
```

**WCF (Weight Correction Factor):**
```
WCF = ρ₀ / ρₜ
```

**API Gravity:**
```
API = (141.5 / SG@60°F) - 131.5
```

---

## 🐛 Troubleshooting

### La app no se instala en iPhone

**Solución:**
- Asegúrate de usar Safari (no Chrome)
- Verifica que estés en HTTPS (o localhost)
- Limpia caché de Safari: Settings > Safari > Clear History

### Los cálculos no funcionan

**Solución:**
- Verifica que todos los campos requeridos estén llenos
- Revisa que los valores sean numéricos válidos
- Consulta el "Audit Trail" para ver errores

### El menú móvil no aparece

**Solución:**
- Reduce el ancho de la ventana a < 1024px
- Recarga la página (Cmd+R)
- Verifica que JavaScript esté habilitado

### La app no funciona offline

**Solución:**
- Abre DevTools > Application > Service Workers
- Verifica que el SW esté "activated"
- Fuerza actualización: Shift+Reload

### Iconos no se muestran

**Solución:**
- Verifica que todos los `icon-*.png` existan
- Regenera iconos: `python generate-icons.py`
- Limpia caché del navegador

---

## 📈 Roadmap Futuro

### v2.1 (Próximamente)
- [ ] Sincronización en la nube
- [ ] Modo oscuro
- [ ] Exportación a PDF mejorada
- [ ] Gráficos interactivos

### v2.2
- [ ] Multi-idioma (ES/EN/FR)
- [ ] Integración con APIs externas
- [ ] Notificaciones push
- [ ] Compartir cálculos

### v3.0
- [ ] Backend con base de datos
- [ ] Autenticación de usuarios
- [ ] Colaboración en tiempo real
- [ ] App nativa iOS/Android

---

## 📄 Licencia y Créditos

**Bunker Calculator PRO v2.0**
- Desarrollado con IBM Carbon Design System
- Iconos generados con Python Pillow
- PWA implementada con Service Workers estándar

**Estándares:**
- API MPMS - American Petroleum Institute
- ASTM D1250 - ASTM International
- ISO 91-1 - International Organization for Standardization

---

## 📞 Soporte

Para reportar bugs o solicitar features:
1. Documenta el problema con screenshots
2. Incluye información del dispositivo (iPhone modelo, iOS versión)
3. Describe los pasos para reproducir el error

---

## 🎉 ¡Listo para Usar!

Tu aplicación está completamente configurada y lista para instalarse en iPhone 13 Pro.

**Pasos finales:**
1. ✅ Abre `bunker-calculator (1).html` en Safari
2. ✅ Toca Compartir → Agregar a Inicio
3. ✅ Disfruta de tu app PWA profesional

**¡Feliz navegación! ⚓🚢**