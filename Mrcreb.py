from colorama import Fore, Style
import pyfiglet

# Fungsi untuk mencetak teks dengan warna
def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

# Fungsi untuk menampilkan judul program
def display_title():
    title = pyfiglet.figlet_format("CHANGE TYPE PROXY", font="slant")  # Buat teks ASCII art dengan font lebih besar
    print_colored(title, Fore.WHITE)  # Tampilkan dengan warna putih

# Fungsi untuk menampilkan penulis
def display_author():
    print_colored("Author by LEONA tg@rexxseller".rjust(50), Fore.MAGENTA)  # Align kanan dengan lebar 50 karakter

# Fungsi untuk menambahkan prefix pilihan (http, https, socks5) ke setiap baris file
def add_prefix_to_file(input_file, output_file, prefix):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    updated_lines = []
    for line in lines:
        line = line.strip()  # Hilangkan spasi atau newline di awal/akhir baris
        if line and not line.startswith(f"{prefix}://"):
            updated_lines.append(f"{prefix}://" + line)
        else:
            updated_lines.append(line)

    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(updated_lines))

    print_colored(f"Proses selesai. Hasil disimpan di {output_file}", Fore.GREEN)

# Main Program
if __name__ == "__main__":
    # Menampilkan header, title, dan author
    display_title()
    display_author()

    # Menanyakan pilihan prefix ke pengguna
    print_colored("Pilih jenis prefix yang ingin ditambahkan:", Fore.CYAN)
    print_colored("[1] http", Fore.YELLOW)
    print_colored("[2] https", Fore.YELLOW)
    print_colored("[3] socks5", Fore.YELLOW)

    # Meminta input dari pengguna
    choice = input("Masukkan pilihan Anda (1/2/3): ").strip()
    if choice == "1":
        prefix = "http"
    elif choice == "2":
        prefix = "https"
    elif choice == "3":
        prefix = "socks5"
    else:
        print_colored("Pilihan tidak valid. Program dihentikan.", Fore.RED)
        exit()

    # Meminta nama file input dan output
    input_file = input("Masukkan nama file input (default: input.txt): ").strip() or "input.txt"
    output_file = input("Masukkan nama file output (default: output.txt): ").strip() or "output.txt"

    # Menjalankan fungsi dengan prefix pilihan
    add_prefix_to_file(input_file, output_file, prefix)
