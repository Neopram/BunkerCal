# 🚀 Deploy Bunker Calculator PWA - Quick Guide

## ⚡ Fastest Way to Deploy (5 minutes)

### Option 1: GitHub Pages (Recommended)

#### Step 1: Create Repository
```bash
# En la carpeta BunkerCal
git init
git add .
git commit -m "Initial commit - Bunker Calculator PWA v2.0"
```

#### Step 2: Push to GitHub
```bash
# Crear repositorio en GitHub primero, luego:
git remote add origin https://github.com/YOUR-USERNAME/BunkerCal.git
git branch -M main
git push -u origin main
```

#### Step 3: Enable GitHub Pages
1. Ir a: `https://github.com/YOUR-USERNAME/BunkerCal/settings/pages`
2. Source: **Deploy from a branch**
3. Branch: **main** → **/ (root)**
4. Click **Save**
5. Esperar 1-2 minutos

#### Step 4: Access Your App
```
https://YOUR-USERNAME.github.io/BunkerCal/bunker-calculator%20(1).html
```

✅ **Done!** HTTPS automático, PWA instalable

---

### Option 2: Netlify (Drag & Drop)

#### Step 1: Go to Netlify
1. Visitar: https://app.netlify.com/drop
2. No requiere cuenta (pero recomendado)

#### Step 2: Drag & Drop
1. Seleccionar toda la carpeta `BunkerCal`
2. Arrastrar a la zona de drop
3. Esperar upload (30 segundos)

#### Step 3: Get URL
```
https://random-name-12345.netlify.app/bunker-calculator%20(1).html
```

✅ **Done!** HTTPS automático, CDN global

---

### Option 3: Vercel (CLI)

#### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

#### Step 2: Deploy
```bash
cd BunkerCal
vercel
```

#### Step 3: Follow Prompts
- Set up and deploy? **Y**
- Which scope? **Your account**
- Link to existing project? **N**
- Project name? **bunker-calculator**
- Directory? **./  (current)**

✅ **Done!** URL: `https://bunker-calculator.vercel.app`

---

## 📱 Test Installation on Mobile

### iPhone (Safari)
1. Abrir URL en Safari
2. Tap botón **Share** (cuadrado con flecha)
3. Scroll y tap **"Add to Home Screen"**
4. Tap **"Add"**
5. ✅ Icono aparece en home screen

### Android (Chrome)
1. Abrir URL en Chrome
2. Tap menú (⋮)
3. Tap **"Add to Home screen"**
4. Tap **"Add"**
5. ✅ Icono aparece en home screen

---

## 🔍 Verify PWA Installation

### Check 1: Service Worker
1. Abrir DevTools (F12)
2. Application → Service Workers
3. ✅ Ver: `service-worker.js` activo

### Check 2: Manifest
1. DevTools → Application → Manifest
2. ✅ Ver: Todos los campos completos

### Check 3: Lighthouse
1. DevTools → Lighthouse
2. Select: **Progressive Web App**
3. Click: **Generate report**
4. ✅ Score: 100/100

---

## 🐛 Troubleshooting

### Problem: Service Worker not registering
**Solution**: Verificar que estés en HTTPS (no HTTP)
```
❌ http://example.com  → No funciona
✅ https://example.com → Funciona
✅ http://localhost    → Funciona (excepción)
```

### Problem: Icons not loading
**Solution**: Verificar que todos los archivos icon-*.png estén en la raíz
```bash
# Verificar iconos
ls icon-*.png

# Deberías ver:
icon-16.png   icon-128.png  icon-167.png  icon-384.png
icon-32.png   icon-144.png  icon-180.png  icon-512.png
icon-72.png   icon-152.png  icon-192.png
icon-96.png
```

### Problem: Manifest not found
**Solution**: Verificar que manifest.json esté en la raíz
```bash
# Verificar manifest
cat manifest.json

# Debería mostrar contenido JSON válido
```

### Problem: Can't install on iOS
**Solution**: 
1. Verificar que estés usando **Safari** (no Chrome iOS)
2. Verificar HTTPS activo
3. Verificar que manifest.json y service-worker.js carguen sin errores

### Problem: Offline mode not working
**Solution**:
1. Abrir DevTools → Application → Service Workers
2. Click **"Update"** para forzar actualización
3. Recargar página (Ctrl+Shift+R)
4. Verificar que cache tenga archivos

---

## 📋 Pre-Deployment Checklist

Antes de hacer deploy, verificar:

