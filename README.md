# Kahoot Data Extractor

Kahoot Data Extractor is a Python-based tool that uses Selenium to scrape quiz data from Kahoot URLs and save it to a file. The tool features a graphical user interface (GUI) built with Tkinter.

## Features

- Extract quiz data from multiple Kahoot URLs.
- Save extracted data to a specified file.
- Progress bar to show the extraction progress.
- User-friendly GUI.

## Requirements

- Python 3.x
- Tkinter
- Selenium
- WebDriver Manager for Chrome

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/cryp71c/kahoot_scrape.git
    cd kahoot_scrape
    ```

2. Install the required Python packages:

    ```sh
    python3 -m pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```sh
    python3 kahoot_scrape.py
    ```

2. Enter the Kahoot URLs (one per line) in the text area.
3. Enter the output filename.
4. Click the "Extract Data" button to start the extraction process.

## Example

1. Enter URLs:

    ```
    https://create.kahoot.it/details/<uuid_x>
    https://create.kahoot.it/details/<uuid_y>
    ```

2. Enter output filename:

    ```
    output.txt
    ```

3. Click "Extract Data" and wait for the process to complete. The extracted data will be saved in `output.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [WebDriver Manager for Chrome](https://pypi.org/project/webdriver-manager/)