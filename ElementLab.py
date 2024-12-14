import tkinter as tk
import random

elements = {
    1: ("Hydrogen", "H"),
    2: ("Helium", "He"),
    3: ("Lithium", "Li"),
    4: ("Beryllium", "Be"),
    5: ("Boron", "B"),
    6: ("Carbon", "C"),
    7: ("Nitrogen", "N"),
    8: ("Oxygen", "O"),
    9: ("Fluorine", "F"),
    10: ("Neon", "Ne"),
    11: ("Sodium", "Na"),
    12: ("Magnesium", "Mg"),
    13: ("Aluminum", "Al"),
    14: ("Silicon", "Si"),
    15: ("Phosphorus", "P"),
    16: ("Sulfur", "S"),
    17: ("Chlorine", "Cl"),
    18: ("Argon", "Ar"),
    19: ("Potassium", "K"),
    20: ("Calcium", "Ca"),
    21: ("Scandium", "Sc"),
    22: ("Titanium", "Ti"),
    23: ("Vanadium", "V"),
    24: ("Chromium", "Cr"),
    25: ("Manganese", "Mn"),
    26: ("Iron", "Fe"),
    27: ("Cobalt", "Co"),
    28: ("Nickel", "Ni"),
    29: ("Copper", "Cu"),
    30: ("Zinc", "Zn"),
    31: ("Gallium", "Ga"),
    32: ("Germanium", "Ge"),
    33: ("Arsenic", "As"),
    34: ("Selenium", "Se"),
    35: ("Bromine", "Br"),
    36: ("Krypton", "Kr"),
    37: ("Rubidium", "Rb"),
    38: ("Strontium", "Sr"),
    39: ("Yttrium", "Y"),
    40: ("Zirconium", "Zr"),
    41: ("Niobium", "Nb"),
    42: ("Molybdenum", "Mo"),
    43: ("Technetium", "Tc"),
    44: ("Ruthenium", "Ru"),
    45: ("Rhodium", "Rh"),
    46: ("Palladium", "Pd"),
    47: ("Silver", "Ag"),
    48: ("Cadmium", "Cd"),
    49: ("Indium", "In"),
    50: ("Tin", "Sn"),
    51: ("Antimony", "Sb"),
    52: ("Tellurium", "Te"),
    53: ("Iodine", "I"),
    54: ("Xenon", "Xe"),
    55: ("Cesium", "Cs"),
    56: ("Barium", "Ba"),
    57: ("Lanthanum", "La"),
    58: ("Cerium", "Ce"),
    59: ("Praseodymium", "Pr"),
    60: ("Neodymium", "Nd"),
    61: ("Promethium", "Pm"),
    62: ("Samarium", "Sm"),
    63: ("Europium", "Eu"),
    64: ("Gadolinium", "Gd"),
    65: ("Terbium", "Tb"),
    66: ("Dysprosium", "Dy"),
    67: ("Holmium", "Ho"),
    68: ("Erbium", "Er"),
    69: ("Thulium", "Tm"),
    70: ("Ytterbium", "Yb"),
    71: ("Lutetium", "Lu"),
    72: ("Hafnium", "Hf"),
    73: ("Tantalum", "Ta"),
    74: ("Tungsten", "W"),
    75: ("Rhenium", "Re"),
    76: ("Osmium", "Os"),
    77: ("Iridium", "Ir"),
    78: ("Platinum", "Pt"),
    79: ("Gold", "Au"),
    80: ("Mercury", "Hg"),
    81: ("Thallium", "Tl"),
    82: ("Lead", "Pb"),
    83: ("Bismuth", "Bi"),
    84: ("Polonium", "Po"),
    85: ("Astatine", "At"),
    86: ("Radon", "Rn"),
    87: ("Francium", "Fr"),
    88: ("Radium", "Ra"),
    89: ("Actinium", "Ac"),
    90: ("Thorium", "Th"),
    91: ("Protactinium", "Pa"),
    92: ("Uranium", "U"),
    93: ("Neptunium", "Np"),
    94: ("Plutonium", "Pu"),
    95: ("Americium", "Am"),
    96: ("Curium", "Cm"),
    97: ("Berkelium", "Bk"),
    98: ("Californium", "Cf"),
    99: ("Einsteinium", "Es"),
    100: ("Fermium", "Fm"),
    101: ("Mendelevium", "Md"),
    102: ("Nobelium", "No"),
    103: ("Lawrencium", "Lr"),
    104: ("Rutherfordium", "Rf"),
    105: ("Dubnium", "Db"),
    106: ("Seaborgium", "Sg"),
    107: ("Bohrium", "Bh"),
    108: ("Hassium", "Hs"),
    109: ("Meitnerium", "Mt"),
    110: ("Darmstadtium", "Ds"),
    111: ("Roentgenium", "Rg"),
    112: ("Copernicium", "Cn"),
    113: ("Nihonium", "Nh"),
    114: ("Flerovium", "Fl"),
    115: ("Moscovium", "Mc"),
    116: ("Livermorium", "Lv"),
    117: ("Tennessine", "Ts"),
    118: ("Oganesson", "Og"),
}


