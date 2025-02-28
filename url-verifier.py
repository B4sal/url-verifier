import requests
from urllib.parse import urlparse

def es_url_valida(url):
    try:
        resultado = urlparse(url)
        # Verifica que tenga un esquema (http o https) y un dominio
        return resultado.scheme in ['http', 'https'] and resultado.netloc
    except ValueError:
        return False

def obtener_destino_url(url, timeout=10):
    try:
        response = requests.get(url, allow_redirects=True, timeout=timeout)
        return {
            'url_final': response.url,
            'codigo_estado': response.status_code,
            'es_segura': response.url.startswith('https')
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def mostrar_info(info):
    if 'error' in info:
        print(f"🚨 Error: {info['error']}")
    else:
        print(f"✅ URL final: {info['url_final']}")
        print(f"🔍 Código de estado: {info['codigo_estado']}")
        print(f"🔒 ¿Es segura (HTTPS)?: {'Sí' if info['es_segura'] else 'No'}")

def main():
    print("🔗 Ingresa una URL para conocer su destino.")
    while True:
        url = input("🌐 Ingresa una URL (o 'salir' para terminar): ").strip()
        if url.lower() == 'salir':
            break

        if not es_url_valida(url):
            print("❌ URL no válida. Asegúrate de que comience con 'http://' o 'https://'.")
            continue

        print(f"\n🔎 Procesando: {url}")
        info = obtener_destino_url(url)
        mostrar_info(info)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()