# Bunker Calculator PWA - Testing Guide

## 🧪 Guía Completa de Testing

### Pre-requisitos
- ✅ Servidor HTTPS (requerido para PWA)
- ✅ Navegador moderno (Chrome 90+, Safari 14+, Edge 90+)
- ✅ Dispositivo móvil para testing real (opcional pero recomendado)

---

## 1️⃣ Testing Local (Desarrollo)

### Opción A: Python HTTP Server
```bash
# En la carpeta BunkerCal
python -m http.server 8000
```
Abrir: `http://localhost:8000/bunker-calculator%20(1).html`

⚠️ **Nota**: Service Worker solo funciona en localhost o HTTPS

### Opción B: Live Server (VS Code)
1. Instalar extensión "Live Server"
2. Click derecho en `bunker-calculator (1).html`
3. Seleccionar "Open with Live Server"

### Opción C: Node.js http-server
```bash
npx http-server -p 8000
```

---

## 2️⃣ Testing PWA Features

### A. Service Worker Registration

**Test 1: Verificar Registro**
1. Abrir DevTools (F12)
2. Ir a Console
3. Buscar mensaje: `[PWA] Service Worker registered:`
4. ✅ **Esperado**: Mensaje de éxito con scope

**Test 2: Verificar en Application Tab**
1. DevTools → Application → Service Workers
2. ✅ **Esperado**: Ver `service-worker.js` activo
3. ✅ **Esperado**: Status: "activated and is running"

**Test 3: Cache Storage**
1. DevTools → Application → Cache Storage
2. ✅ **Esperado**: Ver cache `bunker-calculator-v2.0.0`
3. ✅ **Esperado**: Archivos cacheados:
   - `bunker-calculator (1).html`
   - `manifest.json`

### B. Manifest Validation

**Test 4: Manifest en DevTools**
1. DevTools → Application → Manifest
2. ✅ **Esperado**: Ver todos los campos:
   - Name: "Bunker Calculator PRO"
   - Short name: "Bunker Calc"
   - Start URL: `./bunker-calculator (1).html`
   - Display: standalone
   - Theme color: #0043ce
   - Icons: 8 iconos listados

**Test 5: Manifest Validator Online**
1. Ir a: https://manifest-validator.appspot.com/
2. Pegar contenido de `manifest.json`
3. ✅ **Esperado**: "Valid manifest"

### C. Install Prompt

**Test 6: Install Prompt (Desktop Chrome)**
1. Abrir en Chrome
2. Buscar icono de instalación en barra de direcciones (⊕)
3. Click en "Install"
4. ✅ **Esperado**: App instalada como aplicación de escritorio

**Test 7: Install Prompt (Mobile)**
1. Abrir en Chrome Android o Safari iOS
2. Buscar banner "Add to Home Screen"
3. Agregar a pantalla de inicio
4. ✅ **Esperado**: Icono en home screen

---

## 3️⃣ Testing Mobile Menu

### Test 8: Botón de Menú Móvil
1. Redimensionar ventana a < 1024px
2. ✅ **Esperado**: Ver botón flotante "☰" abajo a la derecha
3. Click en botón
4. ✅ **Esperado**: Sidebar desliza desde la izquierda
5. ✅ **Esperado**: Overlay oscuro aparece

### Test 9: Cerrar con Overlay
1. Abrir menú móvil
2. Click en overlay (área oscura)
3. ✅ **Esperado**: Menú se cierra
4. ✅ **Esperado**: Overlay desaparece

### Test 10: Cerrar al Seleccionar Item
1. Abrir menú móvil
2. Click en cualquier método de cálculo
3. ✅ **Esperado**: Menú se cierra después de 300ms
4. ✅ **Esperado**: Método seleccionado se activa

### Test 11: Prevención de Scroll
1. Abrir menú móvil
2. Intentar hacer scroll en el contenido principal
3. ✅ **Esperado**: Scroll bloqueado mientras menú abierto
4. Cerrar menú
5. ✅ **Esperado**: Scroll restaurado

---

## 4️⃣ Testing Responsive Design

### Test 12: Breakpoint 1400px
1. Redimensionar a 1400px
2. ✅ **Esperado**: Grid de 3 columnas ajustado
3. ✅ **Esperado**: Sidebar visible (200px)
4. ✅ **Esperado**: Panel derecho visible (300px)

