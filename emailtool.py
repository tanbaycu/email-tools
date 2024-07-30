import random
import string
import json
import csv
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

DEFAULT_EXCLUDED_CHARS = "<>,.?/\{}[]:;\"'~`!#$%^&*"
""" can change"""


def generate_random_string(length, chars):

    return "".join(random.choice(chars) for _ in range(length))


def generate_strong_password(length, chars, exclude_chars=DEFAULT_EXCLUDED_CHARS):

    chars = "".join(c for c in chars if c not in exclude_chars)
    return generate_random_string(length, chars)


def apply_custom_format(template, random_part):

    return template.replace("{random}", random_part)


def generate_random_email(template, domain, length_of_random_part, chars, format_type):

    random_part = generate_random_string(length_of_random_part, chars)

    if format_type == "simple":
        return f"{random_part}{domain}"
    elif format_type == "custom":
        return apply_custom_format(template, random_part) + domain
    else:
        return None


def create_random_emails(
    template, num_emails, domain, length_of_random_part, chars, format_type
):

    if not template.endswith(domain):
        console.print(
            "[bold red]Error:[/bold red] Error path, pls use  '<local_part>@domain'."
        )
        return []

    local_part = template[: -len(domain)]

    emails = set()
    while len(emails) < num_emails:
        email = generate_random_email(
            local_part, domain, length_of_random_part, chars, format_type
        )
        if email:
            emails.add(email)
    return list(emails)


def write_emails_to_file(emails, passwords, filename, file_format):

    try:
        if file_format == "txt":
            with open(filename, "w") as file:
                for email, password in zip(emails, passwords):
                    file.write(f"{email} : {password}\n")
        elif file_format == "csv":
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Email", "Password"])
                for email, password in zip(emails, passwords):
                    writer.writerow([email, password])
        elif file_format == "json":
            data = [
                {"email": email, "password": password}
                for email, password in zip(emails, passwords)
            ]
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        elif file_format == "md":
            with open(filename, "w") as file:
                file.write("# Email and Password List\n\n")
                file.write("| Email | Password |\n")
                file.write("|-------|----------|\n")
                for email, password in zip(emails, passwords):
                    file.write(f"| {email} | {password} |\n")
        console.print(
            f"[bold green]Emails and passwords have been saved to {filename}.[/bold green]"
        )
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Could not write to file. {e}")


def display_about():

    about_text = """
[bold cyan]About This Tool[/bold cyan]

[bold]Author:[/bold] T7C Tools
[bold]Description:[/bold] This tool generates random email addresses and strong passwords based on user input.
[bold]Usage:[/bold] 
1. Choose "Generate Emails" to create email addresses and passwords.
2. Follow the prompts to customize the email template, domain, character types, and more.
3. Save the generated emails and passwords to a file if desired.
[bold]Debugging:[/bold] 
- Ensure that the email template ends with the domain.
- Verify that the domain starts with '@'.
- Check the format and length of inputs.
[bold]Contact:[/bold] 
For questions or support, please contact [italic]tranminhtan4953@gmail.com[/italic].
    """
    console.print(
        Panel(
            about_text,
            title="About",
            title_align="center",
            style="bold cyan",
            box=box.ROUNDED,
        )
    )


def display_menu():

    ascii_title = """
   @T7C TOOLS
███████╗        ███╗   ███╗         █████╗         ██╗                ██╗                                  
██╔════╝        ████╗ ████║        ██╔══██╗        ██║                ██║                                  
█████╗          ██╔████╔██║        ███████║        ██║                ██║                                  
██╔══╝          ██║╚██╔╝██║        ██╔══██║        ██║                ██║                                  
███████╗        ██║ ╚═╝ ██║        ██║  ██║        ██║                ███████╗                             
╚══════╝        ╚═╝     ╚═╝        ╚═╝  ╚═╝        ╚═╝                ╚══════╝                             
                                                                                                           
                                                            ████████╗     ██████╗      ██████╗     ██╗     
                                                            ╚══██╔══╝    ██╔═══██╗    ██╔═══██╗    ██║     
                                                               ██║       ██║   ██║    ██║   ██║    ██║     
                                                               ██║       ██║   ██║    ██║   ██║    ██║     
                                                               ██║       ╚██████╔╝    ╚██████╔╝    ███████╗
                                                               ╚═╝        ╚═════╝      ╚═════╝     ╚══════╝
    """
    console.print(
        Panel(
            ascii_title,
            title="Welcome to Email Generator Tool",
            title_align="center",
            style="bold cyan",
            box=box.ROUNDED,
        )
    )

    panel = Panel(
        "Main Menu",
        title="Main Menu",
        subtitle="Select an option",
        title_align="center",
        subtitle_align="center",
        box=box.ROUNDED,
        style="bold cyan",
    )
    console.print(panel)

    while True:
        table = Table(
            title="Options",
            show_header=True,
            header_style="bold magenta",
            box=box.ROUNDED,
        )
        table.add_column("Option", style="dim", width=20)
        table.add_column("Description")

        table.add_row("1", "Generate Emails")
        table.add_row("2", "About")
        table.add_row("3", "Exit")

        console.print(table)

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3"], default="1")

        if choice == "1":
            generate_emails()
        elif choice == "2":
            display_about()
        elif choice == "3":
            console.print("[bold green]Exiting...[/bold green]")
            break


