from fpdf import FPDF

class PDF(FPDF):
    # Header
    def header(self):
        # Add image to pdf
        self.image("./shirtificate.png", 10, 70, 190)
        # Set font to Helvetica, punto=48
        self.set_font("helvetica", "", 48)
        # Add and modify the cell
        self.cell(0, 57, "CS50 Shirtificate", align='C')
        # Perform line break
        self.ln(20)


def main():
    # Get user's name
    name = input("Name: ")
    # Modify the shirt
    shirt(name)


def shirt(s):
    # Create a pdf object
    pdf = PDF()
    # Create an A4 page in portrait mode
    pdf.add_page(orientation="portrait", format="a4")
    # Set the font to Helvetica, punto to 24
    pdf.set_font("helvetica", size=24)
    # Set the color white
    pdf.set_text_color(255, 255, 255)
    # Create a modified cell
    pdf.cell(0, 213, f"{s} took CS50", align='C')
    # Create the output file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()