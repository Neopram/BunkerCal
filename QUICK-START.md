# ⚡ Quick Start Guide - Bunker Calculator PRO v2.0

## 🚀 Inicio Rápido (5 minutos)

### Opción 1: Testing Local Inmediato

```powershell
# 1. Abrir terminal en la carpeta del proyecto
cd c:\Users\feder\Desktop\BunkerCalcPRO

# 2. Iniciar servidor local
python -m http.server 8000

# 3. Abrir en navegador
# http://localhost:8000/bunker-calculator%20(1).html
```

### Opción 2: Verificar PWA

```powershell
# Abrir página de pruebas
# http://localhost:8000/test-pwa.html
```

---

## 📱 Instalar en iPhone 13 Pro (3 pasos)

1. **Abrir en Safari** → `http://tu-url/bunker-calculator (1).html`
2. **Tap Share** (icono cuadrado con flecha) → **Add to Home Screen**
3. **Tap Add** → ¡Listo! Busca el icono azul "BC"

---

## 🌐 Deploy a Internet (GitHub Pages - GRATIS)

```bash
# 1. Inicializar Git
git init
git add .
git commit -m "Initial commit"

# 2. Crear repo en GitHub.com
# Nombre sugerido: bunker-calculator-pro

# 3. Subir código (reemplaza TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/bunker-calculator-pro.git
git branch -M main
git push -u origin main

# 4. Activar GitHub Pages
# Settings → Pages → Source: main branch → Save

# 5. Tu app estará en:
# https://TU-USUARIO.github.io/bunker-calculator-pro/bunker-calculator%20(1).html
```

---

## ✅ Verificación Rápida

### ¿Funciona correctamente?

Abre la consola del navegador (F12) y verifica:

```javascript
// ✅ Service Worker registrado
navigator.serviceWorker.getRegistration().then(reg => {
    console.log('SW:', reg ? '✅ Active' : '❌ Not found');
});

// ✅ Manifest cargado
fetch('manifest.json').then(r => {
    console.log('Manifest:', r.ok ? '✅ Found' : '❌ Not found');
});

// ✅ Iconos disponibles
fetch('icon-192.png').then(r => {
    console.log('Icons:', r.ok ? '✅ Found' : '❌ Not found');
});
```

### Checklist Visual

- [ ] La página carga sin errores
- [ ] El menú hamburguesa (☰) aparece en móvil
- [ ] Los cálculos funcionan
- [ ] No hay errores en consola (F12)
- [ ] Los iconos se ven correctamente

---

## 🐛 Problemas Comunes

### "Service Worker no se registra"
**Solución:** Usa HTTPS o localhost (no `file://`)

### "No puedo instalar en iPhone"
**Solución:** Usa Safari (no Chrome en iOS)

### "El menú móvil no aparece"
**Solución:** Reduce el ancho de ventana a < 1024px

### "Los iconos no cargan"
**Solución:** Ejecuta `python generate-icons.py`

---

## 📚 Documentación Completa

- **README.md** → Guía completa de usuario
- **deploy.md** → Instrucciones de deployment detalladas
- **PROJECT-SUMMARY.md** → Resumen técnico del proyecto
- **test-pwa.html** → Suite de diagnóstico

---

## 🎯 Próximos Pasos

1. ✅ **Testing Local** → Verifica que todo funciona
2. ✅ **Deploy a GitHub Pages** → Hazlo público
3. ✅ **Instalar en iPhone** → Prueba la experiencia PWA
4. ✅ **Compartir** → Envía el link a usuarios

---

## 💡 Tips Útiles

### Regenerar Iconos
```powershell
python generate-icons.py
```

### Actualizar Caché (después de cambios)
```javascript
// En service-worker.js, cambia:
const CACHE_VERSION = 'v2.0.1'; // Incrementa versión
```

### Ver Logs del Service Worker
```
Chrome DevTools → Application → Service Workers
```

---

## 🎉 ¡Listo!

Tu **Bunker Calculator PRO** está completamente configurado y listo para usar.

**¿Necesitas ayuda?** Consulta los archivos de documentación en la carpeta del proyecto.

---

**Bunker Calculator PRO v2.0** | Progressive Web App