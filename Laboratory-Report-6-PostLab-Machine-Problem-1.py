from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="Temperature Converter")
        self.addLabel("Celsius", 0, 0)
        self.celsiusField = self.addTextField("0.0", 1, 0)
        self.addLabel("Fahrenheit", 0, 1)
        self.fahrField = self.addTextField("32.0", 1, 1)
        self.addButton(">>>>", 2, 0, command=self.computeFahr)
        self.addButton("<<<<", 2, 1, command=self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        celcius = float(self.celsiusField.getText())
        self.fahrField.setText(celcius * (9 / 5) + 32)

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        fahr = float(self.fahrField.getText())
        self.celsiusField.setText((fahr - 32) * 5 / 9)


def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")