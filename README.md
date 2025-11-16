# IMF WEO Database File Downloader

This Python script allows users to download specific files from the IMF World Economic Outlook (WEO) database page for October 2024. It fetches the HTML from the IMF "Download Entire Database" page, locates the exact file links using CSS selectors, and provides a simple command-line interface to download files one at a time.

If the IMF website structure changes and the hard-coded `href` values no longer match the HTML, the script will notify the user and exit safely.

---

## Features

- Retrieves the WEO download page automatically.
- Safely extracts file URLs using `BeautifulSoup`.
- Validates user input (1–4 only).
- Downloads the selected file to the local directory.
- Allows repeated downloads in a clean, continuous loop.
- Gracefully exits when the user chooses not to continue.
- Includes clear error messages for missing or changed IMF file links.

---

## Requirements

Install the required Python libraries:

```bash
pip install requests beautifulsoup4
```

---

## How to Run

1. Save the script as `weo_downloader.py`.
2. Run it with:

```bash
python weo_downloader.py
```

3. Choose the file you want to download by entering a number from the menu:

```
1. By Countries
2. By Country Group
3. SDMX Data
4. SDMX Data Definitions
```

4. After each download, the script will ask:

```
Would you like to download another file?
```

Type:

- `yes` to continue
- `no` to exit

---

## File Options and Selectors

The script searches for four specific `<a>` elements on the IMF page:

| Option | Description            | File Type | CSS Selector (exact match) |
|--------|------------------------|-----------|-----------------------------|
| 1      | By Countries           | .xls      | `weooct2024all.xls`        |
| 2      | By Country Groups      | .xls      | `weooct2024alla.xls`       |
| 3      | SDMX Data              | .zip      | `weooct2024-sdmxdata.zip`  |
| 4      | SDMX DSD Definitions   | .xlsx     | `weopub-dsd-oct2024.xlsx`  |

If any of these links are not found (for example, if the IMF modifies the page), the script will print an error message and stop.

---

## Code Structure

### `get_link()`
Safely extracts an `<a>` tag matching the desired CSS selector.  
If the element is missing, prints a detailed message and exits.

### `file_selector()`
Prompts the user to choose a valid option (1–4).  
Loops until valid input is provided.

### `file_extractor()`
Uses the selected index to:
- locate the correct entry in `file_elements`
- extract the file link
- download and save the file

### Main Loop
Runs `file_extractor()` once, then repeatedly prompts the user to download additional files.

---

## Notes

- If the IMF website structure changes, you must update the `file_elements` list with the correct CSS selectors from the new HTML.
- The script currently downloads files into the same directory it is executed from.
- The script exits cleanly with informative messages.