def generate_emails():

    try:
        console.print("[bold cyan]Email Template[/bold cyan]")
        template = Prompt.ask(
            "[bold green]Enter the email template (e.g., user123@yahoo.com):[/bold green]"
        )

        console.print("[bold cyan]Domain[/bold cyan]")
        domain = Prompt.ask(
            "Enter the domain (e.g., @gmail.com, @yahoo.com) [default: @gmail.com]",
            default="@gmail.com",
        )

        if not domain.startswith("@"):
            console.print("[bold red]Error:[/bold red] The domain must start with '@'.")
            return

        console.print("[bold cyan]Random Part Length[/bold cyan]")
        length_of_random_part = int(
            Prompt.ask(
                "Enter the length of the random part (e.g., 4 for 4 digits)",
                default="4",
            )
        )

        console.print("[bold cyan]Character Type[/bold cyan]")
        chars_option = Prompt.ask(
            "Enter the type of random characters (digits, letters, alphanumeric) [default: alphanumeric]",
            default="alphanumeric",
        ).lower()
        if chars_option == "digits":
            chars = string.digits
        elif chars_option == "letters":
            chars = string.ascii_letters
        elif chars_option == "alphanumeric":
            chars = string.ascii_letters + string.digits
        else:
            console.print(
                "[bold red]Error:[/bold red] Invalid character type. Using alphanumeric by default."
            )
            chars = string.ascii_letters + string.digits

        console.print("[bold cyan]Format Type[/bold cyan]")
        format_type = Prompt.ask(
            "Enter the format type (simple, custom) [default: simple]", default="simple"
        ).lower()
        if format_type not in ["simple", "custom"]:
            console.print(
                "[bold red]Error:[/bold red] Invalid format type. Using simple by default."
            )
            format_type = "simple"

        console.print("[bold cyan]Number of Emails[/bold cyan]")
        num_emails = int(Prompt.ask("Enter the number of emails to generate"))

        console.print("[bold cyan]Exclude Characters[/bold cyan]")
        exclude_chars = Prompt.ask(
            "Enter additional characters to exclude from passwords (leave empty for defaults)",
            default=DEFAULT_EXCLUDED_CHARS,
        )
        exclude_chars = exclude_chars if exclude_chars else DEFAULT_EXCLUDED_CHARS

        emails = create_random_emails(
            template, num_emails, domain, length_of_random_part, chars, format_type
        )

        if emails:
            console.print("[bold green]Generated Emails and Passwords:[/bold green]")

            passwords = set()
            password_length = int(
                Prompt.ask("Enter the length of the passwords", default="12")
            )
            while len(passwords) < num_emails:
                password = generate_strong_password(
                    password_length,
                    string.ascii_letters + string.digits + string.punctuation,
                    exclude_chars,
                )
                passwords.add(password)
            passwords = list(passwords)

            table = Table(
                show_header=True, header_style="bold magenta", box=box.ROUNDED
            )
            table.add_column("Index", style="dim", width=6)
            table.add_column("Email")
            table.add_column("Password")

            for idx, (email, password) in enumerate(zip(emails, passwords), start=1):
                table.add_row(str(idx), email, password)

            console.print(table)

            write_to_file = Prompt.ask(
                "Do you want to save the emails and passwords to a file? (yes/no)",
                choices=["yes", "no"],
                default="no",
            )
            if write_to_file == "yes":
                file_format = Prompt.ask(
                    "Enter the file format (txt, csv, json, md) [default: txt]",
                    default="txt",
                ).lower()
                if file_format not in ["txt", "csv", "json", "md"]:
                    console.print(
                        "[bold red]Error:[/bold red] Invalid file format. Using txt by default."
                    )
                    file_format = "txt"
                filename = Prompt.ask("Enter the filename (e.g., emails.txt)")
                write_emails_to_file(emails, passwords, filename, file_format)

    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/bold red] {e}")


if __name__ == "__main__":
    display_menu()

""" Example:
- Enter the email template (e.g., user1234@gmail.com): user{random}@example.com
- Enter the domain (e.g., @gmail.com, @yahoo.com) [default: @example.com]: @example.com
- Enter the length of the random part (e.g., 4 for 4 digits): 4
- Enter the type of random characters (digits, letters, alphanumeric) [default: alphanumeric]: alphanumeric
- Enter the format type (simple, custom) [default: simple]: custom
- Enter the number of emails to generate: 5
- Enter additional characters to exclude from passwords (leave empty for defaults): 
- Enter the length of the passwords: 12
- Do you want to save the emails and passwords to a file? (yes/no): yes
- Enter the file format (txt, csv, json, md) [default: txt]: txt
- Enter the filename (e.g., emails.txt): example.txt
--> results:
- useruj3v@example.com : +[RfMk;2s]4}
- user3@example.com : fN2e~wD`
- user20tm@example.com : 8YxlZxK1LQ
- userfPj2@example.com : <w~8uO^K1
- userNox@example.com : ?3IlxRS[9
"""

