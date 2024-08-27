import socket

from colorama import Fore


def get_manually_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))

        banner_grab = {
            'FTP': b'220 ',
            'SSH': b'SSH-',
            'HTTP': b'HEAD / HTTP/1.1\r\nHost:' + ip.encode() + b'\r\n\r\n'
        }

        for service, banner in banner_grab.items():
            s.send(banner)
            response = s.recv(1024).decode()
            if response:
                if service in response:
                    print(f"{Fore.LIGHTCYAN_EX + service} - {Fore.RESET + response.splitlines()[0]}")
                    return "{service} - {response.splitlines()[0]}"
                else:
                    print(f"{Fore.LIGHTCYAN_EX}Desconocido - {Fore.RESET + response.splitlines()[0]}")
                    return f"Desconocido - {response.splitlines()[0]}"

            else:
                print("[!]No se  obtuvo respuesta")
                return None
    except KeyboardInterrupt as e:
        raise Exception(Fore.YELLOW + "\n[x]Operación cancelada") from e
    except Exception as e:
        print(Fore.RED + "[!]No se pudo obtener la versión del servicio.")


def manualy_grabber_manually(ip, port):
    try:
        print(
            f"{Fore.YELLOW}[!]Problema detectado, se intentará obtener los banners a través de una conexión con "
            f"socket, enviando banners.\n[!]Tenga en cuenta que con esta opción puede no obtener todos los "
            f"resultados como pueda ser con NMAP")
        banner = get_manually_banner(ip, port)
        if banner is not None:
            return banner
    except ValueError:
        print(f"{Fore.RED}[!]Formato incorrecto")
