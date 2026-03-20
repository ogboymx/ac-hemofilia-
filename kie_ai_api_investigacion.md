# Investigación API de Kie.ai - Generación de Imágenes

> **Fecha de investigación:** 2026-03-07  
> **API Key proporcionada:** `ca3b240edcd9134b47a5d016dd6cccd8`

---

## 📋 RESUMEN EJECUTIVO

**¡La API de Kie.ai SÍ existe y funciona!** El problema con los endpoints `/v1/images/generations` y similares es que **Kie.ai usa una estructura de endpoints diferente** a la API estándar de OpenAI.

Kie.ai opera con:
1. **Endpoint unificado para modelos Market**: `/api/v1/jobs/createTask`
2. **Endpoints específicos para ciertos modelos** (como GPT-4o Image): `/api/v1/gpt4o-image/generate`
3. **Endpoint unificado para consultar estado**: `/api/v1/jobs/recordInfo`

---

## 🔗 URL BASE CORRECTA

```
https://api.kie.ai
```

**Nota:** No usar `api.kie.ai/v1` ni `kie.ai/api/v1` - la estructura correcta es `api.kie.ai/api/v1/...`

---

## 🔐 HEADERS REQUERIDOS

Todos los requests deben incluir:

```http
Authorization: Bearer <TU_API_KEY>
Content-Type: application/json
```

**Ejemplo con tu API key:**
```http
Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8
Content-Type: application/json
```

---

## 📡 ENDPOINTS PRINCIPALES

### 1. Crear Tarea (Endpoint Unificado - Market Models)

Para la mayoría de modelos (Seedream, Nano Banana, Flux, etc.):

```http
POST https://api.kie.ai/api/v1/jobs/createTask
```

**Ejemplo para Nano Banana 2:**
```bash
curl --location --request POST 'https://api.kie.ai/api/v1/jobs/createTask' \
--header 'Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8' \
--header 'Content-Type: application/json' \
--data-raw '{
  "model": "nano-banana-2",
  "callBackUrl": "https://your-domain.com/api/callback",
  "input": {
    "prompt": "Comic poster: cool banana hero in shades leaps from sci-fi pad...",
    "image_input": [],
    "google_search": true,
    "aspect_ratio": "auto",
    "resolution": "1K",
    "output_format": "png"
  }
}'
```

**Modelos disponibles via endpoint unificado:**
- `nano-banana-2` (Google Nano Banana 2)
- `google/nano-banana-edit` (Para edición de imágenes)
- `seedream-4.0`, `seedream-v4-text-to-image` (ByteDance Seedream)
- `flux-kontext-pro`, `flux-kontext-max` (Flux Kontext)
- `grok-imagine/text-to-image` (Grok Imagine)
- Y muchos más en https://kie.ai/market

---

### 2. GPT-4o Image / GPT Image 1 (Endpoint Específico)

Este modelo tiene su propio endpoint:

```http
POST https://api.kie.ai/api/v1/gpt4o-image/generate
```

**Ejemplo:**
```bash
curl --location --request POST 'https://api.kie.ai/api/v1/gpt4o-image/generate' \
--header 'Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8' \
--header 'Content-Type: application/json' \
--data-raw '{
  "prompt": "A beautiful sunset over the mountains",
  "size": "1:1",
  "nVariants": 2,
  "isEnhance": true,
  "enableFallback": true,
  "fallbackModel": "FLUX_MAX",
  "callBackUrl": "https://your-callback-url.com/callback"
}'
```

**Parámetros para GPT-4o Image:**
- `prompt` (string): Descripción de la imagen a generar
- `size` (string): Relación de aspecto - opciones: `1:1`, `3:2`, `2:3`
- `filesUrl` (array): URLs de imágenes de referencia (para image-to-image)
- `maskUrl` (string): URL de máscara para edición precisa
- `nVariants` (integer): Número de variaciones a generar
- `isEnhance` (boolean): Mejora de prompt automática
- `enableFallback` (boolean): Usar modelo fallback si el principal falla
- `fallbackModel` (string): `FLUX_MAX` o `GPT_IMAGE_1`
- `callBackUrl` (string): URL para recibir notificación cuando termine

