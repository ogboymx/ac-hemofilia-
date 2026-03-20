#!/bin/bash
# Script para probar múltiples endpoints de Kie.ai
# Uso: chmod +x kie_test.sh && ./kie_test.sh

API_KEY="ca3b240edcd9134b47a5d016dd6cccd8"
PROMPT='A mystical flyer design for a holistic waterfall retreat, vertical portrait orientation. Enchanted forest gradient from deep emerald green to teal, ethereal golden light orbs floating. Spiritual atmosphere'

echo "=========================================="
echo "🎨 PROBANDO ENDPOINTS KIE.AI"
echo "=========================================="
echo ""

# Lista de endpoints a probar
endpoints=(
    "https://api.kie.ai/v1/nano-banana"
    "https://api.kie.ai/nano-banana"
    "https://api.kie.ai/v1/generate"
    "https://api.kie.ai/generate"
    "https://api.kie.ai/v1/images"
    "https://api.kie.ai/images"
    "https://api.kie.ai/v1/task"
    "https://api.kie.ai/task"
)

for url in "${endpoints[@]}"; do
    echo ""
    echo "🔄 Probando: $url"
    
    response=$(curl -s -X POST "$url" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $API_KEY" \
        -d "{
            \"model\": \"nano-banana-2\",
            \"prompt\": \"$PROMPT\",
            \"width\": 800,
            \"height\": 1100
        }" 2>&1)
    
    # Verificar si es JSON válido con éxito
    if echo "$response" | grep -q '"url"\|"image_url"\|"task_id"\|"output"'; then
        echo "✅ ÉXITO! Respuesta:"
        echo "$response" | python3 -m json.tool 2>/dev/null || echo "$response"
        echo ""
        echo "💾 Guardando respuesta..."
        echo "$response" > kie_success_response.json
        exit 0
    else
        echo "❌ Falló:"
        echo "$response" | head -c 200
        echo ""
    fi
    
    sleep 1
done

echo ""
echo "=========================================="
echo "❌ NINGÚN ENDPOINT FUNCIONÓ"
echo "=========================================="
echo ""
echo "Recomendación: Usa el playground web en:"
echo "👉 https://kie.ai/market"
echo ""
echo "Y pega este prompt:"
echo 'A mystical flyer design for a holistic waterfall retreat, vertical portrait orientation 800x1100px. Enchanted forest gradient from deep emerald green to teal, ethereal golden light orbs floating. Spiritual atmosphere, gold and green colors'
