## noe2fiy

As a long-time user of Neo-Store, I've noticed that it has become increasingly sluggish and less responsive after recent updates. Frustrated with the lag, I decided to switch to Droid-ify. However, I soon discovered that Droid-ify does not support Neo-Store formatting. This is where Neo2ify comes into play. This script is designed to bridge that gap, providing a seamless transition for users like me by converting Neo-Store exports into a format compatible with Droid-ify.

I deleted Neo-Store a while ago, so if this script isn't working, please let me know. If the Neo-Store format has changed, I will work on updating the script accordingly.

Basically, this script is functional and should work as intended.

>Please handle other changes, such as implementing a dark or light theme, on your own.

### Features

At the moment, support is only available for favorite apps.

## Usage

To convert your Neo-Store export file to a format compatible with Droid-ify, install python3 first, then run the following command in your terminal:

```shell
python main.py --input NS.xts --output fdroid-ify.json
```

### Parameters

- `--input`: Specify the path to your Neo-Store export file (e.g., `NS.xts`).
- `--output`: Define the desired output file name for the Droid-ify compatible JSON (e.g., `fdroid-ify.json`).

### Example

Here’s a quick example of how to use the script:

1. Export your favorite apps from Neo-Store to a file named `NS.xts`.
2. Run the following command in your terminal:

   ```shell
   python main.py --input NS.xts --output fdroid-ify.json
   ```

3. The script will generate a file named `fdroid-ify.json`, which you can then import into Droid-ify.

## Contributing

If feel to open issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