- [ ] Todos los archivos presentes:
  - [ ] bunker-calculator (1).html
  - [ ] manifest.json
  - [ ] service-worker.js
  - [ ] 12 archivos icon-*.png
  
- [ ] Archivos de documentación (opcionales):
  - [ ] README.md
  - [ ] QUICK-START.md
  - [ ] UPDATE-SUMMARY.md
  - [ ] TESTING-GUIDE.md
  - [ ] CHANGELOG.md
  
- [ ] Testing local:
  - [ ] Abrir en navegador local
  - [ ] Verificar que no haya errores en console
  - [ ] Probar cálculo básico
  - [ ] Verificar menú móvil (resize ventana)

---

## 🎯 Post-Deployment Tasks

Después de hacer deploy:

### 1. Test en Desktop
- [ ] Abrir URL en Chrome
- [ ] Verificar Service Worker registrado
- [ ] Probar instalación (icono en barra de direcciones)
- [ ] Probar offline (DevTools → Network → Offline)

### 2. Test en Mobile
- [ ] Abrir URL en iPhone Safari
- [ ] Instalar en home screen
- [ ] Abrir desde home screen (debe abrir standalone)
- [ ] Probar menú móvil
- [ ] Probar cálculo completo

### 3. Run Lighthouse Audit
- [ ] DevTools → Lighthouse
- [ ] Run audit
- [ ] Verificar PWA score: 100/100
- [ ] Verificar Performance: 90+

### 4. Share with Team
- [ ] Compartir URL
- [ ] Compartir instrucciones de instalación
- [ ] Recopilar feedback

---

## 🔗 Quick Links

### Hosting Platforms
- **GitHub Pages**: https://pages.github.com/
- **Netlify**: https://www.netlify.com/
- **Vercel**: https://vercel.com/
- **Cloudflare Pages**: https://pages.cloudflare.com/

### Testing Tools
- **Lighthouse**: Chrome DevTools → Lighthouse
- **PWA Builder**: https://www.pwabuilder.com/
- **Manifest Validator**: https://manifest-validator.appspot.com/
- **Service Worker Test**: chrome://serviceworker-internals/

### Documentation
- **PWA Docs**: https://web.dev/progressive-web-apps/
- **Service Worker API**: https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
- **Web App Manifest**: https://developer.mozilla.org/en-US/docs/Web/Manifest

---

## 💡 Pro Tips

### Tip 1: Custom Domain
Si tienes un dominio, puedes configurarlo:
- **GitHub Pages**: Settings → Pages → Custom domain
- **Netlify**: Domain settings → Add custom domain
- **Vercel**: Project settings → Domains → Add

### Tip 2: Analytics
Agregar Google Analytics o similar:
```html
<!-- Agregar antes de </head> en bunker-calculator (1).html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Tip 3: Update Strategy
Para actualizar la app:
1. Modificar archivos
2. Cambiar versión en `service-worker.js`:
   ```javascript
   const CACHE_NAME = 'bunker-calculator-v2.0.1'; // Incrementar versión
   ```
3. Commit y push
4. Usuarios recibirán actualización automáticamente

### Tip 4: Performance Monitoring
Usar herramientas como:
- **Lighthouse CI**: Auditorías automáticas en cada deploy
- **WebPageTest**: https://www.webpagetest.org/
- **GTmetrix**: https://gtmetrix.com/

---

## 🎉 Success Criteria

Tu PWA está correctamente desplegada cuando:

✅ URL accesible públicamente  
✅ HTTPS activo (candado verde)  
✅ Service Worker registrado  
✅ Instalable en móviles  
✅ Funciona offline  
✅ Lighthouse PWA: 100/100  
✅ Sin errores en console  
✅ Responsive en todos los tamaños  

---

## 📞 Need Help?

### Common Issues
1. **Service Worker no registra**: Verificar HTTPS
2. **No se puede instalar**: Verificar manifest.json
3. **Iconos no cargan**: Verificar rutas de archivos
4. **Offline no funciona**: Verificar cache en DevTools

### Resources
- Revisar **TESTING-GUIDE.md** para tests detallados
- Revisar **UPDATE-SUMMARY.md** para lista de features
- Usar **validate-pwa.html** para validación automática

---

**¡Listo para producción! 🚀**

*Tiempo estimado de deployment: 5-10 minutos*  
*Dificultad: Fácil ⭐*  
*Costo: Gratis 💰*

---

*Last updated: 2024*  
*Version: 2.0.0*