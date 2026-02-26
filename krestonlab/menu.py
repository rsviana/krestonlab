import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print
from krestonlab.labs import LABS
from krestonlab.docker_manager import *

console = Console()


def banner():
    console.print(Panel.fit(
        "\n"
        "[bold red]KRESTONLAB - v.1[/bold red]\n" \
        "\n"
        "[bold]Offensive Security Local Lab Manager[/bold]" \
        "\n" 
        "KrestonLab é um laboratório para CyberSecurity. Use-o sem moderação"
        "\n"
        ,
        
        border_style="red"
    ))


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
            "📦 Instalar Lab",
            "🚀 Subir Lab",
            "⏹ Parar Lab",
            "🗑 Remover Lab",
            "❌ Sair",


        ]
    ).ask()



def dashboard():
    console.clear()
    banner()

    table = Table(title="Status dos Containers")
    table.add_column("Container")
    table.add_column("Status")

    
    statuses = list_all_status()

    if not statuses:
        console.print("[yellow]Nenhum container encontrado.[/yellow]")
    else:
        for name, status in statuses.items():
            table.add_row(name, status)

        console.print(table)
        print("⚠️ Aqui estarão listados o estados de TODOS os containers que você possuí.")
    pause()
    
    


def start_menu():
    check_docker()

    while True:
        console.clear()
        banner()

        choice = main_menu()

        if choice == "📊 Dashboard":
            dashboard()

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
                data["internal_port"]
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
            console.print("[bold green]" \
            "Até mais, " \
            "Acesse: http://rodrigoviana.dev.br [/bold green]" \
            "" \
            "" \
            "")
            break