### Test 13: Breakpoint 1024px
1. Redimensionar a 1024px
2. ✅ **Esperado**: Layout de 1 columna
3. ✅ **Esperado**: Sidebar oculto (fixed, left: -280px)
4. ✅ **Esperado**: Botón de menú móvil visible
5. ✅ **Esperado**: Panel derecho abajo del contenido

### Test 14: Breakpoint 768px
1. Redimensionar a 768px
2. ✅ **Esperado**: Padding reducido (12px)
3. ✅ **Esperado**: Font sizes reducidos
4. ✅ **Esperado**: Form grid de 1 columna

### Test 15: Breakpoint 480px
1. Redimensionar a 480px
2. ✅ **Esperado**: Header compacto
3. ✅ **Esperado**: Botones stack verticalmente
4. ✅ **Esperado**: Inputs full width

---

## 5️⃣ Testing Funcionalidad Core

### Test 16: Selección de Método
1. Click en "Tank Sounding Method"
2. ✅ **Esperado**: Título cambia a "Tank Sounding Method (ASTM D1250)"
3. ✅ **Esperado**: Icono cambia a 📏
4. ✅ **Esperado**: Nav item se marca como activo
5. ✅ **Esperado**: Audit trail registra cambio

### Test 17: Cambio de Tabs
1. Click en tab "Properties"
2. ✅ **Esperado**: Tab se activa
3. ✅ **Esperado**: Contenido cambia
4. ✅ **Esperado**: Progress bar actualiza
5. ✅ **Esperado**: Sin errores en console

### Test 18: Cálculo en Tiempo Real
1. Ingresar valores en "Measurement" tab:
   - Sounding: 5.450
   - Temperature: 35.0
2. Ir a "Properties" tab:
   - Fuel Type: VLSFO
3. ✅ **Esperado**: Cálculos se actualizan automáticamente
4. ✅ **Esperado**: Resultados visibles en panel derecho

### Test 19: Tooltips Táctiles
1. Click en icono de ayuda (ⓘ)
2. ✅ **Esperado**: Tooltip aparece
3. Click en otro icono de ayuda
4. ✅ **Esperado**: Tooltip anterior se cierra
5. ✅ **Esperado**: Nuevo tooltip se abre
6. Click fuera de tooltip
7. ✅ **Esperado**: Tooltip se cierra

---

## 6️⃣ Testing Offline Functionality

### Test 20: Modo Offline
1. Abrir aplicación online
2. Esperar a que Service Worker se active
3. DevTools → Network → Throttling → Offline
4. Recargar página (F5)
5. ✅ **Esperado**: Aplicación carga desde cache
6. ✅ **Esperado**: Todas las funciones operativas

### Test 21: Persistencia de Datos
1. Ingresar datos de cálculo
2. Cerrar navegador
3. Reabrir aplicación
4. ✅ **Esperado**: Datos restaurados desde localStorage
5. ✅ **Esperado**: Audit trail preservado

---

## 7️⃣ Testing en Dispositivos Reales

### Test 22: iPhone (Safari)
**Instalación:**
1. Abrir en Safari
2. Tap en botón "Share" (cuadrado con flecha)
3. Scroll y tap "Add to Home Screen"
4. ✅ **Esperado**: Icono agregado a home screen

**Funcionalidad:**
1. Abrir desde home screen
2. ✅ **Esperado**: Abre en modo standalone (sin barra Safari)
3. ✅ **Esperado**: Status bar con theme color
4. ✅ **Esperado**: Safe area respetada (notch)
5. ✅ **Esperado**: Menú móvil funcional
6. ✅ **Esperado**: Touch targets adecuados (44px+)

### Test 23: Android (Chrome)
**Instalación:**
1. Abrir en Chrome
2. Tap en menú (⋮)
3. Tap "Add to Home screen"
4. ✅ **Esperado**: Banner de instalación aparece
5. ✅ **Esperado**: Icono agregado a home screen

