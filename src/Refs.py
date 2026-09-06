try:
    import os, re, time, argparse

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--output", default=f"{os.getcwd()}\\output.txt")
    parser.add_argument("--folder")
    parser.add_argument("--help")
    args, unk = parser.parse_known_args()

    if unk:
        print(f"Unknown argument(s): {unk}\nUse '--help' for more information.")

    if args.help:
        print(f"""
usage: python Refs.py [--help] [--folder FOLDER] [--output FILE]

examples:
    python Refs.py --folder "C:\\Users\\Desktop\\test"
    
    python Refs.py --folder "C:\\Users\\Desktop\\test" --output "C:\\Users\\Desktop\\test"

arguments:
    --help: show this help message and exit
    
    --folder: path to target folder
    
    --output: path to output folder for scanned files/folders (outputs.txt will be generated in this folder)

defaults:
    --output: {os.getcwd()}\\output.txt

Advanced recursive regex filesystem searcher
Made by: RequestTimeout(GitHub: https://github.com/RequestTimeout)
""")
        exit(0)

    folder = args.folder if args.folder else exec("""print("Please specify a folder to scan")\nexit()""")
    pattern = input("Enter a valid regular expression pattern: ")
    output_fp = args.output
    matches = []
    scanned = []
    start = time.time()
    for root, dirs, files in os.walk(folder):
        for file in files:
            scanned.append(f"Scanning: {os.path.join(root, file)}")
            if re.search(pattern, file):
                matches.append(f"Match: {os.path.join(root, file)}")
                print(f"Match: {os.path.join(root, file)}")
            else:
                print(f"Scanning: {os.path.join(root, file)}")

    with open(output_fp, "w+", encoding="utf-8") as f:
        f.write("\n".join(scanned))
    t = time.time() - start
    print("=" * 100)
    print(f"Found {len(matches)} matches in '{folder}' for the regular expression '{pattern}' in approximately {int(t // 3600):02}:{int(t % 3600 // 60):02}:{int(t % 60):02}.{int(t % 1 * 1000):03} seconds.")
    print("=" * 100)
    while True:
        yes = input("Do you want to print every matches found? [Y/N] ")
        if yes.lower() == "y":
            break
        elif yes.lower() == "n":
            exit(0)
        else:
            print("Please enter either 'Y' or 'N' for the input")

    print("=" * 100)
    print(f"Showing all {len(matches)} matches after 5 seconds")
    print("=" * 100)
    time.sleep(5)
    for match in matches:
        print(match)
    print()
    print("=" * 100)
    print("Made by: RequestTimeout(GitHub: https://github.com/RequestTimeout)")
except KeyboardInterrupt:
    print("\nKeyboard interrupt received...\nExiting...")
    exit(0)
except re.error:
    print("\nInvalid regular expression pattern entered...\nExiting...")
    exit(0)
