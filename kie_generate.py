#!/usr/bin/env python3
"""
Script para generar imagen de flyer en Kie.ai
Uso: python3 kie_generate.py
"""

import requests
import json
import time
import sys

# CONFIGURACIÓN
API_KEY = "ca3b240edcd9134b47a5d016dd6cccd8"
PROMPT = """A mystical flyer design for a holistic waterfall retreat, vertical portrait orientation 800x1100px. 
Enchanted forest gradient from deep emerald green (#1a3a2f) at top to teal (#5abaaa) at bottom, 
ethereal golden light orbs floating, soft magical particles like fireflies, subtle mist effect. 
Elegant gold decorative border with Celtic-inspired corners. Spiritual, magical, nature-connected atmosphere. 
No fairies, no elves visible. Modern bohemian, ethereal lighting, premium holistic event aesthetic, 
gold and green color palette with water droplets and leaves."""

NEGATIVE_PROMPT = "fairies, elves, gnomes, dwarves, cartoon, childish, text, letters, typography, words, people, humans"

# ENDPOINTS A PROBAR (por orden de probabilidad)
ENDPOINTS = [
    "https://api.kie.ai/v1/nano-banana",
    "https://api.kie.ai/nano-banana",
    "https://api.kie.ai/v1/generate",
    "https://api.kie.ai/generate",
    "https://api.kie.ai/v1/images",
    "https://api.kie.ai/v1/task",
    "https://api.kie.ai/task",
]

def try_endpoint(url):
    """Intenta un endpoint específico"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "model": "nano-banana-2",
        "prompt": PROMPT,
        "negative_prompt": NEGATIVE_PROMPT,
        "width": 800,
        "height": 1100,
        "num_inference_steps": 30,
        "guidance_scale": 7.5
    }
    
    print(f"\n🔄 Probando: {url}")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print(f"📡 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ ÉXITO! Respuesta: {json.dumps(data, indent=2)}")
            return True, data
        else:
            print(f"❌ Error: {response.text[:200]}")
            return False, None
            
    except Exception as e:
        print(f"❌ Excepción: {e}")
        return False, None

def main():
    print("=" * 60)
    print("🎨 GENERADOR DE FLYER - KIE.AI")
    print("=" * 60)
    print(f"\nPrompt: {PROMPT[:100]}...")
    
    # Probar todos los endpoints
    for endpoint in ENDPOINTS:
        success, data = try_endpoint(endpoint)
        if success:
            print("\n" + "=" * 60)
            print("✅ IMAGEN GENERADA!")
            print("=" * 60)
            
            # Guardar respuesta
            with open("kie_response.json", "w") as f:
                json.dump(data, f, indent=2)
            print("\n💾 Respuesta guardada en: kie_response.json")
            
            # Si hay URL de imagen, descargarla
            if "url" in data or "image_url" in data or "output" in data:
                image_url = data.get("url") or data.get("image_url") or data.get("output")
                if image_url:
                    print(f"\n🖼️ Descargando imagen desde: {image_url}")
                    img_response = requests.get(image_url, timeout=30)
                    if img_response.status_code == 200:
                        filename = "flyer_cascadas.png"
                        with open(filename, "wb") as f:
                            f.write(img_response.content)
                        print(f"✅ Imagen guardada como: {filename}")
            
            # Si es async con task_id, hacer polling
            if "task_id" in data:
                task_id = data["task_id"]
                print(f"\n⏳ Tarea async creada: {task_id}")
                print("Haciendo polling... (esto puede tardar 30-60 segundos)")
                
                query_url = endpoint.replace("/generate", "/query").replace("/task", "/query")
                for i in range(30):  # 30 intentos = ~60 segundos
                    time.sleep(2)
                    query_response = requests.post(
                        query_url,
                        headers=headers,
                        json={"task_id": task_id},
                        timeout=10
                    )
                    if query_response.status_code == 200:
                        result = query_response.json()
                        status = result.get("status", "unknown")
                        print(f"  Intento {i+1}: {status}")
                        
                        if status == "completed" or status == "success":
                            print(f"\n✅ COMPLETADO!")
                            print(json.dumps(result, indent=2))
                            break
                        elif status == "failed":
                            print(f"\n❌ Falló: {result}")
                            break
            
            return
        
        time.sleep(1)  # Esperar entre intentos
    
    print("\n" + "=" * 60)
    print("❌ NINGÚN ENDPOINT FUNCIONÓ")
    print("=" * 60)
    print("\nSugerencias:")
    print("1. Verifica que tu API key sea correcta en https://kie.ai/api-key")
    print("2. Revisa la documentación actualizada en https://docs.kie.ai")
    print("3. Intenta generar desde el playground web: https://kie.ai/market")

if __name__ == "__main__":
    main()
