# Prueba Automatizada con Selenium – Video de MrBeast en YouTube

Este proyecto automatiza la búsqueda, validación y apertura de un video específico en YouTube utilizando Selenium en Python.

## Descripción

El script realiza los siguientes pasos:
1. Abre YouTube en Google Chrome.
2. Busca el video "Ayudé A 2000 Personas A Caminar Otra Vez" de MrBeast.
3. Valida que el título del video y el enlace sean los correctos.
4. Toma una captura de pantalla de los resultados.
5. Abre automáticamente el video si se encontró correctamente.
6. Cierra el navegador luego de unos segundos.

## Requisitos

- Python 3.13
- Google Chrome
- Selenium (`pip install selenium`)
- ChromeDriver compatible con tu navegador

## Archivos del Proyecto

- `youtube_test.py` → Script principal con Selenium
- `HistoriasDeUsuario.md` → Historias de usuario con criterios bien definidos
- `reporte.html` → Reporte HTML con resultados y evidencia visual
- `youtube_result.png` → Captura generada al ejecutar el script

## Ejecución

```bash
pip install selenium
python youtube_test.py
