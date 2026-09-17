"""
====================================================================
DIAGRAMA DE FLUJO: SISTEMA DE VENTAS
====================================================================

               ┌────────────────────────┐
               │         INICIO         │
               └───────────┬────────────┘
                           │
                           ▼
     ┌───────────────────────────────────────────┐
     │ Inicializar acumuladores, contadores,     │
     │ venta_mayor, venta_menor y caja_cerrada   │
     └─────────────────────┬─────────────────────┘
                           │
                           ▼
     ┌───────────────────────────────────────────┐
┌───►│       MOSTRAR MENÚ PRINCIPAL (1-5)        │
│    └─────────────────────┬─────────────────────┘
│                          │
│                          ▼
│               ┌──────────────────────┐
│               │   ¿Opción elegida?   │
│               └──────────┬───────────┘
│                          │
│  ├── 1: REGISTRAR ───────┴───────────────────────────────────────────┐
│  │   ├── ¿Caja cerrada? ──► [Sí] ──► [Mostrar Error] ────────────────┼──┐
│  │   └── [No]                                                        │  │
│  │        │                                                          │  │
│  │        ▼                                                          │  │
│  │   [Leer y validar: Cliente, Productos (ciclo FOR) y Medio Pago]   │  │
│  │        │                                                          │  │
│  │        ▼                                                          │  │
│  │   [Calcular subtotal, descuentos (10%/3%) y recargo (2%)]         │  │
│  │        │                                                          │  │
│  │        ▼                                                          │  │
│  │   [Actualizar acumuladores globales, máx/mín y mostrar ticket] ───┘  │
│  │                                                                      │
│  ├── 2, 3 o 4: CONSULTAS Y CIERRE ───────────────────────────────────┤
│  │   ├── ¿Cantidad de ventas > 0? ──► [No] ──► [Mostrar Error] ─────────┼──┤
│  │   └── [Sí]                                                           │  │
│  │        │                                                             │  │
│  │        ▼                                                             │  │
│  │   [Calcular promedio, mostrar reporte (Opción 4 bloquea caja)] ──────┘  │
│  │                                                                         │
│  ├── 5: SALIR ───────────► [Mostrar despedida] ──► [ FIN ]                 │
│  │                                                                         │
│  └── Inválida ───────────► [Mostrar Error] ────────────────────────────────┘
│                                  │
└──────────────────────────────────┘
"""