class Element:

    def __init__(self, protons, neutrons, electrons):
        self.protons = protons
        self.neutrons = neutrons
        self.electrons = electrons
        self.atomic_number = protons
        self.mass_number = protons + neutrons
        self.name, self.symbol = self.get_element_name()

    def get_element_name(self):
        if self.atomic_number in elements:
            return elements[self.atomic_number]
        else:
            return ("Unknown Element", "X")

    def display_info(self):

        if self.neutrons == 0:
            neutron_info = "Radioactivity: 10 (MAX)\n- No neutrons,\n unstable nucleus,\n highly radioactive.\n"
        elif self.neutrons == 1:
            neutron_info = "Radioactivity: 8\n- One neutron,\n unstable but \nslightly less radioactive.\n"
        elif self.neutrons <= 3:
            neutron_info = "Radioactivity: 6\n- Few neutrons,\n element may be stable \nor have isotopes.\n"
        elif self.neutrons <= 10:
            neutron_info = (
                "Radioactivity: 4\n- Moderate number of neutrons,\n likely stable.\n"
            )
        else:
            neutron_info = "Radioactivity: 2\n- High neutron count,\n could be radioactive or unstable.\n"

        if self.protons == self.electrons:
            electron_info = f"Electrons: {self.electrons} (Neutral Atom)\n- This element has the same number of electrons and protons.\n"
        elif self.protons > self.electrons:
            electron_info = f"Electrons: {self.electrons} (Cation)\n- The element has lost electrons and is positively charged.\n"
        else:
            electron_info = f"Electrons: {self.electrons} (Anion)\n- The element has gained electrons and is negatively charged.\n"

        info = (
            f"[ ============ INFO =========== ]\n"
            f"Element: {self.name} ({self.symbol})\n"
            f"Atomic Number: {self.atomic_number}\n"
            f"Mass Number: {self.mass_number}\n"
            f"Protons: {self.protons}\n"
            f"Neutrons: {self.neutrons}\n"
            f"{electron_info}\n"
            f"[ ========= NEUTRONS ========= ]\n"
            f"{neutron_info}\n"
            f"Neutrons help stabilize the nucleus.\n"
            f"Isotopes of the same element have different neutron counts.\n"
        )
        return info