**Consultar estado de tarea GPT-4o:**
```http
GET https://api.kie.ai/api/v1/gpt4o-image/record-info?taskId={taskId}
```

---

### 3. Consultar Estado de Tarea (Unificado)

Para todos los modelos Market (excepto GPT-4o que tiene el suyo propio):

```http
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId={taskId}
```

**Ejemplo:**
```bash
curl --location --request GET 'https://api.kie.ai/api/v1/jobs/recordInfo?taskId=task_12345678' \
--header 'Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8'
```

**Respuesta:**
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "taskId": "task_12345678",
    "model": "nano-banana-2",
    "state": "success",
    "param": "{\"model\":\"nano-banana-2\",...}",
    "resultJson": "{\"resultUrls\":[\"https://example.com/generated-content.jpg\"]}",
    "failCode": "",
    "failMsg": "",
    "costTime": 15000,
    "completeTime": 1698765432000,
    "createTime": 1698765400000,
    "updateTime": 1698765432000
  }
}
```

**Estados posibles:**
- `waiting` - Esperando en cola
- `queuing` - En cola de procesamiento
- `generating` - Generando contenido
- `success` - Completado exitosamente
- `fail` - Falló

---

### 4. Consultar Créditos Disponibles

```http
GET https://api.kie.ai/api/v1/user/credits
```

**Ejemplo:**
```bash
curl --location --request GET 'https://api.kie.ai/api/v1/user/credits' \
--header 'Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8'
```

---

### 5. Obtener URL de Descarga

Las URLs de contenido generado expiran. Para obtener una URL descargable:

```http
POST https://api.kie.ai/api/v1/common/download-url
```

**Ejemplo:**
```bash
curl -X POST "https://api.kie.ai/api/v1/common/download-url" \
  -H "Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://tempfile.1f6cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxbd98"
  }'
```

---

## 💻 EJEMPLOS DE CÓDIGO

### Python - Clase Completa para GPT-4o Image

```python
import requests
import time

