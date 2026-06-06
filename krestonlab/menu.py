import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print

from krestonlab.labs import LABS
from krestonlab.docker_manager import (
    check_docker,
    pull_image,
    run_container,
    stop_container,
    remove_container,
    container_status
)

console = Console()


def banner():
    console.print(
        Panel.fit(
            "[bold red]KRESTONLAB - v.2 ☠️ More Machines ☠️[/bold red]\n\n"
            "[bold]Offensive Security Local Lab Manager [/bold]\n"
            "KrestonLab é um laboratório para CyberSecurity. Use-o sem moderação. ",
            border_style="red"
        )
    )


def pause():
    input("\nPressione Enter para continuar...")


def lab_selector():
    return questionary.select(
        "Escolha o laboratório:",
        choices=list(LABS.keys()) + ["⬅ Voltar"]
    ).ask()


def main_menu():
    return questionary.select(
        "Selecione uma opção:",
        choices=[
            "📊 Dashboard",
            "📊 Status",
            "📦 Instalar Lab",
            "🚀 Subir Lab",
            "⏹ Parar Lab",
            "🗑 Remover Lab",
            "❌ Sair"
        ]
    ).ask()


# -------------------------------------------------


def list_all_status():
    statuses = {}
    for lab in LABS.keys():
        statuses[lab] = container_status(lab)
    return statuses


def dashboard():
    console.clear()
    banner()

    table = Table(title="Status Geral dos Containers")
    table.add_column("Container", style="cyan")
    table.add_column("Porta", style="yellow")
    table.add_column("Status", style="green")

    statuses = list_all_status()

    active = False
    for name, status in statuses.items():
        if status != "Container não existe":
            active = True
            table.add_row(
            name,
            str(LABS[name]["default_port"]),
            status
        )

    if not active:
        console.print("[yellow]Nenhum container encontrado.[/yellow]")
    else:
        console.print(table)

    pause()


def show_status():
    lab = lab_selector()
    if lab == "⬅ Voltar":
        return

    status = container_status(lab)

    console.print(
        Panel.fit(
            f"[bold cyan]{lab}[/bold cyan]\n\nStatus: [bold green]{status}[/bold green]",
            border_style="cyan"
        )
    )

    pause()

def start_menu():
    check_docker()

    while True:
        console.clear()
        banner()

        choice = main_menu()

        if choice == "📊 Dashboard":
            dashboard()

        elif choice == "📊 Status":
            show_status()

        elif choice == "📦 Instalar Lab":
            lab = lab_selector()
            if lab == "⬅ Voltar":
                continue
            pull_image(LABS[lab]["image"])
            pause()

        elif choice == "🚀 Subir Lab":
            lab = lab_selector()
            if lab == "⬅ Voltar":
                continue
            data = LABS[lab]
            run_container(
                lab,
                data["image"],
                data["default_port"],
                data["internal_port"],
                data.get("env", {}),
                data.get("volumes", [])
            )
            pause()

        elif choice == "⏹ Parar Lab":
            lab = lab_selector()
            if lab == "⬅ Voltar":
                continue
            stop_container(lab)
            pause()

        elif choice == "🗑 Remover Lab":
            lab = lab_selector()
            if lab == "⬅ Voltar":
                continue
            remove_container(lab)
            pause()

        elif choice == "❌ Sair":
            console.print(
                "\n[bold green]Até mais!\n"
                "Acesse: http://rodrigoviana.dev.br\n[/bold green]"
            )
            break
