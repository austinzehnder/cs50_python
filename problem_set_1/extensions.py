def main():
    user_input = input("File name: ").strip().lower()

    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    for ext, media_type in media_types.items():
        if user_input.endswith(ext):
            print(media_type)
            break
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