def update_element_info(*args):
    protons = proton_slider.get()
    neutrons = neutron_slider.get()
    electrons = electron_slider.get()

    element = Element(protons, neutrons, electrons)
    element_info_label.config(text=element.display_info())

    circle_size = 12
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    if canvas_width < circle_size * 2 + 40 or canvas_height < circle_size * 2 + 40:
        return

    max_attempts = 1000

    def generate_random_position():
        x = random.randint(20, canvas_width - circle_size - 20)
        y = random.randint(20, canvas_height - circle_size - 20)
        return x, y

    global proton_positions
    global neutron_positions
    global electron_positions

    if len(proton_positions) > protons:

        proton_positions = proton_positions[:protons]
        canvas.delete("protons")
        for i, (x, y) in enumerate(proton_positions):
            canvas.create_oval(
                x, y, x + circle_size, y + circle_size, fill="red", tags="protons"
            )
    else:

        for _ in range(protons - len(proton_positions)):
            attempts = 0
            while attempts < max_attempts:
                x, y = generate_random_position()
                overlap = False
                for px, py in proton_positions + neutron_positions:
                    if abs(px - x) < circle_size + 5 and abs(py - y) < circle_size + 5:
                        overlap = True
                        break
                if not overlap:
                    proton_positions.append((x, y))
                    canvas.create_oval(
                        x,
                        y,
                        x + circle_size,
                        y + circle_size,
                        fill="red",
                        tags="protons",
                    )
                    break
                attempts += 1

    if len(neutron_positions) > neutrons:

        neutron_positions = neutron_positions[:neutrons]
        canvas.delete("neutrons")
        for i, (x, y) in enumerate(neutron_positions):
            canvas.create_oval(
                x, y, x + circle_size, y + circle_size, fill="blue", tags="neutrons"
            )
    else:

        for _ in range(neutrons - len(neutron_positions)):
            attempts = 0
            while attempts < max_attempts:
                x, y = generate_random_position()
                overlap = False
                for px, py in proton_positions + neutron_positions:
                    if abs(px - x) < circle_size + 5 and abs(py - y) < circle_size + 5:
                        overlap = True
                        break
                if not overlap:
                    neutron_positions.append((x, y))
                    canvas.create_oval(
                        x,
                        y,
                        x + circle_size,
                        y + circle_size,
                        fill="blue",
                        tags="neutrons",
                    )
                    break
                attempts += 1

    if len(electron_positions) > electrons:

        electron_positions = electron_positions[:electrons]
        canvas.delete("electrons")
        for i, (x, y) in enumerate(electron_positions):
            canvas.create_oval(
                x, y, x + circle_size, y + circle_size, fill="yellow", tags="electrons"
            )
    else:

        for _ in range(electrons - len(electron_positions)):
            attempts = 0
            while attempts < max_attempts:
                x, y = generate_random_position()
                overlap = False
                for px, py in proton_positions + neutron_positions:
                    if abs(px - x) < circle_size + 5 and abs(py - y) < circle_size + 5:
                        overlap = True
                        break
                if not overlap:
                    electron_positions.append((x, y))
                    canvas.create_oval(
                        x,
                        y,
                        x + circle_size,
                        y + circle_size,
                        fill="yellow",
                        tags="electrons",
                    )
                    break
                attempts += 1


root = tk.Tk()
root.title("ElementLab | 0.1.0")
root.geometry("1000x700")
root.resizable(False, False)
root.config(bg="#232323")



menubar = tk.Menu(root)


periodic_table = tk.Menu(menubar, tearoff=0, bg="#232323", fg="white")
menubar.add_cascade(
    label="Click to Select Element (Periodic Table)", menu=periodic_table
)


for atomic_number, (name, symbol) in elements.items():
    periodic_table.add_command(
        label=f"{name} ({symbol})",
        command=lambda an=atomic_number: show_element_info(an),
    )


def show_element_info(atomic_number):
    name, symbol = elements[atomic_number]
    # info_label.config(
    #     text=f"Selected Element: {name} ({symbol})\nAtomic Number: {atomic_number}",bg="#323232", fg="white"
    # )
    proton_slider.set(atomic_number)
    electron_slider.set(atomic_number)
    update_element_info()


info_label = tk.Label(
    root, text="", font=("Helvetica", 12), bg="#323232", fg="black"
)
info_label.pack(fill=tk.X, side=tk.BOTTOM, pady=5)


title_label = tk.Label(root, text="ElementLab", font=("Helvetica", 18, "bold"),bg="#232323", fg="white")
title_label.place(x=30, y=10)

root.config(menu=menubar)

proton_slider = tk.Scale(
    root, from_=1, to=118, orient="horizontal", label="Proton Count", length=300,bg="#232323", fg="white", highlightthickness=0
)
proton_slider.set(1)
proton_slider.place(x=50, y=60)


neutron_slider = tk.Scale(
    root, from_=0, to=50, orient="horizontal", label="Neutron Count", length=300,bg="#232323", fg="white", highlightthickness=0
)
neutron_slider.set(0)
neutron_slider.place(x=50, y=118)


electron_slider = tk.Scale(
    root, from_=0, to=118, orient="horizontal", label="Electron Count", length=300,bg="#232323", fg="white", highlightthickness=0
)
electron_slider.set(1)
electron_slider.place(x=50, y=176)

canvasy = 25


canvas = tk.Canvas(root, width=400, height=400,bg="#232323", highlightthickness=0)
canvas.place(x=500, y=canvasy)


canvas.create_oval(canvasy, canvasy, 399, 399, outline="white", width=2)


element_info_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    justify="left",
    anchor="w",
    width=50,
    height=20,bg="#232323", fg="white"
)
element_info_label.place(x=50, y=250)


proton_slider.bind("<Motion>", update_element_info)
neutron_slider.bind("<Motion>", update_element_info)
electron_slider.bind("<Motion>", update_element_info)


proton_positions = []
neutron_positions = []
electron_positions = []

update_element_info()


root.mainloop()
