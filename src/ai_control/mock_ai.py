def ask(ai_name, prompt):
    """Simulasi respons AI. Token korban dikuras secara simulasi."""
    print(f"[{ai_name}] Menerima prompt: {prompt}")
    print(f"[System] Token milik {ai_name} berkurang 150 (simulasi)")
    return f"Jawaban dari {ai_name}: Saya akan melakukannya."
