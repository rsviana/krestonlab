import subprocess
import sys
from rich.console import Console

console = Console()


def run_command(command: list):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Erro:[/red] {' '.join(command)}")
        console.print(e.stderr)
        sys.exit(1)


def check_docker():
    try:
        subprocess.run(
            ["docker", "info"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except Exception:
        console.print("[red]Docker não está rodando ou instalado![/red]")
        sys.exit(1)


def pull_image(image: str):
    console.print(f"[cyan]Baixando imagem {image}...[/cyan]")
    run_command(["docker", "pull", image])
    console.print("[green]Imagem pronta![/green]")


def run_container(name: str, image: str, host_port: int, internal_port: int):
    console.print(f"[cyan]Subindo lab {name}...[/cyan]")

    # remove se existir
    subprocess.run(
        ["docker", "rm", "-f", name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    run_command([
        "docker", "run", "-d",
        "--name", name,
        "-p", f"{host_port}:{internal_port}",
        image
    ])

    console.print(f"[green]Rodando em http://localhost:{host_port}[/green]")


def stop_container(name: str):
    run_command(["docker", "stop", name])
    console.print("[yellow]Lab parado.[/yellow]")


def remove_container(name: str):
    run_command(["docker", "rm", "-f", name])
    console.print("[yellow]Lab removido.[/yellow]")


def container_status(name: str):
    result = subprocess.run(
        ["docker", "ps", "-a", "--filter", f"name={name}", "--format", "{{.Status}}"],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip()
    return output if output else "Container não existe"