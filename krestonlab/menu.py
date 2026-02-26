import questionary
from rich.console import Console
from rich.panel import Panel
from rich import box

from krestonlab.labs import (
    LABS,
    install_lab,
    remove_lab,
    list_labs,
    status_containers
)

console = Console()


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]KRESTONLAB - v1.0.0[/bold cyan]\n\n"
            "Offensive Security Local Lab Manager\n"
            "KrestonLab é um laboratório para CyberSecurity.\n"
            "Use-o com responsabilidade.",
            box=box.ROUNDED,
            border_style="cyan",
        )
    )


def start_menu():
    while True:
        console.clear()
        show_banner()

        opcao = questionary.select(
            "Selecione uma opção:",
            choices=[
                "📦 Instalar Lab",
                "🗑 Remover Lab",
                "📋 Listar Labs",
                "📊 Status dos Containers",
                "🚪 Sair"
            ],
        ).ask()

        if opcao == "📦 Instalar Lab":
            lab = questionary.select(
                "Escolha o laboratório:",
                choices=list(LABS.keys())
            ).ask()

            if lab:
                install_lab(lab)
                questionary.press_any_key_to_continue().ask()

        elif opcao == "🗑 Remover Lab":
            lab = questionary.select(
                "Escolha o laboratório:",
                choices=list(LABS.keys())
            ).ask()

            if lab:
                remove_lab(lab)
                questionary.press_any_key_to_continue().ask()

        elif opcao == "📋 Listar Labs":
            list_labs()
            questionary.press_any_key_to_continue().ask()

        elif opcao == "📊 Status dos Containers":
            status_containers()
            questionary.press_any_key_to_continue().ask()

        elif opcao == "🚪 Sair":
            console.print("[bold green]" \
            "Até mais, \n" 
            "Acesse: http://rodrigoviana.dev.br [/bold green]" \
            "\n" 
            "\n" 
            "")
            break