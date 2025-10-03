# 🚀 Deployment Guide - Bunker Calculator PRO

Esta guía te ayudará a desplegar tu PWA en diferentes plataformas.

---

## 📋 Pre-requisitos

✅ Todos los archivos generados:
- `bunker-calculator (1).html`
- `manifest.json`
- `service-worker.js`
- `icon-*.png` (12 archivos)

✅ Requisitos para PWA:
- **HTTPS obligatorio** (excepto localhost)
- Service Worker registrado
- Manifest válido

---

## 🌐 Opción 1: GitHub Pages (Recomendado - GRATIS)

### Paso 1: Crear Repositorio

```bash
# En tu terminal (Git Bash o PowerShell)
cd c:\Users\feder\Desktop\BunkerCalcPRO

# Inicializar Git
git init

# Agregar archivos
git add .

# Commit inicial
git commit -m "Initial commit - Bunker Calculator PRO v2.0"
```

### Paso 2: Subir a GitHub

1. Ve a https://github.com/new
2. Crea un repositorio llamado `bunker-calculator-pro`
3. **NO** inicialices con README

```bash
# Conectar con GitHub (reemplaza TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/bunker-calculator-pro.git

# Subir código
git branch -M main
git push -u origin main
```

### Paso 3: Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Click en **Settings** (Configuración)
3. En el menú lateral, click en **Pages**
4. En "Source", selecciona **main** branch
5. Click en **Save**
6. Espera 1-2 minutos

### Paso 4: Acceder a tu PWA

Tu app estará disponible en:
```
https://TU-USUARIO.github.io/bunker-calculator-pro/bunker-calculator%20(1).html
```

**Opcional:** Renombra el archivo HTML a `index.html` para una URL más limpia:
```
https://TU-USUARIO.github.io/bunker-calculator-pro/
```

---

## ⚡ Opción 2: Netlify (Más Fácil - GRATIS)

### Método A: Drag & Drop

1. Ve a https://app.netlify.com/drop
2. Arrastra la carpeta `BunkerCalcPRO` completa
3. ¡Listo! Obtendrás una URL como: `https://random-name-123.netlify.app`

### Método B: Netlify CLI

```powershell
# Instalar Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
cd c:\Users\feder\Desktop\BunkerCalcPRO
netlify deploy --prod
```

### Configuración Netlify

Crea un archivo `netlify.toml`:

```toml
[build]
  publish = "."

[[redirects]]
  from = "/*"
  to = "/bunker-calculator (1).html"
  status = 200
```

---

## 🔷 Opción 3: Vercel (GRATIS)

### Método A: Vercel CLI

```powershell
# Instalar Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd c:\Users\feder\Desktop\BunkerCalcPRO
vercel --prod
```

### Método B: Vercel Web

1. Ve a https://vercel.com/new
2. Importa tu repositorio de GitHub
3. Click en **Deploy**

---

## 🪟 Opción 4: Servidor Local (Testing)

### Python HTTP Server

```powershell
# Python 3
cd c:\Users\feder\Desktop\BunkerCalcPRO
python -m http.server 8000

# Abre en navegador:
# http://localhost:8000/bunker-calculator%20(1).html
```

### Node.js HTTP Server

```powershell
# Instalar http-server
npm install -g http-server

# Ejecutar
cd c:\Users\feder\Desktop\BunkerCalcPRO
http-server -p 8000

# Abre en navegador:
# http://localhost:8000/bunker-calculator%20(1).html
```

### PHP Built-in Server

```powershell
cd c:\Users\feder\Desktop\BunkerCalcPRO
php -S localhost:8000
```

---

## 📱 Instalación en iPhone 13 Pro

### Desde Safari (iOS)

1. **Abre la URL de tu PWA** en Safari
   - Ejemplo: `https://tu-usuario.github.io/bunker-calculator-pro/`

2. **Toca el botón Compartir**
   - Icono de cuadrado con flecha hacia arriba
   - Está en la barra inferior

3. **Desplázate hacia abajo**
   - Busca "Agregar a pantalla de inicio"
   - Icono con un "+"

4. **Personaliza (opcional)**
   - Edita el nombre si deseas
   - El icono se cargará automáticamente

5. **Toca "Agregar"**
   - La app aparecerá en tu pantalla de inicio
   - Icono azul con "BC"

6. **Abre la app**
   - Toca el icono
   - Se abrirá en modo standalone (pantalla completa)
   - ¡Sin barra de navegador!

### Verificar Instalación

