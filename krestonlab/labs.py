import os
import subprocess
from pathlib import Path
from rich.console import Console
from rich.table import Table


console = Console()
BASE_DIR = Path(__file__).parent / "labs"


LABS = {
    "DVWA": {
        "path": BASE_DIR / "dvwa",
        "compose": """
version: '3'
services:
  dvwa:
    image: vulnerables/web-dvwa
    container_name: dvwa
    ports:
      - "8081:80"
    networks:
      - krestonlab_net

networks:
  krestonlab_net:
"""
    },

    "bWAPP": {
        "path": BASE_DIR / "bwapp",
        "compose": """
version: '3'
services:
  bwapp:
    image: raesene/bwapp
    container_name: bwapp
    ports:
      - "8083:80"
    networks:
      - krestonlab_net

networks:
  krestonlab_net:
"""
    },

    "WebGoat": {
        "path": BASE_DIR / "webgoat",
        "compose": """
version: '3'
services:
  webgoat:
    image: webgoat/webgoat
    container_name: webgoat
    ports:
      - "8084:8080"
    networks:
      - krestonlab_net

networks:
  krestonlab_net:
"""
    },

    "Mutillidae": {
        "path": BASE_DIR / "mutillidae",
        "compose": """
version: '3'
services:
  mutillidae:
    image: citizenstig/nowasp
    container_name: mutillidae
    ports:
      - "8082:80"
    environment:
      MYSQL_DATABASE: owasp10
      MYSQL_USER: root
      MYSQL_PASSWORD: root
      MYSQL_ROOT_PASSWORD: root
      MYSQL_HOST: mysql
    depends_on:
      - mysql
    networks:
      - krestonlab_net

  mysql:
    image: mysql:5.7
    container_name: mutillidae_mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: owasp10
    ports:
      - "3307:3306"
    networks:
      - krestonlab_net

networks:
  krestonlab_net:
"""
    }
}


def run_command(command, cwd=None):
    subprocess.run(command, shell=True, cwd=cwd)


def install_lab(lab_name):
    lab = LABS.get(lab_name)
    if not lab:
        console.print("[red]Lab não encontrado.[/red]")
        return

    lab_path = lab["path"]
    lab_path.mkdir(parents=True, exist_ok=True)

    compose_file = lab_path / "docker-compose.yml"
    compose_file.write_text(lab["compose"])

    console.print(f"[green]Instalando {lab_name}...[/green]")
    run_command("docker compose up -d", cwd=lab_path)

    console.print(f"[bold green]{lab_name} instalado com sucesso![/bold green]")


def remove_lab(lab_name):
    lab = LABS.get(lab_name)
    if not lab:
        console.print("[red]Lab não encontrado.[/red]")
        return

    lab_path = lab["path"]

    console.print(f"[yellow]Removendo {lab_name}...[/yellow]")
    run_command("docker compose down -v", cwd=lab_path)

    console.print(f"[bold red]{lab_name} removido.[/bold red]")


def list_labs():
    table = Table(title="Labs Disponíveis")

    table.add_column("Lab")
    table.add_column("Porta")

    table.add_row("DVWA", "http://localhost:8081")
    table.add_row("Mutillidae", "http://localhost:8082")
    table.add_row("bWAPP", "http://localhost:8083")
    table.add_row("WebGoat", "http://localhost:8084")

    console.print(table)


def status_containers():
    console.print("[cyan]Status dos Containers[/cyan]")
    run_command("docker ps -a")