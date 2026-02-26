import docker
from rich.console import Console
from docker.errors import NotFound

console = Console()
client = docker.from_env()


def check_docker():
    try:
        client.ping()
    except Exception:
        console.print("[bold red]Docker não está rodando ou instalado.[/bold red]")
        raise SystemExit()


def pull_image(image):
    console.print(f"[cyan]Baixando imagem {image}...[/cyan]")
    client.images.pull(image)
    console.print("[bold green]Download concluído![/bold green]")


def run_container(name, image, host_port, internal_port):
    try:
        client.containers.run(
            image,
            name=name.lower(),
            ports={f"{internal_port}/tcp": host_port},
            detach=True
        )
        console.print(f"[bold green]Rodando em http://localhost:{host_port}[/bold green]")
    except Exception as e:
        console.print(f"[red]Erro: {e}[/red]")


def stop_container(name):
    try:
        container = client.containers.get(name.lower())
        container.stop()
        console.print("[yellow]Container parado.[/yellow]")
    except NotFound:
        console.print("[red]Container não encontrado.[/red]")


def remove_container(name):
    try:
        container = client.containers.get(name.lower())
        container.remove(force=True)
        console.print("[bold red]Container removido.[/bold red]")
    except NotFound:
        console.print("[red]Container não encontrado.[/red]")


def container_status(name):
    try:
        container = client.containers.get(name.lower())
        return container.status
    except NotFound:
        return "not_found"


def list_all_status():
    status_map = {}
    for container in client.containers.list(all=True):
        status_map[container.name] = container.status
    return status_map