class KieAIGPT4oImage:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.kie.ai/api/v1/gpt4o-image'
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def generate_image(self, prompt, size='1:1', n_variants=1, **options):
        """
        Genera una imagen usando GPT-4o Image
        
        Args:
            prompt: Descripción de la imagen
            size: Relación de aspecto ('1:1', '3:2', '2:3')
            n_variants: Número de variaciones
            **options: Parámetros adicionales
        """
        payload = {
            'prompt': prompt,
            'size': size,
            'nVariants': n_variants,
            **options
        }
        
        response = requests.post(
            f'{self.base_url}/generate',
            headers=self.headers,
            json=payload
        )
        result = response.json()
        
        if result.get('code') != 200:
            raise Exception(f"Error: {result.get('msg')}")
        
        return result['data']['taskId']

    def get_task_status(self, task_id):
        """Obtiene el estado de una tarea"""
        response = requests.get(
            f'{self.base_url}/record-info?taskId={task_id}',
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        result = response.json()
        
        if result.get('code') != 200:
            raise Exception(f"Error: {result.get('msg')}")
        
        return result['data']

    def wait_for_completion(self, task_id, max_wait_time=300, poll_interval=5):
        """
        Espera a que una tarea se complete
        
        Args:
            task_id: ID de la tarea
            max_wait_time: Tiempo máximo de espera en segundos
            poll_interval: Intervalo entre consultas en segundos
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            status = self.get_task_status(task_id)
            state = status.get('successFlag')
            
            if state == 1:
                print("✅ Generación completada!")
                return status['response']
            elif state == 0:
                print("⏳ Generando...")
                if status.get('progress'):
                    print(f"   Progreso: {float(status['progress']) * 100:.1f}%")
            elif state == 2:
                error = status.get('errorMessage', 'Generación fallida')
                raise Exception(f"❌ Error: {error}")
            
            time.sleep(poll_interval)
        
        raise Exception("⏱️ Timeout esperando resultados")

    def download_image(self, image_url):
        """Obtiene URL de descarga para una imagen"""
        response = requests.post(
            f'{self.base_url}/download-url',
            headers=self.headers,
            json={'imageUrl': image_url}
        )
        result = response.json()
        
        if result.get('code') != 200:
            raise Exception(f"Error: {result.get('msg')}")
        
        return result['data']['downloadUrl']


# Uso del API
if __name__ == '__main__':
    # Inicializar con tu API key
    api = KieAIGPT4oImage('ca3b240edcd9134b47a5d016dd6cccd8')
    
    try:
        # Generar imagen
        print("🎨 Generando imagen...")
        task_id = api.generate_image(
            prompt='A futuristic cityscape with flying cars and neon lights, cyberpunk style',
            size='1:1',
            n_variants=2,
            isEnhance=True
        )
        print(f"📝 Task ID: {task_id}")
        
        # Esperar resultados
        result = api.wait_for_completion(task_id)
        
        # Mostrar URLs de imágenes generadas
        print("\n🖼️ Imágenes generadas:")
        for i, url in enumerate(result['result_urls'], 1):
            print(f"   {i}. {url}")
        
        # Obtener URL de descarga
        download_url = api.download_image(result['result_urls'][0])
        print(f"\n⬇️ URL de descarga: {download_url}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
```

---

### Python - Clase Unificada para Market Models (Nano Banana, Seedream, etc.)

```python
import requests
import time
import json

class KieAIMarketAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.kie.ai/api/v1'
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def create_task(self, model, input_params, callback_url=None):
        """
        Crea una tarea de generación
        
        Args:
            model: Nombre del modelo (ej: 'nano-banana-2', 'seedream-4.0')
            input_params: Diccionario con parámetros de entrada
            callback_url: URL opcional para recibir notificación
        """
        payload = {
            'model': model,
            'input': input_params
        }
        
        if callback_url:
            payload['callBackUrl'] = callback_url
        
        response = requests.post(
            f'{self.base_url}/jobs/createTask',
            headers=self.headers,
            json=payload
        )
        result = response.json()
        
        if result.get('code') != 200:
            raise Exception(f"Error creando tarea: {result.get('msg')}")
        
        return result['data']['taskId']

    def get_task_status(self, task_id):
        """Obtiene el estado de una tarea"""
        response = requests.get(
            f'{self.base_url}/jobs/recordInfo?taskId={task_id}',
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        result = response.json()
        
        if result.get('code') != 200:
            raise Exception(f"Error consultando estado: {result.get('msg')}")
        
        return result['data']

    def wait_for_completion(self, task_id, max_wait_time=600, poll_interval=5):
        """Espera a que una tarea se complete"""
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            status = self.get_task_status(task_id)
            state = status.get('state')
            
            if state == 'success':
                print("✅ Tarea completada!")
                result_json = status.get('resultJson', '{}')
                return json.loads(result_json)
            elif state == 'fail':
                error = status.get('failMsg', 'Tarea fallida')
                raise Exception(f"❌ Error: {error}")
            elif state in ['waiting', 'queuing', 'generating']:
                print(f"⏳ Estado: {state}")
            
            time.sleep(poll_interval)
        
        raise Exception("⏱️ Timeout esperando resultados")

    def get_credits(self):
        """Obtiene créditos disponibles"""
        response = requests.get(
            f'{self.base_url}/user/credits',
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        result = response.json()
        
        if result.get('code') != 200:
            raise Exception(f"Error: {result.get('msg')}")
        
        return result['data']

    def get_download_url(self, file_url):
        """Obtiene URL de descarga para un archivo"""
        response = requests.post(
            f'{self.base_url}/common/download-url',
            headers=self.headers,
            json={'url': file_url}
        )
        result = response.json()
        
        if result.get('code') != 200:
            raise Exception(f"Error: {result.get('msg')}")
        
        return result['data']


# Ejemplos de uso
if __name__ == '__main__':
    api = KieAIMarketAPI('ca3b240edcd9134b47a5d016dd6cccd8')
    
    # Ver créditos disponibles
    try:
        credits = api.get_credits()
        print(f"💰 Créditos disponibles: {credits}")
    except Exception as e:
        print(f"No se pudieron obtener créditos: {e}")
    
    # Ejemplo 1: Generar con Nano Banana 2
    try:
        print("\n🎨 Generando con Nano Banana 2...")
        task_id = api.create_task(
            model='nano-banana-2',
            input_params={
                'prompt': 'A cute robot playing guitar in a cyberpunk city',
                'aspect_ratio': '1:1',
                'resolution': '1K',
                'output_format': 'png'
            }
        )
        print(f"📝 Task ID: {task_id}")
        
        result = api.wait_for_completion(task_id)
        print(f"🖼️ Resultados: {result}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Ejemplo 2: Generar con Flux Kontext Pro
    try:
        print("\n🎨 Generando con Flux Kontext Pro...")
        task_id = api.create_task(
            model='flux-kontext-pro',
            input_params={
                'prompt': 'An astronaut riding a horse in space, digital art',
                'aspectRatio': '16:9',
                'outputFormat': 'png'
            }
        )
        print(f"📝 Task ID: {task_id}")
        
        result = api.wait_for_completion(task_id)
        print(f"🖼️ Resultados: {result}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
```

---

### JavaScript/Node.js

```javascript
class KieAIAPI {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://api.kie.ai/api/v1';
  }

  async generateImage(model, inputParams, callbackUrl = null) {
    const payload = {
      model,
      input: inputParams
    };
    
    if (callbackUrl) {
      payload.callBackUrl = callbackUrl;
    }

    const response = await fetch(`${this.baseUrl}/jobs/createTask`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const result = await response.json();
    
    if (result.code !== 200) {
      throw new Error(`Error: ${result.msg}`);
    }
    
    return result.data.taskId;
  }

  async getTaskStatus(taskId) {
    const response = await fetch(
      `${this.baseUrl}/jobs/recordInfo?taskId=${taskId}`,
      {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`
        }
      }
    );

    const result = await response.json();
    
    if (result.code !== 200) {
      throw new Error(`Error: ${result.msg}`);
    }
    
    return result.data;
  }

  async waitForCompletion(taskId, maxWaitTime = 600000, pollInterval = 5000) {
    const startTime = Date.now();
    
    while (Date.now() - startTime < maxWaitTime) {
      const status = await this.getTaskStatus(taskId);
      
      switch (status.state) {
        case 'success':
          console.log('✅ Tarea completada!');
          return JSON.parse(status.resultJson);
        case 'fail':
          throw new Error(`❌ Error: ${status.failMsg}`);
        case 'waiting':
        case 'queuing':
        case 'generating':
          console.log(`⏳ Estado: ${status.state}`);
          break;
      }
      
      await new Promise(resolve => setTimeout(resolve, pollInterval));
    }
    
    throw new Error('⏱️ Timeout esperando resultados');
  }
}

// Uso
async function main() {
  const api = new KieAIAPI('ca3b240edcd9134b47a5d016dd6cccd8');
  
  try {
    // Generar imagen
    const taskId = await api.generateImage(
      'nano-banana-2',
      {
        prompt: 'A beautiful landscape with mountains and sunset',
        aspect_ratio: '16:9',
        resolution: '2K',
        output_format: 'png'
      }
    );
    
    console.log(`Task ID: ${taskId}`);
    
    // Esperar resultado
    const result = await api.waitForCompletion(taskId);
    console.log('Resultados:', result);
    
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```

---

## 📊 CÓDIGOS DE RESPUESTA

| Código | Descripción | Solución |
|--------|-------------|----------|
| 200 | Éxito | - |
| 401 | No autorizado | Verificar API key en header `Authorization: Bearer <key>` |
| 402 | Créditos insuficientes | Recargar créditos en https://kie.ai/pricing |
| 404 | Recurso no encontrado | Verificar URL del endpoint |
| 422 | Error de validación | Revisar parámetros enviados |
| 429 | Rate limit excedido | Implementar backoff entre requests |
| 455 | Servicio en mantenimiento | Esperar y reintentar |
| 500 | Error del servidor | Reintentar después de unos minutos |
| 501 | Generación fallida | Revisar mensaje de error específico |
| 505 | Función deshabilitada | Contactar soporte |

---

## ⚠️ NOTAS IMPORTANTES

### 1. Tareas Asíncronas
Todas las generaciones en Kie.ai son **asíncronas**. Un response 200 solo significa que la tarea fue creada exitosamente, no que está completa.

### 2. Ciclo de Vida de URLs
- **Imágenes generadas**: Almacenadas por 14 días, luego eliminadas
- **Registros de logs**: Almacenados por 2 meses
- **URLs de descarga**: Expiran después de 20 minutos

### 3. Rate Limits
- **Creación de tareas**: Máximo 20 requests por 10 segundos
- **Consulta de estado**: Máximo 10 requests por segundo
- Se recomienda intervalo de 2-5 segundos entre polls

### 4. Callbacks (Webhooks)
Para producción, se recomienda usar `callBackUrl` en lugar de polling:

```python
# El callback recibe un POST con:
{
  "code": 200,
  "data": {
    "taskId": "task_123456",
    "state": "success",
    "resultJson": "{\"resultUrls\":[\"https://...\"]}"
  }
}
```

### 5. Modelos de Fallback (GPT-4o Image)
Para mayor confiabilidad, habilitar fallback:

```json
{
  "prompt": "...",
  "enableFallback": true,
  "fallbackModel": "FLUX_MAX"
}
```

---

## 🔧 LISTA DE MODELOS DISPONIBLES

Consultar https://kie.ai/market para la lista actualizada. Algunos populares:

### Image Models
- **Google Nano Banana 2**: `nano-banana-2`
- **Google Nano Banana Edit**: `google/nano-banana-edit`
- **ByteDance Seedream 4.0**: `seedream-4.0`
- **Flux Kontext Pro**: `flux-kontext-pro`
- **Flux Kontext Max**: `flux-kontext-max`
- **GPT-4o Image / GPT Image 1**: Usa endpoint específico `/api/v1/gpt4o-image/generate`
- **Grok Imagine**: `grok-imagine/text-to-image`
- **Ideogram**: Varios modelos disponibles
- **Recraft**: Varios modelos disponibles
- **Qwen Image**: Varios modelos disponibles

### Video Models
- **Kling**: Varias versiones
- **Veo 3.1**: Google Veo
- **Runway**: Varias versiones
- **Sora 2**: OpenAI Sora
- **Wan 2.6**: Alibaba Wan
- **Seedance**: ByteDance

---

## 📚 RECURSOS ADICIONALES

- **Documentación oficial**: https://docs.kie.ai
- **Market/Modelos**: https://kie.ai/market
- **Gestión de API Keys**: https://kie.ai/api-key
- **Logs y tareas**: https://kie.ai/logs
- **Soporte**: support@kie.ai
- **Discord/Telegram**: Accesible desde el dashboard

---

## ✅ CHECKLIST PARA INTEGRACIÓN

- [ ] Confirmar que la API key es válida (`GET /api/v1/user/credits`)
- [ ] Elegir el modelo correcto y su endpoint correspondiente
- [ ] Implementar manejo de errores para cada código de respuesta
- [ ] Implementar polling o callback para obtener resultados
- [ ] Descargar imágenes inmediatamente (URLs expiran en 14 días)
- [ ] Implementar rate limiting en el cliente
- [ ] Para producción, usar callbacks en lugar de polling

---

## 🚀 PROBANDO LA API

Test rápido con curl:

```bash
# Verificar créditos
curl -H "Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8" \
  https://api.kie.ai/api/v1/user/credits

# Crear tarea de prueba
curl -X POST https://api.kie.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer ca3b240edcd9134b47a5d016dd6cccd8" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nano-banana-2",
    "input": {
      "prompt": "A cute cat wearing a hat",
      "aspect_ratio": "1:1",
      "resolution": "1K"
    }
  }'
```

---

*Documento generado el 2026-03-07. La información puede cambiar; siempre consultar docs.kie.ai para la documentación más actualizada.*
