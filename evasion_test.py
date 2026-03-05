def signature_detection(payload):

    signatures = [
        "cmd.exe",
        "powershell",
        "wget",
        "nc",
        "bash",
        "whoami"
    ]

    for sig in signatures:
        if sig.lower() in payload.lower():
            return "DETECTED"

    return "BYPASSED"