La app está correctamente instalada si:
- ✅ Aparece en la pantalla de inicio
- ✅ Se abre en pantalla completa (sin Safari UI)
- ✅ La barra de estado es azul (#0043ce)
- ✅ Funciona sin conexión a internet

---

## 🔒 Configuración HTTPS

### ¿Por qué HTTPS?

Las PWAs **requieren HTTPS** por seguridad:
- Service Workers solo funcionan en HTTPS
- Geolocalización y otras APIs requieren HTTPS
- Protección de datos del usuario

### Excepciones

Solo funciona sin HTTPS en:
- `localhost` (desarrollo local)
- `127.0.0.1` (desarrollo local)
- Archivos locales `file://` (limitado)

### Obtener HTTPS Gratis

Todas estas opciones incluyen HTTPS automático:
- ✅ GitHub Pages
- ✅ Netlify
- ✅ Vercel
- ✅ Cloudflare Pages

---

## 🧪 Testing Checklist

Antes de deployment, verifica:

### Funcionalidad Básica
- [ ] La página carga correctamente
- [ ] Todos los estilos se aplican
- [ ] JavaScript funciona sin errores
- [ ] Los cálculos se ejecutan correctamente
- [ ] El menú móvil funciona

### PWA Features
- [ ] Service Worker se registra
- [ ] Manifest.json es accesible
- [ ] Todos los iconos cargan
- [ ] La app es instalable
- [ ] Funciona offline después de la primera carga

### Mobile Optimization
- [ ] Responsive en 390x844px (iPhone 13 Pro)
- [ ] Touch targets mínimo 44px
- [ ] Inputs no causan zoom automático
- [ ] Menú hamburguesa funciona
- [ ] Orientación portrait funciona

### Performance
- [ ] Carga en < 3 segundos
- [ ] Caché funciona correctamente
- [ ] No hay errores en consola
- [ ] Lighthouse score > 90

---

## 🛠️ Troubleshooting Deployment

### Error: Service Worker no se registra

**Causa:** No estás en HTTPS o localhost

**Solución:**
```javascript
// Verifica en la consola del navegador
if ('serviceWorker' in navigator) {
    console.log('Service Worker soportado');
} else {
    console.log('Service Worker NO soportado');
}
```

### Error: Manifest no se carga

**Causa:** Ruta incorrecta o CORS

**Solución:**
- Verifica que `manifest.json` esté en la raíz
- Abre directamente: `https://tu-url/manifest.json`
- Debe devolver JSON válido

### Error: Iconos no aparecen

**Causa:** Rutas incorrectas en manifest.json

**Solución:**
```json
{
  "icons": [
    {
      "src": "./icon-192.png",  // Ruta relativa
      "sizes": "192x192"
    }
  ]
}
```

### Error: No se puede instalar en iPhone

**Causa:** No estás usando Safari

**Solución:**
- Usa Safari (no Chrome en iOS)
- Verifica que estés en HTTPS
- Limpia caché: Settings > Safari > Clear History

---

## 📊 Monitoreo y Analytics

### Google Analytics (Opcional)

Agrega antes de `</head>` en el HTML:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Lighthouse CI

Para monitoreo continuo de performance:

```bash
npm install -g @lhci/cli
lhci autorun --upload.target=temporary-public-storage
```

---

## 🔄 Actualizaciones Futuras

### Actualizar la PWA

1. **Modifica los archivos**
2. **Incrementa la versión del Service Worker**
   ```javascript
   const CACHE_VERSION = 'v2.0.1'; // Cambia aquí
   ```
3. **Commit y push**
   ```bash
   git add .
   git commit -m "Update to v2.0.1"
   git push
   ```
4. **Los usuarios recibirán la actualización automáticamente**

### Forzar Actualización

En el Service Worker, agrega:

```javascript
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_VERSION) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```

---

## 📈 Optimizaciones Adicionales

### Comprimir Archivos

```powershell
# Instalar terser para minificar JS
npm install -g terser

# Minificar service-worker.js
terser service-worker.js -o service-worker.min.js -c -m
```

### Optimizar Imágenes

```powershell
# Instalar imagemin
npm install -g imagemin-cli

# Optimizar iconos
imagemin icon-*.png --out-dir=optimized
```

### Habilitar Compresión

En `netlify.toml`:

```toml
[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000"
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
```

---

## ✅ Deployment Completado

Una vez desplegado, tu PWA estará:
- 🌐 Accesible desde cualquier dispositivo
- 📱 Instalable en iPhone/Android
- ⚡ Funcionando offline
- 🔒 Servida por HTTPS
- 🚀 Lista para producción

**¡Felicidades! Tu Bunker Calculator PRO está en vivo! 🎉**

---

## 📞 Soporte Post-Deployment

Si encuentras problemas:

1. **Verifica la consola del navegador** (F12)
2. **Revisa el Lighthouse report** (DevTools > Lighthouse)
3. **Prueba en modo incógnito** (para evitar caché)
4. **Usa test-pwa.html** para diagnósticos

**URLs útiles:**
- Lighthouse: https://web.dev/measure/
- PWA Builder: https://www.pwabuilder.com/
- Can I Use: https://caniuse.com/serviceworkers