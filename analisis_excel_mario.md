# 📊 Análisis del Archivo Excel - Sistema de Inventario y Ventas

**Archivo analizado:** `19cc5874-a4c2-88ae-8000-0000c80c6897_inve.xlsx`  
**Negocio:** Cerveza Old Rasputin (North Coast Brewing) + Knee Deep Brewing  
**Fecha de análisis:** Marzo 2026

---

## 📋 Resumen de Hojas Encontradas

| Hoja | Nombre | Estado | Descripción |
|------|--------|--------|-------------|
| 1 | Sheet1 | ⚠️ VACÍA | Hoja por defecto sin utilizar |
| 2 | ventas | ✅ ACTIVA | Registro de ventas a clientes |
| 3 | lista de marzo junio 2026 | ✅ ACTIVA | Lista de precios de productos |

**Total de hojas:** 3  
**Hojas útiles:** 2  
**Hojas vacías/innecesarias:** 1

---

## 🔍 Análisis Detallado por Hoja

### Hoja 1: Sheet1

**Estado:** ⚠️ **VACÍA - Debe eliminarse**

- **Dimensiones:** 0 filas × 0 columnas
- **Problema:** Es la hoja por defecto de Excel que no se utilizó
- **Recomendación:** Eliminar esta hoja para mantener el archivo limpio

---

### Hoja 2: "ventas "

**Estado:** ⚠️ **NECESITA REORGANIZACIÓN URGENTE**

#### Estructura Actual
- **Dimensiones:** 102 filas × 35 columnas
- **Datos útiles:** Aproximadamente 30% de las celdas contienen datos
- **Problema principal:** Estructura horizontal poco práctica

#### Columnas Identificadas

**Columnas de Productos (Precios Unitarios):**
| Columna | Descripción | Datos |
|---------|-------------|-------|
| RASPUTIN 355 ML | Precio botella 355ml | $85 |
| RASPUTIN LATA | Precio lata | $106 |
| BROTHER TH | Brother Thelonious | $93 |
| OLD STOCK | Old Stock Ale | $98 |
| BERLINER | Berliner Weisse | $75 |
| LEMERLE | Le Merle Saison | $80 |
| RED ALE | Red Seal Ale | $70 |
| PRANQSTER | Pranqster | $80 |
| BARRILES | Precio barriles | Variable |
| KNEEDEEP | Productos Knee Deep | Variable |

**Columnas Duplicadas (versión .1):**
- `RASPUTIN 355 ML .1`, `RASPUTIN LATA .1`, etc.
- **Problema:** Parecen ser columnas de totales o cálculos secundarios

**Columnas de Clientes:**
- `Unnamed: 0` - Contiene los nombres de los clientes
- Se identificaron **~30 clientes únicos**

**Clientes principales encontrados:**
1. EUROCERVEZAS
2. LA ESPUMA
3. PLAZA GRILLE
4. CALACAS
5. BEER BOSS
6. BEER MINDS
7. LA TREGUA
8. FRITZ
9. beer bank
10. circo volador
11. LA VACA
12. CRAFT GALAXY
13. VENTURA B

**Columnas de Control:**
- `DESCUENTO` - Porcentaje de descuento aplicado
- `TOTAL` - Monto total de la venta
- `ESTILO` - Tipo de registro (PZ=piezas, CANTIDAD)
- Columnas `Unnamed: 14-22` - Estado de pago (PAID)

**Columnas de Gastos (derecha):**
- `GASTOS` - Categoría de gasto
- `Unnamed: 34` - Monto del gasto

**Gastos identificados:**
- ABUELITA: $5,500
- EURO CERVEZAS: $5,400
- PAPA: $2,620, $5,000
- MONASTERIO: $2,850, $4,200
- MULTA AZUL: $2,050
- VERIFICACION: $1,750

#### Problemas Encontrados

