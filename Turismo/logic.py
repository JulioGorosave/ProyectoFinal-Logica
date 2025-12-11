from typing import Dict, List, Any, Optional
import math
from config import PLACE_TYPE, DEFAULT_DIST

# hechos
def _rad(x: float) -> float:
    # grados a radianes, para distancias
    return x * math.pi / 180.0

def dist_km(a: Dict[str, float], b: Dict[str, float]) -> float:
    # distancia "Haversine" en km entre dos puntos
    R = 6371.0
    if a.get("lat") is None or a.get("lon") is None or b.get("lat") is None or b.get("lon") is None:
        return float("inf")
    dlat = _rad(b["lat"] - a["lat"])
    dlon = _rad(b["lon"] - a["lon"])
    lat1 = _rad(a["lat"])
    lat2 = _rad(b["lat"])
    h = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(h))

def calc_cost(precio_noche: float, modo: str, noches: Optional[int]) -> float:
    # calcula el costo segun las noches seleccionadas
    if modo == "por_noche":
        return precio_noche
    if modo == "por_semana":
        return precio_noche * 7
    n = noches if (noches and noches > 0) else 3
    return precio_noche * n

def lugar_cumple_tags(lista: Dict[str, Any], include: List[str], exclude: List[str]) -> bool:
    tags = lista.get("tags", [])
    # utiliza "all" (AND) para ver si todos los tags estan incluidos
    if include and not all(t in tags for t in include):
        return False
    # utiliza "any" (OR) para ver que no este ni un solo tag excluido
    if exclude and any(t in tags for t in exclude):
        return False
    return True

# razones
def _explicar_ciudad(hotel: Dict[str, Any], ciudad: Optional[str]) -> Optional[str]:
    """
    Regla R1: ciudad.
    - Si no se especifica ciudad en la consulta, la regla se considera satisfecha.
    - Si se especifica ciudad, solo pasan los hoteles que estén en esa ciudad.
    """
    if not ciudad:
        # no hay restricción -> la regla se cumple por omisión
        return "No se especificó ciudad: cualquier ciudad es válida."
    if hotel.get("ciudad") == ciudad:
        return f"Coincide la ciudad requerida: {ciudad}."
    # None = la regla NO se cumple, el hotel será descartado
    return None

def _explicar_presupuesto(hotel: Dict[str, Any], costo: float, presupuesto: Optional[float]) -> Optional[str]:
    """
    Regla R2: presupuesto.
    - Si no se especifica presupuesto, la regla se considera satisfecha.
    - Si se especifica, el costo calculado debe ser <= presupuesto.
    """
    if presupuesto is None:
        return f"No se especificó presupuesto: se acepta el costo calculado ({costo:.2f} MXN)."
    if costo <= float(presupuesto):
        return f"Costo {costo:.2f} MXN ≤ presupuesto {float(presupuesto):.2f} MXN."
    return None

def _explicar_tags(hotel: Dict[str, Any], incluir: List[str], excluir: List[str]) -> Optional[str]:
    """
    Regla R3: tags del hotel.
    Utiliza la función lugar_cumple_tags, pero también genera una explicación textual.
    """
    tags_hotel = hotel.get("tags", [])
    # si no hay restricciones, la regla se cumple
    if not incluir and not excluir:
        return "No se especificaron tags: no se aplica restricción por etiquetas."
    # verificar con la lógica ya existente
    if not lugar_cumple_tags(hotel, incluir, excluir):
        return None

    parts: List[str] = []
    if incluir:
        innie = [t for t in incluir if t in tags_hotel]
        parts.append(f"Incluye todos los tags requeridos: {', '.join(innie)}.")
    if excluir:
        outie = [t for t in excluir if t not in tags_hotel]
        if outie:
            parts.append(f"No contiene los tags excluidos: {', '.join(excluir)}.")

    return " ".join(parts) if parts else "Cumple las restricciones de tags."

# motor de inferencia
def mostrar_hoteles(
    hoteles: List[Dict[str, Any]],
    presupuesto: Optional[float] = None,
    modo: str = "por_noche",
    noches: Optional[int] = None,
    ciudad: Optional[str] = None,
    tags_incluir: Optional[List[str]] = None,
    tags_excluir: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    """
    dado un conjunto de "hechos" (hoteles) y una "consulta" (presupuesto, ciudad, tags),
    se aplican una serie de reglas:
        R1: ciudad
        R2: presupuesto
        R3: tags (etiquetas)
    Solo los hoteles que satisfacen TODAS las reglas se consideran resultados válidos.
    """
    tags_incluir = tags_incluir or []
    tags_excluir = tags_excluir or []
    resultados: List[Dict[str, Any]] = []

    for h in hoteles:
        explicaciones: List[str] = []

        # 1) Regla R1: Ciudad
        razon_ciudad = _explicar_ciudad(h, ciudad)
        if razon_ciudad is None:
            continue
        explicaciones.append(f"R1 (Ciudad): {razon_ciudad}")

        # 2) Regla R2: Presupuesto
        costo = calc_cost(h.get("precio_noche", 0.0), modo, noches)
        razon_presupuesto = _explicar_presupuesto(h, costo, presupuesto)
        if razon_presupuesto is None:
            continue
        explicaciones.append(f"R2 (Presupuesto): {razon_presupuesto}")

        # 3) Regla R3: Tags del hotel
        razon_tags = _explicar_tags(h, tags_incluir, tags_excluir)
        if razon_tags is None:
            continue
        explicaciones.append(f"R3 (Tags): {razon_tags}")

        # Resultado (si pasa por todas las reglas)
        resultados.append({
            "id": h["id"],
            "nom": h["nom"],
            "ciudad": h["ciudad"],
            "precio_noche": h["precio_noche"],
            "costo_calculado": round(costo, 2),
            "tags": h.get("tags", []),
            "lat": h.get("lat"),
            "lon": h.get("lon"),
            "img": h.get("img"),
            "explicacion": explicaciones,
        })

    # Ordenar por costo calculado (barato primero)
    resultados.sort(key=lambda x: x["costo_calculado"])
    return resultados
