from InquirerPy import inquirer
from rich.console import Console
from krestonlab.labs import LABS
from krestonlab.docker_manager import *

console = Console()


def choose_lab():
    return inquirer.select(
        message="Escolha o laboratório:",
        choices=list(LABS.keys())
    ).execute()


def start_menu():
    while True:
        option = inquirer.select(
            message="Selecione uma opção:",
            choices=[
                "🚀 Subir Lab",
                "⬇️ Instalar Lab",
                "⛔ Parar Lab",
                "🗑️ Remover Lab",
                "📊 Status",
                "❌ Sair"
            ],
        ).execute()

        if option == "❌ Sair":
            break

        lab = choose_lab()
        data = LABS[lab]

        if option == "⬇️ Instalar Lab":
            check_docker()
            pull_image(data["image"])

        elif option == "🚀 Subir Lab":
            check_docker()
            run_container(
                lab,
                data["image"],
                data["default_port"],
                data["internal_port"]
            )

        elif option == "⛔ Parar Lab":
            stop_container(lab)

        elif option == "🗑️ Remover Lab":
            remove_container(lab)

        elif option == "📊 Status":
            status = container_status(lab)
            console.print(f"[blue]Status:[/blue] {status}")