| Problema | Severidad | Descripción |
|----------|-----------|-------------|
| Columnas sin nombre | 🔴 Alta | 21 columnas se llaman "Unnamed: X" |
| Estructura horizontal | 🔴 Alta | Productos como columnas dificultan análisis |
| Columnas vacías | 🟡 Media | 8 columnas completamente vacías |
| Nombres con espacios | 🟡 Media | "ventas " (con espacio al final) |
| Datos duplicados | 🟡 Media | 24 filas duplicadas |
| Mezcla de ventas y gastos | 🔴 Alta | Dos tipos de datos en una hoja |
| Formatos inconsistentes | 🟡 Media | Algunos precios en diferentes columnas |

---

### Hoja 3: "lista de marzo junio 2026 "

**Estado:** ⚠️ **NECESITA REESTRUCTURACIÓN**

#### Estructura Actual
- **Dimensiones:** 69 filas × 10 columnas
- **Contenido:** Lista de precios de cervezas (envases y barriles)
- **Problema principal:** Columnas sin nombre, estructura poco clara

#### Contenido Identificado

**Sección 1: Cervezas Knee Deep Brewing (Botellas/Latas)**

| Producto | ML | Precio Unitario | 15% Descuento |
|----------|-----|-----------------|---------------|
| SIMTRA TRIPLE IPA | 473 ML | $185 | $157.25 |
| SLOOOWMO IPA | 355 ML | $70 | $59.50 |
| SLOOOWMO IPA | 564 ML | $130 | $110.50 |
| HOPTOLOGIST DOBLE IPA | 473 ML | $138 | $117.30 |
| HOLA SR LAGER | 355 ML | $49 | - |
| TAHOE DEEP IMPERIAL IPA | 473 ML | $138 | $117.30 |
| BREAKING BUD IPA | 473 ML | $138 | $117.30 |
| POCKET ROCKET IPA | 750 ML | $800 | $680 |
| FOLSOME HAZE | 473 ML | $98 | $83.30 |
| DEEP CLARITY | 355 ML | $70 | $59.50 |
| DEEP ISLAND | 355 ML | $70 | $59.50 |

**Sección 2: Cervezas North Coast (Botellas/Latas)**

| Producto | ML | Precio Unitario | 15% Descuento |
|----------|-----|-----------------|---------------|
| OLD RASPUTIN | 473 ML | $106 | $90.10 |
| OLD RASPUTIN | 355 ML | $85 | $72.25 |
| BROTHER THELONIOUS | 355 ML | $93 | $79.05 |
| OLD STOCK 2025 | 355 ML | $98 | $83.30 |
| CHERRY TART BERLINER WEISSE | 355 ML | $75 | $63.75 |
| RED SEAL ALE | 355 ML | $70 | $59.50 |
| LE MERLE SAISON | 355 ML | $80 | $68 |
| PRANQSTER BELGIAN GOLDEN ALE | 355 ML | $80 | $68 |
| FOGGY DAY IPA | 355 ML | $70 | $59.50 |
| ACME BEER | 355 ML | $49 | - |
| SCRIMSHAW PILSNER | 355 ML | $49 | - |
| SCRIMSHAW PILSNER | 473 ML | $70 | $59.50 |

**Nota especial:** Precio promocional de $60 durante FIFA World Cup 2026

**Sección 3: Barriles (KEGS) - North Coast**

| Producto | Litros | Precio Barril | 15% Descuento |
|----------|--------|---------------|---------------|
| OLD RASPUTIN | 20 LTS | $4,500 | $3,825 |
| LE MERLE SAISON | 20 LTS | $4,500 | $3,825 |
| PRANQSTER | 20 LTS | $4,300 | $3,655 |
| RED SEAL ALE | 20 LTS | $4,300 | $3,655 |
| SCRIMSHAW | 20 LTS | $4,300 | $3,655 |
| FOGGY DAY IPA | 20 LTS | $4,300 | $3,655 |
| BROTHER THELONIOUS | 20 LTS | $5,000 | $4,250 |
| OLD STOCK | 20 LTS | $5,500 | $4,675 |

**Sección 4: Barriles (KEGS) - Knee Deep**

