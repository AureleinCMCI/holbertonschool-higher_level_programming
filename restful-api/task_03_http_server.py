import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Got GET request %s" % (self.path))

        # Si la requête est pour la racine "/"
        if self.path == '/':
            self.send_response(200)  # Réponse OK (200)
            self.send_header('Content-type', 'text/plain')  # Définir le type comme texte
            self.end_headers()

            # Envoyer le message en texte
            self.wfile.write(b"Hello, this is a simple API!")

        # Si la requête est pour "/data", renvoyer des données JSON
        elif self.path == '/data':
            self.send_response(200)  # Réponse OK (200)
            self.send_header('Content-type', 'application/json')  # Définir le type de contenu comme JSON
            self.end_headers()

            # Créer un dictionnaire de données JSON
            data = {"name": "John", "age": 30, "city": "New York"}

            # Convertir le dictionnaire en JSON et l'envoyer dans la réponse
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Si la requête est pour "/status", renvoyer un message OK
        elif self.path == '/status':
            self.send_response(200)  # Réponse OK (200)
            self.send_header('Content-type', 'text/plain')  # Définir le type comme texte
            self.end_headers()

            # Envoyer le message de statut
            self.wfile.write(b"OK")

        else:
            # Gérer les autres demandes avec une réponse 404 (non trouvé)
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            # Envoyer un message d'erreur pour les pages non trouvées
            self.wfile.write(b"Page not found. The endpoint you are looking for does not exist.")

def run():
    # Serveur sur localhost avec le port 8000
    server_address = ('', 8000)  
    httpd = HTTPServer(server_address, MyHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()

run()
