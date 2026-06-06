import typer
from krestonlab.labs import LABS
from krestonlab.docker_manager import *

app = typer.Typer()


@app.command()
def list():
    for name, data in LABS.items():
        print(f"{name} - {data['description']}")


@app.command()
def install(lab: str):
    check_docker()
    pull_image(LABS[lab]["image"])


@app.command()
def start(lab: str):
    check_docker()
    data = LABS[lab]
    run_container(
        lab,
        data["image"],
        data["default_port"],
        data["internal_port"],
        data.get("env", {}),
        data.get("volumes", [])
    )


@app.command()
def stop(lab: str):
    stop_container(lab)


@app.command()
def remove(lab: str):
    remove_container(lab)


@app.command()
def status(lab: str):
    print(container_status(lab))


def run():
    app()