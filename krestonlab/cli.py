import typer
from rich.console import Console
from rich.table import Table
from krestonlab.labs import LABS
from krestonlab.docker_manager import *

app = typer.Typer()
console = Console()

@app.command()
def list():
    """Lista laboratórios disponíveis"""
    table = Table(title="Labs Disponíveis")
    table.add_column("Nome")
    table.add_column("Descrição")
    table.add_column("Porta Padrão")

    for name, data in LABS.items():
        table.add_row(name, data["description"], str(data["default_port"]))

    console.print(table)

@app.command()
def install(lab: str):
    """Baixa imagem do laboratório"""
    check_docker()
    if lab not in LABS:
        console.print("[red]Lab inválido[/red]")
        raise typer.Exit()

    pull_image(LABS[lab]["image"])

@app.command()
def start(lab: str, port: int = None):
    """Inicia laboratório"""
    check_docker()

    if lab not in LABS:
        console.print("[red]Lab inválido[/red]")
        raise typer.Exit()

    data = LABS[lab]
    host_port = port if port else data["default_port"]

    network = create_network()
    run_container(lab, data["image"], host_port, data["internal_port"], network)

@app.command()
def stop(lab: str):
    """Para laboratório"""
    stop_container(lab)

@app.command()
def remove(lab: str):
    """Remove laboratório"""
    remove_container(lab)

@app.command()
def status(lab: str):
    """Verifica status"""
    state = container_status(lab)
    console.print(f"[blue]Status:[/blue] {state}")

def run():
    app()