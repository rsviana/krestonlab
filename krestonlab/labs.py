LABS = {
    "DVWA": {
        "image": "vulnerables/web-dvwa",
        "internal_port": 80,
        "default_port": 8080,
        "description": "Damn Vulnerable Web Application"
    },
    "Mutillidae": {
        "description": "OWASP Mutillidae II",
        "image": "citizenstig/nowasp",
        "default_port": 8081,
        "internal_port": 80
    },
    "WebGoat": {
        "image": "szsecurity/webgoat",
        "internal_port": 80,
        "default_port": 8082,
        "description": "OWASP WebGoat"
    },
    "bWAPP": {
        "image": "citizenstig/nowasp",
        "internal_port": 80,
        "default_port": 8083,
    }
}