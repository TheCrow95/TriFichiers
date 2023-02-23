from pathlib import Path

dirs = {".jpg": "Images",
        ".bmp": "Images",
        ".png": "Images",
        ".jpeg": "Images",
        ".gif": "Vidéos",
        ".avi": "Vidéos",
        ".mp4": "Vidéos",
        ".pdf": "Documents",
        ".PDF": "Documents",
        ".txt": "Documents",
        ".pptx": "Documents",
        ".csv": "Documents",
        ".xls": "Documents",
        ".odp": "Documents",
        ".pages": "Documents",
        ".mp3": "Musiques",
        ".flac": "Musiques",
        ".wav": "Musiques"}

tri_dir = Path.home()
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    # Si aucune correspondance n'est trouvée pour l'extension, on place les fichiers dans un dossier Divers
    output_dir = tri_dir / dirs.get(f.suffix, "Divers")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