| Producto | Litros | Precio Barril | 15% Descuento |
|----------|--------|---------------|---------------|
| SIMTRA TRIPLE IPA | 20 LTS | $5,500 | $4,675 |
| SLOOOWMO IPA | 20 LTS | $4,500 | $3,825 |
| HOPTOLOGIST DOBLE IPA | 20 LTS | $5,100 | $4,335 |
| TAHOE DEEP IMPERIAL IPA | 20 LTS | $4,800 | $4,080 |
| BREAKING BUD IPA | 20 LTS | $4,800 | $4,080 |
| FOLSOME HAZE | 20 LTS | $4,500 | $3,825 |
| DEEP CLARITY | 20 LTS | $4,500 | $3,825 |

**Notas importantes:**
- Costo de envío a Cabo: $8 por caja / $650 por barril
- Todos los barriles son one-way con acople Sankey D
- Descuento del 15% disponible después de 15 unidades (cajas o barriles)

#### Problemas Encontrados

| Problema | Severidad | Descripción |
|----------|-----------|-------------|
| Todas las columnas sin nombre | 🔴 Alta | Las 10 columnas son "Unnamed: X" |
| Filas vacías | 🟡 Media | ~27 filas completamente vacías |
| Formato irregular | 🟡 Media | Productos y precios no alineados |
| Datos duplicados | 🟡 Media | 21 filas duplicadas |
| Dos estructuras en una | 🟡 Media | Botellas y barriles mezclados |

---

## 🎯 Recomendaciones Específicas de Mejora

### 1. ELIMINAR HOJAS INNECESARIAS
- **Eliminar** `Sheet1` completamente

### 2. REESTRUCTURAR HOJA DE VENTAS

**Problema actual:** Los productos están como columnas, lo que dificulta:
- Agregar nuevos productos
- Hacer análisis de ventas
- Generar reportes

**Solución propuesta:**

```
Estructura VERTICAL (una fila = una venta):

| FECHA       | CLIENTE      | PRODUCTO          | CANTIDAD | PRECIO_UNIT | DESCUENTO | TOTAL   | ESTADO |
|-------------|--------------|-------------------|----------|-------------|-----------|---------|--------|
| 2026-03-01  | LA ESPUMA    | RASPUTIN 355 ML   | 12       | 85          | 0         | 1020    | PAID   |
| 2026-03-01  | LA ESPUMA    | BROTHER TH        | 8        | 93          | 0         | 744     | PAID   |
| 2026-03-02  | EUROCERVEZAS | RASPUTIN 355 ML   | 240      | 85          | 0         | 20400   | PAID   |
```

### 3. SEPARAR GASTOS EN HOJA INDEPENDIENTE

**Nueva hoja: "Gastos"**

```
| FECHA       | CATEGORIA      | DESCRIPCION    | MONTO  | METODO_PAGO |
|-------------|----------------|----------------|--------|-------------|
| 2026-03-01  | ABUELITA       | -              | 5500   | EFECTIVO    |
| 2026-03-01  | MONASTERIO     | -              | 2850   | TRANSFER    |
| 2026-03-01  | MULTA AZUL     | -              | 2050   | TARJETA     |
```

### 4. MEJORAR HOJA DE PRECIOS

**Nueva estructura más clara:**

```
| CERVECERIA    | PRODUCTO              | TIPO     | ML/LTS | PRECIO_LISTA | DESC_15% | COSTO_ENVIO |
|---------------|-----------------------|----------|--------|--------------|----------|-------------|
| North Coast   | OLD RASPUTIN          | BOTELLA  | 355    | 85           | 72.25    | 8           |
| North Coast   | OLD RASPUTIN          | BOTELLA  | 473    | 106          | 90.10    | 8           |
| North Coast   | OLD RASPUTIN          | BARRIL   | 20 LTS | 4500         | 3825     | 650         |
| Knee Deep     | SIMTRA TRIPLE IPA     | LATA     | 473    | 185          | 157.25   | 8           |
| Knee Deep     | SIMTRA TRIPLE IPA     | BARRIL   | 20 LTS | 5500         | 4675     | 650         |
```

### 5. NOMBRAR CORRECTAMENTE LAS COLUMNAS

