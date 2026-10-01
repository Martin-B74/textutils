# About textutils
textutils is a lightweight, open-source Python library designed for quick and basic text processing.

## Available Functionality
* **`word_count(text)`**: Counts the total number of words in a given string.
* **`character_count(text)`**: Counts the total number of characters in a given string.
* **`reverse(text)`**: Reverses the input string.
* **`capitalize_words(text)`**: Capitalizes the first letter of every word in the text.

## Usage
Here is a minimal example of how to use the library:

```python
import textutils

sample_text = "hello world"

# Count words
print(textutils.word_count(sample_text))  # Output: 2

# Capitalize words
print(textutils.capitalize_words(sample_text))  # Output: Hello World
```

## Contributing
Contributions are welcome! If you would like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your branch and open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.