**Funcionalidad:**
1. Abrir desde home screen
2. ✅ **Esperado**: Splash screen con icono
3. ✅ **Esperado**: Abre en modo standalone
4. ✅ **Esperado**: Status bar con theme color (#0043ce)
5. ✅ **Esperado**: Todas las funciones operativas

---

## 8️⃣ Testing de Performance

### Test 24: Lighthouse Audit
1. DevTools → Lighthouse
2. Seleccionar:
   - ✅ Performance
   - ✅ Progressive Web App
   - ✅ Best Practices
   - ✅ Accessibility
   - ✅ SEO
3. Click "Generate report"

**Scores Esperados:**
- PWA: 100/100 ✅
- Performance: 90+ ✅
- Accessibility: 90+ ✅
- Best Practices: 90+ ✅

### Test 25: PWA Checklist
1. Lighthouse → PWA
2. ✅ **Esperado**: Todos los checks en verde:
   - ✅ Registers a service worker
   - ✅ Responds with 200 when offline
   - ✅ Has a `<meta name="viewport">` tag
   - ✅ Contains some content when JS unavailable
   - ✅ Provides a valid `apple-touch-icon`
   - ✅ Has a `<meta name="theme-color">` tag
   - ✅ Manifest has name
   - ✅ Manifest has short_name
   - ✅ Manifest has icons
   - ✅ Manifest has start_url
   - ✅ Manifest has display

---

## 9️⃣ Testing de Keyboard Shortcuts

### Test 26: Atajos de Teclado
1. **Ctrl+S / Cmd+S**: Exportar datos
   - ✅ **Esperado**: Descarga archivo JSON
2. **Ctrl+O / Cmd+O**: Importar datos
   - ✅ **Esperado**: Abre selector de archivos
3. **Ctrl+P / Cmd+P**: Generar reporte
   - ✅ **Esperado**: Abre modal de reporte
4. **Ctrl+Enter / Cmd+Enter**: Calcular
   - ✅ **Esperado**: Ejecuta cálculo completo

---

## 🔟 Testing de Compatibilidad

### Test 27: Navegadores Desktop
- [ ] Chrome 90+ (Windows/Mac/Linux)
- [ ] Edge 90+ (Windows/Mac)
- [ ] Firefox 88+ (Windows/Mac/Linux)
- [ ] Safari 14+ (Mac)

### Test 28: Navegadores Mobile
- [ ] Chrome Android 90+
- [ ] Safari iOS 14+
- [ ] Samsung Internet 14+
- [ ] Firefox Android 88+

### Test 29: Dispositivos
- [ ] iPhone 13 Pro (390x844)
- [ ] iPhone SE (375x667)
- [ ] iPad Pro (1024x1366)
- [ ] Samsung Galaxy S21 (360x800)
- [ ] Pixel 5 (393x851)

---

## 🐛 Checklist de Bugs Conocidos (Resueltos)

- [x] ~~Error: `event is not defined` en selectMethod~~ → **RESUELTO**: Parámetro event agregado
- [x] ~~Error: `event is not defined` en switchTab~~ → **RESUELTO**: Parámetro event agregado
- [x] ~~Error: Cannot read property 'style' of null (wedgeSection)~~ → **RESUELTO**: Null check agregado
- [x] ~~Menú móvil no funciona~~ → **RESUELTO**: toggleMobileMenu implementado
- [x] ~~Service Worker no registrado~~ → **RESUELTO**: Registro agregado en DOMContentLoaded
- [x] ~~Overlay no cierra menú~~ → **RESUELTO**: Event listener agregado
- [x] ~~DOMContentLoaded duplicado~~ → **RESUELTO**: Consolidado en uno solo

---

## 📊 Reporte de Testing

### Template de Reporte
```
Fecha: _______________
Tester: _______________
Dispositivo: _______________
Navegador: _______________
Versión: _______________

Tests Pasados: ___/29
Tests Fallados: ___/29
Bugs Encontrados: ___

Notas:
_______________________________
_______________________________
_______________________________
```

---

## 🚀 Deployment Testing

### Test 30: Deploy en GitHub Pages
1. Subir archivos a repositorio
2. Habilitar GitHub Pages
3. Visitar URL: `https://username.github.io/BunkerCal/bunker-calculator%20(1).html`
4. ✅ **Esperado**: HTTPS activo
5. ✅ **Esperado**: PWA instalable
6. ✅ **Esperado**: Service Worker funcional

### Test 31: Deploy en Netlify
1. Drag & drop carpeta en Netlify
2. Visitar URL generada
3. ✅ **Esperado**: HTTPS automático
4. ✅ **Esperado**: PWA instalable
5. ✅ **Esperado**: Performance óptimo

---

## ✅ Criterios de Aceptación

La aplicación está lista para producción cuando:

- ✅ Todos los 31 tests pasan
- ✅ Lighthouse PWA score: 100/100
- ✅ Sin errores en console
- ✅ Funciona offline
- ✅ Instalable en iOS y Android
- ✅ Responsive en todos los breakpoints
- ✅ Touch targets > 44px
- ✅ Cálculos precisos (ASTM D1250)
- ✅ Audit trail completo
- ✅ LocalStorage funcional

---

*Happy Testing! 🧪*