Eliminar todos los "Unnamed: X" y usar nombres descriptivos:
- `cliente` en lugar de `Unnamed: 0`
- `fecha` en lugar de `Unnamed: 14`
- `estado_pago` en lugar de `Unnamed: 15`

### 6. VALIDACIÓN DE DATOS

Implementar reglas de validación:
- Fechas consistentes
- Precios numéricos
- Nombres de clientes estandarizados
- Evitar filas duplicadas

---

## 🏗️ Propuesta de Estructura Optimizada

### NUEVA ESTRUCTURA DEL ARCHIVO

```
📁 INVENTARIO_VENTAS_2026.xlsx
│
├── 📋 HOJA 1: "Clientes"
│   ├── ID_CLIENTE
│   ├── NOMBRE
│   ├── CONTACTO
│   ├── TELEFONO
│   ├── EMAIL
│   ├── DIRECCION
│   └── TIPO (Mayorista/Minorista)
│
├── 📋 HOJA 2: "Productos"
│   ├── SKU
│   ├── CERVECERIA (North Coast / Knee Deep)
│   ├── NOMBRE_PRODUCTO
│   ├── TIPO (Botella/Lata/Barril)
│   ├── PRESENTACION (355ml/473ml/20LTS)
│   ├── PRECIO_UNITARIO
│   ├── PRECIO_DESCUENTO (15%)
│   └── COSTO_ENVIO
│
├── 📋 HOJA 3: "Ventas"
│   ├── ID_VENTA
│   ├── FECHA
│   ├── ID_CLIENTE
│   ├── SKU_PRODUCTO
│   ├── CANTIDAD
│   ├── PRECIO_UNITARIO
│   ├── DESCUENTO_APLICADO
│   ├── TOTAL
│   ├── ESTADO_PAGO (Pendiente/Pagado)
│   └── METODO_PAGO
│
├── 📋 HOJA 4: "Gastos"
│   ├── ID_GASTO
│   ├── FECHA
│   ├── CATEGORIA
│   ├── DESCRIPCION
│   ├── MONTO
│   └── METODO_PAGO
│
└── 📋 HOJA 5: "Inventario"
    ├── SKU_PRODUCTO
    ├── FECHA_ACTUALIZACION
    ├── STOCK_INICIAL
    ├── ENTRADAS
    ├── SALIDAS
    └── STOCK_ACTUAL
```

### BENEFICIOS DE LA NUEVA ESTRUCTURA

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Escalabilidad** | ❌ Difícil agregar productos | ✅ Solo agregar filas |
| **Análisis** | ❌ Muy complejo | ✅ Fácil con tablas dinámicas |
| **Mantenimiento** | ❌ Propenso a errores | ✅ Estructura clara |
| **Reportes** | ❌ Manual y tedioso | ✅ Automatizable |
| **Datos faltantes** | ❌ Muchos vacíos | ✅ Controlado |
| **Integridad** | ❌ Duplicados comunes | ✅ Validaciones |

---

## ⚡ Pasos Inmediatos Recomendados

1. **Hacer copia de respaldo** del archivo actual
2. **Crear nuevo archivo** con la estructura propuesta
3. **Migrar datos** de las hojas actuales a la nueva estructura
4. **Validar** que todos los datos se transfirieron correctamente
5. **Eliminar** el archivo antiguo una vez confirmado

---

## 📌 Conclusión

El archivo actual **funciona** pero tiene serios problemas de organización que dificultan su mantenimiento y análisis. La estructura horizontal de la hoja de ventas es el problema más crítico.

**Prioridad de correcciones:**
1. 🔴 **URGENTE:** Reestructurar hoja de ventas a formato vertical
2. 🔴 **URGENTE:** Nombrar todas las columnas correctamente
3. 🟡 **MEDIA:** Separar gastos a hoja independiente
4. 🟡 **MEDIA:** Limpiar hoja de precios
5. 🟢 **BAJA:** Eliminar hoja vacía Sheet1

Con estas mejoras, el sistema será mucho más fácil de mantener, analizar y escalar a medida que el negocio crezca.

---

*Documento generado automáticamente - Análisis de Excel*
