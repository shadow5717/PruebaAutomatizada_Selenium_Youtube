# Historias de Usuario – Prueba Automatizada (YouTube - MrBeast)

## Historia 1: Búsqueda del video específico
**Como** estudiante, **quiero** buscar el video "Ayudé A 2000 Personas A Caminar Otra Vez" en YouTube, **para** validar que el sistema puede localizar contenido exacto.

- Criterios de Aceptación:
  - El título encontrado contiene la frase específica.
- Criterios de Rechazo:
  - Se encuentra un video diferente o el título es incorrecto.

## Historia 2: Validación del enlace oficial
**Como** usuario, **quiero** validar que el enlace contiene el ID `"SM66GDRyIVY"`, **para** confirmar que se trata del video original de MrBeast.

- Criterios de Aceptación:
  - El enlace del video es el oficial.
- Criterios de Rechazo:
  - El enlace lleva a un video distinto.

## Historia 3: Captura automática como evidencia
**Como** tester, **quiero** que el script tome una captura de los resultados, **para** documentar el comportamiento de la prueba.

- Criterios de Aceptación:
  - Se genera el archivo `youtube_result.png`.
- Criterios de Rechazo:
  - La imagen no se crea o está vacía.

## Historia 4: Estabilidad y ejecución sin errores
**Como** supervisor, **quiero** asegurarme de que el script se ejecute sin errores, **para** confirmar la fiabilidad del sistema.

- Criterios de Aceptación:
  - El script se ejecuta de principio a fin sin errores.
- Criterios de Rechazo:
  - Ocurre un fallo o excepción.

## Historia 5: Autonomía completa del proceso
**Como** estudiante, **quiero** que la prueba funcione sin intervención manual, **para** garantizar su ejecución automática.

- Criterios de Aceptación:
  - El script se ejecuta y cierra sin requerir input.
- Criterios de Rechazo:
  - Se necesita pulsar teclas o responder durante la prueba.

## Historia 6: Espera inteligente de elementos
**Como** programador, **quiero** que el script espere a que se cargue el contenido antes de acceder a los resultados, **para** evitar errores de sincronización.

- Criterios de Aceptación:
  - Se utiliza `WebDriverWait` para manejar elementos dinámicos.
- Criterios de Rechazo:
  - El script falla por elementos que no han cargado.

## Historia 7: Reproducción automática del video
**Como** estudiante, **quiero** que al encontrar el video, este se abra automáticamente, **para** verificar que el enlace redirige correctamente al contenido buscado.

- Criterios de Aceptación:
  - El video se abre en el navegador luego de la validación.
- Criterios de Rechazo:
  - El video no se abre aunque fue encontrado correctamente.
